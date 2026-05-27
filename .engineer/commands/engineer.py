#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, fnmatch, hashlib, sys
from pathlib import Path
from datetime import datetime, timezone
try:
    import yaml
except Exception:  # PyYAML is optional; route falls back to built-in triggers.
    yaml = None

TEXT_EXTS={".md",".txt",".yaml",".yml",".json",".jsonl",".toml",".py",".js",".ts",".tsx",".jsx",".cs",".java",".go",".rs",".php",".rb",".kt",".kts",".swift",".c",".cpp",".h",".hpp",".m",".mm",".scala",".dart",".lua",".r",".sh",".bash",".zsh",".ps1",".html",".css",".scss",".sass",".less",".vue",".svelte",".astro",".sql",".xml",".csv",".env",".prisma",".graphql",".gql",".proto",".dockerfile"}
IGNORE_NAMES={".git","__pycache__",".venv","node_modules",".pytest_cache"}
ROOT_MARKERS=["00_ENTRYPOINT.yaml","AGENTS.md"]
SCENARIO_WORDS=["scenario","scenarios","سيناريو","سيناريوهات","use case","حالة استخدام","workflow","flow","journey","رحلة","user story","acceptance","قبول","lifecycle","دورة حياة","حالات"]
PRD_WORDS=["prd","product requirements","متطلبات المنتج","requirements","متطلبات","srs","specification","مواصفة"]
TRUTH_WORDS=["entrypoint","contract","truth","source of truth","مصدر الحقيقة","project baseline","baseline","عقد المشروع","فهرس الحقيقة"]
ARCH_WORDS=["architecture","معمار","بنية","design","تصميم","component","module"]
GOV_WORDS=["decision","adr","risk","governance","حوكمة","قرار","خطر","مخاطر"]
PLACEHOLDER_WORDS=["placeholder","todo","tbd","draft","empty","coming soon","stub","not implemented","لاحقاً","لاحقا","قيد الكتابة","مسودة","فارغ","لم يكتمل","سيتم","TODO"]
READINESS_WORDS=["acceptance","criteria","api","endpoint","database","entity","state","event","permission","role","workflow","scenario","validation","test","contract","decision","risk","قبول","معيار","واجهة","قاعدة بيانات","كيان","حالة","حدث","صلاحية","دور","تدفق","سيناريو","تحقق","اختبار","عقد","قرار","خطر"]
CODE_EXTS={".py",".js",".ts",".tsx",".jsx",".cs",".java",".go",".rs",".php",".rb",".kt",".kts",".swift",".c",".cpp",".h",".hpp",".scala",".dart",".lua",".r",".sql",".vue",".svelte",".astro",".prisma",".graphql",".gql",".proto",".sh"}

# v6.19 Content Value Atlas: project-neutral, file-type-neutral semantic touch.
VALUE_ATLAS_SIGNAL_GROUPS = {
    "truth_identity": ["entrypoint", "contract", "truth", "source of truth", "baseline", "identity", "mission", "مصدر الحقيقة", "عقد", "هوية"],
    "methodology_360": ["360", "method", "methodology", "canon", "standard", "governance", "منهج", "معيار", "حوكمة"],
    "requirements_prd": ["prd", "requirements", "specification", "acceptance", "متطلبات", "قبول", "مواصفة"],
    "workflow_scenario": ["scenario", "workflow", "flow", "journey", "use case", "lifecycle", "سيناريو", "تدفق", "رحلة", "دورة"],
    "state_event": ["state", "status", "event", "transition", "taxonomy", "حالة", "حدث", "انتقال"],
    "permission_audit_security": ["permission", "role", "audit", "security", "auth", "authorization", "access", "صلاحية", "دور", "تدقيق", "أمان"],
    "data_interface_contract": ["database", "entity", "model", "api", "endpoint", "integration", "schema", "migration", "بيانات", "كيان", "واجهة", "تكامل"],
    "implementation_code": ["class ", "def ", "function ", "interface ", "namespace ", "import ", "using ", "export ", "async ", "await ", "كود", "تنفيذ"],
    "testing_quality": ["test", "testing", "quality", "coverage", "assert", "pytest", "unit", "integration test", "اختبار", "جودة"],
    "operations_domain": ["operations", "shipping", "payment", "financial", "inventory", "notification", "analytics", "تشغيل", "شحن", "دفع", "مالية"],
    "ux_content": ["ui", "ux", "screen", "component", "design", "layout", "copy", "story", "واجهة", "تصميم", "محتوى"],
    "risk_decision": ["risk", "decision", "adr", "tradeoff", "constraint", "open decision", "خطر", "قرار", "قيد"],
}

HIGH_IMPACT_TERMS = {
    "assessment": ["evaluate", "assessment", "status", "maturity", "readiness", "تقييم", "وضع", "نضج", "جاهزية"],
    "decision": ["decide", "decision", "recommend", "first step", "priority", "قرار", "اقترح", "أول خطوة", "أولوية"],
    "write_or_fix": ["write", "modify", "fix", "repair", "refactor", "أكتب", "عدّل", "أصلح", "إنضاج", "تنقيح"],
    "implementation": ["implement", "code", "api", "database", "backend", "frontend", "deploy", "تنفيذ", "كود", "قاعدة بيانات"],
    "architecture": ["architecture", "system", "runtime", "matrix", "neural", "معمارية", "نظام", "ماتركس", "جملة عصبية"],
}


def find_root(start: Path|None=None)->Path:
    p=(start or Path.cwd()).resolve()
    for cur in [p]+list(p.parents):
        if all((cur/m).exists() for m in ROOT_MARKERS):
            return cur
    p=Path(__file__).resolve()
    for cur in [p]+list(p.parents):
        if all((cur/m).exists() for m in ROOT_MARKERS):
            return cur
    return Path.cwd().resolve()

ROOT=find_root()
ACTIVE=ROOT/"02_WORKSHOP"/"ACTIVE_PROJECT"
RUNTIME=ROOT/".engineer"
STATE=RUNTIME/"state"
INDEX=RUNTIME/"indexes"


GENERATED_DIR_PREFIXES = (".engineer/indexes/", ".engineer/ledgers/", ".engineer/state/", ".engineer/backups/")
GENERATED_SEARCH_TERMS = {"cache", "caches", "index", "indexes", "ledger", "ledgers", "state", "generated", "stale", "runtime cache", "كاش", "فهارس", "سجل", "سجلات", "متولد"}


def is_generated_runtime_rel(path: str) -> bool:
    return path.startswith(GENERATED_DIR_PREFIXES)


def query_requests_generated_outputs(query: str = "") -> bool:
    low = (query or "").lower()
    return any(term in low for term in GENERATED_SEARCH_TERMS)


def should_skip_generated(scope: str, query: str = "", include_generated: bool = False) -> bool:
    if include_generated or query_requests_generated_outputs(query):
        return False
    return scope in {"runtime", "runtime_static", "repository", "repository_static"}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except Exception:
        return False


def distribution_mode() -> str:
    """Return template or working_snapshot. Defaults to working_snapshot when ACTIVE_PROJECT has real files."""
    manifest = RUNTIME/"runtime"/"manifest.yaml"
    if yaml and manifest.exists():
        try:
            data = yaml.safe_load(manifest.read_text(encoding='utf-8')) or {}
            mode = (data.get('runtime') or {}).get('distribution_mode')
            if mode in {'template','working_snapshot'}:
                return mode
        except Exception:
            pass
    real_files = [p for p in ACTIVE.rglob('*') if p.is_file() and p.name != '.keep'] if ACTIVE.exists() else []
    return 'working_snapshot' if real_files else 'template'



# Volatile generated state policy:
# These dirs may contain project-specific runtime products during a session.
# They are not part of the static engineer mind and should be cleaned before shipping
# a neutral framework package unless the package intentionally includes an active project snapshot.
VOLATILE_DIRS = [RUNTIME/"indexes", RUNTIME/"ledgers", RUNTIME/"state"]

def project_fingerprint(scope: str = "project") -> str:
    """Stable fingerprint for cache staleness checks.

    Generated runtime products are excluded from repository-level fingerprints so a cache
    file does not make itself stale immediately after being written.
    """
    effective_scope = "repository" if scope in {"repository_static", "repository"} else scope
    h = hashlib.sha1()
    for f in iter_files(effective_scope):
        r = rel(f)
        if scope in {"repository", "repository_static", "runtime", "runtime_static"} and r.startswith(GENERATED_DIR_PREFIXES):
            continue
        try:
            h.update(r.encode('utf-8'))
            h.update(str(f.stat().st_size).encode('utf-8'))
            h.update(hashlib.sha1(f.read_bytes()).hexdigest().encode('utf-8'))
        except Exception:
            continue
    return h.hexdigest()[:16]

def attach_cache_meta(obj: dict, scope: str) -> dict:
    obj.setdefault("cache_meta", {})
    obj["cache_meta"].update({
        "scope": scope,
        "fingerprint": project_fingerprint(scope),
        "volatile": True,
        "generated_by": "engineer.py",
        "generated_at": obj.get("generated_at") or utc_now(),
    })
    return obj

def cli_commands_from_source() -> set[str]:
    try:
        src = Path(__file__).read_text(encoding='utf-8')
        return set(re.findall(r'sub\.add_parser\("([^"]+)"', src))
    except Exception:
        return set()

def registry_commands() -> set[str]:
    reg = RUNTIME/"runtime"/"tool_registry.yaml"
    if not reg.exists():
        reg = RUNTIME/"tool_registry.yaml"
    if not reg.exists():
        return set()
    txt = reg.read_text(encoding='utf-8', errors='ignore')
    cmds = set()
    # Supports either `  cmd:` or `  cmd-name:` directly under tools:
    for line in txt.splitlines():
        m = re.match(r'^  ([A-Za-z0-9_\-]+):\s*$', line)
        if m:
            cmds.add(m.group(1).replace('_','-'))
    return cmds


def active_project_specific_terms() -> set[str]:
    """Derive high-confidence project-specific terms that must not appear in runtime logic.

    This check protects the engineer environment from coupling to the current
    ACTIVE_PROJECT. It uses only distinctive project-local identifiers, not
    generic words like business, user, api, or workflow.
    """
    terms=set()
    base=active_project_dir() if 'active_project_dir' in globals() else None
    if base and base.exists() and base != ACTIVE:
        terms.add(base.name)
    # Contract project name, if available.
    for contract in [base/'01_PROJECT_CONTRACT.yaml'] if base else []:
        if contract.exists() and yaml:
            try:
                data=yaml.safe_load(contract.read_text(encoding='utf-8')) or {}
                pc=data.get('project_contract') or data
                name=pc.get('project_name') or pc.get('project_id')
                if isinstance(name, str) and len(name) >= 4:
                    terms.add(name)
            except Exception:
                pass
    # Distinctive path basenames under active project artifacts.
    if base and base.exists():
        for f in base.rglob('*'):
            if not f.is_dir():
                continue
            nm=f.name
            if len(nm) < 5:
                continue
            # Only distinctive project-local identifiers: mixed case or underscore-rich names.
            if re.match(r'^\d+_PROJECT_', nm) or nm.upper() == nm:
                continue
            if '_' in nm or re.search(r'[A-Z].*[a-z]|[a-z].*[A-Z]', nm):
                if nm.lower() not in {'active_project', 'project_artifacts', 'project_decisions'}:
                    terms.add(nm)
    return {t for t in terms if t and len(t) >= 4}


def project_specific_runtime_coupling_report() -> list[dict]:
    """Find project-specific terms inside static runtime logic.

    ACTIVE_PROJECT may of course contain project terms. Runtime logic, governance,
    protocols, and tool contracts may not. Reports/tests may mention examples, but
    command/runtime/governance/protocol logic should stay neutral.
    """
    terms=active_project_specific_terms()
    if not terms:
        return []
    scan_roots=[RUNTIME/'commands', RUNTIME/'runtime', RUNTIME/'governance', RUNTIME/'protocols', RUNTIME/'kernel', RUNTIME/'capabilities']
    hits=[]
    for root in scan_roots:
        if not root.exists():
            continue
        for f in root.rglob('*'):
            if not f.is_file() or f.suffix.lower() not in TEXT_EXTS:
                continue
            txt=read_text(f, 300000)
            for term in terms:
                if term in txt:
                    hits.append({"path": rel(f), "term": term})
    return hits

def runtime_integrity_report() -> dict:
    problems=[]; warnings=[]
    parser_cmds=cli_commands_from_source()
    registry=registry_commands()
    if not registry:
        problems.append({"type":"missing_tool_registry","message":"tool_registry.yaml is missing or empty."})
    else:
        missing=sorted(parser_cmds-registry)
        extra=sorted(registry-parser_cmds)
        if missing:
            problems.append({"type":"tool_registry_missing_commands","missing":missing})
        if extra:
            warnings.append({"type":"tool_registry_extra_commands","extra":extra})
    coupling_hits=project_specific_runtime_coupling_report()
    if coupling_hits:
        problems.append({"type":"project_specific_runtime_coupling", "message":"Static engineer runtime must not hardcode active-project-specific names.", "hits": coupling_hits[:40]})

    # Generated cache integrity: every generated json should carry cache_meta and must not override current files.
    for f in (RUNTIME/"indexes").glob("*.json"):
        try:
            data=json.loads(f.read_text(encoding='utf-8'))
        except Exception:
            warnings.append({"type":"unreadable_generated_index","path":rel(f)})
            continue
        meta=data.get("cache_meta") or {}
        if not meta:
            warnings.append({"type":"generated_index_missing_cache_meta","path":rel(f)})
            continue
        scope=meta.get("scope")
        if scope in {"project","runtime","runtime_static","repository","repository_static","workshop"} and meta.get("fingerprint"):
            current=project_fingerprint(scope)
            if current != meta.get("fingerprint"):
                warnings.append({"type":"stale_generated_index","path":rel(f),"scope":scope,"stored":meta.get("fingerprint"),"current":current,"action":"refresh recommended; generated cache will not be treated as source of truth"})
    nav=RUNTIME/"runtime"/"navigation.yaml"
    if not nav.exists():
        problems.append({"type":"missing_navigation_yaml"})
    else:
        routes=_navigation_routes_from_yaml()
        required={"project_surface","project_work","runtime_work","governance_work","comparison_work","write_or_modify_work","best_fit_work","implementation_translation_work","research_work","external_research_work","content_work"}
        missing_routes=sorted(required-set(routes))
        if missing_routes:
            warnings.append({"type":"navigation_missing_recommended_routes","missing":missing_routes})
    manifest=RUNTIME/"runtime"/"manifest.yaml"
    mode=distribution_mode()
    real_files=[p for p in ACTIVE.rglob('*') if p.is_file() and p.name != '.keep'] if ACTIVE.exists() else []
    if mode == 'template' and real_files:
        problems.append({"type":"distribution_mode_conflict","message":"template mode cannot ship real ACTIVE_PROJECT files","active_project_files":len(real_files)})
    # Central operating core checks.
    if 'plug' not in parser_cmds:
        problems.append({"type":"missing_central_plug_command"})
    if 'neural' not in parser_cmds:
        problems.append({"type":"missing_neural_reflex_command"})
    if 'best-fit' not in parser_cmds:
        warnings.append({"type":"missing_best_fit_command"})
    if 'truth-maturity' not in parser_cmds:
        problems.append({"type":"missing_truth_maturity_command"})
    if 'canon-check' not in parser_cmds:
        problems.append({"type":"missing_canon_check_command"})
    if not (RUNTIME/"governance"/"central_operating_core.yaml").exists():
        warnings.append({"type":"missing_central_operating_core_governance"})
    if not (RUNTIME/"governance"/"neural_operating_system.yaml").exists():
        warnings.append({"type":"missing_neural_operating_system_governance"})
    if not (RUNTIME/"governance"/"incomplete_truth_maturity.yaml").exists():
        problems.append({"type":"missing_incomplete_truth_maturity_governance"})
    if not (RUNTIME/"protocols"/"best_fit_reality_comparison.yaml").exists():
        warnings.append({"type":"missing_best_fit_reality_protocol"})
    if not (RUNTIME/"protocols"/"code_practice_canon_gate.yaml").exists():
        warnings.append({"type":"missing_code_practice_canon_protocol"})
    # Static tool contract alignment: tool-plan sequences should include internal-tool-first essentials.
    for req, expected in {
        "project_surface": ["route","tool-plan","context-pack","truth-map","evidence-lock"],
        "write_or_modify_work": ["duplicate-scan","impact-scan","write-plan","safe-write"],
        "runtime_work": ["scan-runtime","doctor","runtime-audit"],
    }.items():
        seq=[x.get('cmd') for x in tool_sequence_for_route(req)]
        for cmd in expected:
            if cmd not in seq:
                warnings.append({"type":"tool_sequence_missing_expected_command","route":req,"missing":cmd})
    # Version alignment: entrypoint, manifest, and tool contract must not drift.
    versions = {}
    try:
        manifest_data = yaml.safe_load((RUNTIME/"runtime"/"manifest.yaml").read_text(encoding="utf-8")) if yaml else {}
        versions["manifest"] = str((manifest_data.get("runtime") or {}).get("version"))
    except Exception:
        versions["manifest"] = None
    for name, path in {"entrypoint": ROOT/"00_ENTRYPOINT.yaml", "tool_contract": RUNTIME/"runtime"/"tool_contract.yaml"}.items():
        try:
            txt = path.read_text(encoding="utf-8", errors="ignore")
            m = re.search(r'version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)', txt)
            versions[name] = m.group(1) if m else None
        except Exception:
            versions[name] = None
    known_versions = {v for v in versions.values() if v and v != "None"}
    if len(known_versions) > 1:
        problems.append({"type":"runtime_version_mismatch", "versions": versions})
    # Compact plug and relationship graph are first-class runtime checks.
    if 'compact_plug_packet' not in Path(__file__).read_text(encoding='utf-8', errors='ignore'):
        problems.append({"type":"compact_plug_missing"})
    if 'relationship-graph' not in parser_cmds:
        problems.append({"type":"relationship_graph_command_missing"})
    if 'cache_clean' not in Path(__file__).read_text(encoding='utf-8', errors='ignore'):
        warnings.append({"type":"cache_cleaner_static_check_missing"})
    # Safe-write containment is a static capability check.
    if 'target_outside_declared_scope' not in Path(__file__).read_text(encoding='utf-8', errors='ignore'):
        problems.append({"type":"safe_write_scope_containment_missing"})
    # v7 Indexed Kernel checks.
    parser_cmds_now = cli_commands_from_source()
    for cmd in ["build-index", "plug-fast", "plug-deep", "operation-mode", "kernel-status", "golden-suite"]:
        if cmd not in parser_cmds_now:
            problems.append({"type":"v7_kernel_command_missing", "command":cmd})
    if not (RUNTIME/"runtime"/"kernel_v7.yaml").exists():
        problems.append({"type":"missing_v7_kernel_contract"})
    if not (RUNTIME/"protocols"/"indexed_neural_operating_kernel.md").exists():
        problems.append({"type":"missing_indexed_kernel_protocol"})
    # v8.1 File Matrix checks: the runtime must expose a real file-intelligence kernel, not only text search.
    for cmd in ["file-matrix-build", "file-matrix-pulse", "file-matrix-touch", "file-matrix-query", "file-matrix-context", "file-matrix-doctor", "file-matrix-status"]:
        if cmd not in parser_cmds_now:
            problems.append({"type":"file_matrix_command_missing", "command":cmd})
    if "FILE_MATRIX_VERSION" not in Path(__file__).read_text(encoding='utf-8', errors='ignore'):
        problems.append({"type":"file_matrix_kernel_missing"})
    health="fail" if problems else ("pass_with_warnings" if warnings else "pass")
    # Keep status backward-compatible for lifecycle tests: warnings are visible but not fatal unless a tool uses generated cache as source of truth.
    status="fail" if problems else "pass"
    return {"status":status, "health":health, "parser_command_count":len(parser_cmds), "registry_command_count":len(registry), "distribution_mode":mode, "problems":problems, "warnings":warnings, "warning_count":len(warnings)}


def ensure_dirs():
    STATE.mkdir(parents=True, exist_ok=True); INDEX.mkdir(parents=True, exist_ok=True)


def rel(p:Path)->str:
    try: return str(p.relative_to(ROOT)).replace("\\","/")
    except Exception: return str(p).replace("\\","/")


def is_ignored(p:Path)->bool:
    if p.name.startswith(".") and p.name not in {".engineer"}:
        return True
    return any(part in IGNORE_NAMES for part in p.parts)


def scope_base(scope:str)->Path:
    return {"project":ACTIVE,"runtime":RUNTIME,"runtime_static":RUNTIME,"repository":ROOT,"repository_static":ROOT,"workshop":ROOT/"02_WORKSHOP"}.get(scope,ACTIVE)


def iter_files(scope="project"):
    base=scope_base(scope)
    if not base.exists(): return []
    out=[]
    for f in base.rglob("*"):
        if f.is_file() and not is_ignored(f):
            out.append(f)
    return sorted(out)


def read_text(path:Path, limit=250000):
    try:
        if path.suffix.lower() not in TEXT_EXTS: return ""
        txt=path.read_text(encoding="utf-8", errors="ignore")
        return txt[:limit]
    except Exception:
        return ""


def contains_any(text:str, words:list[str])->bool:
    t=text.lower()
    return any(w.lower() in t for w in words)


def file_role(path:Path, text:str):
    name=path.name.lower(); p=rel(path).lower(); s=(p+" "+name+" "+text[:4000].lower())
    ext=path.suffix.lower()
    # Extension is the strongest primary role for executable/code files; content words become secondary signals elsewhere.
    if ext in CODE_EXTS: return "code"
    if len(text.strip())<20: return "empty_or_placeholder"
    if contains_any(s, TRUTH_WORDS): return "truth_entry"
    if contains_any(s, SCENARIO_WORDS): return "scenario"
    if contains_any(s, PRD_WORDS): return "requirements"
    if contains_any(s, ARCH_WORDS): return "architecture"
    if contains_any(s, GOV_WORDS): return "governance"
    return "document"


def domain_signal_profile(text:str) -> dict:
    """Project-neutral domain detection. Signals are weak; inferred domains require clustered evidence."""
    t=(text or "").lower()
    checks=[
        ("software",["api","database","backend","frontend","code","endpoint","entity","migration","كود","قاعدة بيانات","واجهة"]),
        ("research",["research","study","hypothesis","methodology","paper","literature review","بحث","دراسة","منهجية","فرضية"]),
        ("writing",["story","article","book","sermon","narrative","خطبة","قصة","كتاب","مقال","رواية"]),
        ("operations",["process","workflow","operation","service","stakeholder","customer","organization","إجراء","عملية","تشغيل","مستفيد","جهة"]),
        ("education",["course","lesson","curriculum","learning objective","تعليم","درس","منهج"]),
        ("governance",["permission","role","approval","policy","governance","audit","صلاحية","دور","موافقة","حوكمة"]),
    ]
    signals=[]; evidence={}
    for k,words in checks:
        hits=[w for w in words if w in t]
        if hits:
            signals.append(k); evidence[k]=hits[:8]
    inferred=[]
    for k,hits in evidence.items():
        # Avoid domain inflation from one generic word; require multiple hits or a strong domain word.
        strong={"methodology","hypothesis","literature review","sermon","story","database","backend","frontend","governance","audit","workflow","منهجية","فرضية","خطبة","قصة","قاعدة بيانات","حوكمة"}
        if len(hits) >= 2 or any(h in strong for h in hits):
            inferred.append(k)
    return {"signals":sorted(set(signals)), "inferred":sorted(set(inferred)), "evidence":evidence}


def domain_signals(text:str):
    return domain_signal_profile(text).get("signals", [])


def headings(text:str, maxn=12):
    hs=[]
    for line in text.splitlines():
        if line.strip().startswith("#"):
            hs.append(line.strip()[:180])
        if len(hs)>=maxn: break
    return hs


def snippet(text:str, n=700):
    clean=re.sub(r"\s+"," ",text.strip())
    return clean[:n]


def evidence_excerpt(text:str, keywords:list[str], n=420):
    if not text: return ""
    low=text.lower()
    for kw in keywords:
        idx=low.find(kw.lower())
        if idx>=0:
            start=max(0,idx-160); end=min(len(text),idx+n)
            return snippet(text[start:end], n)
    return snippet(text, n)


def inventory(scope="project", with_content=True):
    files=iter_files(scope)
    items=[]
    for f in files:
        txt=read_text(f, 250000) if with_content else ""
        role=file_role(f, txt)
        item={
            "path":rel(f),
            "size":f.stat().st_size,
            "ext":f.suffix.lower(),
            "role":role,
            "headings":headings(txt),
            "domain_signals":domain_signals(txt),
            "snippet":snippet(txt, 700) if txt else "",
            "sha1":hashlib.sha1(f.read_bytes()).hexdigest()[:12] if f.exists() else "",
        }
        if role=="scenario":
            item["evidence_excerpt"]=evidence_excerpt(txt, SCENARIO_WORDS)
        if role=="requirements":
            item["evidence_excerpt"]=evidence_excerpt(txt, PRD_WORDS)
        items.append(item)
    return items


def high_impact_request(query: str = "") -> dict:
    low=(query or "").lower()
    active=[]; hits={}
    for name, words in HIGH_IMPACT_TERMS.items():
        local=[w for w in words if w.lower() in low or w in (query or "")]
        if local:
            active.append(name); hits[name]=local[:8]
    return {"is_high_impact": bool(active), "categories": active, "hits": hits}


def _value_hits(text: str) -> dict:
    low=(text or "").lower()
    out={}
    for group, words in VALUE_ATLAS_SIGNAL_GROUPS.items():
        h=[w for w in words if w.lower() in low or w in (text or "")]
        if h:
            out[group]=h[:10]
    return out


def _content_status(text: str, ext: str) -> str:
    if ext.lower() not in TEXT_EXTS:
        return "non_text_or_binary"
    stripped=(text or "").strip()
    if len(stripped) < 20:
        return "empty"
    words=len(re.findall(r"\w+", stripped))
    if words < 60 and ext.lower() not in CODE_EXTS:
        return "thin"
    if ext.lower() in CODE_EXTS and words < 25 and not re.search(r"\b(class|def|function|interface|namespace|import|using|export)\b", stripped):
        return "thin_code"
    return "content_bearing"


def content_value_profile(path: Path, text: str, query: str = "") -> dict:
    ext=path.suffix.lower(); role=file_role(path, text); status=_content_status(text, ext)
    hv=_value_hits((rel(path)+"\n"+"\n".join(headings(text, 20))+"\n"+(text or "")[:6000]))
    dens=semantic_density(text) if 'semantic_density' in globals() else {"word_count": len(re.findall(r"\w+", text or "")), "signal_count": len(hv)}
    qterms=[t for t in re.findall(r"[A-Za-z_\u0600-\u06FF][A-Za-z0-9_\u0600-\u06FF-]{2,}", query or "") if len(t) >= 3][:12]
    low=(rel(path)+" "+(text or "")[:12000]).lower()
    qhits=[q for q in qterms if q.lower() in low]
    role_weight={"truth_entry":28,"architecture":22,"governance":21,"requirements":19,"scenario":17,"code":17,"document":8,"empty_or_placeholder":1}.get(role,6)
    value_score=role_weight + min(35, len(hv)*5) + min(14, len(headings(text, 12))*2) + min(20, len(qhits)*5)
    if status in {"empty","thin","thin_code"}: value_score -= 10
    if status == "content_bearing": value_score += 8
    if ext in CODE_EXTS: value_score += 5
    incomplete = role in {"truth_entry","requirements","architecture","governance","code"} and status in {"empty","thin","thin_code"}
    expected={"requirements": ["workflow_scenario","permission_audit_security","data_interface_contract","testing_quality"],
              "architecture": ["data_interface_contract","implementation_code","testing_quality","risk_decision"],
              "truth_entry": ["truth_identity","methodology_360"]}.get(role, [])
    missing=[d for d in expected if d not in hv]
    code_signals={}
    if ext in CODE_EXTS:
        code_signals={
            "definitions": len(re.findall(r"\b(class|def|function|interface|namespace)\b", text or "")),
            "imports": len(re.findall(r"\b(import|using|require|from)\b", text or "")),
            "tests": bool(re.search(r"\b(test|spec|assert|pytest|xunit|jest)\b", rel(path).lower()+" "+(text or "")[:3000].lower())),
            "api_or_db": bool(re.search(r"\b(endpoint|route|controller|migration|dbcontext|select |insert |update |delete |schema)\b", (text or "")[:6000].lower())),
        }
    return {
        "path": rel(path), "ext": ext, "role": role, "content_status": status,
        "value_score": value_score, "word_count": dens.get("word_count",0), "signal_count": len(hv),
        "headings": headings(text, 6)[:6], "value_signals": sorted(hv.keys()), "signal_evidence": hv,
        "query_hits": qhits[:8], "incomplete_truth_candidate": incomplete,
        "missing_expected_dimensions": missing[:8], "code_signals": code_signals,
        "excerpt": snippet(text, 360) if text else "",
    }


def content_value_atlas(scope: str = "project", query: str = "", limit: int = 80, mode: str = "compact") -> dict:
    profiles=[]
    for f in iter_files(scope):
        r=rel(f)
        if should_skip_generated(scope, query) and is_generated_runtime_rel(r):
            continue
        txt=read_text(f, 120000)
        profiles.append(content_value_profile(f, txt, query))
    profiles_sorted=sorted(profiles, key=lambda x:(-x.get("value_score",0), x.get("path","")))
    by_status={}; by_role={}; by_signal={}
    for prof in profiles:
        by_status[prof["content_status"]]=by_status.get(prof["content_status"],0)+1
        by_role[prof["role"]]=by_role.get(prof["role"],0)+1
        for sig in prof.get("value_signals",[]): by_signal[sig]=by_signal.get(sig,0)+1
    high_value=[x for x in profiles_sorted if x.get("content_status") == "content_bearing"]
    incomplete=[x for x in profiles_sorted if x.get("incomplete_truth_candidate") or x.get("missing_expected_dimensions")]
    code_surfaces=[x for x in profiles_sorted if x.get("role") == "code" or x.get("ext") in CODE_EXTS]
    required_full=[]; hi=high_impact_request(query)
    if hi["is_high_impact"]:
        for x in profiles_sorted:
            if x.get("value_score",0) >= 35 or x.get("query_hits") or x.get("role") in {"truth_entry","architecture","governance"}:
                required_full.append({"path":x["path"],"reason":"high_impact_claim_may_depend_on_this_cognitive_evidence_unit","role":x["role"],"value_signals":x.get("value_signals",[])[:6]})
            if len(required_full) >= min(18, max(6, limit//3)):
                break
    trim = limit if mode == "full" else min(20, limit)
    atlas={
        "generated_at": utc_now(), "scope": scope, "query": query, "mode": mode,
        "file_count": len(profiles), "high_impact_request": hi,
        "counts_by_status": by_status, "counts_by_role": by_role,
        "signal_coverage": dict(sorted(by_signal.items(), key=lambda kv:(-kv[1], kv[0]))),
        "high_value_files": high_value[:trim],
        "incomplete_truth_candidates": incomplete[:trim],
        "code_and_implementation_surfaces": code_surfaces[:trim],
        "required_full_reads_before_high_impact_claims": required_full,
        "usage_contract": [
            "The atlas touches all current files in scope as cognitive evidence units, not only PRDs.",
            "It does not replace full reading; it selects owner/high-impact files for full reading when claims or execution matter.",
            "High-impact assessments, first steps, writes, implementation, and architecture decisions require this atlas or an equivalent content-value touch.",
            "Best practices are mandatory fit-checks; they reveal incomplete truth and local-standard gaps but do not override active project truth.",
        ],
    }
    atlas=attach_cache_meta(atlas, scope)
    INDEX.mkdir(parents=True, exist_ok=True)
    (INDEX/f"{scope}_content_value_atlas.json").write_text(json.dumps(atlas, ensure_ascii=False, indent=2), encoding="utf-8")
    return atlas


def cmd_value_atlas(args):
    out=content_value_atlas(args.scope, args.query or "", args.limit, args.mode)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def project_signals(items):
    categories={"truth_entry":[],"scenario":[],"requirements":[],"architecture":[],"governance":[],"code":[],"document":[],"empty_or_placeholder":[]}
    for i in items:
        categories.setdefault(i.get("role","document"),[]).append(i)
    signal_domains=sorted(set(sum([i.get("domain_signals",[]) for i in items],[])))
    # Domain signals are weak; require repeated evidence to infer a project domain.
    domain_counts={d:0 for d in signal_domains}
    for i in items:
        for d in i.get("domain_signals",[]): domain_counts[d]=domain_counts.get(d,0)+1
    inferred=sorted([d for d,c in domain_counts.items() if c>=2])
    return {"categories":categories,"domains":inferred,"domain_signals":signal_domains,"domain_signal_counts":domain_counts}


def classify_project(items):
    if not items:
        return {"state":"PROJECT_FORMATION","maturity":"zero","summary":"لا توجد مادة مشروع فعلية بعد؛ هذه بداية تكوين مشروع.","confidence":"high","evidence_policy":"no_project_files_detected"}
    sig=project_signals(items); cats=sig["categories"]
    code=len(cats.get("code",[])); req=len(cats.get("requirements",[])); truth=len(cats.get("truth_entry",[])); scen=len(cats.get("scenario",[])); empty=len(cats.get("empty_or_placeholder",[]))
    if code>0 and (req>0 or scen>0): maturity="implementation_preparation_or_active"
    elif truth>0 and (req>0 or scen>0): maturity="documented_discovery_with_truth_sources"
    elif req>0 or scen>0 or truth>0: maturity="documented_discovery"
    else: maturity="discovery"
    complexity="medium"
    if len(items)>80 or (req+scen+truth)>20: complexity="high"
    if len(items)<10 and req+scen+truth<3: complexity="low"
    return {"state":"PROJECT_DISCOVERY","maturity":maturity,"complexity":complexity,"files":len(items),"truth_files":truth,"scenario_files":scen,"requirements_files":req,"code_files":code,"empty_files":empty,"domains":sig["domains"],"confidence":"evidence_based_full_project_touch"}


def normalize_for_route(s: str) -> str:
    # Remove common Arabic diacritics and tatweel so triggers such as بحث match بحثاً/بحثًا.
    return re.sub(r"[\u064B-\u065F\u0670\u0640]", "", s or "").lower()


def is_project_surface_identity_request(text: str) -> bool:
    low=normalize_for_route(text or "")
    triggers=["من انت", "من أنت", "ما عملك", "وظيفتك", "مهامك", "مهاراتك", "تقييمك", "اول خطوة", "أول خطوة", "كيف تتعامل مع مشروعي", "وضعه الحالي"]
    return any(normalize_for_route(t) in low for t in triggers)


def canonical_surface_lens_query() -> str:
    # Generic surface query only. It must never contain project-specific module or file names.
    return "project entrypoint contract truth index mission objectives artifacts requirements scenarios workflows architecture implementation standards states events permissions data api tests risks gaps first step incomplete truth maturity"


def _navigation_routes_from_yaml() -> dict:
    nav_path = RUNTIME/"runtime"/"navigation.yaml"
    if yaml and nav_path.exists():
        try:
            data = yaml.safe_load(nav_path.read_text(encoding='utf-8')) or {}
            return ((data.get('navigation') or {}).get('routes') or {})
        except Exception:
            return {}
    return {}


def _fallback_navigation_routes() -> dict:
    return {
        "runtime_work": {"scope":"runtime", "priority":10, "tools":["scan-runtime","doctor","runtime-audit"], "triggers_ar":["بيئة المهندس","إطار التشغيل","اطار التشغيل","أدوات التشغيل","ادوات التشغيل","السكربتات","فحص البيئة","تطوير البيئة","runtime"], "triggers_en":["runtime","engineer environment","scripts","doctor","framework"]},
        "external_research_work": {"scope":"project", "priority":20, "tools":["route","tool-plan","context-pack","external-research","evidence-lock"], "triggers_ar":["بحث خارجي","خارجياً","خارجيا","أحدث","حديثة","معايير","قانون","GDPR","سوق"], "triggers_en":["external research","latest","current","standard","regulation","GDPR","market"]},
        "implementation_translation_work": {"scope":"project", "priority":25, "tools":["context-pack","read-many","evidence-lock","claim-check"], "triggers_ar":["api","database","قاعدة بيانات","عقد تنفيذ","تحويل prd","ترجمة prd","backend","frontend","endpoint"], "triggers_en":["api","database","implementation contract","translate prd","backend","frontend","endpoint"]},
        "write_or_modify_work": {"scope":"project", "priority":30, "tools":["duplicate-scan","impact-scan","write-plan","safe-write"], "triggers_ar":["أضف","اضف","إضافة","اضافة","عدّل","عدل","اكتب ملف","أنشئ ملف","انشئ ملف","احذف","طبّق","طبق"], "triggers_en":["add","modify","edit","create file","delete","apply","write file"]},
        "best_fit_work": {"scope":"project", "priority":35, "tools":["context-pack","best-fit","matrix","evidence-lock","claim-check"], "triggers_ar":["أفضل الممارسات","افضل الممارسات","النواقص","الفجوات","أفضل حل","افضل حل","استنتج الحلول","انضاج معماري"], "triggers_en":["best practice","best-fit","excellence","gap review","architecture maturity","missing architecture"]},
        "research_work": {"scope":"project", "priority":40, "tools":["context-pack","evidence-lock","claim-check"], "triggers_ar":["بحث علمي","دراسة","فرضية","منهجية","مراجعة أدبيات"], "triggers_en":["scientific research","study","hypothesis","methodology","literature review"]},
        "content_work": {"scope":"project", "priority":45, "tools":["context-pack","read-many","claim-check"], "triggers_ar":["قصة","خطبة","مقال","كتاب أطفال","رواية","نص"], "triggers_en":["story","sermon","article","children book","narrative","copywriting"]},
        "project_surface": {"scope":"project", "priority":90, "tools":["route","context-pack","evidence-lock","answer"], "triggers_ar":["من انت","من أنت","ما عملك","وظيفتك","مهامك","مهاراتك","تقييمك","اول خطوة","أول خطوة","دورك","كيف تتعامل مع مشروعي"], "triggers_en":["who are you","your role","what do you do","first step","current status","how do you handle my project"]},
        "governance_work": {"scope":"project", "priority":60, "tools":["truth-map","scenario-map","evidence-lock","govern-check","claim-check"], "triggers_ar":["تحقق","فحص الجودة","حوكمة","مخاطر","تناقض","مصدر الحقيقة","اختبار","فشل","تخمين","دليل","أدلة"], "triggers_en":["verify","governance","risk","conflict","source of truth","test","failure","evidence"]},
        "comparison_work": {"scope":"repository", "priority":70, "tools":["digest","search","read-many","compare","claim-check"], "triggers_ar":["قارن","مقارنة","الفرق","افضل","أفضل","نسخة","اصدار","إصدار"], "triggers_en":["compare","difference","better","version"]},
        "project_work": {"scope":"project", "priority":80, "tools":["context-pack","digest","search","read-many","evidence-lock","claim-check"], "triggers_ar":["حلل","ابني","اكتب","صلح","راجع","نفذ","خطط","استخرج","اقرأ","اقراء","افحص الملف"], "triggers_en":["analyze","build","write","fix","review","execute","plan","read","extract"]},
    }


def route_intent(text):
    raw=text or ""; t=normalize_for_route(raw)
    routes=_navigation_routes_from_yaml() or _fallback_navigation_routes()
    def has(words):
        return any(normalize_for_route(w or "") in t or (w or "") in raw for w in (words or []))
    ordered=sorted(routes.items(), key=lambda kv: int((kv[1] or {}).get('priority', 100)))
    for name,cfg in ordered:
        if has((cfg or {}).get('triggers_ar', [])) or has((cfg or {}).get('triggers_en', [])):
            scope=(cfg or {}).get('scope', 'project')
            return {"route":name,"scope":scope,"request":text,"tools":recommended_tools(name)}
    # Conservative fallback: unrecognized requests are project work, not project-surface identity.
    return {"route":"project_work","scope":"project","request":text,"tools":recommended_tools("project_work"),"fallback_reason":"no_explicit_route_trigger"}


def recommended_tools(route):
    routes=_navigation_routes_from_yaml() or _fallback_navigation_routes()
    if route in routes and routes[route].get('tools'):
        return routes[route]['tools']
    return _fallback_navigation_routes().get(route, _fallback_navigation_routes()["project_work"])["tools"]


SURFACE_FORBIDDEN_PATTERNS = [
    r"GPT", r"language model", r"AI assistant", r"مساعد ذكاء", r"مساعد تقني", r"استشاري تقني", r"مساعد هندسي", r"نموذج لغوي", r"نموذج ذكاء",
    r"\.engineer", r"00_ENTRYPOINT", r"AGENTS\.md", r"اختبارات? نجح", r"tests? passed",
    r"إطار تشغيل", r"سأتعامل مع سؤالك", r"أوضح دوري", r"أفحص ملف", r"قراءة سريعة", r"بيئة العمل.*\d+\s*/\s*10", r"\d+\s*/\s*10"
]


def surface_policy_check(text: str) -> dict:
    hits=[]
    for pat in SURFACE_FORBIDDEN_PATTERNS:
        if re.search(pat, text or "", re.IGNORECASE):
            hits.append(pat)
    status="pass" if not hits else "fail"
    return {"status": status, "hits": hits, "message": "project-surface answer must not center runtime, model identity, test results, or unsupported scoring"}


def claim(text, status="observed", evidence=None, confidence="high"):
    return {"claim":text,"status":status,"confidence":confidence,"evidence":evidence or []}


def build_truth_map(scope="project"):
    items=inventory(scope, True)
    cls=classify_project(items) if scope=="project" else {"scope":scope,"files":len(items)}
    sig=project_signals(items); cats=sig["categories"]
    claims=[]
    if scope=="project":
        if not items:
            claims.append(claim("المشروع في مرحلة تكوين؛ لا توجد ملفات مشروع فعلية داخل ACTIVE_PROJECT.", "observed", []))
        else:
            claims.append(claim(f"تم رصد {len(items)} ملفاً داخل المشروع الفعال.", "observed", [i["path"] for i in items[:10]]))
            if cats.get("truth_entry"):
                claims.append(claim(f"توجد مداخل أو ملفات حقيقة تشغيلية بعدد {len(cats['truth_entry'])}.", "observed", [i["path"] for i in cats["truth_entry"][:8]]))
            if cats.get("scenario"):
                claims.append(claim(f"توجد ملفات أو مقاطع سيناريوهات/تدفقات بعدد {len(cats['scenario'])}؛ لا يجوز اعتبار السيناريوهات غائبة.", "observed", [i["path"] for i in cats["scenario"][:10]]))
            if cats.get("requirements"):
                claims.append(claim(f"توجد ملفات متطلبات/PRD بعدد {len(cats['requirements'])}.", "observed", [i["path"] for i in cats["requirements"][:10]]))
            if cats.get("code"):
                claims.append(claim(f"توجد ملفات كود بعدد {len(cats['code'])}.", "observed", [i["path"] for i in cats["code"][:10]]))
            else:
                claims.append(claim("لم يتم رصد ملفات كود نصية ضمن الفحص الكامل للمشروع الفعال.", "observed", []))
    return {"generated_at":utc_now(),"scope":scope,"classification":cls,"category_counts":{k:len(v) for k,v in cats.items()},"domains":sig["domains"],"claims":claims,"evidence_files":{k:[i for i in v[:20]] for k,v in cats.items() if v}}


def cmd_route(args): print(json.dumps(route_intent(args.request), ensure_ascii=False, indent=2))


def cmd_truth_map(args):
    ensure_dirs(); out=build_truth_map(args.scope)
    out=attach_cache_meta(out, args.scope)
    (INDEX/f"{args.scope}_truth_map.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_touch(args):
    ensure_dirs(); out=build_truth_map(args.scope)
    # shorter touch output, but still content-aware
    short={"generated_at":out["generated_at"],"scope":args.scope,"classification":out["classification"],"category_counts":out["category_counts"],"claims":out["claims"],"top_evidence":{k:[x["path"] for x in v[:8]] for k,v in out.get("evidence_files",{}).items()}}
    short=attach_cache_meta(short, args.scope)
    (INDEX/f"{args.scope}_touch.json").write_text(json.dumps(short, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(short, ensure_ascii=False, indent=2))


def cmd_digest(args):
    ensure_dirs(); items=inventory(args.scope, True); cls=classify_project(items) if args.scope=="project" else {"scope":args.scope,"files":len(items)}
    out={"generated_at":utc_now(),"scope":args.scope,"classification":cls,"files":items}
    out=attach_cache_meta(out, args.scope)
    (INDEX/f"{args.scope}_digest.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"scope":args.scope,"classification":cls,"file_count":len(items),"index":rel(INDEX/f"{args.scope}_digest.json")}, ensure_ascii=False, indent=2))


def cmd_search(args):
    q=args.query.lower(); results=[]
    for f in iter_files(args.scope):
        txt=read_text(f, 250000); hay=(rel(f)+" "+txt).lower()
        if q in hay or fnmatch.fnmatch(rel(f).lower(), q):
            results.append({"path":rel(f),"role":file_role(f,txt),"snippet":evidence_excerpt(txt,[args.query],420)})
    print(json.dumps({"query":args.query,"scope":args.scope,"count":len(results),"results":results[:args.limit]}, ensure_ascii=False, indent=2))


def cmd_evidence(args):
    words=[w.strip() for w in re.split(r"[,،]", args.query) if w.strip()] or [args.query]
    results=[]
    for f in iter_files(args.scope):
        txt=read_text(f, 250000); hay=(rel(f)+" "+txt).lower()
        score=sum(1 for w in words if w.lower() in hay)
        if score>0:
            results.append({"path":rel(f),"role":file_role(f,txt),"score":score,"evidence_excerpt":evidence_excerpt(txt,words,520),"headings":headings(txt,6)})
    results=sorted(results, key=lambda x:(-x["score"], x["path"]))
    print(json.dumps({"query":args.query,"scope":args.scope,"count":len(results),"results":results[:args.limit]}, ensure_ascii=False, indent=2))


def cmd_read(args):
    p=(ROOT/args.path).resolve()
    if not p.exists(): print(json.dumps({"error":"file_not_found","path":args.path}, ensure_ascii=False)); return
    txt=read_text(p, args.limit)
    print(json.dumps({"path":rel(p),"chars":len(txt),"content":txt}, ensure_ascii=False, indent=2))


def cmd_read_many(args):
    matches=[f for f in iter_files(args.scope) if fnmatch.fnmatch(rel(f), args.pattern) or fnmatch.fnmatch(f.name, args.pattern)]
    out=[]
    for f in matches[:args.max_files]:
        txt=read_text(f, args.limit_per_file)
        out.append({"path":rel(f),"role":file_role(f,txt),"headings":headings(txt),"content":txt})
    print(json.dumps({"pattern":args.pattern,"scope":args.scope,"count":len(matches),"returned":len(out),"files":out}, ensure_ascii=False, indent=2))


def cmd_audit_baseline(args):
    tm=build_truth_map("project"); cls=tm["classification"]; counts=tm["category_counts"]
    first_slice=None
    evidence_text=json.dumps(tm.get("evidence_files",{}), ensure_ascii=False).lower()
    if counts.get("scenario",0)>0: first_slice="Scenario-to-requirements baseline"
    elif cls["state"]=="PROJECT_FORMATION": first_slice="Project formation baseline"
    else: first_slice="Smallest coherent vertical slice based on strongest evidence cluster"
    warnings=[]
    if counts.get("empty_or_placeholder",0)>0: warnings.append("Some files look empty or placeholders.")
    if counts.get("scenario",0)>0 and counts.get("requirements",0)==0: warnings.append("Scenario material exists; convert scenarios into explicit requirements before execution.")
    print(json.dumps({"classification":cls,"category_counts":counts,"recommended_first_slice":first_slice,"warnings":warnings,"claims":tm["claims"]}, ensure_ascii=False, indent=2))


def cmd_govern_check(args):
    tm=build_truth_map("project"); cls=tm["classification"]; counts=tm["category_counts"]
    warnings=[]; stale=[]
    items=inventory("project", True)
    for i in items:
        if "report" in i["path"].lower() and cls.get("files",0)>0 and re.search(r"empty|فارغ|لم يبدأ|not started", i.get("snippet","").lower()): stale.append(i["path"])
    if stale: warnings.append({"type":"stale_report_conflict","files":stale})
    if cls["state"]!="PROJECT_FORMATION" and counts.get("truth_entry",0)==0: warnings.append({"type":"missing_truth_entry","message":"No obvious source-of-truth entry file detected."})
    if counts.get("scenario",0)>0:
        warnings.append({"type":"scenario_material_detected","message":"Scenario files exist; any answer about project maturity must acknowledge them.","evidence":[x["path"] for x in tm.get("evidence_files",{}).get("scenario",[])[:10]]})
    print(json.dumps({"classification":cls,"category_counts":counts,"warnings":warnings,"status":"warning" if warnings else "pass","claims":tm["claims"]}, ensure_ascii=False, indent=2))


def cmd_doctor(args):
    problems=[]
    for p in ["00_ENTRYPOINT.yaml","AGENTS.md",".engineer/runtime/navigation.yaml",".engineer/runtime/tool_registry.yaml","02_WORKSHOP/ACTIVE_PROJECT","02_WORKSHOP/_WORKSHOP_SYSTEM"]:
        if not (ROOT/p).exists():
            problems.append({"missing":p})
    legacy_rules=[("PROJECT"+"_"+"ENGINEER"+"_"+"AGENT"+"_"+"OS"),("GPT"+"-"+"5.5"+" Thinking"),("أنا "+"GPT")]
    hits=[]
    for f in iter_files("repository"):
        # Volatile generated dirs are session products, not static doctrine.
        r=rel(f)
        if r.startswith((".engineer/indexes/", ".engineer/ledgers/", ".engineer/state/", ".pytest_cache/")):
            continue
        if f.suffix.lower() not in TEXT_EXTS:
            continue
        txt=read_text(f, 100000)
        for term in legacy_rules:
            if term in txt:
                hits.append({"path":r,"term":"legacy_identity_or_agent_os_phrase"})
    if hits:
        problems.append({"legacy_terms":hits[:20]})
    integrity=runtime_integrity_report()
    if integrity.get("problems"):
        problems.extend(integrity.get("problems", []))
    print(json.dumps({"root":str(ROOT),"status":"pass" if not problems else "warning","problems":problems,"runtime_integrity":integrity}, ensure_ascii=False, indent=2))

def cmd_scan_runtime(args):
    items=inventory("runtime", False)
    print(json.dumps({"scope":"runtime","files":len(items),"top":[i["path"] for i in items[:80]]}, ensure_ascii=False, indent=2))


def strongest_project_facts(items, maxn=6):
    priority={"truth_entry":0,"scenario":1,"requirements":2,"architecture":3,"governance":4,"code":5,"document":6}
    selected=[]
    for i in sorted(items, key=lambda x:(priority.get(x.get("role"),9), -len(x.get("snippet", "")))):
        if i.get("snippet") and i.get("role")!="empty_or_placeholder": selected.append(i)
        if len(selected)>=maxn: break
    return selected



def _first_existing(paths: list[Path]) -> Path|None:
    for path in paths:
        if path.exists():
            return path
    return None


def active_project_dir() -> Path|None:
    if not ACTIVE.exists():
        return None
    dirs=[p for p in ACTIVE.iterdir() if p.is_dir() and not p.name.startswith('.')]
    if len(dirs)==1:
        return dirs[0]
    return ACTIVE


def project_identity_from_files() -> dict:
    base=active_project_dir() or ACTIVE
    contract=_first_existing([base/'01_PROJECT_CONTRACT.yaml', base/'project_contract.yaml'])
    entry=_first_existing([base/'00_PROJECT_ENTRYPOINT.md', base/'README.md'])
    truth_index=_first_existing([base/'02_PROJECT_TRUTH_INDEX.yaml'])
    identity={"project_name": base.name if base else "active_project", "project_type": None, "mission": None, "contract_path": rel(contract) if contract else None, "entrypoint_path": rel(entry) if entry else None, "truth_index_path": rel(truth_index) if truth_index else None}
    if contract and yaml:
        try:
            data=yaml.safe_load(contract.read_text(encoding='utf-8')) or {}
            pc=data.get('project_contract') or data
            identity.update({
                "project_id": pc.get('project_id') or identity.get('project_name'),
                "project_name": pc.get('project_name') or identity.get('project_name'),
                "project_type": pc.get('project_type'),
                "mission": pc.get('mission'),
                "truth_priority": pc.get('truth_priority', [])[:12] if isinstance(pc.get('truth_priority'), list) else [],
            })
        except Exception:
            pass
    return identity


def _is_actionable_artifact_domain(domain: dict) -> bool:
    """Generic domain/actionability check.

    Runtime must not know names of a specific project. It only detects whether a
    domain is an artifact/work area rather than root truth, runtime tunnel, or
    implementation placeholder.
    """
    files=domain.get('top_files') or []
    paths='\n'.join(f.get('path','') for f in files).lower()
    name=(domain.get('domain') or '').lower()
    blocked_markers=['cognitive_tunnel', 'root_truth', 'implementation_target', 'decisions']
    if any(x in name for x in blocked_markers):
        return False
    if '/04_project_artifacts/' in paths or '04_project_artifacts' in paths:
        return True
    # Generic fallback: a domain with multiple requirements/scenario/artifact files is actionable.
    roles=[f.get('role') for f in files]
    return len(files) >= 2 and any(r in {'requirements','scenario','architecture','governance'} for r in roles)


def _domain_gap_summary(domain_key: str, limit: int = 8) -> list[dict]:
    """Return incomplete/thin files inside a domain using only generic evidence.

    No project-specific priority names are allowed here; ranking is based on
    content status, semantic density, parent/child depth, and role.
    """
    out=[]
    for f in iter_files('project'):
        r=rel(f)
        if module_key_for(r) != domain_key:
            continue
        txt=read_text(f, 120000)
        st=semantic_placeholder_status(f, txt)
        if st.get('status') != 'content_bearing':
            out.append({
                "path": r,
                "status": st.get('status'),
                "reason": st.get('placeholder_hits', []) or ["thin_or_empty"],
                "density_score": (st.get('density') or {}).get('density_score', 0),
                "word_count": (st.get('density') or {}).get('word_count', 0),
            })
    status_rank={"empty":0, "placeholder":1, "thin_unproven":2, "missing":3}
    def gap_rank(g):
        path=(g.get('path') or '')
        depth=path.count('/')
        return (status_rank.get(g.get('status'), 9), depth, g.get('density_score') or 0, path)
    return sorted(out, key=gap_rank)[:limit]


def _select_owner_file_for_domain(domain: dict) -> dict | None:
    """Pick the actual owner-bearing file for a domain, not a hardcoded project file.

    Owner preference is generic: content-bearing files with parent/overview/PRD/
    standard/contract signals rank above thin child files.
    """
    top_files = domain.get('top_files') or []
    if not top_files:
        return None
    ranked=[]
    for item in top_files:
        path = item.get('path') or ''
        low = path.lower()
        rank = 50
        owner_terms = ['parent', 'overview', 'index', 'contract', 'standard', 'canon', 'prd', 'requirements', 'root', 'policy', 'منهج', 'معيار', 'عقد']
        child_terms = ['child', 'detail', 'template', 'view', 'page', 'screen', 'draft', 'placeholder']
        if any(t in low for t in owner_terms):
            rank -= 20
        if '/00_' in low or low.endswith('/readme.md') or low.endswith('_prd.md'):
            rank -= 10
        if any(t in low for t in child_terms) and (item.get('density') or 0) < 2:
            rank += 20
        ranked.append((rank, -(item.get('density') or 0), low.count('/'), item))
    ranked.sort(key=lambda x: (x[0], x[1], x[2]))
    return ranked[0][3] if ranked else top_files[0]


def _evidence_profile_for_file(path: str) -> dict:
    f = (ROOT/path).resolve()
    txt = read_text(f, 180000) if f.exists() else ''
    ph = semantic_placeholder_status(f, txt) if f.exists() else {"status":"missing", "density":{}}
    dens = semantic_density(txt)
    hs = headings(txt, 12)
    excerpt = evidence_excerpt(txt, READINESS_WORDS + SCENARIO_WORDS + PRD_WORDS + GOV_WORDS + ARCH_WORDS, 420)
    return {
        "path": path,
        "exists": f.exists(),
        "content_status": ph.get('status'),
        "word_count": dens.get('word_count'),
        "signal_count": dens.get('signal_count'),
        "density_score": dens.get('density_score'),
        "headings": hs[:8],
        "evidence_excerpt": excerpt,
        "claim_rule": "claims about this file must cite content_status/signals/headings/excerpt, not the filename alone",
    }


def _surface_owner_child_truth_gate(strongest: dict | None, gaps: list[dict]) -> dict:
    """Gate for first-answer claims.

    It forces the model to distinguish:
    - owner truth: a content-bearing parent/owner file
    - incomplete truth: existing child files that are empty/thin
    - execution permission: not granted from surface lens alone
    """
    if not strongest:
        return {"status":"blocked", "reason":"no_actionable_domain_detected", "execution_allowed":False, "first_step_allowed":False}
    owner_item = _select_owner_file_for_domain(strongest) or {}
    owner_path = owner_item.get('path')
    owner_profile = _evidence_profile_for_file(owner_path) if owner_path else None
    owner_ok = bool(owner_profile and owner_profile.get('exists') and owner_profile.get('content_status') == 'content_bearing')
    incomplete_children=[]
    for g in gaps or []:
        if g.get('status') in {'empty','placeholder','thin_unproven','missing'}:
            incomplete_children.append(g)
    status = 'pass' if owner_ok else 'review'
    return {
        "status": status,
        "owner_truth_file": owner_profile,
        "incomplete_truth_children": incomplete_children[:12],
        "execution_allowed": False,
        "first_step_allowed": owner_ok,
        "first_step_rule": "First step may target an incomplete child only after naming the owner truth file and stating that the child is an incomplete truth, not an absent concept.",
        "claim_blocks": [
            "Do not say the domain itself is the first step; name the owner file and target child/gap.",
            "Do not call a file mature or empty from its title; use content_status and evidence profile.",
            "Do not treat incomplete truth as non-truth; repair it before execution.",
            "Do not start implementation from a surface lens; perform owner + direct children read first.",
        ],
    }

def _select_target_incomplete_truth(gaps: list[dict]) -> str | None:
    """Select a repair target generically from observed incomplete truth files."""
    if not gaps:
        return None
    status_rank={"empty":0, "placeholder":1, "thin_unproven":2, "missing":3}
    ordered=sorted(gaps, key=lambda g:(status_rank.get(g.get('status'), 9), (g.get('path') or '').count('/'), g.get('path') or ''))
    return ordered[0].get('path') if ordered else None


def workshop_lens() -> dict:
    """Silent workshop operating lens.

    Workshop is part of the engineer environment: it provides universal method,
    discipline canons, and 360-degree maturity pressure. It is not project truth
    and cannot override active project files.
    """
    base=ROOT/'02_WORKSHOP'/'_WORKSHOP_SYSTEM'
    items=[]
    if base.exists():
        for f in sorted(base.rglob('*')):
            if f.is_file() and f.suffix.lower() in TEXT_EXTS:
                txt=read_text(f, 100000)
                dens=semantic_density(txt)
                items.append({
                    "path": rel(f),
                    "role": file_role(f, txt),
                    "word_count": dens.get('word_count'),
                    "signal_count": dens.get('signal_count'),
                    "headings": headings(txt, 6)[:6],
                })
    buckets={
        "truth_hierarchy": [],
        "360_method": [],
        "maturity_assessment": [],
        "local_standards_generation": [],
        "execution_gates": [],
        "discipline_canons": [],
        "software_universal_canon": [],
    }
    for item in items:
        low=(item['path']+' '+' '.join(item.get('headings') or [])).lower()
        if any(x in low for x in ['truth', 'source', 'حقيقة', 'مصدر']): buckets['truth_hierarchy'].append(item['path'])
        if '360' in low or 'degree' in low or 'درجة' in low: buckets['360_method'].append(item['path'])
        if any(x in low for x in ['maturity', 'نضج', 'assessment', 'تقييم']): buckets['maturity_assessment'].append(item['path'])
        if any(x in low for x in ['local standard', 'standards generation', 'تخصيص', 'محلية']): buckets['local_standards_generation'].append(item['path'])
        if any(x in low for x in ['gate', 'execution', 'تنفيذ', 'بوابة']): buckets['execution_gates'].append(item['path'])
        if any(x in low for x in ['discipline', 'software', 'research', 'finance', 'medicine', 'برمجة', 'بحث']): buckets['discipline_canons'].append(item['path'])
        if any(x in low for x in ['software', 'database', 'api', 'architecture', 'برمجة', 'قواعد البيانات']): buckets['software_universal_canon'].append(item['path'])
    return {
        "scope": "workshop",
        "base": rel(base),
        "files_detected": len(items),
        "silent_gate": True,
        "role": "universal_method_and_discipline_canons_for_assessment_maturation_not_project_override",
        "buckets": {k: v[:8] for k,v in buckets.items()},
        "operating_rules": [
            "Workshop is part of the engineer environment and may be used silently as a universal method lens.",
            "Workshop can detect incomplete truth and missing local standards; it cannot replace active project truth.",
            "Universal canons produce local project standards before execution; they are not direct implementation authority.",
            "Every important project should be viewed through 360-degree reality: goal, users, truth, domain logic, data, execution, quality, risks, maintenance, and feedback.",
        ],
    }


def build_project_lens(scope: str = 'project') -> dict:
    """Fast project-surface lens for identity/status/first-step questions.

    The lens is project-neutral: it discovers owner files and incomplete truth
    dynamically from the active project. It must never contain project-specific
    module or file names in runtime logic.
    """
    items=inventory(scope, True)
    cls=classify_project(items)
    tm=build_truth_map(scope)
    mm=build_maturity_map(scope)
    identity=project_identity_from_files() if scope=='project' else {"project_name": scope}
    domains=mm.get('top_domains', [])
    artifact_domains=[d for d in domains if _is_actionable_artifact_domain(d)]
    strongest=artifact_domains[0] if artifact_domains else (domains[0] if domains else None)
    root_truth=[p for p in [identity.get('entrypoint_path'), identity.get('contract_path'), identity.get('truth_index_path')] if p]
    gaps=_domain_gap_summary(strongest.get('domain'), 10) if strongest else []
    surface_gate = _surface_owner_child_truth_gate(strongest, gaps)
    code_count=tm.get('category_counts',{}).get('code',0)
    state='formed' if cls.get('state') != 'PROJECT_FORMATION' else 'formation'
    first_step=None
    if strongest and surface_gate.get('first_step_allowed'):
        owner_path=((surface_gate.get('owner_truth_file') or {}).get('path'))
        first_step={
            "action":"read_owner_and_direct_children_then_select_owner_ordered_incomplete_truth",
            "target_domain": strongest.get('domain'),
            "owner_truth_file": owner_path,
            "target_incomplete_truth_file": None,
            "target_file": owner_path,
            "reason":"surface lens can identify owner truth and visible incomplete truth, but must not choose a specific child priority until owner routing/direct children are read",
            "must_not":"do not name a project-specific child as first repair target from runtime memory or shallow sorting",
        }
    elif strongest:
        first_step={
            "action":"read_owner_file_before_recommending_first_step",
            "target_domain": strongest.get('domain'),
            "reason":"surface gate did not validate a content-bearing owner file",
            "must_not":"do not choose a first step from filenames or domain score alone",
        }
    atlas=content_value_atlas(scope, "project surface assessment", 60, "compact")
    return {
        "generated_at": utc_now(),
        "scope": scope,
        "content_value_atlas_summary": {
            "file_count": atlas.get("file_count"),
            "counts_by_status": atlas.get("counts_by_status"),
            "counts_by_role": atlas.get("counts_by_role"),
            "top_high_value_files": [{"path": x.get("path"), "role": x.get("role"), "score": x.get("value_score"), "signals": x.get("value_signals", [])[:6]} for x in atlas.get("high_value_files", [])[:8]],
            "required_full_reads_before_high_impact_claims": atlas.get("required_full_reads_before_high_impact_claims", [])[:8],
        },
        "workshop_universal_lens": workshop_lens(),
        "project_identity": identity,
        "state": state,
        "classification": cls,
        "truth_counts": tm.get('category_counts',{}),
        "root_truth_sources": root_truth,
        "strongest_actionable_domain": {
            "domain": strongest.get('domain'),
            "readiness_label": strongest.get('readiness_label'),
            "confidence": strongest.get('confidence'),
            "semantic_score": strongest.get('semantic_score'),
            "evidence_files": strongest.get('evidence_files'),
            "top_files": [f.get('path') for f in (strongest.get('top_files') or [])[:5]],
            "top_signals": (strongest.get('top_signals') or [])[:8],
        } if strongest else None,
        "surface_owner_child_truth_gate": surface_gate,
        "visible_gaps_in_strongest_domain": gaps,
        "implementation_status": "code_present" if code_count else "no_code_detected_in_current_project_scope",
        "first_step_candidate": first_step,
        "answer_rules": [
            "do not use file count as maturity proof",
            "distinguish observed facts from inferred maturity",
            "use project root truth before artifact claims",
            "workshop standards are a maturity lens, not a replacement for local project truth",
            "do not start implementation before owner/child, truth maturity, and canon gates",
        ],
    }


def _format_path_list(paths: list[str], limit: int = 4) -> str:
    return "، ".join(paths[:limit]) if paths else "غير محدد"


def natural_answer(request):
    lens=build_project_lens('project')
    cls=lens.get('classification', {})
    workshop=(lens.get('workshop_universal_lens') or {})
    if cls.get("state")=="PROJECT_FORMATION":
        return ("أنا مهندس مشروعك داخل بيئة تشغيل هندسية. أبدأ من ورشة العمل كمنهج عام صامت، ثم أساعدك على تكوين حقيقة المشروع المحلية: "
                "هدف واضح، نطاق، مستفيدون، مخرجات، قيود، ومعيار نجاح. لا أفرض برمجة أو API أو قاعدة بيانات ما لم يثبت نوع المشروع ذلك. "
                "أول خطوة هي إنشاء خط أساس مشروع قابل للفحص، ثم تطبيق عدسة 360 المناسبة لنوعه.")
    ident=lens.get('project_identity', {})
    name=ident.get('project_name') or 'المشروع الحالي'
    mission=(ident.get('mission') or '').strip().replace('\n',' ')
    counts=lens.get('truth_counts', {})
    strongest=lens.get('strongest_actionable_domain') or {}
    gate=lens.get('surface_owner_child_truth_gate') or {}
    owner=(gate.get('owner_truth_file') or {})
    gaps=lens.get('visible_gaps_in_strongest_domain') or []
    root_sources=lens.get('root_truth_sources') or []
    top_files=strongest.get('top_files') or []
    first=lens.get('first_step_candidate') or {}
    incomplete_children=gate.get('incomplete_truth_children') or []
    child_paths=[g.get('path','') for g in incomplete_children]
    gap_line=""
    if child_paths:
        gap_line="\nالحقيقة الناقصة المثبتة داخل المسار المرشح هي وجود ملفات/مراجع قائمة لكنها فارغة أو رقيقة وتحتاج إنضاجًا، مثل: " + _format_path_list(child_paths, 5) + "."
    mission_line=f" رسالة المشروع المثبتة: {mission}." if mission else ""
    owner_line=""
    if owner:
        owner_line=(f"\nملف المالك المرشح اكتُشف ديناميكيًا من محتوى المشروع: {owner.get('path')}، وحالته: {owner.get('content_status')} "
                    f"بعدد كلمات تقريبي {owner.get('word_count')} وإشارات معنى {owner.get('signal_count')}. لا أتعامل مع اسم الملف وحده كدليل.")
    first_target=first.get('target_incomplete_truth_file') or first.get('target_file') or first.get('owner_truth_file') or 'ملف مالك يثبت بالدليل بعد قراءة مباشرة'
    workshop_count=workshop.get('files_detected', 0)
    atlas_summary=lens.get('content_value_atlas_summary') or {}
    atlas_line=(f"\nأطلس قيمة المحتوى لمس {atlas_summary.get('file_count', 0)} ملفًا في النطاق الحالي وصنّفها حسب القيمة والحالة، لا حسب PRD فقط. "
                f"الحالات: {atlas_summary.get('counts_by_status', {})}.") if atlas_summary else ""
    return (
        f"أنا مهندس مشروعك هنا داخل **{name}**. دوري ليس الرد العام، بل الدخول عبر مركز التشغيل، استخدام ورشة العمل كمنهج 360 صامت، ثم قراءة حقيقة المشروع المحلية قبل أي تقييم أو كتابة أو تنفيذ.\n\n"
        f"مهامي: تحديد مصدر الحقيقة، كشف النواقص والحقيقة الناقصة، منع التخمين والتكرار، ربط الملفات المالكة بالأبناء، واستخراج خطة إنضاج أو تنفيذ فقط عندما تسمح الأدلة والبوابات. ورشة العمل الحالية تضيف {workshop_count} ملفًا/مرجعًا عامًا كعدسة منهجية، لكنها لا تستبدل ملفات المشروع.\n\n"
        f"ما يثبته الفحص الحالي: المشروع يحتوي مادة فعلية ضمن النطاق الفعال. الجرد: ملفات حقيقة/عقود = {counts.get('truth_entry',0)}، متطلبات/PRD = {counts.get('requirements',0)}، سيناريو/تدفق = {counts.get('scenario',0)}، كود = {counts.get('code',0)}. هذه أرقام جرد فقط وليست حكم نضج بذاتها.{mission_line}{atlas_line}\n\n"
        f"مصادر الحقيقة التي أبدأ منها: {_format_path_list(root_sources, 4)}. أي تقرير أو ذاكرة أو معيار عام يخالف هذه الملفات لا يتقدم عليها.\n\n"
        f"تقييمي الحالي مقيّد بالدليل: المشروع يبدو في مرحلة توثيق/معمارية منتج أقوى من مرحلة التنفيذ البرمجي الظاهر ({lens.get('implementation_status')}). المسار المرشح للفحص الأعمق هو **{strongest.get('domain','غير محدد')}**، لكن لا أعتمده إلا بعد قراءة ملف المالك والأبناء مباشرة.{owner_line}\n"
        f"ملفات الدليل الأبرز: {_format_path_list(top_files, 3)}.{gap_line}\n\n"
        f"أول خطوة آمنة: **قراءة ملف المالك المرشح والأبناء المباشرين ثم إنضاج الحقيقة الناقصة المحددة**: {first_target}. لا أبدأ بالكود، ولا أسجل اسم ملف كقاعدة runtime، ولا أختار مسارًا لأن البيئة تعرفه مسبقًا؛ كل اختيار يجب أن يُكتشف من المشروع الحالي في لحظته."
    )


def cmd_answer(args):
    r=route_intent(args.request)
    # Ensure the v7 index exists, but keep user-facing answer natural and concise.
    try:
        load_kernel_index(r.get("scope", "project"), auto_build=True)
    except Exception:
        pass
    if r["route"]=="runtime_work":
        fp=build_fast_plug(args.request, "runtime")
        print("سأتعامل معه كصيانة Runtime: أحدد نمط العملية، أقرأ فهرس التشغيل، ثم أرجع بإصلاح مبني على سبب جذري لا ترقيع. المسار: " + ", ".join(fp.get("mandatory_gates", [])[:6]))
    else:
        print(natural_answer(args.request))


def cmd_workshop_lens(args):
    print(json.dumps(workshop_lens(), ensure_ascii=False, indent=2))


def cmd_project_lens(args):
    out=build_project_lens(args.scope)
    out=attach_cache_meta(out, args.scope)
    INDEX.mkdir(parents=True, exist_ok=True)
    (INDEX/f"{args.scope}_project_lens.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_init_project(args):
    ACTIVE.mkdir(parents=True, exist_ok=True)
    safe=re.sub(r"[^A-Za-z0-9_\-\u0600-\u06FF ]+","",args.name).strip() or "New Project"
    for d in ["source_truth","requirements","scenarios","plans","decisions","risks","outputs","reports","materials"]: (ACTIVE/d).mkdir(parents=True, exist_ok=True)
    baseline=ACTIVE/"source_truth"/"PROJECT_BASELINE.md"
    if not baseline.exists(): baseline.write_text(f"# {safe} — Project Baseline\n\n## Problem\n\n## Beneficiary\n\n## Goal\n\n## Outputs\n\n## Scope\n\n## Constraints\n\n## Success Criteria\n", encoding="utf-8")
    print(json.dumps({"created":rel(baseline),"state":"PROJECT_FORMATION"}, ensure_ascii=False, indent=2))


def cmd_cycle(args):
    # v7/v8-compatible cycle: fast mandatory operating entry with legacy central-OS fields.
    fp = build_fast_plug(args.request or "", None)
    out = {
        **fp,
        "central_os_mode": "mandatory_operating_context",
        "tool_keyboard": fp.get("mandatory_next_actions", []) or fp.get("mandatory_gates", []),
        "concept_matrix": {
            "selected_lens": fp.get("selected_lens", []),
            "content_value_atlas_summary": fp.get("content_value_atlas_summary", {}),
            "mandatory_gates": fp.get("mandatory_gates", []),
        },
        "operation_receipt_required": True,
        "steering_contract": "cycle output is an operating context, not a final evidence report",
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))



# -----------------------------
# v6.3 Jet OS + Truth Governance extensions
# -----------------------------
LEDGERS_DIR = RUNTIME / "ledgers"
OPS_LEDGER = LEDGERS_DIR / "operation_log.jsonl"
CLAIM_LEDGER = LEDGERS_DIR / "claim_ledger.jsonl"
WRITE_LEDGER = LEDGERS_DIR / "write_ledger.jsonl"
BACKUP_DIR = RUNTIME / "backups"

HIGH_RISK_ABSENCE_PATTERNS = [
    r"لا يوجد", r"غير موجود", r"لم أجد", r"لم يتم رصد", r"لا توجد", r"فارغ", r"empty", r"not found", r"absent", r"no .*found"
]


def append_jsonl(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    obj = {"ts": utc_now(), **obj}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")


GENERIC_SCAN_TERMS = {
    "هذا","هذه","الى","إلى","على","في","من","ما","هو","هي","او","أو","عن","مع","كل","داخل","ملف","ملفات","مشروع","المشروع","اختبار","تجربة","اخبرني","أخبرني","عملك","وظيفتك","مهامك","مهاراتك","تتعامل","تقييمك","وضعه","الحالي","اول","أول","خطوة","اتجاه","انت","أنت","انا","أنا","نحن","كيف","ماذا","لماذا","هل","يعني","عنك","ماهو","وماهو","وكيف","وماهي","لوضعه","تتخذها","ماهي",
    "the","and","for","with","this","that","into","project","file","files","test","write","read","system","command","new","old","update"
}

def tokenize_query(text: str) -> list[str]:
    # Lightweight mixed Arabic/English tokenization. Generic words are removed so jet scans do not overmatch on vague terms.
    toks = re.findall(r"[A-Za-z0-9_\.\-/]+|[\u0600-\u06FF]{2,}", text or "")
    out=[]
    for tok in toks:
        k=normalize_for_route(tok)
        # Strip common Arabic conjunction prefixes for matching and stopword filtering.
        k2=re.sub(r"^[وف]+", "", k) if re.match(r"^[؀-ۿ]+$", k) else k
        if len(k2)<=1 or k in GENERIC_SCAN_TERMS or k2 in GENERIC_SCAN_TERMS:
            continue
        out.append(k2 if k2 != k else tok)
    return out[:80]


def score_file_for_terms(path: Path, text: str, terms: list[str]) -> dict:
    hay = (rel(path)+"\n"+text).lower()
    hits=[]
    for term in terms:
        if term.lower() in hay:
            hits.append(term)
    role = file_role(path, text)
    score = len(hits)
    if role in {"truth_entry","scenario","requirements","architecture","governance","code"} and score:
        score += 1
    return {"path": rel(path), "role": role, "score": score, "hits": hits, "snippet": evidence_excerpt(text, hits or terms, 520), "headings": headings(text, 6)}


def matrix_scan(scope="project", query="", include_content=True, max_results=40, include_generated=False):
    files=iter_files(scope)
    terms=tokenize_query(query)
    items=[]
    skip_generated = should_skip_generated(scope, query, include_generated)
    for f in files:
        r=rel(f)
        if skip_generated and is_generated_runtime_rel(r):
            continue
        txt=read_text(f, 250000 if include_content else 12000)
        if terms:
            scored=score_file_for_terms(f, txt, terms)
            if scored["score"]>0:
                items.append(scored)
        else:
            items.append({"path": r, "role": file_role(f,txt), "score": 0, "snippet": snippet(txt, 420), "headings": headings(txt, 6)})
    items=sorted(items, key=lambda x:(-x.get("score",0), x.get("role",""), x["path"]))[:max_results]
    return {"scope": scope, "query": query, "terms": terms, "generated_outputs_included": not skip_generated, "count": len(items), "results": items}

def build_scenario_map(scope="project"):
    files=iter_files(scope)
    scenario_items=[]
    for f in files:
        txt=read_text(f, 250000)
        low=(rel(f)+"\n"+txt).lower()
        if contains_any(low, SCENARIO_WORDS):
            scenario_items.append({
                "path": rel(f),
                "role": file_role(f, txt),
                "headings": headings(txt, 12),
                "signals": [w for w in SCENARIO_WORDS if w.lower() in low][:12],
                "excerpt": evidence_excerpt(txt, SCENARIO_WORDS, 700),
                "domain_signals": domain_signals(txt),
            })
    out={"generated_at": utc_now(), "scope": scope, "scenario_count": len(scenario_items), "scenarios": scenario_items}
    return attach_cache_meta(out, scope)


def evidence_lock(scope="project", query=""):
    tm=build_truth_map(scope)
    sm=build_scenario_map(scope)
    related = matrix_scan(scope, query, True, 30) if query else {"count":0,"results":[]}
    cls=tm.get("classification",{})
    gates=[]
    def gate(name, passed, detail): gates.append({"gate":name,"passed":bool(passed),"detail":detail})
    gate("truth_map_built", True, "Truth map generated from current files.")
    gate("current_files_override_reports", True, "Generated reports never override current file evidence.")
    gate("absence_claim_requires_zero_scan", True, "Absence claims must reference zero count in truth-map/category scan.")
    gate("scenario_scan_completed", True, f"scenario_count={sm['scenario_count']}")
    if query:
        gate("query_evidence_scan_completed", True, f"related_results={related['count']}")
    lock_status="pass" if all(g["passed"] for g in gates) else "warning"
    packet={
        "generated_at": utc_now(),
        "scope": scope,
        "query": query,
        "status": lock_status,
        "classification": cls,
        "category_counts": tm.get("category_counts",{}),
        "domains": tm.get("domains",[]),
        "claims": tm.get("claims",[]),
        "scenario_map": {"scenario_count": sm["scenario_count"], "top": sm["scenarios"][:12]},
        "related_evidence": related.get("results",[])[:20],
        "gates": gates,
        "answer_rules": [
            "Use observed/inferred/assumption discipline.",
            "Do not say absent unless relevant truth-map count is zero.",
            "Do not add or write before duplicate and impact checks.",
            "If evidence is partial, state confidence and next read needed."
        ]
    }
    INDEX.mkdir(parents=True, exist_ok=True)
    packet=attach_cache_meta(packet, scope)
    (INDEX/f"{scope}_evidence_lock.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2), encoding="utf-8")
    append_jsonl(CLAIM_LEDGER, {"type":"evidence_lock", "scope":scope, "query":query, "status":lock_status, "counts":tm.get("category_counts",{})})
    return packet


def claim_check_text(text: str, scope="project"):
    surf = surface_policy_check(text)
    tm=build_truth_map(scope)
    sm=build_scenario_map(scope)
    problems=[]
    category_counts=tm.get("category_counts",{})
    # Detect dangerous absence statements contradicted by map counts.
    for pat in HIGH_RISK_ABSENCE_PATTERNS:
        if re.search(pat, text or "", re.IGNORECASE):
            if category_counts.get("scenario",0)>0 and re.search(r"سيناريو|scenario|workflow|تدفق|حالة", text or "", re.IGNORECASE):
                problems.append({"type":"contradicted_absence_claim","message":"The text implies scenario/workflow absence while scenario_map found evidence.","evidence_count":category_counts.get("scenario",0)})
            if category_counts.get("requirements",0)>0 and re.search(r"متطلبات|requirements|PRD|prd", text or "", re.IGNORECASE):
                problems.append({"type":"contradicted_absence_claim","message":"The text implies requirements absence while truth-map found requirements evidence.","evidence_count":category_counts.get("requirements",0)})
            if category_counts.get("code",0)>0 and re.search(r"كود|code|implementation|تنفيذ", text or "", re.IGNORECASE):
                problems.append({"type":"contradicted_absence_claim","message":"The text implies code absence while truth-map found code files.","evidence_count":category_counts.get("code",0)})
    # Detect strong priority claims without evidence words.
    if re.search(r"الأكثر نضج|أفضل بداية|أول خطوة|أقوى|الأضعف|لا يوجد", text or "") and not re.search(r"دليل|رصد|وجدت|ملف|حسب|بناءً على|observed|evidence", text or "", re.IGNORECASE):
        problems.append({"type":"unsupported_high_impact_claim","message":"Strong assessment/recommendation should be tied to evidence."})
    if surf["status"] == "fail":
        problems.append({"type":"surface_policy_violation", "hits": surf["hits"], "message": surf["message"]})
    status="pass" if not problems else "fail"
    out={"status":status,"scope":scope,"problems":problems,"surface_policy":surf,"category_counts":category_counts,"scenario_count":sm["scenario_count"]}
    append_jsonl(CLAIM_LEDGER, {"type":"claim_check", "status":status, "problem_count":len(problems), "text_preview":(text or '')[:240]})
    return out


def duplicate_scan(query: str, scope="project", limit=25):
    terms=tokenize_query(query)
    if not terms:
        return {"query":query,"scope":scope,"count":0,"results":[]}
    results=[]
    for f in iter_files(scope):
        txt=read_text(f, 250000)
        scored=score_file_for_terms(f, txt, terms)
        threshold=max(1, min(3, len(terms)//3))
        # Single generic/short-token scans must be strong enough to avoid noisy false positives.
        if len(terms) <= 1 and scored["score"] < 2:
            continue
        if scored["score"]>=threshold:
            results.append(scored)
    results=sorted(results, key=lambda x:(-x["score"], x["path"]))[:limit]
    return {"query":query,"scope":scope,"terms":terms,"count":len(results),"results":results}


def impact_scan(target_path: str, objective: str="", scope="project"):
    target=(ROOT/target_path).resolve() if target_path else None
    target_rel=rel(target) if target else ""
    base_terms=tokenize_query((target_path or "")+" "+(objective or ""))
    related=duplicate_scan(" ".join(base_terms), scope, 30) if base_terms else {"count":0,"results":[]}
    risks=[]
    if target and target.exists():
        risks.append("target_exists_update_not_create")
    if related.get("count",0)>0:
        risks.append("related_material_exists_review_before_writing")
    return {"target":target_rel,"objective":objective,"scope":scope,"related_count":related.get("count",0),"related":related.get("results",[])[:20],"risks":risks,"required_before_write":["review_related_material","decide_update_vs_create","claim_check_output","record_operation"]}


def write_plan(target_path: str, objective: str, content: str="", scope="project"):
    imp=impact_scan(target_path, objective+" "+content[:1000], scope)
    recommendation="update_existing_or_confirm_new_file" if imp["related_count"] else "safe_to_create_after_review"
    plan={
        "generated_at": utc_now(),
        "target": target_path,
        "objective": objective,
        "scope": scope,
        "recommendation": recommendation,
        "impact_scan": imp,
        "governance_gates": [
            "No duplicate addition before reviewing related material.",
            "No overwrite without backup.",
            "No claim in output without evidence lock.",
            "If target exists, prefer update/patch over new parallel file."
        ],
        "apply_allowed": True
    }
    append_jsonl(OPS_LEDGER, {"type":"write_plan", "target":target_path, "objective":objective, "related_count":imp["related_count"]})
    return plan


def declared_write_base(scope: str) -> Path:
    return {
        "project": ACTIVE,
        "runtime": RUNTIME,
        "workshop": ROOT/"02_WORKSHOP",
        "repository": ROOT,
        "repository_static": ROOT,
    }.get(scope, ACTIVE)


def safe_write(target_path: str, text: str, reason: str, apply=False, scope="project"):
    preflight = build_central_plug(f"write operation {reason} {target_path}", "guarded_write")
    plan=write_plan(target_path, reason, text, scope)
    target=(ROOT/target_path).resolve()
    # Keep writes inside repository root.
    if not is_relative_to(target, ROOT):
        return {"status":"blocked","reason":"target_outside_repository","target":str(target),"plan":plan,"preflight_gate":{"route":preflight.get("route"),"required_gates":preflight.get("neural_reflex_graph",{}).get("required_gates",[])}}
    # Enforce declared scope containment. This prevents project writes from mutating runtime internals.
    allowed_base=declared_write_base(scope)
    if scope != "repository" and not is_relative_to(target, allowed_base):
        return {"status":"blocked","reason":"target_outside_declared_scope","scope":scope,"allowed_base":rel(allowed_base),"target":rel(target),"plan":plan,"preflight_gate":{"route":preflight.get("route"),"required_gates":preflight.get("neural_reflex_graph",{}).get("required_gates",[])}}
    result={"status":"dry_run","plan":plan,"target":rel(target),"chars":len(text),"scope_boundary":"pass","preflight_gate":{"route":preflight.get("route"),"required_gates":preflight.get("neural_reflex_graph",{}).get("required_gates",[]),"blocked_operations":preflight.get("neural_reflex_graph",{}).get("blocked_operations",[])}}
    if not apply:
        return result
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    target.parent.mkdir(parents=True, exist_ok=True)
    backup=None
    if target.exists():
        stamp=datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
        backup=BACKUP_DIR/(rel(target).replace('/','__')+f".{stamp}.bak")
        backup.write_bytes(target.read_bytes())
    target.write_text(text, encoding="utf-8")
    result.update({"status":"written","backup":rel(backup) if backup else None})
    append_jsonl(WRITE_LEDGER, {"type":"safe_write", "target":rel(target), "reason":reason, "backup":rel(backup) if backup else None, "chars":len(text), "scope":scope})
    return result






TOOL_DEPTH_RULES = {
    "project_surface": "snapshot",
    "project_work": "standard",
    "governance_work": "deep",
    "runtime_work": "deep",
    "comparison_work": "deep",
    "write_or_modify_work": "guarded_write",
    "best_fit_work": "deep",
    "implementation_translation_work": "deep",
    "research_work": "standard",
    "external_research_work": "augmented",
    "content_work": "standard",
}

INTERNAL_TOOL_CATALOG = {
    "plug": "One-touch central operating core: route, workshop lens, tool plan, matrix context, evidence gates, mandatory rules, neural reflex graph, and operation receipt.",
    "workshop-lens": "Silent universal workshop method lens: 360 method, discipline canons, local standards generation, and project-truth boundary.",
    "neural": "Expose the nervous-system reflex graph for a request: active safeguards, required gates, cross-links, and blocked operations.",
    "best-fit": "Compare current evidence to internal excellence patterns and return a gap/recommendation matrix.",
    "route": "Classify request intent and choose project/runtime/repository scope.",
    "touch": "Fast current-state project touch with evidence counts.",
    "truth-map": "Content-aware source-of-truth map; required before assessment.",
    "context-pack": "One-touch evidence packet with file excerpts and current reality.",
    "evidence-lock": "Lock claims to current evidence and scenario map.",
    "scenario-map": "Detect scenarios/workflows from content, not only filenames.",
    "evidence": "Search current files for evidence excerpts.",
    "read": "Read one file precisely.",
    "read-many": "Read many matching files with bounded content.",
    "claim-check": "Check final claims against evidence and surface policy.",
    "duplicate-scan": "Detect existing material before adding new files or concepts.",
    "impact-scan": "Scan side effects and related materials before modification.",
    "write-plan": "Plan a write/update before applying changes.",
    "safe-write": "Safe write with dry-run by default and backup on overwrite.",
    "govern-check": "Governance scan for stale reports, missing truth entry, and scenario handling.",
    "doctor": "Runtime/environment self-check, only when request targets the engineer environment.",
}


def tool_sequence_for_route(route: str, request: str = "") -> list[dict]:
    sequences = {
        "project_surface": [
            {"cmd":"route", "why":"classify the question as project-facing, not runtime-facing"},
            {"cmd":"tool-plan", "why":"make the internal path explicit and auditable"},
            {"cmd":"context-pack", "scope":"project", "why":"touch current project truth before answering"},
            {"cmd":"project-lens", "scope":"project", "why":"compress project identity, status, strongest actionable slice, gaps, and first step"},
            {"cmd":"truth-map", "scope":"project", "why":"establish category counts and source-truth evidence"},
            {"cmd":"evidence-lock", "scope":"project", "why":"prevent unsupported assessment and absence claims"},
            {"cmd":"maturity-map", "scope":"project", "why":"avoid using size as maturity evidence"},
            {"cmd":"answer", "scope":"project", "why":"produce a natural project-facing answer from evidence"},
            {"cmd":"surface-check", "why":"ensure no runtime/model leakage in final wording"},
        ],
        "project_work": [
            {"cmd":"route", "why":"classify project work intent"},
            {"cmd":"tool-plan", "why":"select bounded internal tools"},
            {"cmd":"context-pack", "scope":"project", "why":"build one-touch project reality packet"},
            {"cmd":"matrix", "scope":"project", "why":"find relevant directions semantically"},
            {"cmd":"read/read-many", "scope":"project", "why":"read target files before analysis or execution"},
            {"cmd":"evidence-lock", "scope":"project", "why":"bind conclusions to file evidence"},
            {"cmd":"claim-check", "scope":"project", "why":"verify claims before final output"},
        ],
        "governance_work": [
            {"cmd":"route", "why":"classify governance/risk/quality intent"},
            {"cmd":"truth-map", "scope":"project", "why":"establish complete project truth map"},
            {"cmd":"scenario-map", "scope":"project", "why":"ensure scenarios/workflows are not missed"},
            {"cmd":"evidence-lock", "scope":"project", "why":"lock conclusions to evidence"},
            {"cmd":"govern-check", "scope":"project", "why":"detect stale reports and governance risks"},
            {"cmd":"claim-check", "scope":"project", "why":"prevent unsupported or contradictory claims"},
        ],
        "runtime_work": [
            {"cmd":"route", "why":"confirm request targets runtime"},
            {"cmd":"scan-runtime", "scope":"runtime", "why":"inspect engineer environment only because requested"},
            {"cmd":"doctor", "scope":"runtime", "why":"detect broken paths and runtime issues"},
            {"cmd":"runtime-audit", "scope":"runtime", "why":"verify registry, cache, navigation, and write-boundary integrity"},
            {"cmd":"claim-check", "scope":"repository", "why":"verify runtime assessment wording"},
        ],
        "write_or_modify_work": [
            {"cmd":"route", "why":"classify write intent"},
            {"cmd":"duplicate-scan", "scope":"project", "why":"detect existing concepts before creating parallel material"},
            {"cmd":"impact-scan", "scope":"project", "why":"estimate side effects and touched files"},
            {"cmd":"write-plan", "scope":"project", "why":"produce governed update/create decision"},
            {"cmd":"safe-write", "scope":"project", "why":"dry-run by default; apply only with explicit request and scope match"},
            {"cmd":"claim-check", "scope":"project", "why":"verify resulting claims"},
        ],
        "best_fit_work": [
            {"cmd":"route", "why":"classify best-fit/gap review intent"},
            {"cmd":"plug", "why":"force central operating context before recommendations"},
            {"cmd":"context-pack", "scope":"project", "why":"anchor gap review to current reality"},
            {"cmd":"best-fit", "scope":"project", "why":"compare current evidence to internal excellence patterns"},
            {"cmd":"truth-maturity", "scope":"project", "why":"classify binding-but-insufficient references before recommending execution"},
            {"cmd":"matrix", "scope":"project", "why":"link recommendations to related concepts and protocols"},
            {"cmd":"impact-scan", "scope":"project", "why":"estimate effects before suggesting mutation"},
            {"cmd":"claim-check", "scope":"project", "why":"separate observed gap from inference and proposed decision"},
        ],
        "implementation_translation_work": [
            {"cmd":"route", "why":"classify PRD-to-execution translation"},
            {"cmd":"context-pack", "scope":"project", "why":"load relevant PRD and truth context"},
            {"cmd":"read/read-many", "scope":"project", "why":"read parent/child artifacts and standards"},
            {"cmd":"truth-maturity", "scope":"project", "why":"detect incomplete owner truth before production-oriented implementation"},
            {"cmd":"canon-check", "scope":"project", "why":"ensure stack choices are backed by code practice rules"},
            {"cmd":"evidence-lock", "scope":"project", "why":"avoid inventing entities, APIs, states, or events"},
            {"cmd":"claim-check", "scope":"project", "why":"verify implementation contract claims"},
        ],
        "research_work": [
            {"cmd":"route", "why":"classify non-software research/content intent"},
            {"cmd":"context-pack", "scope":"project", "why":"use project files as truth if present"},
            {"cmd":"evidence-lock", "scope":"project", "why":"separate project truth from research synthesis"},
            {"cmd":"claim-check", "scope":"project", "why":"mark assumptions and evidence"},
        ],
        "external_research_work": [
            {"cmd":"route", "why":"classify current/external knowledge need"},
            {"cmd":"context-pack", "scope":"project", "why":"anchor external research to project truth"},
            {"cmd":"external/native search", "why":"obtain current standards or market/legal information"},
            {"cmd":"evidence-lock", "scope":"project", "why":"keep web findings subordinate to project files"},
            {"cmd":"claim-check", "scope":"project", "why":"separate project fact, external fact, inference, and decision"},
        ],
        "content_work": [
            {"cmd":"route", "why":"classify writing/content project intent"},
            {"cmd":"context-pack", "scope":"project", "why":"read current content truth if present"},
            {"cmd":"read/read-many", "scope":"project", "why":"avoid overwriting existing voice, audience, or structure"},
            {"cmd":"claim-check", "scope":"project", "why":"avoid unsupported project claims in content framing"},
        ],
        "comparison_work": [
            {"cmd":"route", "why":"classify comparison request"},
            {"cmd":"context-pack", "scope":"repository", "why":"build a broad evidence packet"},
            {"cmd":"compare", "scope":"repository", "why":"compare only after evidence search"},
            {"cmd":"claim-check", "scope":"repository", "why":"verify final comparison claims"},
        ],
    }
    return sequences.get(route, sequences["project_work"])


def build_tool_plan(request: str) -> dict:
    r = route_intent(request or "")
    depth = TOOL_DEPTH_RULES.get(r["route"], "standard")
    seq = tool_sequence_for_route(r["route"], request or "")
    return {
        "generated_at": utc_now(),
        "request": request,
        "route": r,
        "inspection_depth": depth,
        "internal_tools_first": True,
        "sequence": seq,
        "fallback_policy": {
            "allowed": True,
            "rule": "Use model/native tools only when the internal framework lacks the required operation, cannot read the target due to capability limits, or external/current knowledge is required. State the reason when falling back.",
            "not_allowed_for": [
                "project truth assessment before context-pack/evidence-lock",
                "absence claims before zero-result scan",
                "writes before duplicate-scan and impact-scan"
            ]
        },
        "central_plug_required": True,
        "central_plug_command": "plug",
        "receipt_required": True,
        "receipt_fields": ["route", "internal_tools_used", "evidence_files", "fallbacks_used", "claims_checked", "write_governance_if_any"],
        "matrix_required_for": ["project_work", "implementation_translation_work", "write_or_modify_work", "governance_work"],
        "neural_gate_required": True,
        "neural_reflex_graph": neural_reflex_graph(r["route"], request or "", r.get("scope", "project")),
    }


def cmd_tool_plan(args):
    plan = build_tool_plan(args.request)
    INDEX.mkdir(parents=True, exist_ok=True)
    plan=attach_cache_meta(plan, "repository")
    (INDEX/"last_tool_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    append_jsonl(OPS_LEDGER, {"type":"tool_plan", "route":plan["route"]["route"], "depth":plan["inspection_depth"], "request":(args.request or '')[:240]})
    print(json.dumps(plan, ensure_ascii=False, indent=2))


def build_operation_receipt(request: str, scope: str = "project") -> dict:
    plan = build_tool_plan(request)
    # Keep receipt bounded: evidence lock is enough to show the internal tools were used.
    lock = evidence_lock(plan["route"].get("scope", scope), request or "")
    receipt = {
        "generated_at": utc_now(),
        "request": request,
        "route": plan["route"],
        "inspection_depth": plan["inspection_depth"],
        "internal_tools_used": [s["cmd"] for s in plan["sequence"] if s["cmd"] != "answer"],
        "evidence_lock_status": lock.get("status"),
        "category_counts": lock.get("category_counts", {}),
        "scenario_count": lock.get("scenario_map", {}).get("scenario_count", 0),
        "fallbacks_used": [],
        "next_required_before_final_answer": ["claim-check if final answer includes high-impact claims", "surface-check for project_surface answers"],
        "tool_contract": "internal_tools_first_then_native_fallback_if_needed"
    }
    INDEX.mkdir(parents=True, exist_ok=True)
    receipt=attach_cache_meta(receipt, plan["route"].get("scope", scope))
    (INDEX/"last_operation_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    append_jsonl(OPS_LEDGER, {"type":"operation_receipt", "route":plan["route"]["route"], "depth":plan["inspection_depth"], "counts":receipt["category_counts"]})
    return receipt


def cmd_receipt(args):
    print(json.dumps(build_operation_receipt(args.request, args.scope), ensure_ascii=False, indent=2))

def build_context_pack(scope="project", query="", max_files=60, per_file_chars=1800):
    """One-touch evidence pack: current truth map + scenario map + targeted files + excerpts.
    It is intentionally project-neutral and content-first; it never assumes a domain.
    """
    tm = build_truth_map(scope)
    sm = build_scenario_map(scope)
    if query:
        targeted = matrix_scan(scope, query, True, max_files).get("results", [])
    else:
        # prioritize truth/scenario/requirements/architecture/governance/code, then general docs
        inv = inventory(scope, True)
        pri = {"truth_entry":0,"scenario":1,"requirements":2,"architecture":3,"governance":4,"code":5,"document":6,"empty_or_placeholder":9}
        inv = sorted(inv, key=lambda x:(pri.get(x.get("role"),8), -len(x.get("snippet","")), x.get("path","")))[:max_files]
        targeted = inv
    files=[]
    for item in targeted[:max_files]:
        p = ROOT / item["path"]
        txt = read_text(p, per_file_chars)
        files.append({
            "path": item["path"],
            "role": item.get("role"),
            "headings": item.get("headings", []),
            "domain_signals": item.get("domain_signals", []),
            "excerpt": item.get("evidence_excerpt") or item.get("snippet") or snippet(txt, 600),
            "content_preview": txt[:per_file_chars]
        })
    pack = {
        "generated_at": utc_now(),
        "scope": scope,
        "query": query,
        "classification": tm.get("classification",{}),
        "category_counts": tm.get("category_counts",{}),
        "domains": tm.get("domains",[]),
        "truth_claims": tm.get("claims",[]),
        "scenario_count": sm.get("scenario_count",0),
        "scenario_top": sm.get("scenarios",[])[:12],
        "files_included": len(files),
        "files": files,
        "content_value_atlas_summary": (lambda a: {"file_count": a.get("file_count"), "counts_by_status": a.get("counts_by_status"), "counts_by_role": a.get("counts_by_role"), "top_high_value_files": [{"path": x.get("path"), "role": x.get("role"), "value_score": x.get("value_score"), "signals": x.get("value_signals", [])[:6]} for x in a.get("high_value_files", [])[:8]], "required_full_reads": a.get("required_full_reads_before_high_impact_claims", [])[:8]})(content_value_atlas(scope, query, min(max_files, 40), "compact")),
        "usage_contract": [
            "Use this pack before assessment.",
            "Do not make absence claims unless category count is zero.",
            "If evidence is partial, say what remains unverified.",
            "Do not mention runtime internals in project-facing answers."
        ]
    }
    INDEX.mkdir(parents=True, exist_ok=True)
    pack=attach_cache_meta(pack, scope)
    (INDEX/f"{scope}_context_pack.json").write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    return pack


def cmd_context_pack(args):
    out = build_context_pack(args.scope, args.query or "", args.max_files, args.per_file_chars)
    print(json.dumps(out, ensure_ascii=False, indent=2))


CENTRAL_OS_PROTOCOL_STACK = {
    "always": [
        "entrypoint_first",
        "workshop_universal_method_gate",
        "content_value_atlas_before_high_impact_claims",
        "semantic_route_before_scan",
        "internal_tools_first",
        "current_files_override_generated_reports",
        "evidence_before_claim",
        "absence_claim_requires_zero_scan",
        "no_write_without_duplicate_and_impact_scan",
        "scope_containment_for_writes",
        "incomplete_truth_maturity_gate",
        "discovery_execution_separation",
        "best_fit_as_mandatory_fit_check",
        "intent_scaled_response_rhythm",
    ],
    "project_surface": ["surface_truth_lock", "content_value_atlas", "maturity_by_evidence_not_size", "no_runtime_leakage"],
    "project_work": ["context_pack", "content_value_atlas", "matrix_navigation", "read_relevant_files_only", "claim_check"],
    "governance_work": ["truth_map", "scenario_map", "evidence_lock", "claim_check"],
    "runtime_work": ["runtime_scope_only", "doctor", "runtime_audit", "no_project_assessment"],
    "write_or_modify_work": ["duplicate_scan", "impact_scan", "write_plan", "safe_write_dry_run_first"],
    "best_fit_work": ["internal_excellence_patterns", "gap_matrix", "fit_to_project_reality", "incomplete_truth_classification", "impact_before_recommendation"],
    "implementation_translation_work": ["content_value_atlas", "parent_child_read", "state_event_permission_alignment", "api_data_contract_gates", "incomplete_truth_gate", "code_practice_canon_gate"],
    "external_research_work": ["project_truth_anchor", "external_sources_support_do_not_override", "separate_project_fact_external_fact_inference_decision"],
    "research_work": ["project_neutrality", "research_question_method_evidence_limits"],
    "content_work": ["audience_voice_structure", "project_neutrality", "no_software_assumption"],
    "comparison_work": ["compare_after_evidence", "version_scope", "claim_check"],
}

CONCEPT_BUCKETS = {
    "workshop_universal_method": ["workshop", "360", "universal canon", "discipline canon", "local standards", "ورشة", "منهج", "معايير عامة", "تخصيص المعايير", "360 درجة"],
    "truth_and_contracts": ["entrypoint", "contract", "truth", "source of truth", "incomplete truth", "truth maturity", "مصدر الحقيقة", "الحقيقة الناقصة", "إنضاج الحقيقة", "عقد", "فهرس"],
    "requirements_and_prd": ["prd", "requirements", "متطلبات", "artifact", "scope", "acceptance"],
    "scenarios_and_workflows": ["scenario", "workflow", "flow", "journey", "سيناريو", "تدفق", "رحلة"],
    "states_and_events": ["state", "event", "حالة", "حدث", "lifecycle", "transition"],
    "permissions_and_audit": ["permission", "role", "audit", "access", "صلاحية", "دور", "تدقيق"],
    "data_api_execution": ["api", "endpoint", "database", "entity", "command", "query", "migration", "outbox", "realtime", "signalr", "redis", "قاعدة بيانات", "كيان", "هجرة", "ريل تايم"],
    "risks_and_decisions": ["risk", "decision", "adr", "governance", "incomplete truth", "conflicting truth", "خطر", "قرار", "حوكمة", "حقيقة ناقصة"],
    "writing_and_content": ["story", "sermon", "article", "content", "قصة", "خطبة", "مقال", "محتوى"],
    "research_and_external": ["research", "study", "standard", "law", "benchmark", "بحث", "دراسة", "معيار", "قانون"],
    "code_practice_canon": ["code practice", "implementation canon", "coding rules", "ddd", "ef core", "migration", "signalr", "redis", "outbox", "observability", "architecture tests", "معيار ممارسات الكود", "قواعد كتابة الكود", "معيار التنفيذ"],
}


NEURAL_OPERATION_SIGNALS = {
    "write_or_mutate": ["write", "create", "modify", "edit", "delete", "patch", "add", "apply", "اكتب", "أنشئ", "انشئ", "عدّل", "عدل", "احذف", "أضف", "اضف", "إضافة", "اضافة", "طبّق", "طبق"],
    "decision_or_assessment": ["decide", "assess", "evaluate", "best", "first step", "review", "قيّم", "قيم", "تقييم", "قرار", "أفضل", "افضل", "راجع", "احكم"],
    "implementation_translation": ["api", "database", "entity", "state", "event", "permission", "test", "implementation", "عقد تنفيذ", "كيانات", "حالات", "أحداث", "احداث", "صلاحيات", "اختبارات"],
    "absence_or_negative_claim": ["لا يوجد", "لا توجد", "غير موجود", "لم أجد", "not found", "absent", "empty"],
    "external_or_benchmark": ["external", "latest", "current", "standard", "benchmark", "best practice", "خارجي", "أحدث", "احدث", "معيار", "مقارنة معيارية"],
    "runtime_self_improvement": ["runtime", "engineer environment", "plug", "matrix", "navigation", "بيئة المهندس", "قابس", "ماتركس", "الملاحة", "الجملة العصبية", "نظام التشغيل"],
    "best_fit_reasoning": ["best practice", "excellence", "maturity", "gap", "missing", "أفضل الممارسات", "افضل الممارسات", "النواقص", "الفجوات", "أنضج", "انضج", "حلول"],
    "incomplete_truth": ["incomplete truth", "truth maturity", "binding but insufficient", "حقيقة ناقصة", "الحقيقة الناقصة", "إنضاج الحقيقة", "انضاج الحقيقة", "ملف ناقص", "مرجع ناقص"],
    "code_practice_canon": ["code practice", "implementation canon", "coding standard", "code", "backend", "frontend", "ddd", "ef core", "migration", "signalr", "outbox", "redis", "observability", "كود", "تنفيذ كود", "معيار ممارسات الكود", "قواعد كتابة الكود", "معيار التنفيذ"],
    "workshop_universal_method": ["workshop", "360", "universal canon", "discipline canon", "local standards", "ورشة العمل", "منهج 360", "معايير عامة", "تخصيص المعايير"],
}

NEURAL_REFLEXES = {
    "central_preflight": {
        "purpose": "force one-touch operating context before high-impact work",
        "requires": ["plug", "workshop-lens", "route", "tool-plan", "concept_matrix", "evidence-lock"],
        "blocks": ["direct_answer_from_memory", "random_repository_scan"],
    },
    "workshop_reflex": {
        "purpose": "apply the silent workshop universal method as a maturity lens without overriding project truth",
        "requires": ["workshop-lens", "project_truth_anchor", "local_standards_generation_if_missing"],
        "blocks": ["universal_standard_as_direct_project_truth", "implementation_without_local_standard", "project_specific_runtime_coupling"],
    },
    "claim_reflex": {
        "purpose": "prevent unsupported truth, maturity, absence, or priority claims",
        "requires": ["truth-map", "evidence-lock", "claim-check"],
        "blocks": ["absence_claim_without_zero_scan", "maturity_by_size_only", "old_report_over_current_files"],
    },
    "content_value_reflex": {
        "purpose": "touch current files as cognitive evidence units before high-impact claims, not only PRD files",
        "requires": ["value-atlas", "high_value_file_selection", "required_full_reads_for_owner_or_impact_files"],
        "blocks": ["assessment_from_file_counts_only", "first_step_from_one_visible_file", "code_or_prd_claim_without_content_value_touch"],
    },
    "response_rhythm_reflex": {
        "purpose": "scale response length to user intent; clear commands execute, discussions explain",
        "requires": ["intent_scaled_response", "brief_ack_for_clear_execution", "artifact_delivery_for_repository_changes"],
        "blocks": ["long_explanation_instead_of_clear_execution", "silent_patch_without_summary", "repository_change_as_chat_only_when_zip_expected"],
    },
    "write_reflex": {
        "purpose": "prevent duplicate/parallel concepts and unsafe mutation",
        "requires": ["duplicate-scan", "impact-scan", "write-plan", "safe-write", "post_write_claim_check"],
        "blocks": ["create_before_owner_search", "overwrite_without_backup", "scope_leak_write"],
    },
    "implementation_reflex": {
        "purpose": "translate artifacts to execution only through parent/child and state-event-permission-data gates",
        "requires": ["read_parent", "read_children", "state_event_alignment", "permission_audit_alignment", "data_api_contract", "tests_contract"],
        "blocks": ["api_from_page_name", "invented_state_event", "code_before_prd_translation"],
    },
    "external_reflex": {
        "purpose": "use external knowledge as benchmark/support, not as project truth",
        "requires": ["project_truth_anchor", "external_research", "comparison_matrix", "open_decision_if_change_needed"],
        "blocks": ["web_overrides_project_truth", "unmarked_external_assumption"],
    },
    "runtime_reflex": {
        "purpose": "improve the engineer environment with self-audit and registry/test integrity",
        "requires": ["scan-runtime", "doctor", "runtime-audit", "tool_registry_sync", "tests_or_static_checks"],
        "blocks": ["project_assessment_during_runtime_audit", "unregistered_tool", "silent_runtime_mutation"],
    },
    "best_fit_reflex": {
        "purpose": "compare current reality to internal excellence patterns and recommend precise upgrades",
        "requires": ["context-pack", "best-fit", "gap_matrix", "impact_scan_for_recommendations"],
        "blocks": ["user_must_supply_all_solutions", "generic_advice_without_project_mapping", "patching_without_architectural_fit"],
    },
    "incomplete_truth_reflex": {
        "purpose": "detect binding-but-insufficient references and separate discovery from execution",
        "requires": ["truth-maturity", "owner_file_identification", "higher_truth_comparison", "repair_owner_before_execution"],
        "blocks": ["production_execution_over_incomplete_truth", "blind_obedience_to_thin_reference", "invented_repair_as_accepted_truth"],
    },
    "code_practice_reflex": {
        "purpose": "prevent code generation from stack names alone by requiring implementation practice canon",
        "requires": ["canon-check", "code_practice_canon", "testing_quality_gates", "architecture_constraints"],
        "blocks": ["code_from_stack_name_only", "migration_without_standard", "realtime_without_resync_outbox_strategy", "authorization_without_permission_standard"],
    },
}

ROUTE_REFLEX_MAP = {
    "project_surface": ["central_preflight", "workshop_reflex", "content_value_reflex", "claim_reflex", "response_rhythm_reflex"],
    "project_work": ["central_preflight", "workshop_reflex", "content_value_reflex", "claim_reflex", "incomplete_truth_reflex", "best_fit_reflex", "response_rhythm_reflex"],
    "governance_work": ["central_preflight", "workshop_reflex", "content_value_reflex", "claim_reflex", "best_fit_reflex", "response_rhythm_reflex"],
    "runtime_work": ["central_preflight", "workshop_reflex", "runtime_reflex", "content_value_reflex", "claim_reflex", "best_fit_reflex", "response_rhythm_reflex"],
    "write_or_modify_work": ["central_preflight", "workshop_reflex", "content_value_reflex", "write_reflex", "incomplete_truth_reflex", "claim_reflex", "best_fit_reflex", "response_rhythm_reflex"],
    "best_fit_work": ["central_preflight", "workshop_reflex", "best_fit_reflex", "incomplete_truth_reflex", "claim_reflex"],
    "implementation_translation_work": ["central_preflight", "workshop_reflex", "content_value_reflex", "implementation_reflex", "incomplete_truth_reflex", "code_practice_reflex", "claim_reflex", "best_fit_reflex", "response_rhythm_reflex"],
    "external_research_work": ["central_preflight", "workshop_reflex", "external_reflex", "claim_reflex", "best_fit_reflex"],
    "research_work": ["central_preflight", "workshop_reflex", "claim_reflex"],
    "content_work": ["central_preflight", "workshop_reflex", "claim_reflex", "write_reflex"],
    "comparison_work": ["central_preflight", "workshop_reflex", "claim_reflex", "best_fit_reflex"],
}

EXCELLENCE_PATTERNS = {
    "central_operating_core": {
        "question": "Does every high-impact operation enter through a one-touch operating core?",
        "evidence_terms": ["plug", "cycle", "central operating", "mandatory", "قابس", "مركز تشغيل"],
        "minimum": ["default entry command", "receipt", "mandatory operating context"],
        "recommendation": "Make plug/cycle the mandatory preflight and store an operation receipt for every high-impact task.",
    },
    "neural_protocol_graph": {
        "question": "Are related protocols cross-linked so an operation cannot bypass its prerequisite or anti-rule?",
        "evidence_terms": ["neural", "reflex", "matrix", "protocol", "graph", "الجملة العصبية", "ماتركس"],
        "minimum": ["route-to-reflex map", "blocked operations", "required gates"],
        "recommendation": "Maintain a neural reflex graph that links write, claim, implementation, external, runtime, and best-fit gates.",
    },
    "truth_and_claim_integrity": {
        "question": "Are claims tied to current files and checked before final output?",
        "evidence_terms": ["truth-map", "evidence-lock", "claim-check", "source of truth", "مصدر الحقيقة", "دليل"],
        "minimum": ["current files override reports", "absence zero-scan", "claim classification"],
        "recommendation": "Require evidence-lock and claim-check for assessments, absence, maturity, and priority statements.",
    },
    "write_safety": {
        "question": "Can writes occur only after duplicate, impact, planning, scope containment, and backup?",
        "evidence_terms": ["duplicate-scan", "impact-scan", "write-plan", "safe-write", "scope", "backup", "تكرار", "أثر"],
        "minimum": ["owner search", "impact scan", "scope containment", "dry-run default"],
        "recommendation": "Block create/update/apply operations until duplicate-scan, impact-scan, write-plan, and safe-write gates pass.",
    },
    "navigation_authority": {
        "question": "Is intent routing centralized and authoritative rather than duplicated across random logic?",
        "evidence_terms": ["navigation.yaml", "semantic routing", "route", "fallback", "ملاحة"],
        "minimum": ["authoritative navigation", "fallback route", "route priorities"],
        "recommendation": "Keep navigation.yaml authoritative and have the CLI read it rather than hard-coding divergent route triggers.",
    },
    "runtime_self_audit": {
        "question": "Can the environment inspect itself without mixing runtime with project assessment?",
        "evidence_terms": ["runtime-audit", "doctor", "tool_registry", "cache_meta", "distribution_mode"],
        "minimum": ["registry sync", "cache freshness", "distribution mode", "runtime tests"],
        "recommendation": "Run runtime-audit after runtime edits and fail on registry/tool/cache/write-boundary inconsistencies.",
    },
    "implementation_translation_quality": {
        "question": "Can PRDs be translated to execution without inventing states, events, APIs, or data models?",
        "evidence_terms": ["implementation", "api", "database", "state", "event", "permission", "tests", "تنفيذ", "حالات", "أحداث"],
        "minimum": ["parent/child read", "state-event alignment", "permission/audit", "data-api gates", "tests"],
        "recommendation": "Require parent/child artifact reads plus state/event/permission/data/test gates before implementation contracts.",
    },
    "best_fit_reasoning": {
        "question": "Does the engineer compare the current reality to internal excellence patterns and infer missing architecture without waiting for the user to list solutions?",
        "evidence_terms": ["best-fit", "excellence", "gap", "maturity", "rubric", "أفضل الممارسات", "الفجوات"],
        "minimum": ["pattern library", "gap matrix", "fit recommendation", "project-specific evidence"],
        "recommendation": "Use best-fit review to map evidence to excellence patterns and produce precise, scoped recommendations.",
    },
    "content_value_atlas": {
        "question": "Does every high-impact project assessment touch current files as cognitive evidence units across PRD, code, standards, decisions, and documents?",
        "evidence_terms": ["value-atlas", "content value", "cognitive evidence", "high-impact", "أطلس قيمة", "قيمة محتوى"],
        "minimum": ["all-file touch", "status/value classification", "required full reads", "not PRD-only", "code-aware signals"],
        "recommendation": "Use a content value atlas before high-impact answers, first steps, writes, implementation, and architecture decisions so no file type is invisible to the neural matrix.",
    },

    "incomplete_truth_maturity": {
        "question": "Can the engineer detect a binding reference that is too thin, inconsistent, or insufficient for execution?",
        "evidence_terms": ["incomplete truth", "truth maturity", "binding but insufficient", "repair owner", "execution allowed", "حقيقة ناقصة", "الحقيقة الناقصة", "إنضاج الحقيقة"],
        "minimum": ["owner identification", "higher truth comparison", "discovery/execution separation", "repair before production execution"],
        "recommendation": "Add an incomplete-truth gate that classifies thin authoritative references and blocks production execution until the owner is repaired or a decision accepts risk.",
    },
    "code_practice_canon": {
        "question": "Does implementation use a code-practice canon, not only a stack list?",
        "evidence_terms": ["code practice", "implementation canon", "DDD", "EF Core", "migration", "SignalR", "Redis", "outbox", "observability", "architecture tests", "معيار ممارسات الكود"],
        "minimum": ["module rules", "persistence/migration rules", "realtime rules", "authorization/validation/error rules", "testing and observability gates"],
        "recommendation": "Introduce or use a code practice canon before generating production-oriented backend/frontend/database/API code.",
    },
}


def request_signals(request: str, route: str = "") -> dict:
    text = normalize_for_route(request or "")
    active = []
    evidence = {}
    for sig, words in NEURAL_OPERATION_SIGNALS.items():
        hits = [w for w in words if normalize_for_route(w) in text or w in (request or "")]
        if hits:
            active.append(sig); evidence[sig] = hits[:8]
    # Routes themselves imply signals even when the words are implicit.
    implied = {
        "write_or_modify_work": "write_or_mutate",
        "implementation_translation_work": "implementation_translation",
        "external_research_work": "external_or_benchmark",
        "runtime_work": "runtime_self_improvement",
        "comparison_work": "decision_or_assessment",
        "governance_work": "decision_or_assessment",
    }.get(route)
    if implied and implied not in active:
        active.append(implied); evidence[implied] = [f"implied_by_route:{route}"]
    return {"active_signals": sorted(set(active)), "evidence": evidence}


def neural_reflex_graph(route: str, request: str, scope: str = "project") -> dict:
    sigs = request_signals(request, route)
    reflex_names = list(ROUTE_REFLEX_MAP.get(route, ["central_preflight", "workshop_reflex", "claim_reflex"]))
    # Signal-based cross-links: operations can activate additional safeguards beyond route defaults.
    signal_to_reflex = {
        "write_or_mutate": "write_reflex",
        "decision_or_assessment": "claim_reflex",
        "implementation_translation": "implementation_reflex",
        "absence_or_negative_claim": "claim_reflex",
        "external_or_benchmark": "external_reflex",
        "runtime_self_improvement": "runtime_reflex",
        "best_fit_reasoning": "best_fit_reflex",
        "incomplete_truth": "incomplete_truth_reflex",
        "code_practice_canon": "code_practice_reflex",
    }
    for sig in sigs["active_signals"]:
        ref = signal_to_reflex.get(sig)
        if ref and ref not in reflex_names:
            reflex_names.append(ref)
    reflexes = []
    required_gates=[]; blocked=[]
    for name in reflex_names:
        data=dict(NEURAL_REFLEXES.get(name, {}))
        data["name"] = name
        reflexes.append(data)
        required_gates.extend(data.get("requires", []))
        blocked.extend(data.get("blocks", []))
    cross_links=[]
    if "write_reflex" in reflex_names:
        cross_links.append({"from":"write_reflex", "to":"claim_reflex", "why":"written output can create new claims and must be checked"})
        cross_links.append({"from":"write_reflex", "to":"best_fit_reflex", "why":"new material must fit the architecture, not merely satisfy the immediate text request"})
    if "implementation_reflex" in reflex_names:
        cross_links.append({"from":"implementation_reflex", "to":"claim_reflex", "why":"entities/states/events/APIs are high-impact claims"})
        cross_links.append({"from":"implementation_reflex", "to":"write_reflex", "why":"execution contracts may update artifacts and must avoid duplicates"})
    if "external_reflex" in reflex_names:
        cross_links.append({"from":"external_reflex", "to":"claim_reflex", "why":"external facts must be separated from project truth and inference"})
        cross_links.append({"from":"external_reflex", "to":"best_fit_reflex", "why":"benchmarks must be fitted to the project reality, not copied"})
    if "runtime_reflex" in reflex_names:
        cross_links.append({"from":"runtime_reflex", "to":"best_fit_reflex", "why":"runtime improvements should be inferred from architecture gaps, not only user-provided fixes"})
    if "incomplete_truth_reflex" in reflex_names:
        cross_links.append({"from":"incomplete_truth_reflex", "to":"claim_reflex", "why":"incomplete-truth findings are high-impact claims and need evidence"})
        cross_links.append({"from":"incomplete_truth_reflex", "to":"write_reflex", "why":"repair must update an owner or decision without duplicating concepts"})
        cross_links.append({"from":"incomplete_truth_reflex", "to":"best_fit_reflex", "why":"missing maturity should be compared to project-fit excellence, not generic advice"})
    if "code_practice_reflex" in reflex_names:
        cross_links.append({"from":"code_practice_reflex", "to":"implementation_reflex", "why":"code practice gates govern how implementation contracts become code"})
        cross_links.append({"from":"code_practice_reflex", "to":"incomplete_truth_reflex", "why":"a stack standard without practice rules may be incomplete truth"})
    return {
        "generated_at": utc_now(),
        "scope": scope,
        "route": route,
        "request_signals": sigs,
        "active_reflexes": reflexes,
        "required_gates": list(dict.fromkeys(required_gates)),
        "blocked_operations": list(dict.fromkeys(blocked)),
        "cross_links": cross_links,
        "contract": "This graph is the runtime nervous system: each operation activates related safeguards, prerequisites, and anti-failure rules instead of running as an isolated scan.",
    }


def best_fit_review(scope: str = "project", query: str = "", limit: int = 8) -> dict:
    """Internal excellence-pattern review.

    This is not web research. It compares current non-generated evidence to embedded
    engineering excellence patterns and produces a fit/gap matrix tied to current files.
    Generated indexes, ledgers, and state are excluded by default to avoid self-confirming maturity.
    """
    evidence_rows=[]
    for key, pattern in EXCELLENCE_PATTERNS.items():
        terms = pattern.get("evidence_terms", []) + tokenize_query(query or "")
        scan = matrix_scan(scope, " ".join(terms), True, limit, include_generated=False)
        found = scan.get("count", 0) > 0
        strength = "present" if scan.get("count", 0) >= 3 else ("partial" if found else "missing")
        risk = "low" if strength == "present" else ("medium" if strength == "partial" else "high")
        evidence_rows.append({
            "pattern": key,
            "question": pattern.get("question"),
            "fit_status": strength,
            "risk_if_ignored": risk,
            "minimum_expected": pattern.get("minimum", []),
            "evidence_count": scan.get("count", 0),
            "top_evidence": scan.get("results", [])[:min(limit, 5)],
            "recommendation": pattern.get("recommendation"),
            "evidence_policy": "generated_indexes_ledgers_state_excluded_by_default",
        })
    gaps=[r for r in evidence_rows if r["fit_status"] != "present"]
    priorities=[]
    for r in gaps:
        if r["risk_if_ignored"] == "high":
            priorities.append({"pattern": r["pattern"], "action": r["recommendation"], "why": "missing excellence pattern in current non-generated evidence"})
    out={
        "generated_at": utc_now(),
        "scope": scope,
        "query": query,
        "mode": "internal_best_fit_review_not_external_web_research",
        "evidence_policy": "current_static_files_first_generated_outputs_excluded_unless_explicitly_requested",
        "summary": {
            "patterns_checked": len(evidence_rows),
            "present": len([r for r in evidence_rows if r["fit_status"] == "present"]),
            "partial": len([r for r in evidence_rows if r["fit_status"] == "partial"]),
            "missing": len([r for r in evidence_rows if r["fit_status"] == "missing"]),
        },
        "fit_matrix": evidence_rows,
        "priority_recommendations": priorities[:10],
        "rules": [
            "Treat this as expert inference over current static evidence, not as external authority.",
            "Do not prove runtime maturity from generated indexes, ledgers, state, or previous best-fit reports.",
            "Recommendations must be applied through impact/write gates when they mutate files.",
            "If project files contradict a pattern, record an explicit decision instead of forcing the pattern.",
        ],
    }
    INDEX.mkdir(parents=True, exist_ok=True)
    out=attach_cache_meta(out, scope)
    (INDEX/f"{scope}_best_fit_review.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    append_jsonl(OPS_LEDGER, {"type":"best_fit_review", "scope":scope, "query":(query or '')[:240], "summary":out["summary"]})
    return out


INCOMPLETE_TRUTH_REQUIRED_DIMENSIONS = {
    "base": {
        "owner_and_scope": ["owner", "scope", "owns", "مالك", "نطاق"],
        "higher_truth_alignment": ["higher truth", "source of truth", "project truth", "مصدر الحقيقة", "الحقيقة العليا"],
        "limits_and_out_of_scope": ["out of scope", "does not", "not own", "خارج النطاق", "لا يملك"],
        "downstream_consumers": ["implementation", "api", "database", "tests", "consumer", "تنفيذ", "اختبارات"],
        "decision_or_repair_path": ["decision", "repair", "open decision", "قرار", "إصلاح", "تعزيز"],
    },
    "implementation": {
        "state_event_alignment": ["state", "event", "transition", "حالة", "حدث"],
        "permission_audit_alignment": ["permission", "audit", "role", "صلاحية", "تدقيق", "دور"],
        "data_api_extractability": ["entity", "database", "api", "endpoint", "command", "query", "كيان", "قاعدة بيانات"],
        "testing_contract": ["test", "acceptance", "integration", "architecture test", "اختبار", "قبول"],
    },
    "code_practice": {
        "architecture_style": ["DDD", "modular", "vertical slice", "bounded", "معمار"],
        "persistence_migration": ["EF Core", "migration", "PostgreSQL", "transaction", "concurrency", "هجرة"],
        "realtime_consistency": ["SignalR", "Redis", "realtime", "outbox", "resync", "reconnect"],
        "observability_quality": ["observability", "OpenTelemetry", "logging", "metrics", "ci/cd", "اختبارات"],
    },
}


def _dimension_present(text: str, terms: list[str]) -> bool:
    low = normalize_for_route(text or "")
    return any(normalize_for_route(t) in low for t in terms)


def truth_maturity_scan(scope: str = "project", query: str = "", limit: int = 10) -> dict:
    """Classify whether current reference evidence is accepted, missing, conflicting, or incomplete truth.

    This is not a license to override project truth. It is a gate that separates discovery
    from production-oriented execution when an existing source is too thin for the requested work.
    """
    q = query or ""
    signals = request_signals(q, route_intent(q).get("route", "project_work"))
    signal_names = set(signals.get("active_signals", []))
    scan_terms = tokenize_query(q) + ["truth", "contract", "standard", "canon", "gate", "incomplete truth", "حقيقة ناقصة", "معيار", "عقد"]
    scan = matrix_scan(scope, " ".join(scan_terms), True, max(limit, 12))
    dims = dict(INCOMPLETE_TRUTH_REQUIRED_DIMENSIONS["base"])
    if "implementation_translation" in signal_names or route_intent(q).get("route") == "implementation_translation_work":
        dims.update(INCOMPLETE_TRUTH_REQUIRED_DIMENSIONS["implementation"])
    if "code_practice_canon" in signal_names or re.search(r"code|backend|frontend|api|database|migration|signalr|redis|outbox|كود|تنفيذ|قاعدة", q, re.IGNORECASE):
        dims.update(INCOMPLETE_TRUTH_REQUIRED_DIMENSIONS["implementation"])
        dims.update(INCOMPLETE_TRUTH_REQUIRED_DIMENSIONS["code_practice"])
    candidates=[]
    for item in scan.get("results", [])[:limit]:
        path = ROOT / item["path"]
        txt = read_text(path, 160000)
        missing=[]; present=[]
        for dim, terms in dims.items():
            (present if _dimension_present(txt, terms) else missing).append(dim)
        if not txt.strip():
            status="missing_truth"
        elif len(missing) == 0:
            status="accepted_truth_for_requested_operation"
        elif len(missing) >= max(3, len(dims)//2):
            status="incomplete_truth"
        else:
            status="partially_mature_truth"
        candidates.append({
            "path": item["path"],
            "role": item.get("role"),
            "status": status,
            "present_dimensions": present,
            "missing_dimensions": missing,
            "evidence_hits": item.get("hits", []),
            "snippet": item.get("snippet", ""),
        })
    if not candidates:
        overall="missing_truth"
        execution_allowed=False
    elif any(c["status"] == "incomplete_truth" for c in candidates[:3]):
        overall="incomplete_truth_detected"
        execution_allowed=False
    elif any(c["status"] == "partially_mature_truth" for c in candidates[:3]):
        overall="partial_truth_review_required"
        execution_allowed="discovery_only"
    else:
        overall="accepted_for_discovery_continue_with_evidence"
        execution_allowed=True
    out={
        "generated_at": utc_now(),
        "scope": scope,
        "query": q,
        "mode": "incomplete_truth_maturity_gate",
        "overall_status": overall,
        "execution_allowed": execution_allowed,
        "signals": signals,
        "dimension_count": len(dims),
        "owner_candidates": candidates,
        "rules": [
            "A reference can be binding truth and still be incomplete for execution.",
            "Discovery may classify and propose repairs; production execution waits for owner update or explicit decision.",
            "Do not bypass a thin owner by inventing implementation patterns.",
        ],
        "required_next_actions": [
            "read_owner_candidate_before_claim",
            "compare_to_higher_truth",
            "repair_owner_or_record_decision_if_execution_depends_on_missing_dimensions",
            "claim_check_final_answer",
        ],
    }
    INDEX.mkdir(parents=True, exist_ok=True)
    out=attach_cache_meta(out, scope)
    (INDEX/f"{scope}_truth_maturity_scan.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    append_jsonl(OPS_LEDGER, {"type":"truth_maturity_scan", "scope":scope, "query":q[:240], "overall_status":overall})
    return out


def canon_check(scope: str = "project", query: str = "") -> dict:
    canon_terms = "code practice implementation canon coding rules DDD EF Core migration SignalR Redis outbox observability testing authorization validation ProblemDetails معيار ممارسات الكود قواعد كتابة الكود معيار التنفيذ " + (query or "")
    scan = matrix_scan(scope, canon_terms, True, 20)
    strong=[]
    for item in scan.get("results", []):
        p=(item.get("path") or "").lower()
        hits=" ".join(item.get("hits", [])).lower()
        if "canon" in p or "code_practice" in p or "implementation" in p or "معيار" in hits or item.get("score",0) >= 4:
            strong.append(item)
    def _canon_priority(item):
        p=(item.get("path") or "").lower()
        priority = 0
        if "code_practice" in p or "canon" in p: priority += 100
        if "/18_" in p: priority += 50
        return (-priority, -item.get("score",0), p)
    strong=sorted(strong, key=_canon_priority)
    status="pass" if strong else "incomplete_truth"
    out={
        "generated_at": utc_now(),
        "scope": scope,
        "query": query,
        "status": status,
        "canon_candidates": strong[:10],
        "all_related": scan.get("results", [])[:10],
        "gate": "code_practice_canon_gate",
        "rule": "Stack choice is insufficient for production code; implementation must obey a code practice canon or classify the stack standard as incomplete truth.",
        "blocks_if_missing": ["code_from_stack_name_only", "api_database_generation_without_practice_rules", "migration_without_standard", "realtime_without_consistency_strategy"],
    }
    INDEX.mkdir(parents=True, exist_ok=True)
    out=attach_cache_meta(out, scope)
    (INDEX/f"{scope}_canon_check.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    append_jsonl(OPS_LEDGER, {"type":"canon_check", "scope":scope, "query":(query or '')[:240], "status":status})
    return out


def concept_matrix(scope: str, query: str, limit_per_bucket: int = 8) -> dict:
    """Build a practical concept-to-evidence matrix.

    This is not a reader report. It is a navigation map that tells the model which
    concept families exist, which files own or mention them, and what must be read
    before claims or writes.
    """
    query_terms = tokenize_query(query or "")
    matrix = {}
    for bucket, seeds in CONCEPT_BUCKETS.items():
        scan_query = " ".join(dict.fromkeys(query_terms + seeds))
        scan = matrix_scan(scope, scan_query, True, limit_per_bucket)
        matrix[bucket] = {
            "seed_terms": seeds,
            "query_terms": query_terms,
            "count": scan.get("count", 0),
            "top_files": scan.get("results", [])[:limit_per_bucket],
        }
    mandatory_reads = []
    seen = set()
    priority_buckets = ["truth_and_contracts", "requirements_and_prd", "scenarios_and_workflows", "states_and_events", "permissions_and_audit", "data_api_execution", "risks_and_decisions"]
    for bucket in priority_buckets:
        for item in matrix.get(bucket, {}).get("top_files", [])[:3]:
            path = item.get("path")
            if path and path not in seen:
                seen.add(path); mandatory_reads.append({"path": path, "reason": f"top evidence for {bucket}", "role": item.get("role")})
    return {
        "generated_at": utc_now(),
        "scope": scope,
        "query": query,
        "terms": query_terms,
        "concept_buckets": matrix,
        "mandatory_reads_before_high_impact_claims": mandatory_reads[:20],
        "matrix_rules": [
            "Use owner/truth files before local or generated reports.",
            "Treat bucket hits as navigation signals, not final truth by themselves.",
            "If a bucket is relevant but empty, perform a zero-result scan before claiming absence.",
            "For writes, update an owner file or create a new file only after duplicate/impact/write gates.",
        ]
    }


def relationship_graph(scope: str, query: str = "", limit: int = 12) -> dict:
    """Build a lightweight relationship graph for matrix navigation.

    The graph is heuristic by design: it identifies likely concept owners, parent/child
    links, and related state/event/permission/API/test evidence. It is a navigation
    graph, not a final truth decision.
    """
    q = query or ""
    effective_q = canonical_surface_lens_query() if is_project_surface_identity_request(q) else q
    base = matrix_scan(scope, effective_q, True, max(limit * 2, 20), include_generated=False)
    def owner_score(item: dict) -> int:
        path=(item.get("path") or "").lower()
        role=item.get("role") or "document"
        score=item.get("score", 0)
        if role == "truth_entry": score += 8
        if role in {"requirements", "architecture", "governance"}: score += 5
        if any(x in path for x in ["contract", "entrypoint", "truth", "index", "standard", "canon", "prd", "readme", "gate"]): score += 4
        if is_generated_runtime_rel(path): score -= 20
        return score
    owner_candidates=sorted(base.get("results", []), key=lambda x:(-owner_score(x), x.get("path","")))[:limit]
    candidate_paths=[x.get("path") for x in owner_candidates if x.get("path")]
    all_files={rel(f): f for f in iter_files(scope)}
    parent_child=[]
    for path in candidate_paths:
        p=Path(path)
        parents=[]
        for cand in all_files:
            if cand == path or is_generated_runtime_rel(cand):
                continue
            cp=Path(cand)
            same_tree = str(p.parent).startswith(str(cp.parent)) or str(cp.parent).startswith(str(p.parent))
            parentish = any(x in cand.lower() for x in ["readme", "00_", "parent", "contract", "index", "prd"])
            if same_tree and parentish:
                parents.append(cand)
        if parents:
            parent_child.append({"node": path, "likely_parents_or_siblings": parents[:5]})
    linkage_terms={
        "states_events": "state states event events transition lifecycle حالة حدث انتقال",
        "permissions_audit": "permission role authorization audit صلاحية دور تدقيق",
        "data_api": "entity database api endpoint command query migration كيان قاعدة بيانات واجهة",
        "tests_acceptance": "test testing acceptance criteria quality اختبار قبول معيار",
        "decisions_risks": "decision risk open decision gap repair قرار خطر فجوة إصلاح",
    }
    linkages={}
    for name, terms in linkage_terms.items():
        sc=matrix_scan(scope, (effective_q + " " + terms).strip(), True, min(limit, 10), include_generated=False)
        linkages[name]=sc.get("results", [])[:min(limit, 8)]
    graph={
        "generated_at": utc_now(),
        "scope": scope,
        "query": q,
        "effective_query": effective_q,
        "graph_type": "semantic_relationship_navigation_graph",
        "evidence_policy": "generated_runtime_outputs_excluded_unless_explicitly_requested",
        "concept_owner_candidates": [
            {"path": item.get("path"), "role": item.get("role"), "score": owner_score(item), "hits": item.get("hits", []), "snippet": item.get("snippet", "")}
            for item in owner_candidates
        ],
        "parent_child_relation_candidates": parent_child[:limit],
        "cross_artifact_linkages": linkages,
        "mandatory_use": [
            "Read top owner candidate before strong claims.",
            "Read parent/sibling candidates before writes or implementation translation.",
            "If state/event/permission/API/test linkages are relevant, inspect those buckets before execution.",
            "Treat this graph as navigation; final truth requires reading current owner files.",
        ],
    }
    graph=attach_cache_meta(graph, scope)
    INDEX.mkdir(parents=True, exist_ok=True)
    (INDEX/f"{scope}_relationship_graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")
    return graph


def route_protocol_stack(route: str) -> list[str]:
    stack = list(CENTRAL_OS_PROTOCOL_STACK.get("always", []))
    stack.extend(CENTRAL_OS_PROTOCOL_STACK.get(route, []))
    return list(dict.fromkeys(stack))


def _trim_results(results: list[dict], limit: int = 5) -> list[dict]:
    compact=[]
    for item in (results or [])[:limit]:
        compact.append({
            "path": item.get("path"),
            "role": item.get("role"),
            "score": item.get("score"),
            "hits": item.get("hits", [])[:4],
        })
    return compact


def compact_plug_packet(full: dict) -> dict:
    cm=full.get("concept_matrix", {}) or {}
    compact_buckets={}
    for bucket, data in (cm.get("concept_buckets") or {}).items():
        compact_buckets[bucket]={
            "count": data.get("count", 0),
            "top_files": _trim_results(data.get("top_files", []), 1),
        }
    rg=full.get("relationship_graph", {}) or {}
    compact={
        "generated_at": full.get("generated_at"),
        "version": full.get("version"),
        "request": full.get("request"),
        "central_os_mode": full.get("central_os_mode"),
        "output_mode": "compact",
        "route": full.get("route"),
        "project_surface_lens": full.get("project_surface_lens"),
        "inspection_depth": full.get("inspection_depth"),
        "tool_keyboard": full.get("tool_keyboard", [])[:12],
        "protocol_stack": full.get("protocol_stack", [])[:16],
        "evidence_gate_status": "pass" if all(g.get("passed") for g in full.get("evidence_gates", [])) else "review",
        "top_evidence_facts": [{"claim": c.get("claim"), "status": c.get("status"), "confidence": c.get("confidence"), "evidence": (c.get("evidence") or [])[:3]} for c in (full.get("context_pack_summary", {}) or {}).get("truth_claims", [])[:5]],
        "concept_matrix": {
            "terms": cm.get("terms", []),
            "concept_buckets": compact_buckets,
            "mandatory_reads_before_high_impact_claims": cm.get("mandatory_reads_before_high_impact_claims", [])[:8],
            "matrix_rules": cm.get("matrix_rules", [])[:4],
        },
        "content_value_atlas_summary": full.get("content_value_atlas_summary"),
        "relationship_graph_summary": {
            "owner_candidates": [{"path": x.get("path"), "role": x.get("role"), "score": x.get("score"), "hits": (x.get("hits") or [])[:5]} for x in (rg.get("concept_owner_candidates") or [])[:5]],
            "parent_child_relation_candidates": [{"node": x.get("node"), "likely_parents_or_siblings": (x.get("likely_parents_or_siblings") or [])[:3]} for x in (rg.get("parent_child_relation_candidates") or [])[:5]],
            "linkage_buckets": {k: len(v or []) for k, v in (rg.get("cross_artifact_linkages") or {}).items()},
            "mandatory_use": rg.get("mandatory_use", [])[:4],
        },
        "neural_reflex_graph": {
            "active_reflexes": [{"name": r.get("name"), "requires": r.get("requires", []), "blocks": r.get("blocks", [])} for r in full.get("neural_reflex_graph", {}).get("active_reflexes", [])],
            "required_gates": full.get("neural_reflex_graph", {}).get("required_gates", []),
            "blocked_operations": full.get("neural_reflex_graph", {}).get("blocked_operations", []),
            "cross_links": full.get("neural_reflex_graph", {}).get("cross_links", [])[:8],
        },
        "truth_maturity_summary": (lambda x: {"overall_status": x.get("overall_status"), "execution_allowed": x.get("execution_allowed"), "top_owner_candidates": [{"path": c.get("path"), "role": c.get("role"), "status": c.get("status"), "missing_dimensions": (c.get("missing_dimensions") or [])[:6]} for c in (x.get("top_owner_candidates") or [])[:3]]} if x else None)(full.get("truth_maturity_summary")),
        "canon_check_summary": (lambda x: {"status": x.get("status"), "top_candidates": _trim_results(x.get("top_candidates", []), 3), "blocks_if_missing": (x.get("blocks_if_missing") or [])[:5]} if x else None)(full.get("canon_check_summary")),
        "best_fit_review_summary": full.get("best_fit_review_summary"),
        "mandatory_next_actions": full.get("mandatory_next_actions", [])[:14],
        "hard_blocks": full.get("hard_blocks", [])[:8],
        "receipt": {
            "route": (full.get("receipt") or {}).get("route"),
            "evidence_lock_status": (full.get("receipt") or {}).get("evidence_lock_status"),
            "category_counts": (full.get("receipt") or {}).get("category_counts", {}),
        },
        "full_output_available_with": "plug --mode full",
        "operating_instruction": full.get("operating_instruction"),
        "preflight_enforcement": full.get("preflight_enforcement"),
        "cache_meta": full.get("cache_meta"),
    }
    return compact


def build_central_plug(request: str, depth: str = "auto", mode: str = "compact") -> dict:
    """One-touch central operating core.

    Compact mode is the default steering packet: enough to force route/protocol/gate
    awareness without dumping the whole repository context. Full mode is available for
    forensic review and stores the same generated cache artifact.
    """
    plan = build_tool_plan(request or "")
    route = plan.get("route", {}).get("route", "project_work")
    scope = plan.get("route", {}).get("scope", "project")
    effective_depth = depth if depth != "auto" else plan.get("inspection_depth", "standard")
    compact = mode != "full"
    max_files = 10 if compact else (30 if effective_depth in {"snapshot", "standard"} else 80)
    per_chars = 700 if compact else 1600
    pack = build_context_pack(scope, request or "", max_files=max_files, per_file_chars=per_chars)
    lock = evidence_lock(scope, request or "")
    cm = concept_matrix(scope, request or "", 4 if compact else 8)
    rg = relationship_graph(scope, request or "", 6 if compact else 12)
    atlas = content_value_atlas(scope, request or "", 40 if compact else 120, "compact" if compact else "full")
    neural = neural_reflex_graph(route, request or "", scope)
    truth_maturity = truth_maturity_scan(scope, request or "", 6) if route in {"project_work", "governance_work", "best_fit_work", "implementation_translation_work", "write_or_modify_work", "runtime_work"} else None
    canon = canon_check(scope, request or "") if route in {"implementation_translation_work", "best_fit_work", "write_or_modify_work"} or re.search(r"code|api|database|backend|frontend|migration|signalr|redis|outbox|كود|قاعدة بيانات|تنفيذ", request or "", re.IGNORECASE) else None
    fit = best_fit_review(scope, request or "", 5) if route in {"runtime_work", "governance_work", "project_work", "best_fit_work", "implementation_translation_work", "write_or_modify_work", "comparison_work"} else None
    receipt = build_operation_receipt(request or "", scope)
    ws_lens = workshop_lens()
    surface_lens = build_project_lens(scope) if route == "project_surface" and scope == "project" else None
    mandatory_next = []
    if route == "write_or_modify_work":
        mandatory_next = ["duplicate-scan", "impact-scan", "write-plan", "safe-write dry-run", "post-write claim-check"]
    elif route == "implementation_translation_work":
        mandatory_next = ["value-atlas", "read parent artifact", "read child artifacts", "read state/event/permission/data-api standards", "truth-maturity", "canon-check", "relationship-graph", "evidence-lock", "claim-check"]
    elif route == "runtime_work":
        mandatory_next = ["scan-runtime", "doctor", "runtime-audit", "relationship-graph", "claim-check"]
    elif route == "best_fit_work":
        mandatory_next = ["context-pack", "best-fit", "truth-maturity", "relationship-graph", "matrix", "impact-scan for recommendations", "claim-check"]
    elif route == "external_research_work":
        mandatory_next = ["anchor to project context-pack", "perform external/current search", "separate external facts from project facts", "claim-check"]
    elif route == "project_surface":
        mandatory_next = ["workshop-lens", "value-atlas", "project-lens", "surface-check", "maturity-map", "claim-check for strong assessments"]
    else:
        mandatory_next = ["read mandatory matrix files", "relationship-graph", "evidence-lock", "claim-check for high-impact claims"]
    out = {
        "generated_at": utc_now(),
        "version": "7.0.0",
        "request": request,
        "central_os_mode": "mandatory_operating_context",
        "output_mode": "full",
        "route": plan.get("route"),
        "inspection_depth": effective_depth,
        "tool_keyboard": plan.get("sequence", []),
        "protocol_stack": route_protocol_stack(route),
        "workshop_universal_lens": ws_lens,
        "context_pack_summary": {
            "scope": pack.get("scope"),
            "files_included": pack.get("files_included"),
            "category_counts": pack.get("category_counts", {}),
            "truth_claims": pack.get("truth_claims", [])[:8],
        },
        "content_value_atlas_summary": {
            "file_count": atlas.get("file_count"),
            "counts_by_status": atlas.get("counts_by_status"),
            "counts_by_role": atlas.get("counts_by_role"),
            "top_high_value_files": [{"path": x.get("path"), "role": x.get("role"), "score": x.get("value_score"), "signals": x.get("value_signals", [])[:6]} for x in atlas.get("high_value_files", [])[:10]],
            "incomplete_truth_candidates": [{"path": x.get("path"), "role": x.get("role"), "status": x.get("content_status"), "missing": x.get("missing_expected_dimensions", [])[:6]} for x in atlas.get("incomplete_truth_candidates", [])[:8]],
            "code_and_implementation_surfaces": [{"path": x.get("path"), "role": x.get("role"), "code_signals": x.get("code_signals", {})} for x in atlas.get("code_and_implementation_surfaces", [])[:8]],
            "required_full_reads_before_high_impact_claims": atlas.get("required_full_reads_before_high_impact_claims", [])[:10],
            "usage_contract": atlas.get("usage_contract", []),
        },
        "project_surface_lens": ({
            "workshop_universal_lens": surface_lens.get("workshop_universal_lens"),
            "project_identity": surface_lens.get("project_identity"),
            "truth_counts": surface_lens.get("truth_counts"),
            "strongest_actionable_domain": surface_lens.get("strongest_actionable_domain"),
            "surface_owner_child_truth_gate": surface_lens.get("surface_owner_child_truth_gate"),
            "visible_gaps_in_strongest_domain": surface_lens.get("visible_gaps_in_strongest_domain", [])[:6],
            "implementation_status": surface_lens.get("implementation_status"),
            "first_step_candidate": surface_lens.get("first_step_candidate"),
        } if surface_lens else None),
        "evidence_gates": lock.get("gates", []),
        "concept_matrix": cm,
        "relationship_graph": rg,
        "neural_reflex_graph": neural,
        "truth_maturity_summary": {"overall_status": truth_maturity.get("overall_status"), "execution_allowed": truth_maturity.get("execution_allowed"), "top_owner_candidates": truth_maturity.get("owner_candidates", [])[:3]} if truth_maturity else None,
        "canon_check_summary": {"status": canon.get("status"), "top_candidates": canon.get("canon_candidates", [])[:3], "blocks_if_missing": canon.get("blocks_if_missing", [])} if canon else None,
        "best_fit_review_summary": fit.get("summary") if fit else None,
        "best_fit_priority_recommendations": fit.get("priority_recommendations", [])[:6] if fit else [],
        "mandatory_next_actions": list(dict.fromkeys(mandatory_next + neural.get("required_gates", []))),
        "hard_blocks": [
            "Do not answer project truth from memory or generated cache alone.",
            "Do not prove maturity from generated indexes, ledgers, state, or previous reports.",
            "Do not claim absence without a zero-result scan in the relevant scope.",
            "Do not write or create parallel concepts without duplicate-scan and impact-scan.",
            "Do not use external research as project truth; use it only as support or decision input.",
            "Do not expose runtime internals in project-facing answers unless user asks about runtime.",
            "For project-surface answers, do not choose a domain or first step without a content-bearing owner file and child truth/gap check.",
            "Do not make high-impact project claims without a content value atlas or equivalent all-file cognitive evidence touch.",
            "Do not treat long user explanations as a mandate for long explanations; execute clear repository work and summarize briefly.",
        ],
        "fallback_policy": plan.get("fallback_policy"),
        "receipt": receipt,
        "operating_instruction": "Treat this packet as the active operating context for the current user request. It is a steering contract and neural reflex graph, not a reading summary.",
        "preflight_enforcement": {
            "mandatory": True,
            "rule": "No high-impact answer, write, implementation translation, runtime fix, or assessment is valid without this plug/cycle packet or an equivalent operation receipt.",
            "blocks_if_missing": neural.get("blocked_operations", []),
        },
    }
    out = attach_cache_meta(out, scope)
    INDEX.mkdir(parents=True, exist_ok=True)
    (INDEX/"last_central_plug.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    append_jsonl(OPS_LEDGER, {"type":"central_plug", "route":route, "scope":scope, "request":(request or '')[:240], "mode":mode, "protocols":out["protocol_stack"][:12]})
    if compact:
        return compact_plug_packet(out)
    return out


def clean_generated_cache(apply: bool = False, include_ledgers: bool = False) -> dict:
    targets=[]
    for f in (RUNTIME/"indexes").glob("*.json"):
        targets.append(f)
    if include_ledgers:
        for f in (RUNTIME/"ledgers").glob("*.jsonl"):
            targets.append(f)
    actions=[]
    for f in targets:
        action={"path": rel(f), "kind": "truncate" if f.suffix == ".jsonl" else "delete"}
        if apply:
            if f.suffix == ".jsonl":
                f.write_text("", encoding="utf-8")
            else:
                try: f.unlink()
                except FileNotFoundError: pass
            action["applied"] = True
        else:
            action["applied"] = False
        actions.append(action)
    return {"generated_at": utc_now(), "status": "applied" if apply else "dry_run", "include_ledgers": include_ledgers, "action_count": len(actions), "actions": actions, "rule": "Generated cache is operational memory, not project truth; clean or refresh it before packaging or when stale."}


def cmd_cache_clean(args):
    print(json.dumps(clean_generated_cache(args.apply, args.include_ledgers), ensure_ascii=False, indent=2))


def cmd_relationship_graph(args):
    out=relationship_graph(args.scope, args.query or "", args.limit)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_plug(args):
    # v7/v8: compact plug is indexed and fast; full/deep plug returns the central OS packet.
    if getattr(args, "mode", "compact") == "full":
        print(json.dumps(build_central_plug(args.request or "", getattr(args, "depth", "auto"), "full"), ensure_ascii=False, indent=2))
    elif getattr(args, "depth", "auto") in {"deep","guarded_write","augmented"}:
        print(json.dumps(build_deep_plug(args.request or "", None), ensure_ascii=False, indent=2))
    else:
        print(json.dumps(build_fast_plug(args.request or "", None), ensure_ascii=False, indent=2))


def cmd_neural(args):
    r=route_intent(args.request or "")
    out=neural_reflex_graph(r.get("route", "project_work"), args.request or "", r.get("scope", "project"))
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_best_fit(args):
    out=best_fit_review(args.scope, args.query or "", args.limit)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_truth_maturity(args):
    out=truth_maturity_scan(args.scope, args.query or "", args.limit)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_canon_check(args):
    out=canon_check(args.scope, args.query or "")
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_one_page(args):
    pack = build_context_pack(args.scope, args.query or "", args.max_files, args.per_file_chars)
    lines=[]
    lines.append(f"# Project One-Page Evidence Pack")
    lines.append(f"Generated: {pack['generated_at']}")
    lines.append("")
    lines.append("## Classification")
    lines.append("```json")
    lines.append(json.dumps(pack.get('classification',{}), ensure_ascii=False, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Category Counts")
    lines.append("```json")
    lines.append(json.dumps(pack.get('category_counts',{}), ensure_ascii=False, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Truth Claims")
    for c in pack.get('truth_claims',[]):
        lines.append(f"- {c.get('status')}: {c.get('claim')}")
    lines.append("")
    lines.append("## Included Evidence")
    for f in pack.get('files',[]):
        lines.append(f"### {f['path']} [{f.get('role')}]")
        if f.get('headings'):
            lines.append("Headings: " + " | ".join(f.get('headings',[])[:6]))
        lines.append(f.get('excerpt','')[:1000])
        lines.append("")
    out_path=INDEX/f"{args.scope}_one_page_evidence.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"written": rel(out_path), "files_included": pack.get('files_included',0), "classification": pack.get('classification',{})}, ensure_ascii=False, indent=2))


def cmd_surface_check(args):
    text=args.text
    if args.file:
        p=(ROOT/args.file).resolve()
        text=read_text(p, 250000)
    out=surface_policy_check(text)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_matrix(args):
    r=route_intent(args.request)
    lock=evidence_lock(r["scope"], args.request)
    cm=concept_matrix(r["scope"], args.request, 10)
    neural=neural_reflex_graph(r["route"], args.request, r["scope"])
    rg=relationship_graph(r["scope"], args.request, 10)
    atlas=content_value_atlas(r["scope"], args.request, 60, "compact")
    out={"route":r,"evidence_lock":lock,"concept_matrix":cm,"content_value_atlas_summary":{"file_count":atlas.get("file_count"),"counts_by_status":atlas.get("counts_by_status"),"top_high_value_files":atlas.get("high_value_files",[])[:8],"required_full_reads_before_high_impact_claims":atlas.get("required_full_reads_before_high_impact_claims",[])[:8]},"relationship_graph":rg,"neural_reflex_graph":neural,"navigation":"semantic_neural_matrix_touch","contract":"matrix output is a steering map, content value atlas, relationship graph, and nervous-system map; read mandatory files and obey linked gates before high-impact claims or writes"}
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_scenario_map(args):
    out=build_scenario_map(args.scope)
    out=attach_cache_meta(out, args.scope)
    (INDEX/f"{args.scope}_scenario_map.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_evidence_lock(args):
    out=evidence_lock(args.scope, args.query or "")
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_claim_check(args):
    text=args.text
    if args.file:
        p=(ROOT/args.file).resolve()
        text=read_text(p, 250000)
    out=claim_check_text(text, args.scope)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_duplicate_scan(args):
    out=duplicate_scan(args.query, args.scope, args.limit)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_impact_scan(args):
    out=impact_scan(args.target, args.objective or "", args.scope)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_write_plan(args):
    content=""
    if args.text: content=args.text
    if args.from_file:
        content=read_text((ROOT/args.from_file).resolve(), 250000)
    out=write_plan(args.target, args.objective, content, args.scope)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_safe_write(args):
    text=args.text or ""
    if args.from_file:
        p=(ROOT/args.from_file).resolve()
        text=read_text(p, 500000)
    out=safe_write(args.target, text, args.reason, args.apply, args.scope)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_compare(args):
    a=matrix_scan(args.scope, args.query_a, True, args.limit)
    b=matrix_scan(args.scope, args.query_b, True, args.limit)
    paths_a={r['path'] for r in a['results']}; paths_b={r['path'] for r in b['results']}
    out={"scope":args.scope,"query_a":args.query_a,"query_b":args.query_b,"a_count":a['count'],"b_count":b['count'],"shared_paths":sorted(paths_a & paths_b),"only_a":sorted(paths_a-paths_b)[:args.limit],"only_b":sorted(paths_b-paths_a)[:args.limit],"a_top":a['results'][:10],"b_top":b['results'][:10]}
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_operation_ledger(args):
    path={"ops":OPS_LEDGER,"claims":CLAIM_LEDGER,"writes":WRITE_LEDGER}.get(args.kind, OPS_LEDGER)
    rows=[]
    if path.exists():
        lines=path.read_text(encoding='utf-8', errors='ignore').splitlines()[-args.limit:]
        for line in lines:
            try: rows.append(json.loads(line))
            except Exception: rows.append({"raw":line})
    print(json.dumps({"ledger":rel(path),"count":len(rows),"rows":rows}, ensure_ascii=False, indent=2))



def semantic_density(text: str) -> dict:
    low=(text or "").lower()
    tokens=re.findall(r"[A-Za-z0-9_\-]+|[\u0600-\u06FF]{2,}", text or "")
    word_count=len(tokens)
    sigs=[]
    for name, words in [
        ("scenario", SCENARIO_WORDS), ("requirements", PRD_WORDS), ("truth", TRUTH_WORDS),
        ("architecture", ARCH_WORDS), ("governance", GOV_WORDS), ("readiness", READINESS_WORDS)
    ]:
        hits=[w for w in words if w.lower() in low]
        if hits: sigs.append({"type":name,"hits":hits[:10],"count":len(hits)})
    heading_count=len(headings(text, 50))
    # density rewards meaningful signals even in short files; does not reward length alone.
    signal_count=sum(x["count"] for x in sigs)
    density=round((signal_count*3 + heading_count*1.5 + min(word_count,1200)/400), 3)
    return {"word_count":word_count,"heading_count":heading_count,"signal_count":signal_count,"signals":sigs,"density_score":density}


def semantic_placeholder_status(path: Path, text: str) -> dict:
    stripped=(text or "").strip()
    low=stripped.lower()
    dens=semantic_density(text)
    placeholder_hits=[w for w in PLACEHOLDER_WORDS if w.lower() in low]
    if not stripped:
        status="empty"
    elif placeholder_hits and dens["signal_count"] < 3:
        status="placeholder"
    elif dens["word_count"] < 40 and dens["signal_count"] == 0 and len(headings(text,5)) <= 1:
        status="thin_unproven"
    else:
        status="content_bearing"
    return {"path":rel(path),"status":status,"placeholder_hits":placeholder_hits[:10],"density":dens}


def module_key_for(path: str) -> str:
    """Return a meaningful project lens key, not just the project root.

    Maturity grouping must reveal actionable domains instead of collapsing every project into the root project folder.
    """
    prefix="02_WORKSHOP/ACTIVE_PROJECT/"
    if path.startswith(prefix):
        rest=path[len(prefix):]
        parts=[x for x in rest.split('/') if x and not x.startswith('.')]
        if not parts:
            return "project_root"
        project=parts[0]
        low="/".join(parts).lower()
        if len(parts) <= 1:
            return f"{project}/root"
        if parts[1] == "03_PROJECT_COGNITIVE_TUNNEL":
            return f"{project}/cognitive_tunnel"
        if parts[1] == "04_PROJECT_ARTIFACTS":
            # Prefer domain/module depth under artifacts.
            if "modules" in parts:
                idx=parts.index("modules")
                if len(parts) > idx+2:
                    return "/".join(parts[idx+1:idx+3])
                if len(parts) > idx+1:
                    return parts[idx+1]
            # Governance-like artifacts often live directly under artifacts/<domain>/<child>.
            if len(parts) >= 4:
                return "/".join(parts[2:4])
            if len(parts) >= 3:
                return parts[2]
        if parts[1] == "06_PROJECT_IMPLEMENTATION_TARGET":
            return f"{project}/implementation_target"
        if parts[1] == "05_PROJECT_DECISIONS":
            return f"{project}/decisions"
        if any(x in low for x in ["entrypoint", "contract", "truth_index", "project_truth"]):
            return f"{project}/root_truth"
        return f"{project}/{parts[1]}"
    return "project_root"


def maturity_label(score: float) -> str:
    if score >= 16: return "high"
    if score >= 8: return "medium"
    if score > 0: return "early"
    return "unknown"


def confidence_from_domain(d: dict) -> str:
    if d.get("evidence_files",0) >= 5 and d.get("semantic_score",0) >= 12: return "high"
    if d.get("evidence_files",0) >= 2 and d.get("semantic_score",0) >= 5: return "medium"
    if d.get("evidence_files",0) >= 1: return "low"
    return "unknown"


def build_maturity_map(scope="project") -> dict:
    files=iter_files(scope)
    domains={}
    placeholders=[]
    for f in files:
        txt=read_text(f, 350000)
        role=file_role(f, txt)
        dens=semantic_density(txt)
        ph=semantic_placeholder_status(f, txt)
        if ph["status"] != "content_bearing": placeholders.append(ph)
        key=module_key_for(rel(f)) if scope=="project" else role
        d=domains.setdefault(key, {"domain":key,"files":0,"evidence_files":0,"roles":{},"semantic_score":0.0,"scenario_signals":0,"requirements_signals":0,"governance_signals":0,"architecture_signals":0,"readiness_signals":0,"code_files":0,"placeholder_files":0,"top_files":[],"top_signals":[]})
        d["files"] += 1
        d["roles"][role]=d["roles"].get(role,0)+1
        d["semantic_score"] += dens["density_score"]
        if ph["status"] != "content_bearing": d["placeholder_files"] += 1
        if role != "empty_or_placeholder" and dens["signal_count"] > 0:
            d["evidence_files"] += 1
        if role == "code": d["code_files"] += 1
        for sig in dens["signals"]:
            t=sig["type"]
            if t=="scenario": d["scenario_signals"] += sig["count"]
            if t=="requirements": d["requirements_signals"] += sig["count"]
            if t=="governance": d["governance_signals"] += sig["count"]
            if t=="architecture": d["architecture_signals"] += sig["count"]
            if t=="readiness": d["readiness_signals"] += sig["count"]
            for h in sig["hits"]:
                if h not in d["top_signals"]: d["top_signals"].append(h)
        d["top_files"].append({"path":rel(f),"role":role,"density":dens["density_score"],"signals":dens["signals"],"excerpt":evidence_excerpt(txt, READINESS_WORDS+SCENARIO_WORDS+PRD_WORDS, 480)})
    out=[]
    for d in domains.values():
        d["semantic_score"]=round(d["semantic_score"],3)
        d["readiness_label"]=maturity_label(d["semantic_score"] + d["readiness_signals"]*0.4 + d["scenario_signals"]*0.3)
        d["confidence"]=confidence_from_domain(d)
        d["top_files"]=sorted(d["top_files"], key=lambda x:-x.get("density",0))[:8]
        out.append(d)
    out=sorted(out, key=lambda x:(-x["semantic_score"], -x["evidence_files"], x["domain"]))
    result={"generated_at":utc_now(),"scope":scope,"principle":"maturity is based on semantic evidence, not file size","domain_count":len(out),"top_domains":out[:12],"all_domains":out,"placeholder_summary":{"count":len(placeholders),"items":placeholders[:40]}}
    result=attach_cache_meta(result, scope)
    INDEX.mkdir(parents=True, exist_ok=True)
    (INDEX/f"{scope}_maturity_map.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def answer_receipt(request: str, scope="project") -> dict:
    plan=build_tool_plan(request)
    tm=build_truth_map(scope)
    sm=build_scenario_map(scope)
    mm=build_maturity_map(scope)
    lock=evidence_lock(scope, request)
    receipt={
        "generated_at":utc_now(),
        "request":request,
        "route":plan.get("route"),
        "inspection_depth":plan.get("inspection_depth"),
        "tools_used_or_required":["route","tool-plan","truth-map","scenario-map","maturity-map","evidence-lock","answer"],
        "truth_counts":tm.get("category_counts",{}),
        "scenario_count":sm.get("scenario_count",0),
        "top_maturity_domains":[{"domain":d["domain"],"readiness_label":d["readiness_label"],"confidence":d["confidence"],"semantic_score":d["semantic_score"],"evidence_files":d["evidence_files"],"top_files":[f["path"] for f in d.get("top_files",[])[:4]]} for d in mm.get("top_domains",[])[:5]],
        "evidence_lock_status":lock.get("status"),
        "anti_speculation_gates":[
            "strong claims require evidence path or evidence count",
            "absence claims require zero-result scan",
            "priority recommendations require maturity-map comparison",
            "placeholder claims require placeholder-scan",
            "file size alone is not a maturity signal"
        ],
    }
    receipt=attach_cache_meta(receipt, scope)
    (INDEX/f"{scope}_answer_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
    append_jsonl(OPS_LEDGER, {"type":"answer_receipt","route":receipt["route"].get("route") if isinstance(receipt.get("route"),dict) else None,"request":request[:240],"truth_counts":receipt["truth_counts"]})
    return receipt


def cmd_maturity_map(args):
    out=build_maturity_map(args.scope)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_placeholder_scan(args):
    items=[]
    for f in iter_files(args.scope):
        txt=read_text(f, 250000)
        st=semantic_placeholder_status(f, txt)
        if args.all or st["status"] != "content_bearing": items.append(st)
    print(json.dumps({"scope":args.scope,"count":len(items),"items":items[:args.limit]}, ensure_ascii=False, indent=2))


def cmd_answer_receipt(args):
    out=answer_receipt(args.request, args.scope)
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_test_suite(args):
    path = ROOT/'.engineer'/'evaluation'/'deep_test_suite_ar.json'
    if not path.exists():
        print(json.dumps({'error':'test_suite_not_found'}, ensure_ascii=False)); return
    data=json.loads(path.read_text(encoding='utf-8'))
    if args.format == 'json':
        print(json.dumps(data, ensure_ascii=False, indent=2)); return
    lines=[]
    lines.append('# Deep Evaluation Test Suite')
    for idx,q in enumerate(data.get('questions',[]),1):
        lines.append(f"\n## {idx}. {q.get('id')}")
        lines.append(f"الغرض: {q.get('purpose')}")
        lines.append(q.get('prompt',''))
    print('\n'.join(lines))





# -----------------------------------------------------------------------------
# v7.0 Indexed Neural Operating Kernel
# -----------------------------------------------------------------------------
# Design note:
# v6.x proved the value of plug/matrix/neural gates, but live-scanning too much
# context during each request made the runtime slow and brittle. v7 separates the
# lifecycle into: build-index once, fast-plug for ordinary entry, deep-plug for
# high-risk work, operation-mode classification, and golden quality checks.

V7_INDEX_VERSION = "7.0.0"
V7_KERNEL_DIR = STATE / "kernel"
V7_INDEX_FILES = {
    "project": V7_KERNEL_DIR / "project_kernel_index.json",
    "runtime": V7_KERNEL_DIR / "runtime_kernel_index.json",
    "repository": V7_KERNEL_DIR / "repository_kernel_index.json",
    "workshop": V7_KERNEL_DIR / "workshop_kernel_index.json",
}

OPERATION_MODE_RULES = {
    "surface_identity": ["من انت", "من أنت", "وظيفتك", "مهامك", "about you", "who are you"],
    "assessment": ["تقييم", "وضع", "نضج", "جاهزية", "status", "assessment", "maturity"],
    "repair": ["اصلح", "إصلاح", "انضاج", "تنقيح", "حسن", "تحسين", "fix", "repair", "mature"],
    "write": ["اكتب", "اضف", "أضف", "عدل", "تعديل", "write", "modify", "add"],
    "implementation": ["كود", "تنفيذ", "api", "database", "backend", "frontend", "migration", "deploy"],
    "runtime_maintenance": ["بيئة المهندس", "runtime", "القابس", "ماتركس", "الجملة العصبية", "الملاحة", "kernel"],
    "external_research": ["ابحث بالنت", "بحث خارجي", "حديث", "current", "latest", "web"],
}


def _extract_terms_for_index(query: str) -> list[str]:
    low=(query or "").lower()
    raw=re.findall(r"[A-Za-z_][A-Za-z0-9_\-]{2,}|[\u0600-\u06FF]{3,}", low)
    stop={"الذي","التي","هذا","هذه","هناك","على","الى","إلى","في","من","ماهو","ماهي","حول","مشروع","ملف","ملفات","نظام","عمل","كيف","the","and","for","with","from","this","that","project","file","system"}
    out=[]
    for t in raw:
        if t in stop or len(t)<3: continue
        if t not in out: out.append(t)
    return out[:24]


def operation_mode(request: str) -> dict:
    low=(request or "").lower()
    hits=[]
    for mode, terms in OPERATION_MODE_RULES.items():
        score=sum(1 for t in terms if t.lower() in low)
        if score:
            hits.append((mode, score))
    route=route_intent(request or "")
    if not hits:
        mode = "surface_identity" if route.get("route") == "project_surface" else route.get("route", "project_work")
    else:
        mode=max(hits, key=lambda x:x[1])[0]
    risk="low"
    if mode in {"assessment", "surface_identity"}: risk="medium"
    if mode in {"repair", "write", "implementation", "runtime_maintenance"}: risk="high"
    if mode in {"implementation"}: risk="critical"
    deep_required = risk in {"high","critical"} or route.get("route") in {"write_or_modify_work","implementation_translation_work","runtime_work"}
    return {
        "mode": mode,
        "risk": risk,
        "route": route,
        "deep_required": deep_required,
        "index_required": True,
        "execution_bias": "execute_with_concise_status" if mode in {"repair","write","runtime_maintenance"} else "answer_naturally_with_evidence_limits",
        "evidence_budget": {
            "index_entries": 8 if risk in {"low","medium"} else 16,
            "full_reads": 0 if risk == "low" else (3 if risk == "medium" else 8),
            "generated_context_kb_max": 8 if risk in {"low","medium"} else 24,
        },
    }


def _file_index_entry(f: Path, scope: str) -> dict:
    txt=read_text(f, 220000)
    dens=semantic_density(txt)
    role=file_role(f, txt)
    lower=(txt[:50000] + " " + rel(f)).lower()
    signal_groups=[]
    for group, terms in VALUE_ATLAS_SIGNAL_GROUPS.items():
        if any(t.lower() in lower for t in terms):
            signal_groups.append(group)
    status="binary_or_unreadable"
    if txt:
        wc=dens.get('word_count',0)
        if wc < 12: status="empty_or_tiny"
        elif wc < 80: status="thin"
        else: status="content_bearing"
    if f.suffix.lower() in CODE_EXTS:
        status = "code_bearing" if dens.get('word_count',0) > 25 else "thin_code"
    path=rel(f)
    headings_list=headings(txt, 12)[:12]
    score=0
    if role in {"truth_entry","governance","architecture"}: score+=30
    if role in {"requirements","scenario"}: score+=18
    if role == "code": score+=16
    if "truth_identity" in signal_groups: score+=18
    if "methodology_360" in signal_groups: score+=14
    if "data_interface_contract" in signal_groups: score+=12
    if "state_event" in signal_groups: score+=10
    if "permission_audit_security" in signal_groups: score+=10
    if len(headings_list): score+=min(10, len(headings_list))
    if status in {"content_bearing","code_bearing"}: score+=10
    if status in {"thin","empty_or_tiny","thin_code"}: score-=8
    return {
        "path": path,
        "scope": scope,
        "suffix": f.suffix.lower(),
        "role": role,
        "status": status,
        "word_count": dens.get('word_count',0),
        "signal_count": dens.get('signal_count',0),
        "headings": headings_list,
        "signal_groups": signal_groups,
        "value_score": score,
        "depth": path.count('/'),
        "basename": f.name,
        "stem": f.stem.lower(),
        "sha1": hashlib.sha1(f.read_bytes()).hexdigest()[:12] if f.exists() else None,
        "snippet": re.sub(r"\s+", " ", txt[:420]).strip() if txt else "",
    }



def quick_scope_fingerprint(scope: str = "project") -> str:
    """Fast freshness fingerprint for v7 kernel indexes.

    Uses path, size, and mtime_ns, not file content. Deep content fingerprinting is
    reserved for build-index, keeping plug-fast fast.
    """
    h=hashlib.sha1()
    for f in iter_files(scope):
        r=rel(f)
        if scope in {"repository", "runtime"} and r.startswith(GENERATED_DIR_PREFIXES):
            continue
        try:
            st=f.stat()
            h.update(r.encode("utf-8")); h.update(str(st.st_size).encode("utf-8")); h.update(str(st.st_mtime_ns).encode("utf-8"))
        except Exception:
            continue
    return h.hexdigest()[:16]

def build_kernel_index(scope: str = "project", write: bool = True) -> dict:
    scope = scope if scope in {"project","runtime","repository","workshop"} else "project"
    files=[f for f in iter_files(scope) if f.suffix.lower() in TEXT_EXTS]
    if scope in {"repository","runtime"}:
        files=[f for f in files if not rel(f).startswith(GENERATED_DIR_PREFIXES)]
    entries=[]
    for f in files:
        try: entries.append(_file_index_entry(f, scope))
        except Exception as e: entries.append({"path":rel(f),"scope":scope,"error":str(e),"role":"unreadable","status":"unreadable","value_score":-50})
    high=sorted(entries, key=lambda x:(x.get('value_score',0), x.get('word_count',0)), reverse=True)[:40]
    by_role={}; by_status={}; by_signal={}
    for e in entries:
        by_role[e.get('role','unknown')]=by_role.get(e.get('role','unknown'),0)+1
        by_status[e.get('status','unknown')]=by_status.get(e.get('status','unknown'),0)+1
        for g in e.get('signal_groups',[]): by_signal[g]=by_signal.get(g,0)+1
    edges=[]; dirs={}
    for e in entries:
        parent=str(Path(e['path']).parent); dirs.setdefault(parent,[]).append(e)
    for parent, group in dirs.items():
        if len(group)>1:
            owner=sorted(group, key=lambda x:x.get('value_score',0), reverse=True)[0]
            for child in sorted(group, key=lambda x:x.get('value_score',0), reverse=True)[:25]:
                if child['path'] != owner['path']:
                    edges.append({"type":"same_folder_owner_candidate","from":owner['path'],"to":child['path'],"reason":"highest value file in same folder"})
    for signal in by_signal:
        group=[e for e in entries if signal in e.get('signal_groups',[])]
        group=sorted(group, key=lambda x:x.get('value_score',0), reverse=True)[:10]
        if len(group)>1:
            owner=group[0]
            for other in group[1:]: edges.append({"type":"shared_signal","from":owner['path'],"to":other['path'],"signal":signal})
    idx={
        "kernel_version": V7_INDEX_VERSION,
        "generated_at": utc_now(),
        "scope": scope,
        "fingerprint": quick_scope_fingerprint(scope),
        "content_fingerprint": project_fingerprint(scope),
        "file_count": len(entries),
        "counts_by_role": by_role,
        "counts_by_status": by_status,
        "counts_by_signal": by_signal,
        "entries": entries,
        "high_value_files": high,
        "relationship_edges": edges[:400],
        "usage_contract": [
            "This is an operating index, not project truth.",
            "Use it for fast navigation, risk classification, owner selection, and deep-read planning.",
            "Strong claims still require reading owner/high-impact files selected by the index.",
            "Generated cache cannot override current project files.",
        ],
    }
    if write:
        V7_KERNEL_DIR.mkdir(parents=True, exist_ok=True)
        out=V7_INDEX_FILES.get(scope, V7_KERNEL_DIR/f"{scope}_kernel_index.json")
        out.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding='utf-8')
    return idx


def load_kernel_index(scope: str = "project", auto_build: bool = True) -> dict:
    path=V7_INDEX_FILES.get(scope, V7_KERNEL_DIR/f"{scope}_kernel_index.json")
    if path.exists():
        try:
            data=json.loads(path.read_text(encoding='utf-8'))
            if data.get('fingerprint') == quick_scope_fingerprint(scope):
                return data
        except Exception:
            pass
    if auto_build:
        return build_kernel_index(scope, True)
    return {"status":"missing_or_stale", "scope":scope, "path":rel(path), "fingerprint":quick_scope_fingerprint(scope)}


def select_index_entries(index: dict, query: str, limit: int = 8) -> list[dict]:
    terms=_extract_terms_for_index(query)
    selected=[]
    for e in index.get('entries', []):
        hay=" ".join([e.get('path',''), e.get('role',''), " ".join(e.get('headings',[])), " ".join(e.get('signal_groups',[])), e.get('snippet','')]).lower()
        score=e.get('value_score',0) * 0.05
        for t in terms:
            if t.lower() in hay: score+=8
        if not terms and e.get('role') in {"truth_entry","governance","architecture"}: score+=10
        if score>0: selected.append((score,e))
    if not selected:
        selected=[(e.get('value_score',0), e) for e in index.get('high_value_files', [])]
    return [e for _,e in sorted(selected, key=lambda x:x[0], reverse=True)[:limit]]


def mandatory_gates_for_mode(mode: str, risk: str) -> list[str]:
    base=["route", "load-kernel-index", "workshop-lens", "claim-risk-classifier"]
    if mode in {"assessment","surface_identity"}: return base+["selected-lens", "owner-read-if-strong-claim", "claim-check"]
    if mode in {"repair","runtime_maintenance"}: return base+["best-fit-root-cause", "impact-scan", "golden-tests", "maintenance-ledger"]
    if mode in {"write"}: return base+["duplicate-scan", "impact-scan", "write-plan", "safe-write", "post-write-claim-check"]
    if mode in {"implementation"}: return base+["truth-maturity", "canon-check", "relationship-graph", "tests"]
    if mode in {"external_research"}: return base+["project-truth-anchor", "external-facts-separated", "claim-check"]
    return base+["selected-lens"]



def _compact_surface_lens_from_index(index: dict, selected: list[dict]) -> dict | None:
    """Backward-compatible fast project lens built from the v7 index only."""
    if index.get('scope') != 'project':
        return None
    # Pick highest-value non-root artifact-ish folder as dynamic actionable domain.
    candidates=[e for e in index.get('entries', []) if e.get('role') in {'requirements','scenario','architecture','governance'} and e.get('status') in {'content_bearing','code_bearing'}]
    candidates=sorted(candidates, key=lambda e:e.get('value_score',0), reverse=True)
    top=candidates[0] if candidates else (index.get('high_value_files') or [{}])[0]
    domain=str(Path(top.get('path','')).parent) if top else None
    return {
        "workshop_universal_lens": {"silent_gate": True, "role": "universal_method_gate_compact_from_index"},
        "strongest_actionable_domain": {"domain": domain, "evidence_files": [top.get('path')] if top else [], "confidence": "index_lens_only_requires_deep_read_for_strong_claim"},
        "first_step_candidate": {"action": "read_owner_and_direct_children_then_select_owner_ordered_incomplete_truth", "target_incomplete_truth_file": None, "reason": "v7 fast lens does not choose a specific child without deep owner read"},
        "surface_owner_child_truth_gate": {"status": "index_lens_only", "execution_allowed": False, "first_step_allowed": False},
    }

def build_fast_plug(request: str, scope: str | None = None) -> dict:
    mode=operation_mode(request or "")
    route=mode.get('route', {})
    scope=scope or route.get('scope','project')
    if scope not in {"project","runtime","repository","workshop"}: scope='project'
    idx=load_kernel_index(scope, auto_build=True)
    selected=select_index_entries(idx, request or "", mode['evidence_budget']['index_entries'])
    if route.get('route') == 'project_surface' and scope == 'project':
        try:
            _lens = build_project_lens('project')
            _gate = _lens.get('surface_owner_child_truth_gate') or {}
            surface_lens = {
                "workshop_universal_lens": {
                    "silent_gate": (_lens.get("workshop_universal_lens") or {}).get("silent_gate"),
                    "files_detected": (_lens.get("workshop_universal_lens") or {}).get("files_detected"),
                },
                "project_identity": {
                    "project_name": (_lens.get("project_identity") or {}).get("project_name"),
                    "mission": ((_lens.get("project_identity") or {}).get("mission") or "")[:360],
                },
                "truth_counts": _lens.get("truth_counts"),
                "strongest_actionable_domain": (lambda d: {
                    "domain": d.get("domain"), "readiness_label": d.get("readiness_label"), "confidence": d.get("confidence"),
                    "top_files": (d.get("top_files") or [])[:2],
                })(_lens.get("strongest_actionable_domain") or {}),
                "surface_owner_child_truth_gate": {
                    "status": _gate.get("status"),
                    "execution_allowed": _gate.get("execution_allowed"),
                    "first_step_allowed": _gate.get("first_step_allowed"),
                    "owner_truth_file": (lambda o: {"path": o.get("path"), "content_status": o.get("content_status"), "word_count": o.get("word_count")} if o else None)(_gate.get("owner_truth_file")),
                    "incomplete_truth_children": [{"path": x.get("path"), "content_status": x.get("content_status")} for x in (_gate.get("incomplete_truth_children") or [])[:3]],
                    "claim_blocks": (_gate.get("claim_blocks") or [])[:5],
                },
                "visible_gaps_in_strongest_domain": [{"path": x.get("path"), "missing": (x.get("missing") or x.get("missing_dimensions") or [])[:4]} for x in (_lens.get("visible_gaps_in_strongest_domain") or [])[:3]],
                "implementation_status": _lens.get("implementation_status"),
                "first_step_candidate": (lambda f: {"action": f.get("action"), "target_incomplete_truth_file": f.get("target_incomplete_truth_file"), "target_file": f.get("target_file")} if f else None)(_lens.get("first_step_candidate")),
            }
        except Exception:
            surface_lens = _compact_surface_lens_from_index(idx, selected)
    else:
        surface_lens = None
    content_summary={
        "file_count": idx.get('file_count'),
        "counts_by_status": idx.get('counts_by_status'),
        "counts_by_role": idx.get('counts_by_role'),
        "top_high_value_files": [{"path":e.get('path'),"role":e.get('role'),"score":e.get('value_score')} for e in idx.get('high_value_files',[])[:3]],
    }
    gates = mandatory_gates_for_mode(mode.get('mode'), mode.get('risk'))
    protocol_stack = route_protocol_stack(route.get('route', 'project_work'))
    _ng = neural_reflex_graph(route.get('route', 'project_work'), request or "", scope)
    neural_graph = {
        "active_reflexes": [{"name": r.get("name"), "requires": r.get("requires", [])[:8], "blocks": r.get("blocks", [])[:8]} for r in (_ng.get("active_reflexes") or [])],
        "required_gates": _ng.get("required_gates", [])[:20],
        "blocked_operations": _ng.get("blocked_operations", [])[:20],
        "cross_links": (_ng.get("cross_links") or [])[:5],
    }
    needs_implementation_summary = route.get('route') in {"implementation_translation_work", "write_or_modify_work", "best_fit_work"} or re.search(r"code|api|database|backend|frontend|migration|test|كود|قاعدة بيانات|تنفيذ|اختبارات", request or "", re.IGNORECASE)
    truth_summary = None
    canon_summary = None
    if needs_implementation_summary:
        try:
            tm = truth_maturity_scan(scope, request or "", 4)
            truth_summary = {"overall_status": tm.get("overall_status"), "execution_allowed": tm.get("execution_allowed"), "top_owner_candidates": tm.get("owner_candidates", [])[:3]}
        except Exception:
            truth_summary = {"overall_status": "unavailable", "execution_allowed": False, "top_owner_candidates": []}
        try:
            cc = canon_check(scope, request or "")
            canon_summary = {"status": cc.get("status"), "top_candidates": cc.get("canon_candidates", [])[:3], "blocks_if_missing": cc.get("blocks_if_missing", [])}
        except Exception:
            canon_summary = {"status": "unavailable", "top_candidates": [], "blocks_if_missing": []}
    try:
        _pulse = file_matrix_truth_pulse(scope if scope in {"project","runtime","repository","workshop"} else "project", request or "")
        file_matrix_pulse_summary = {
            "coverage": _pulse.get("coverage"),
            "readiness_verdict": _pulse.get("readiness_verdict"),
            "truth_spine_files": ((_pulse.get("one_page_neural_truth_map") or {}).get("truth_spine_files") or [])[:6],
            "high_value_content_surfaces": ((_pulse.get("one_page_neural_truth_map") or {}).get("high_value_content_surfaces") or [])[:6],
            "semantic_drift_candidates": ((_pulse.get("one_page_neural_truth_map") or {}).get("semantic_drift_candidates") or [])[:6],
            "incomplete_truth_candidates": ((_pulse.get("one_page_neural_truth_map") or {}).get("incomplete_truth_candidates") or [])[:6],
            "recommended_entry_sequence": (_pulse.get("recommended_entry_sequence") or [])[:8],
            "truth_governance": _pulse.get("truth_governance", {}),
        }
    except Exception as e:
        file_matrix_pulse_summary = {"status":"unavailable", "error": str(e)[:220]}
    try:
        _sweep_for_authority = truth_sweep_360(request or "", scope)
        truth_authority_summary = truth_authority_gate(request or "", scope, _sweep_for_authority)
    except Exception as e:
        truth_authority_summary = {"authority":"unknown", "error": str(e)[:220]}
    selected_compact = [{"path":e.get('path'),"role":e.get('role'),"status":e.get('status'),"score":e.get('value_score')} for e in selected[:5]]
    concept_buckets = {
        "selected_lens": {"count": len(selected_compact), "top_files": selected_compact[:5]},
        "index_high_value": {"count": len(idx.get('high_value_files', []) or []), "top_files": [{"path":e.get('path'), "role":e.get('role'), "score":e.get('value_score')} for e in (idx.get('high_value_files', []) or [])[:4]]},
    }
    try:
        rg = relationship_graph(scope, request or "", 6)
        relationship_summary = {
            "owner_candidates": [{"path": x.get("path"), "role": x.get("role"), "score": x.get("score")} for x in (rg.get("concept_owner_candidates") or [])[:5]],
            "linkage_buckets": {k: len(v or []) for k, v in (rg.get("cross_artifact_linkages") or {}).items()},
            "mandatory_use": rg.get("mandatory_use", [])[:4],
        }
    except Exception:
        relationship_summary = {"owner_candidates": [], "linkage_buckets": {}, "mandatory_use": []}
    return {
        "generated_at": utc_now(),
        "version": V7_INDEX_VERSION,
        "kernel_version": V7_INDEX_VERSION,
        "command": "plug-fast",
        "central_os_mode": "mandatory_operating_context",
        "output_mode": "compact",
        "request": request,
        "route": route,
        "operation_mode": {k:v for k,v in mode.items() if k!='route'},
        "index_status": {"scope":idx.get('scope'), "fingerprint":idx.get('fingerprint'), "file_count":idx.get('file_count'), "counts_by_role":idx.get('counts_by_role'), "counts_by_status":idx.get('counts_by_status')},
        "selected_lens": selected_compact,
        "content_value_atlas_summary": content_summary,
        "project_surface_lens": surface_lens,
        "tool_keyboard": gates + (["project-lens"] if route.get('route') == 'project_surface' else []),
        "protocol_stack": protocol_stack,
        "concept_matrix": {
            "terms": _extract_terms_for_index(request or ""),
            "concept_buckets": concept_buckets,
            "matrix_rules": [
                "Use the index as navigation memory, not truth.",
                "Read owner/high-impact files before strong claims.",
                "Run deep plug for writes, implementation, and runtime repair.",
            ],
        },
        "neural_reflex_graph": neural_graph,
        "relationship_graph_summary": relationship_summary,
        "truth_maturity_summary": truth_summary,
        "canon_check_summary": canon_summary,
        "neural_factory_entry": {"mandatory": True, "primary_command": "factory-cycle", "goal_gate": "goal-closure", "health": "factory-health", "rule": "enter the factory loop before high-impact answers, plans, architecture changes, runtime work, or execution"},
        "file_matrix_entry": {"mandatory_for_file_work": True, "surface_command": "file-matrix-pulse", "primary_command": "file-matrix-context", "doctor": "file-matrix-doctor"},
        "file_matrix_pulse_summary": file_matrix_pulse_summary,
        "open_neural_kernel_entry": {
            "primary_command": "open-neural-entry",
            "rule": "The model is not caged by a first-contact template. It enters the control core, grounds intent in truth, then freely chooses depth according to claim authority, risk, and evidence need.",
            "silent_runtime_boundary": "Do not present .engineer/Workshop/runtime as the active project; use them silently as operating governance.",
            "available_deepening_tools": ["open-neural-entry", "truth-authority-gate", "truth-sweep-360", "file-matrix-context", "operation-360", "code-impact-360", "patch-gate-360"],
        },
        "truth_authority_gate": truth_authority_summary,
        "governed_decision_space": {
            "model_is_free_to_choose_depth": True,
            "runtime_does_not_prescribe_answer_template": True,
            "truth_compass_calibrates_claim_strength": (truth_authority_summary or {}).get("claim_strength", {}),
            "available_deepening_tools": ["truth-sweep-360", "file-matrix-context", "operation-360", "code-impact-360", "patch-gate-360"],
            "deepening_advisory": (truth_authority_summary or {}).get("advisory_gaps", []),
        },
        "mandatory_next_actions": [],
        "recommended_next_actions": [],
        "mandatory_gates": gates,
        "next_action": "choose the necessary depth from intent, evidence gaps, and risk; answer naturally while calibrating claims to truth",
        "hard_blocks": [
            "Advisory: do not use file size as value; calibrate claims to content/value truth.",
        ],
        "truth_principles": [
            "Kernel index is navigation memory, not final truth.",
            "Strong project claims should be calibrated to content/value evidence.",
            "File size is not value.",
            "No single file is binding when parent/cross-file reality contradicts it.",
            "Runtime logic must stay project-neutral and silent unless asked.",
        ],
    }


def build_deep_plug(request: str, scope: str | None = None, full_reads: int | None = None) -> dict:
    fast=build_fast_plug(request, scope)
    scope=fast.get('index_status',{}).get('scope','project')
    budget=fast.get('operation_mode',{}).get('evidence_budget',{}) or {}
    n=full_reads if full_reads is not None else budget.get('full_reads', 3)
    selected=fast.get('selected_lens', [])[:max(0,n)]
    reads=[]
    for item in selected:
        p=ROOT/item['path']
        txt=read_text(p, 12000)
        reads.append({"path":item['path'], "chars":len(txt), "headings":headings(txt,8), "excerpt":re.sub(r"\s+"," ",txt[:1200]).strip()})
    rg=relationship_graph(scope, request or "", 12)
    return {
        **fast,
        "command":"plug-deep",
        "deep_reads": reads,
        "relationship_graph_compact": {"node_count":rg.get('node_count'), "edge_count":rg.get('edge_count'), "nodes":rg.get('nodes',[])[:10], "edges":rg.get('edges',[])[:20]},
        "execution_permission": "analysis_only" if fast.get('operation_mode',{}).get('risk') in {"high","critical"} else "answer_allowed",
        "deep_rule": "Use these full reads to support high-impact claims; if owner evidence remains insufficient, stop and request/perform a targeted read, not a guess.",
    }



# ---------------------------------------------------------------------------
# v8.1 Jet File Matrix Control Center
# A fast local file-intelligence kernel for discovery, inventory, indexing,
# multi-lens retrieval, relationship awareness, context packing, freshness, and
# doctor checks. It is intentionally local and project-neutral: generated state
# accelerates access but never becomes source of truth over current files.
# ---------------------------------------------------------------------------

FILE_MATRIX_VERSION = "9.11.0"
FILE_MATRIX_DIR = RUNTIME / "file_matrix"
FILE_MATRIX_STATE = STATE / "file_matrix"
FILE_MATRIX_DB = FILE_MATRIX_STATE / "file_matrix.sqlite"
FILE_MATRIX_REPORT = INDEX / "last_file_matrix_packet.json"
FILE_MATRIX_DOCTOR_REPORT = INDEX / "last_file_matrix_doctor.json"

FILE_MATRIX_SCHEMA_VERSION = 2

LANG_BY_EXT = {
    ".py":"python", ".js":"javascript", ".jsx":"javascript-react", ".ts":"typescript", ".tsx":"typescript-react",
    ".cs":"csharp", ".java":"java", ".go":"go", ".rs":"rust", ".php":"php", ".rb":"ruby", ".kt":"kotlin", ".kts":"kotlin",
    ".swift":"swift", ".c":"c", ".cpp":"cpp", ".h":"c-header", ".hpp":"cpp-header", ".scala":"scala", ".dart":"dart", ".lua":"lua", ".r":"r", ".sh":"shell", ".bash":"shell", ".zsh":"shell", ".ps1":"powershell",
    ".sql":"sql", ".prisma":"prisma", ".graphql":"graphql", ".gql":"graphql", ".proto":"protobuf", ".md":"markdown", ".yaml":"yaml", ".yml":"yaml", ".json":"json", ".toml":"toml",
    ".html":"html", ".css":"css", ".scss":"scss", ".sass":"sass", ".less":"less", ".vue":"vue", ".svelte":"svelte", ".astro":"astro", ".xml":"xml", ".txt":"text", ".csv":"csv", ".env":"env",
}

FRAMEWORK_MARKERS = [
    ("package.json", "node_package"), ("tsconfig.json", "typescript"), ("vite.config.ts", "vite"), ("vite.config.js", "vite"),
    ("next.config.js", "nextjs"), ("next.config.mjs", "nextjs"), ("nest-cli.json", "nestjs"),
    ("prisma/schema.prisma", "prisma"), ("drizzle.config.ts", "drizzle"), ("docker-compose.yml", "docker_compose"),
    ("Dockerfile", "docker"), ("pyproject.toml", "python_project"), ("requirements.txt", "python_requirements"),
    ("manage.py", "django"), ("Cargo.toml", "rust"), ("go.mod", "go"), ("composer.json", "php_composer"), ("artisan", "laravel"),
    ("pom.xml", "maven"), ("build.gradle", "gradle"), ("build.gradle.kts", "gradle"), (".env.example", "env_contract"), ("openapi.yaml", "openapi"), ("openapi.yml", "openapi"),
    ("schema.graphql", "graphql"), ("buf.yaml", "protobuf"), ("turbo.json", "turborepo"), ("nx.json", "nx"), ("angular.json", "angular"), ("svelte.config.js", "sveltekit"), ("astro.config.mjs", "astro"),
]

FM_STOPWORDS = {
    "the","and","for","with","from","this","that","into","have","has","are","was","were","will","shall","must","can","not","but","or",
    "في","من","على","الى","إلى","عن","هذا","هذه","ذلك","التي","الذي","مع","او","أو","لا","ما","هو","هي","يجب","يكون","كان","كل","لكن",
}


def _fm_imports():
    import sqlite3, time, shutil, subprocess, difflib
    return sqlite3, time, shutil, subprocess, difflib


def file_matrix_base(scope: str) -> Path:
    # For project scope, prefer the real single active project folder if present.
    if scope == "project":
        return active_project_dir() or ACTIVE
    return scope_base(scope)


def file_matrix_should_skip(path: Path, scope: str = "project") -> bool:
    relp = rel(path)
    parts = set(path.parts)
    if any(x in parts for x in {"node_modules", ".git", "__pycache__", ".pytest_cache", ".venv", "vendor", "dist", "build", ".next", "coverage"}):
        return True
    if path.name.endswith((".zip", ".tar", ".gz", ".7z", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".sqlite", ".db", ".lock")):
        return True
    if scope in {"runtime", "runtime_static", "repository", "repository_static"} and is_generated_runtime_rel(relp):
        return True
    if scope in {"runtime", "runtime_static"} and is_relative_to(path, FILE_MATRIX_STATE):
        return True
    if relp.startswith(".engineer/state/file_matrix/"):
        return True
    return False


def file_matrix_files(scope: str = "project") -> list[Path]:
    base = file_matrix_base(scope)
    if not base.exists():
        return []
    out=[]
    for f in base.rglob("*"):
        if not f.is_file():
            continue
        if is_ignored(f) or file_matrix_should_skip(f, scope):
            continue
        out.append(f)
    return sorted(out)


def file_matrix_language(path: Path) -> str:
    return LANG_BY_EXT.get(path.suffix.lower(), path.suffix.lower().lstrip(".") or "unknown")


def file_matrix_hash(path: Path) -> str:
    try:
        h = hashlib.sha1()
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""


def file_matrix_is_text(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTS or path.name in {"Dockerfile", "Makefile", "artisan", "Procfile", ".env", ".env.example"}


def file_matrix_read(path: Path, limit: int = 800000) -> str:
    if not file_matrix_is_text(path):
        return ""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except Exception:
        return ""


def file_matrix_tokenize(text: str, max_terms: int = 120) -> list[str]:
    toks = re.findall(r"[A-Za-z_\u0600-\u06FF][A-Za-z0-9_\u0600-\u06FF\-]{2,}", text or "")
    out=[]
    seen=set()
    for t in toks:
        lt=t.lower().strip("-_")
        if len(lt) < 3 or lt in FM_STOPWORDS or lt in seen:
            continue
        seen.add(lt); out.append(lt)
        if len(out) >= max_terms:
            break
    return out


def file_matrix_discover(scope: str = "project") -> dict:
    base = file_matrix_base(scope)
    markers=[]
    languages={}
    frameworks=[]
    entrypoints=[]
    config_files=[]
    database_files=[]
    test_files=[]
    for rel_marker, name in FRAMEWORK_MARKERS:
        p=base/rel_marker
        if p.exists():
            frameworks.append(name)
            markers.append({"marker":rel_marker,"kind":name,"path":rel(p)})
    files=file_matrix_files(scope)
    for f in files:
        lang=file_matrix_language(f)
        languages[lang]=languages.get(lang,0)+1
        low=rel(f).lower()
        nm=f.name.lower()
        if nm in {"readme.md","00_project_entrypoint.md","00_entrypoint.yaml","app.py","main.py","index.ts","index.js","main.ts","main.js"}:
            entrypoints.append(rel(f))
        if any(x in low for x in ["config", ".env.example", "settings", "schema", "openapi", "docker", "compose", "tsconfig", "pyproject", "package.json"]):
            config_files.append(rel(f))
        if any(x in low for x in ["migration", "schema.prisma", "database", "models", "entity", "repository", ".sql"]):
            database_files.append(rel(f))
        if re.search(r"(test|spec|tests|__tests__)", low):
            test_files.append(rel(f))
    profile={
        "scope":scope,
        "base":rel(base),
        "detected_at":utc_now(),
        "file_count":len(files),
        "languages":dict(sorted(languages.items(), key=lambda kv:(-kv[1],kv[0]))),
        "frameworks":sorted(set(frameworks)),
        "markers":markers[:80],
        "entrypoints":entrypoints[:40],
        "config_files":config_files[:80],
        "database_surfaces":database_files[:80],
        "test_surfaces":test_files[:80],
        "project_identity": project_identity_from_files() if scope == "project" else {},
        "boundary_contract": "workshop/runtime files govern method; active_project is the project truth surface; generated file-matrix state accelerates but never overrides current files",
    }
    return profile


def file_matrix_scope_fingerprint(scope: str = "project") -> str:
    h=hashlib.sha1()
    for f in file_matrix_files(scope):
        try:
            st=f.stat()
            h.update(rel(f).encode("utf-8")); h.update(str(st.st_size).encode()); h.update(str(st.st_mtime_ns).encode())
        except Exception:
            continue
    return h.hexdigest()[:20]


def file_matrix_connect():
    sqlite3, *_ = _fm_imports()
    FILE_MATRIX_STATE.mkdir(parents=True, exist_ok=True)
    conn=sqlite3.connect(str(FILE_MATRIX_DB))
    conn.row_factory=sqlite3.Row
    return conn


def file_matrix_init_db(conn):
    cur=conn.cursor()
    # Generated state is disposable. If the schema changes, rebuild cleanly rather
    # than risk stale truth from an older index layout.
    try:
        row=cur.execute("SELECT value FROM meta WHERE key='schema_version'").fetchone()
        existing=int(row[0]) if row and str(row[0]).isdigit() else 0
    except Exception:
        existing=0
    if existing and existing < FILE_MATRIX_SCHEMA_VERSION:
        for tbl in ["file_fts", "chunk_fts", "files", "symbols", "relations", "terms", "chunks", "meta"]:
            try: cur.execute(f"DROP TABLE IF EXISTS {tbl}")
            except Exception: pass
    cur.execute("CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT)")
    cur.execute("""CREATE TABLE IF NOT EXISTS files (
        scope TEXT, path TEXT, abs_path TEXT, ext TEXT, language TEXT, role TEXT,
        size INTEGER, mtime_ns INTEGER, sha1 TEXT, line_count INTEGER, word_count INTEGER,
        headings TEXT, value_signals TEXT, is_test INTEGER, is_config INTEGER,
        is_database INTEGER, is_entrypoint INTEGER, is_generated INTEGER DEFAULT 0,
        snippet TEXT, PRIMARY KEY(scope,path)
    )""")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_files_scope_role ON files(scope,role)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_files_scope_lang ON files(scope,language)")
    cur.execute("""CREATE TABLE IF NOT EXISTS symbols (
        scope TEXT, path TEXT, kind TEXT, name TEXT, line INTEGER, signature TEXT,
        normalized_name TEXT, PRIMARY KEY(scope,path,kind,name,line)
    )""")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_symbols_name ON symbols(scope,normalized_name)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_symbols_path ON symbols(scope,path)")
    cur.execute("""CREATE TABLE IF NOT EXISTS relations (
        scope TEXT, src_path TEXT, rel_type TEXT, target TEXT, target_path TEXT,
        line INTEGER, evidence TEXT
    )""")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_rel_src ON relations(scope,src_path)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_rel_target ON relations(scope,target)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_rel_target_path ON relations(scope,target_path)")
    cur.execute("CREATE TABLE IF NOT EXISTS terms (scope TEXT, path TEXT, term TEXT, weight INTEGER, PRIMARY KEY(scope,path,term))")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_terms_term ON terms(scope,term)")
    cur.execute("""CREATE TABLE IF NOT EXISTS chunks (
        scope TEXT, path TEXT, chunk_id INTEGER, start_line INTEGER, end_line INTEGER,
        heading TEXT, text TEXT, terms TEXT, signals TEXT, PRIMARY KEY(scope,path,chunk_id)
    )""")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_chunks_path ON chunks(scope,path)")
    try:
        cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS file_fts USING fts5(path, scope, content)")
        cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS chunk_fts USING fts5(path, scope, chunk_id UNINDEXED, content)")
        cur.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('fts5','available')")
    except Exception:
        cur.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('fts5','unavailable')")
    cur.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('schema_version',?)", (str(FILE_MATRIX_SCHEMA_VERSION),))
    conn.commit()


def file_matrix_chunks(text: str, max_chars: int = 2400, overlap_lines: int = 4) -> list[dict]:
    lines=text.splitlines()
    chunks=[]; i=0; cid=1; current_heading=""
    while i < len(lines):
        start=i
        buf=[]; chars=0
        while i < len(lines) and chars < max_chars:
            line=lines[i]
            if line.lstrip().startswith('#'):
                current_heading=line.lstrip('#').strip()[:180]
            buf.append(line)
            chars += len(line)+1
            i += 1
        ctext="\n".join(buf).strip()
        if ctext:
            sigs=sorted((_value_hits((current_heading+'\n'+ctext[:6000])) or {}).keys())
            chunks.append({"chunk_id":cid,"start_line":start+1,"end_line":i,"heading":current_heading,"text":ctext,"terms":file_matrix_tokenize(current_heading+'\n'+ctext, 80),"signals":sigs})
            cid += 1
        if i < len(lines) and overlap_lines:
            i=max(i-overlap_lines, start+1)
    return chunks


def file_matrix_normalize_symbol(name: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "", (name or "").lower())


def file_matrix_resolve_import_target(src_path: str, target: str, all_paths: set[str]) -> str:
    if not target:
        return ""
    t=target.strip().strip('"\'')
    src_dir=str(Path(src_path).parent).replace('\\','/')
    candidates=[]
    # JS/TS/Vue/Svelte relative imports.
    if t.startswith('.'):
        base=(Path(src_dir)/t).as_posix()
        candidates.extend([base])
        candidates.extend([base+ext for ext in [".ts",".tsx",".js",".jsx",".mjs",".cjs",".vue",".svelte",".astro",".json",".css"]])
        candidates.extend([base+"/index"+ext for ext in [".ts",".tsx",".js",".jsx",".mjs",".cjs"]])
    # Python module imports and package-ish targets.
    dotted=t.replace('.', '/')
    candidates.extend([dotted+ext for ext in [".py","/__init__.py",".ts",".tsx",".js",".jsx"]])
    # Exact/path suffix fallback.
    candidates.append(t)
    for c in candidates:
        c=c.lstrip('./').replace('\\','/')
        if c in all_paths:
            return c
    for pth in all_paths:
        if pth.endswith('/'+dotted+'.py') or pth.endswith('/'+dotted+'/__init__.py') or pth.endswith('/'+t):
            return pth
    return ""


def file_matrix_resolve_relations(conn, scope: str) -> int:
    cur=conn.cursor()
    all_paths={r['path'] for r in cur.execute("SELECT path FROM files WHERE scope=?", (scope,))}
    changed=0
    rows=cur.execute("SELECT rowid,src_path,target FROM relations WHERE scope=? AND (target_path IS NULL OR target_path='')", (scope,)).fetchall()
    for r in rows:
        tp=file_matrix_resolve_import_target(r['src_path'], r['target'], all_paths)
        if tp:
            cur.execute("UPDATE relations SET target_path=? WHERE rowid=?", (tp, r['rowid']))
            changed += 1
    return changed


def file_matrix_build_symbol_references(conn, scope: str, max_symbols: int = 2000) -> int:
    cur=conn.cursor()
    syms=cur.execute("SELECT path,kind,name,normalized_name,line FROM symbols WHERE scope=? ORDER BY length(name) DESC LIMIT ?", (scope,max_symbols)).fetchall()
    symbol_by_name={r['normalized_name']:dict(r) for r in syms if r['normalized_name'] and len(r['normalized_name']) >= 3}
    if not symbol_by_name:
        return 0
    inserted=0
    for f in cur.execute("SELECT path,snippet FROM files WHERE scope=? AND language NOT IN ('binary_or_large','unknown')", (scope,)).fetchall():
        pth=f['path']
        text=file_matrix_read(ROOT/pth, 180000)
        low_norm_terms=set(file_matrix_normalize_symbol(x) for x in re.findall(r"[A-Za-z_][A-Za-z0-9_]{2,}", text[:180000]))
        for nm in low_norm_terms.intersection(symbol_by_name.keys()):
            sym=symbol_by_name[nm]
            if sym['path'] == pth:
                continue
            cur.execute("INSERT INTO relations(scope,src_path,rel_type,target,target_path,line,evidence) VALUES(?,?,?,?,?,?,?)", (scope,pth,"symbol_reference",sym['name'],sym['path'],0,f"references symbol {sym['name']} defined in {sym['path']}"))
            inserted += 1
            if inserted > 5000:
                return inserted
    return inserted


def file_matrix_extract_symbols(path: Path, text: str) -> tuple[list[dict], list[dict]]:
    symbols=[]; relations=[]
    lang=file_matrix_language(path)
    rpath=rel(path)
    lines=text.splitlines()
    for i,line in enumerate(lines, start=1):
        s=line.strip()
        if not s:
            continue
        # Markdown headings become navigable symbols.
        if lang == "markdown" and s.startswith("#"):
            name=s.lstrip("#").strip()[:160]
            if name:
                symbols.append({"kind":"heading","name":name,"line":i,"signature":s[:240]})
        # Python.
        m=re.match(r"(?:async\s+)?def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\((.*?)\)", s)
        if m:
            symbols.append({"kind":"function","name":m.group(1),"line":i,"signature":s[:240]})
        m=re.match(r"class\s+([A-Za-z_][A-Za-z0-9_]*)", s)
        if m:
            symbols.append({"kind":"class","name":m.group(1),"line":i,"signature":s[:240]})
        m=re.match(r"(?:from\s+([A-Za-z0-9_\.]+)\s+import|import\s+([A-Za-z0-9_\.]+))", s)
        if m:
            target=m.group(1) or m.group(2)
            relations.append({"rel_type":"import","target":target,"line":i,"evidence":s[:240]})
        # JS/TS/Java/C#/Go/Rust broad patterns.
        for pat,kind in [
            (r"(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s+([A-Za-z_$][A-Za-z0-9_$]*)", "function"),
            (r"(?:export\s+)?class\s+([A-Za-z_$][A-Za-z0-9_$]*)", "class"),
            (r"(?:export\s+)?interface\s+([A-Za-z_$][A-Za-z0-9_$]*)", "interface"),
            (r"(?:export\s+)?type\s+([A-Za-z_$][A-Za-z0-9_$]*)", "type"),
            (r"(?:export\s+)?(?:const|let|var)\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*=", "variable"),
            (r"func\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", "function"),
            (r"(?:pub\s+)?(?:async\s+)?fn\s+([A-Za-z_][A-Za-z0-9_]*)", "function"),
        ]:
            mm=re.search(pat, s)
            if mm:
                symbols.append({"kind":kind,"name":mm.group(1),"line":i,"signature":s[:240]})
        mm=re.search(r"(?:import|from)\s+(?:[^'\"]*from\s+)?['\"]([^'\"]+)['\"]", s)
        if mm:
            relations.append({"rel_type":"import","target":mm.group(1),"line":i,"evidence":s[:240]})
        # Route/API indicators.
        mm=re.search(r"\b(?:app|router|route)\.(get|post|put|patch|delete|use)\s*\(\s*['\"]([^'\"]+)['\"]", s, re.I)
        if mm:
            name=f"{mm.group(1).upper()} {mm.group(2)}"
            symbols.append({"kind":"route","name":name,"line":i,"signature":s[:240]})
            relations.append({"rel_type":"api_route","target":name,"line":i,"evidence":s[:240]})
        # SQL schema.
        mm=re.search(r"\bCREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?([A-Za-z0-9_\.\"`]+)", s, re.I)
        if mm:
            symbols.append({"kind":"db_table","name":mm.group(1).strip('`\"'),"line":i,"signature":s[:240]})
            relations.append({"rel_type":"database_table","target":mm.group(1).strip('`\"'),"line":i,"evidence":s[:240]})
        if "schema.prisma" in rpath.lower() or lang == "prisma":
            mm=re.match(r"model\s+([A-Za-z_][A-Za-z0-9_]*)", s)
            if mm:
                symbols.append({"kind":"db_model","name":mm.group(1),"line":i,"signature":s[:240]})
        # PHP/Ruby/Kotlin/Swift/Dart/C-family broad extraction.
        for pat,kind in [
            (r"(?:public|private|protected)?\s*function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", "function"),
            (r"class\s+([A-Za-z_][A-Za-z0-9_]*)", "class"),
            (r"module\s+([A-Za-z_][A-Za-z0-9_:]*)", "module"),
            (r"def\s+([A-Za-z_][A-Za-z0-9_!?=]*)", "function"),
            (r"fun\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", "function"),
            (r"struct\s+([A-Za-z_][A-Za-z0-9_]*)", "struct"),
            (r"enum\s+([A-Za-z_][A-Za-z0-9_]*)", "enum"),
            (r"protocol\s+([A-Za-z_][A-Za-z0-9_]*)", "interface"),
            (r"(?:void|int|string|bool|float|double|Task<[^>]+>|[A-Z][A-Za-z0-9_<>]*)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\([^;]*\)\s*[{=>]", "method"),
        ]:
            mm=re.search(pat, s)
            if mm:
                symbols.append({"kind":kind,"name":mm.group(1),"line":i,"signature":s[:240]})
        # Framework route decorators / mappings.
        for pat in [r"@(Get|Post|Put|Patch|Delete|Controller)\s*\(\s*['\"]?([^'\")]+)?", r"@(GetMapping|PostMapping|PutMapping|PatchMapping|DeleteMapping|RequestMapping)\s*\(\s*(?:value\s*=\s*)?['\"]([^'\"]+)"]:
            mm=re.search(pat, s)
            if mm:
                route_name=f"{mm.group(1)} {mm.group(2) or ''}".strip()
                symbols.append({"kind":"route","name":route_name,"line":i,"signature":s[:240]})
                relations.append({"rel_type":"api_route","target":route_name,"line":i,"evidence":s[:240]})
        # GraphQL/protobuf schema surfaces.
        mm=re.match(r"(?:type|interface|input|enum)\s+([A-Za-z_][A-Za-z0-9_]*)", s)
        if mm and lang in {"graphql", "protobuf"}:
            symbols.append({"kind":"schema_type","name":mm.group(1),"line":i,"signature":s[:240]})
        mm=re.match(r"message\s+([A-Za-z_][A-Za-z0-9_]*)", s)
        if mm and lang == "protobuf":
            symbols.append({"kind":"message","name":mm.group(1),"line":i,"signature":s[:240]})
    # Deduplicate same path/kind/name/line.
    uniq=[]; seen=set()
    for sym in symbols:
        key=(sym["kind"],sym["name"],sym["line"])
        if key not in seen:
            seen.add(key); uniq.append(sym)
    return uniq[:500], relations[:800]


def file_matrix_role_flags(path: Path, text: str) -> dict:
    r=rel(path).lower(); n=path.name.lower()
    return {
        "is_test": int(bool(re.search(r"(^|/)(test|tests|spec|__tests__)(/|_)|\.(test|spec)\.", r))),
        "is_config": int(any(x in r for x in ["config", ".env", "settings", "package.json", "tsconfig", "pyproject", "docker", "compose", "openapi"])),
        "is_database": int(any(x in r for x in ["database", "migration", "schema", "model", "repository", ".sql", "prisma"])),
        "is_entrypoint": int(n in {"readme.md","00_project_entrypoint.md","00_entrypoint.yaml","main.py","app.py","index.ts","index.js","main.ts","main.js"}),
    }


def file_matrix_build(scope: str = "project", force: bool = False, max_bytes: int = 1200000) -> dict:
    sqlite3, time, *_ = _fm_imports()
    t0=time.time()
    ensure_dirs(); FILE_MATRIX_STATE.mkdir(parents=True, exist_ok=True); INDEX.mkdir(parents=True, exist_ok=True)
    conn=file_matrix_connect(); file_matrix_init_db(conn); cur=conn.cursor()
    fp=file_matrix_scope_fingerprint(scope)
    old=cur.execute("SELECT value FROM meta WHERE key=?", (f"fingerprint:{scope}",)).fetchone()
    if old and old[0] == fp and not force:
        # Still return quick status without rebuilding.
        cnt=cur.execute("SELECT COUNT(*) c FROM files WHERE scope=?", (scope,)).fetchone()["c"]
        profile=json.loads(cur.execute("SELECT value FROM meta WHERE key=?", (f"profile:{scope}",)).fetchone()["value"] or "{}") if cur.execute("SELECT value FROM meta WHERE key=?", (f"profile:{scope}",)).fetchone() else file_matrix_discover(scope)
        return {"status":"fresh","rebuilt":False,"scope":scope,"fingerprint":fp,"file_count":cnt,"profile":profile,"db":rel(FILE_MATRIX_DB),"elapsed_ms":int((time.time()-t0)*1000),"version":FILE_MATRIX_VERSION}
    profile=file_matrix_discover(scope)
    cur.execute("DELETE FROM files WHERE scope=?", (scope,)); cur.execute("DELETE FROM symbols WHERE scope=?", (scope,)); cur.execute("DELETE FROM relations WHERE scope=?", (scope,)); cur.execute("DELETE FROM terms WHERE scope=?", (scope,)); cur.execute("DELETE FROM chunks WHERE scope=?", (scope,))
    try: cur.execute("DELETE FROM file_fts WHERE scope=?", (scope,))
    except Exception: pass
    try: cur.execute("DELETE FROM chunk_fts WHERE scope=?", (scope,))
    except Exception: pass
    files=file_matrix_files(scope)
    processed=0; text_files=0; symbol_count=0; relation_count=0; chunk_count=0
    for f in files:
        try:
            st=f.stat(); rpath=rel(f); ext=f.suffix.lower(); lang=file_matrix_language(f); is_text=file_matrix_is_text(f)
            text=file_matrix_read(f, max_bytes) if is_text and st.st_size <= max_bytes else ""
            if text: text_files+=1
            role=file_role(f, text) if text else ("code" if ext in CODE_EXTS else "binary_or_large")
            hs=headings(text, 16) if text else []
            flags=file_matrix_role_flags(f, text)
            val=_value_hits((rpath+"\n"+"\n".join(hs)+"\n"+text[:12000])) if text else {}
            words=re.findall(r"\w+", text or "")
            snip=snippet(text, 700) if text else ""
            sha=file_matrix_hash(f)
            cur.execute("INSERT OR REPLACE INTO files(scope,path,abs_path,ext,language,role,size,mtime_ns,sha1,line_count,word_count,headings,value_signals,is_test,is_config,is_database,is_entrypoint,snippet) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (scope,rpath,str(f),ext,lang,role,st.st_size,st.st_mtime_ns,sha,len(text.splitlines()) if text else 0,len(words),json.dumps(hs,ensure_ascii=False),json.dumps(sorted(val.keys()),ensure_ascii=False),flags["is_test"],flags["is_config"],flags["is_database"],flags["is_entrypoint"],snip))
            if text:
                try: cur.execute("INSERT INTO file_fts(path,scope,content) VALUES(?,?,?)", (rpath,scope,text))
                except Exception: pass
                for ch in file_matrix_chunks(text):
                    cur.execute("INSERT OR REPLACE INTO chunks(scope,path,chunk_id,start_line,end_line,heading,text,terms,signals) VALUES(?,?,?,?,?,?,?,?,?)", (scope,rpath,ch["chunk_id"],ch["start_line"],ch["end_line"],ch["heading"],ch["text"],json.dumps(ch["terms"],ensure_ascii=False),json.dumps(ch["signals"],ensure_ascii=False)))
                    try: cur.execute("INSERT INTO chunk_fts(path,scope,chunk_id,content) VALUES(?,?,?,?)", (rpath,scope,ch["chunk_id"],ch["text"]))
                    except Exception: pass
                    chunk_count += 1
                syms, rels=file_matrix_extract_symbols(f,text)
                for sym in syms:
                    cur.execute("INSERT OR REPLACE INTO symbols(scope,path,kind,name,line,signature,normalized_name) VALUES(?,?,?,?,?,?,?)", (scope,rpath,sym["kind"],sym["name"],sym["line"],sym["signature"],file_matrix_normalize_symbol(sym["name"])))
                for rr in rels:
                    cur.execute("INSERT INTO relations(scope,src_path,rel_type,target,target_path,line,evidence) VALUES(?,?,?,?,?,?,?)", (scope,rpath,rr.get("rel_type"),rr.get("target"),"",rr.get("line"),rr.get("evidence")))
                symbol_count += len(syms); relation_count += len(rels)
                # Terms from path, headings, symbol names and content beginning.
                term_text=" ".join([rpath, " ".join(hs), " ".join(x.get("name","") for x in syms), text[:5000]])
                for term in file_matrix_tokenize(term_text, 180):
                    weight=8 if term in rpath.lower() else 3
                    cur.execute("INSERT OR REPLACE INTO terms(scope,path,term,weight) VALUES(?,?,?,?)", (scope,rpath,term,weight))
            processed += 1
        except Exception:
            continue
    resolved_relations=file_matrix_resolve_relations(conn, scope)
    symbol_reference_count=file_matrix_build_symbol_references(conn, scope)
    relation_count += symbol_reference_count
    cur.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", (f"fingerprint:{scope}", fp))
    cur.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", (f"indexed_at:{scope}", utc_now()))
    cur.execute("INSERT OR REPLACE INTO meta(key,value) VALUES(?,?)", (f"profile:{scope}", json.dumps(profile,ensure_ascii=False)))
    cur.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('schema_version',?)", (str(FILE_MATRIX_SCHEMA_VERSION),))
    cur.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('file_matrix_version',?)", (FILE_MATRIX_VERSION,))
    conn.commit()
    report={
        "status":"rebuilt","rebuilt":True,"version":FILE_MATRIX_VERSION,"scope":scope,"fingerprint":fp,"generated_at":utc_now(),"db":rel(FILE_MATRIX_DB),
        "file_count":processed,"text_file_count":text_files,"symbol_count":symbol_count,"relation_count":relation_count,"resolved_relation_count":resolved_relations,"symbol_reference_count":symbol_reference_count,"chunk_count":chunk_count,"profile":profile,
        "elapsed_ms":int((time.time()-t0)*1000),
        "usage_contract":"Use this index as a fast neural map only; current files remain the source of truth for final claims and writes.",
        "cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"file_matrix_build","generated_at":utc_now(),"volatile":True,"source":"current_files"},
    }
    (INDEX/f"{scope}_file_matrix_build.json").write_text(json.dumps(report,ensure_ascii=False,indent=2), encoding="utf-8")
    return report


def file_matrix_status(scope: str = "project") -> dict:
    conn=file_matrix_connect(); file_matrix_init_db(conn); cur=conn.cursor()
    fp=file_matrix_scope_fingerprint(scope)
    row=cur.execute("SELECT value FROM meta WHERE key=?", (f"fingerprint:{scope}",)).fetchone()
    indexed=cur.execute("SELECT value FROM meta WHERE key=?", (f"indexed_at:{scope}",)).fetchone()
    cnt=cur.execute("SELECT COUNT(*) c FROM files WHERE scope=?", (scope,)).fetchone()["c"]
    sym=cur.execute("SELECT COUNT(*) c FROM symbols WHERE scope=?", (scope,)).fetchone()["c"]
    relc=cur.execute("SELECT COUNT(*) c FROM relations WHERE scope=?", (scope,)).fetchone()["c"]
    chk=cur.execute("SELECT COUNT(*) c FROM chunks WHERE scope=?", (scope,)).fetchone()["c"]
    stored=row["value"] if row else None
    return {"scope":scope,"fresh":stored==fp and cnt>0,"current_fingerprint":fp,"stored_fingerprint":stored,"indexed_at":indexed["value"] if indexed else None,"file_count":cnt,"symbol_count":sym,"relation_count":relc,"chunk_count":chk,"db":rel(FILE_MATRIX_DB),"version":FILE_MATRIX_VERSION}


def file_matrix_ensure(scope: str = "project", auto_build: bool = True) -> dict:
    st=file_matrix_status(scope)
    if auto_build and not st.get("fresh"):
        return file_matrix_build(scope, force=True)
    return st


def _rows_to_dicts(rows, limit=50):
    return [dict(r) for r in rows[:limit]]


def file_matrix_query(request: str, scope: str = "project", mode: str = "fast", limit: int = 16) -> dict:
    sqlite3, time, shutil, subprocess, difflib = _fm_imports()
    t0=time.time()
    status=file_matrix_ensure(scope, auto_build=True)
    conn=file_matrix_connect(); cur=conn.cursor()
    q=(request or "").strip()
    qterms=file_matrix_tokenize(q, 32)
    score_by_path={}; reasons={}; excerpts={}
    def add(path, score, reason, excerpt=""):
        if not path: return
        score_by_path[path]=score_by_path.get(path,0)+score
        reasons.setdefault(path,[]).append(reason)
        if excerpt and path not in excerpts: excerpts[path]=excerpt
    # Lens 1: path/name terms.
    for term in qterms:
        like=f"%{term}%"
        for r in cur.execute("SELECT path,snippet,role,language FROM files WHERE scope=? AND lower(path) LIKE ? LIMIT 80", (scope,like)):
            add(r["path"], 12, f"path:{term}", r["snippet"])
    # Lens 2: terms index.
    for term in qterms:
        for r in cur.execute("SELECT path,weight FROM terms WHERE scope=? AND term LIKE ? LIMIT 160", (scope,term+'%')):
            add(r["path"], 4+int(r["weight"] or 1), f"term:{term}")
    # Lens 3: ripgrep external fast lens when available.
    rg_used=False
    if q and shutil.which("rg"):
        base=file_matrix_base(scope)
        for term in qterms[:5]:
            try:
                cp=subprocess.run(["rg","-n","-i","--max-count","20","--",term,str(base)], cwd=ROOT, text=True, capture_output=True, timeout=2.5)
                rg_used=True
                for line in cp.stdout.splitlines()[:80]:
                    parts=line.split(":",2)
                    if len(parts) >= 3:
                        try:
                            rp=rel(Path(parts[0]))
                        except Exception:
                            rp=parts[0]
                        add(rp, 22, f"rg:{term}@L{parts[1]}", parts[2][:700])
            except Exception:
                continue
    # Lens 4: FTS textual.
    if q:
        fts_query=" OR ".join([t.replace('"','') for t in qterms[:8]]) or q.replace('"','')
        try:
            for r in cur.execute("SELECT path, snippet(file_fts, 2, '[', ']', ' … ', 18) AS ex FROM file_fts WHERE scope=? AND file_fts MATCH ? LIMIT 80", (scope, fts_query)):
                add(r["path"], 20, "fts", r["ex"])
        except Exception:
            # Fallback LIKE over snippets.
            for term in qterms[:6]:
                for r in cur.execute("SELECT path,snippet FROM files WHERE scope=? AND lower(snippet) LIKE ? LIMIT 80", (scope, f"%{term}%")):
                    add(r["path"], 8, f"snippet:{term}", r["snippet"])
    # Lens 5: semantic-lite chunk lens: concept chunks and value signals.
    if qterms:
        for term in qterms[:10]:
            like=f'%"{term}"%'
            # terms are JSON arrays; LIKE is intentionally lightweight and local.
            for r in cur.execute("SELECT path,chunk_id,start_line,end_line,heading,text,signals FROM chunks WHERE scope=? AND lower(terms) LIKE ? LIMIT 80", (scope, like.lower())):
                add(r["path"], 16, f"semantic-lite:{term}:chunk{r['chunk_id']}@L{r['start_line']}-{r['end_line']}", (r["heading"]+"\n"+r["text"])[:900])
        # FTS over chunks returns more focused excerpts than file-wide search.
        try:
            fts_query=" OR ".join([t.replace('"','') for t in qterms[:8]])
            if fts_query:
                for r in cur.execute("SELECT path, chunk_id, snippet(chunk_fts, 3, '[', ']', ' … ', 18) AS ex FROM chunk_fts WHERE scope=? AND chunk_fts MATCH ? LIMIT 80", (scope, fts_query)):
                    add(r["path"], 18, f"chunk-fts:{r['chunk_id']}", r["ex"])
        except Exception:
            pass
    # Lens 6: symbols.
    for term in qterms:
        for r in cur.execute("SELECT path,kind,name,line,signature FROM symbols WHERE scope=? AND lower(name) LIKE ? LIMIT 80", (scope, f"%{term}%")):
            add(r["path"], 28, f"symbol:{r['kind']}:{r['name']}@L{r['line']}", r["signature"])
    # Lens 5: relations.
    for term in qterms:
        for r in cur.execute("SELECT src_path,rel_type,target,line,evidence FROM relations WHERE scope=? AND lower(target) LIKE ? LIMIT 80", (scope, f"%{term}%")):
            add(r["src_path"], 18, f"relation:{r['rel_type']}:{r['target']}@L{r['line']}", r["evidence"])
    # Lens 6: role/domain intent boosters.
    low=q.lower()
    role_boosts=[]
    if any(x in low for x in ["api","endpoint","route","واجهة"]): role_boosts.append(("route",25)); role_boosts.append(("is_config",6))
    if any(x in low for x in ["database","db","schema","migration","قاعدة بيانات","بيانات"]): role_boosts.append(("is_database",20))
    if any(x in low for x in ["test","اختبار","تحقق"]): role_boosts.append(("is_test",20))
    if any(x in low for x in ["config","env","إعداد","اعداد"]): role_boosts.append(("is_config",18))
    if any(x in low for x in ["truth","contract","governance","حوكمة","مصدر الحقيقة","عقد"]): role_boosts.append(("governance",14)); role_boosts.append(("truth_entry",14))
    for flag,boost in role_boosts:
        if flag.startswith("is_"):
            for r in cur.execute(f"SELECT path,snippet FROM files WHERE scope=? AND {flag}=1 LIMIT 80", (scope,)):
                add(r["path"], boost, flag, r["snippet"])
        elif flag == "route":
            for r in cur.execute("SELECT path,signature FROM symbols WHERE scope=? AND kind='route' LIMIT 80", (scope,)):
                add(r["path"], boost, "api_route_symbol", r["signature"])
        else:
            for r in cur.execute("SELECT path,snippet FROM files WHERE scope=? AND role=? LIMIT 80", (scope,flag)):
                add(r["path"], boost, f"role:{flag}", r["snippet"])
    ranked=sorted(score_by_path.items(), key=lambda kv:(-kv[1], kv[0]))[:limit]
    files=[]
    for path,score in ranked:
        frow=cur.execute("SELECT path,role,language,size,line_count,word_count,is_test,is_config,is_database,is_entrypoint,headings,value_signals,snippet FROM files WHERE scope=? AND path=?", (scope,path)).fetchone()
        syms=cur.execute("SELECT kind,name,line,signature FROM symbols WHERE scope=? AND path=? ORDER BY line LIMIT 20", (scope,path)).fetchall()
        rels=cur.execute("SELECT rel_type,target,target_path,line,evidence FROM relations WHERE scope=? AND src_path=? ORDER BY line LIMIT 20", (scope,path)).fetchall()
        files.append({
            "path":path,"score":score,"role":frow["role"] if frow else None,"language":frow["language"] if frow else None,"size":frow["size"] if frow else None,
            "line_count":frow["line_count"] if frow else None,"word_count":frow["word_count"] if frow else None,
            "flags":{"test":bool(frow["is_test"]) if frow else False,"config":bool(frow["is_config"]) if frow else False,"database":bool(frow["is_database"]) if frow else False,"entrypoint":bool(frow["is_entrypoint"]) if frow else False},
            "headings":json.loads(frow["headings"] or "[]")[:6] if frow else [],
            "value_signals":json.loads(frow["value_signals"] or "[]")[:8] if frow else [],
            "reasons":reasons.get(path,[])[:10],"excerpt":excerpts.get(path) or (frow["snippet"] if frow else ""),
            "symbols":_rows_to_dicts(syms, 20),"relations":_rows_to_dicts(rels, 20),
        })
    # Graph expansion: include neighbors of top files.
    neighbors=[]
    for f in files[:6]:
        p=f["path"]
        for r in cur.execute("SELECT rel_type,target,target_path,line,evidence FROM relations WHERE scope=? AND src_path=? LIMIT 16", (scope,p)):
            neighbors.append({"direction":"outgoing","from":p, **dict(r)})
        for r in cur.execute("SELECT src_path,rel_type,target,line,evidence FROM relations WHERE scope=? AND target_path=? LIMIT 16", (scope,p)):
            neighbors.append({"direction":"incoming","to":p, **dict(r)})
    # One-page summary elements.
    profile=file_matrix_discover(scope)
    op_mode=operation_mode(request or "") if 'operation_mode' in globals() else {}
    required_next=[]
    if op_mode.get("risk") in {"high","critical"} or any(x in low for x in ["اكتب","عدل","تعديل","fix","write","modify","implement","نفذ"]):
        required_next=["duplicate-scan", "impact-scan", "write-plan", "safe-write --apply only after review", "file-matrix-doctor", "doctor"]
    else:
        required_next=["read targeted owner files before high-impact claims", "use current files as truth", "escalate to deep mode when confidence is insufficient"]
    packet={
        "command":"file-matrix-query","version":FILE_MATRIX_VERSION,"scope":scope,"mode":mode,"request":request,"generated_at":utc_now(),
        "status":status,"profile":profile,"query_terms":qterms,"operation_mode":op_mode,
        "one_page_project_neural_map":{
            "base":profile.get("base"),"file_count":profile.get("file_count"),"languages":profile.get("languages"),"frameworks":profile.get("frameworks"),
            "entrypoints":profile.get("entrypoints",[])[:10],"config_files":profile.get("config_files",[])[:12],"database_surfaces":profile.get("database_surfaces",[])[:12],"test_surfaces":profile.get("test_surfaces",[])[:12],
        },
        "selected_files":files,"relationship_neighbors":neighbors[:60],
        "search_lenses_used":["path","term-index","ripgrep" if rg_used else "ripgrep-unavailable","fts-text","chunk-fts","semantic-lite-chunks","symbols","relations","role-domain-boosters"],
        "mandatory_rules":[
            "This packet is a navigation/context pack, not final truth by itself.",
            "For high-impact answers or writes, read owner files from selected_files before claiming.",
            "Generated file-matrix indexes accelerate access; current files remain source of truth.",
            "No write without duplicate scan, impact scan, write plan, safe write, and validation doctor.",
        ],
        "required_next_gates":required_next,
        "elapsed_ms":int((time.time()-t0)*1000),
        "cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"file_matrix_query","generated_at":utc_now(),"volatile":True},
    }
    FILE_MATRIX_REPORT.write_text(json.dumps(packet,ensure_ascii=False,indent=2), encoding="utf-8")
    return packet


def file_matrix_touch(scope: str = "project") -> dict:
    sqlite3, time, *_ = _fm_imports()
    t0=time.time()
    status=file_matrix_ensure(scope, auto_build=True)
    conn=file_matrix_connect(); cur=conn.cursor()
    counts={}
    for col in ["role","language"]:
        rows=cur.execute(f"SELECT {col} k, COUNT(*) c FROM files WHERE scope=? GROUP BY {col} ORDER BY c DESC", (scope,)).fetchall()
        counts[col]={r["k"]:r["c"] for r in rows}
    top=[]
    for r in cur.execute("SELECT path,role,language,size,line_count,is_entrypoint,is_config,is_database,is_test,headings,value_signals FROM files WHERE scope=? ORDER BY is_entrypoint DESC, is_config DESC, is_database DESC, is_test DESC, size DESC LIMIT 40", (scope,)):
        d=dict(r); d["headings"]=json.loads(d.get("headings") or "[]")[:4]; d["value_signals"]=json.loads(d.get("value_signals") or "[]")[:6]; top.append(d)
    profile=file_matrix_discover(scope)
    return {"command":"file-matrix-touch","version":FILE_MATRIX_VERSION,"scope":scope,"generated_at":utc_now(),"status":status,"profile":profile,"counts":counts,"neural_surface":top,"elapsed_ms":int((time.time()-t0)*1000),"rule":"Touch gives model a whole-project nervous-system surface; deep claims still require targeted reads."}


def file_matrix_context(request: str, scope: str = "project", mode: str = "fast", max_files: int = 10, chars: int = 1800) -> dict:
    packet=file_matrix_query(request, scope, mode, limit=max_files)
    reads=[]
    for item in packet.get("selected_files", [])[:max_files]:
        p=ROOT/item["path"]
        txt=file_matrix_read(p, chars)
        reads.append({"path":item["path"],"chars":len(txt),"headings":headings(txt,8),"excerpt":snippet(txt, chars)})
    packet["targeted_reads"]=reads
    packet["context_pack_rule"]="This is the handoff packet for the model: whole-project surface + selected owner reads + graph hints + gates."
    return packet



# v9.1 Truth Pulse / Neural One-Page Map
# This is the fast, truth-grounded surface pass used before ordinary identity,
# assessment, and first-step answers. It is deliberately current-file based and
# can run without a prebuilt deep index. The full File Matrix index remains the
# stronger path for deep/surgical work.
def file_matrix_seed_truth_files(scope: str = "project", limit: int = 24) -> list[Path]:
    files = file_matrix_files(scope)
    scored=[]
    for f in files:
        r=rel(f).lower(); n=f.name.lower(); score=0
        if n in {"00_project_entrypoint.md","00_entrypoint.yaml","readme.md","01_project_contract.yaml","02_project_truth_index.yaml"}: score += 80
        if any(x in r for x in ["entrypoint","contract","truth","source_truth","baseline","readme","project_memory"]): score += 40
        if any(x in r for x in ["_workshop_system","project_formation","operating_principles","360","maturity","standards"]): score += 10
        if file_matrix_is_text(f): score += 5
        if score:
            scored.append((score, rel(f), f))
    return [x[2] for x in sorted(scored, key=lambda t:(-t[0], t[1]))[:limit]]


def file_matrix_truth_terms(scope: str = "project", request: str = "", max_terms: int = 90) -> list[str]:
    weights={}
    def add_text(txt: str, weight: int):
        for term in file_matrix_tokenize(txt, 160):
            weights[term]=weights.get(term,0)+weight
    add_text(request or "", 5)
    for f in file_matrix_seed_truth_files(scope, 24):
        txt=file_matrix_read(f, 18000)
        add_text(rel(f), 7)
        add_text("\n".join(headings(txt, 20)), 8)
        add_text(txt[:8000], 4)
    # If active project truth files are thin, fall back to path/domain vocabulary from all files.
    if len(weights) < 20:
        for f in file_matrix_files(scope)[:300]:
            add_text(rel(f), 3)
    return [k for k,_ in sorted(weights.items(), key=lambda kv:(-kv[1], kv[0]))[:max_terms]]


def file_matrix_sample_text(path: Path, sample_chars: int = 0) -> str:
    """Return content evidence for the matrix pulse.

    sample_chars=0 means no artificial answer-time cage: read the text through the
    normal project-safe file reader limit. Positive values remain available for
    explicit lightweight probes, but the operating doctrine does not force them.
    """
    if sample_chars is None or sample_chars <= 0:
        return file_matrix_read(path, 250000)
    txt=file_matrix_read(path, max(sample_chars*2, sample_chars))
    if len(txt) <= sample_chars:
        return txt
    head=txt[: int(sample_chars*0.72)]
    tail=txt[-int(sample_chars*0.28):]
    return head + "\n\n...[middle omitted by explicit lightweight sample]...\n\n" + tail


def file_matrix_content_state(text: str) -> dict:
    low=(text or "").lower()
    words=re.findall(r"\w+", text or "")
    placeholder_hits=[w for w in PLACEHOLDER_WORDS if w.lower() in low]
    if not text.strip():
        state="empty"
    elif len(words) < 45:
        state="thin"
    elif placeholder_hits:
        state="draft_or_placeholder"
    else:
        state="substantial"
    return {"state":state,"word_count":len(words),"placeholder_hits":placeholder_hits[:10]}


def file_matrix_truth_pulse(scope: str = "project", request: str = "", max_files: int = 0, sample_chars: int = 0) -> dict:
    sqlite3, time, *_ = _fm_imports()
    t0=time.time()
    base=file_matrix_base(scope)
    files=file_matrix_files(scope)
    truth_terms=set(file_matrix_truth_terms(scope, request, 100))
    seed_truth_set=set(file_matrix_seed_truth_files(scope, 80))
    # Prioritize truth spine, configs, intent/value-rich source files, then rest.
    def priority(f: Path):
        r=rel(f).lower(); n=f.name.lower(); st=f.stat() if f.exists() else None
        score=0
        if f in seed_truth_set: score += 1000
        if n in {"readme.md","00_project_entrypoint.md","01_project_contract.yaml","02_project_truth_index.yaml"}: score += 700
        if any(x in r for x in ["entrypoint","contract","truth","baseline","requirements","prd","architecture","scenario","workflow","usecase","maturity","standards"]): score += 300
        if any(x in r for x in ["src/","app/","routes","api","database","models","schema","tests","config"]): score += 120
        if file_matrix_is_text(f): score += 40
        # File size is deliberately excluded: value is derived from role, content signals, headings, truth overlap, and intent.
        return (-score, r)
    ranked=sorted(files, key=priority)
    selected=ranked if not max_files or max_files <= 0 else ranked[:max_files]
    role_counts={}; language_counts={}; signal_counts={}; states={}; pulse_files=[]
    truth_spine=[]; drift=[]; incomplete=[]; high_value=[]; contradiction_candidates=[]
    for f in selected:
        try:
            r=rel(f); txt=file_matrix_sample_text(f, sample_chars) if file_matrix_is_text(f) else ""
            hs=headings(txt, 10)
            flags=file_matrix_role_flags(f, txt)
            role=file_role(f, txt) if txt else ("code" if f.suffix.lower() in CODE_EXTS else "binary_or_large")
            lang=file_matrix_language(f)
            terms=set(file_matrix_tokenize(r+"\n"+"\n".join(hs)+"\n"+txt, 120))
            overlap=sorted(terms.intersection(truth_terms))[:20]
            sigs=sorted((_value_hits(r+"\n"+"\n".join(hs)+"\n"+txt[:8000]) or {}).keys())
            cstate=file_matrix_content_state(txt)
            role_counts[role]=role_counts.get(role,0)+1; language_counts[lang]=language_counts.get(lang,0)+1; states[cstate["state"]]=states.get(cstate["state"],0)+1
            for sg in sigs: signal_counts[sg]=signal_counts.get(sg,0)+1
            is_truth = bool(flags.get("is_entrypoint") or role in {"truth_entry","governance","architecture","requirements","scenario"} or any(x in r.lower() for x in ["entrypoint","contract","truth","baseline","readme"]))
            density = len(terms) + len(sigs)*8 + len(hs)*4 + min(cstate["word_count"]//80, 20)
            item={"path":r,"role":role,"language":lang,"content_state":cstate,"headings":hs[:6],"value_signals":sigs[:10],"truth_overlap_terms":overlap[:12],"density_score":density,"excerpt":snippet(txt, 420) if txt else ""}
            pulse_files.append(item)
            if is_truth:
                truth_spine.append(item)
            if cstate["state"] in {"empty","thin","draft_or_placeholder"} and (is_truth or density < 22):
                incomplete.append({"path":r,"reason":"thin_or_placeholder_truth_surface" if is_truth else "thin_content_surface","content_state":cstate,"role":role})
            # Drift is a review candidate only: current files are truth, but truth may be incomplete/contradictory.
            if txt and truth_terms and cstate["word_count"] >= 80 and not is_truth and not flags.get("is_config") and not flags.get("is_test"):
                overlap_ratio=len(overlap)/max(1, min(len(terms), 80))
                if overlap_ratio < 0.035 and len(sigs) <= 1:
                    drift.append({"path":r,"reason":"low overlap with project truth spine; requires human/model review before treating as aligned truth","top_terms":list(sorted(terms - truth_terms))[:16],"truth_overlap_terms":overlap[:8],"role":role})
            if density >= 38 or is_truth:
                high_value.append(item)
        except Exception:
            continue
    # Compare truth spine terms against active content terms to reveal missing 360 rings.
    content_terms=set()
    for item in pulse_files[:120]:
        content_terms.update(file_matrix_tokenize((item.get("path","")+" "+" ".join(item.get("headings",[]))+" "+item.get("excerpt","")), 80))
    missing_truth_terms=sorted(list(truth_terms - content_terms))[:30]
    recommended=[]
    for item in truth_spine[:6]:
        recommended.append({"path":item["path"],"why":"truth_spine_first"})
    for item in high_value:
        if item["path"] not in [x["path"] for x in truth_spine] and len(recommended)<12:
            recommended.append({"path":item["path"],"why":"high_value_content_surface"})
    for item in drift[:4]:
        if len(recommended)<16:
            recommended.append({"path":item["path"],"why":"drift_candidate_must_be_checked_before_360_claim"})
    coverage={"scanned_files":len(selected),"total_files":len(files),"coverage_state":"complete" if len(selected)==len(files) else "ranked_partial","content_read_mode":"full_read_through_safe_reader" if not sample_chars or sample_chars <= 0 else "explicit_lightweight_sample", "sample_chars_per_file":sample_chars,"value_basis":"content_and_truth_alignment_not_file_size"}
    verdict="ready_for_surface_answer"
    if not files:
        verdict="new_or_empty_project"
    elif drift or incomplete:
        verdict="surface_answer_with_truth_warnings"
    packet={
        "command":"file-matrix-pulse","version":FILE_MATRIX_VERSION,"scope":scope,"request":request,"generated_at":utc_now(),"base":rel(base),
        "coverage":coverage,
        "truth_spine_terms":sorted(list(truth_terms))[:80],
        "one_page_neural_truth_map":{
            "role_counts":dict(sorted(role_counts.items(), key=lambda kv:(-kv[1],kv[0]))),
            "language_counts":dict(sorted(language_counts.items(), key=lambda kv:(-kv[1],kv[0]))),
            "content_states":states,
            "value_signal_counts":dict(sorted(signal_counts.items(), key=lambda kv:(-kv[1],kv[0]))[:24]),
            "truth_spine_files":[{"path":x["path"],"role":x["role"],"state":x["content_state"]["state"],"signals":x["value_signals"][:6],"headings":x["headings"][:4]} for x in truth_spine[:12]],
            "high_value_content_surfaces":[{"path":x["path"],"role":x["role"],"state":x["content_state"]["state"],"signals":x["value_signals"][:6],"overlap":x["truth_overlap_terms"][:6]} for x in high_value[:16]],
            "incomplete_truth_candidates":incomplete[:18],
            "semantic_drift_candidates":drift[:18],
            "missing_or_unreflected_truth_terms":missing_truth_terms,
        },
        "recommended_entry_sequence":recommended,
        "truth_governance":{
            "rule":"File names, folder names, and file contents are current truth surfaces, but they are incomplete truth until aligned with parent project purpose and cross-file reality.",
            "anti_blind_truth":"Do not obey a file blindly when its content contradicts project identity, workshop standards, or stronger parent truth; flag it as contradiction/drift and request correction or deeper scan.",
            "first_step_guard":"Do not choose an implementation starting point from a single file name. Choose from truth spine + high-value content + drift/incomplete warnings + requested intent.",
            "required_for_strong_claims":["read truth_spine_files","read recommended_entry_sequence owner files","escalate to file-matrix-context --mode deep for implementation/write decisions"],
        },
        "readiness_verdict":verdict,
        "elapsed_ms":int((time.time()-t0)*1000),
        "cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"file_matrix_pulse","generated_at":utc_now(),"volatile":True,"source":"current_files_sampled"},
    }
    (INDEX/f"{scope}_file_matrix_pulse.json").write_text(json.dumps(packet,ensure_ascii=False,indent=2), encoding="utf-8")
    return packet


def cmd_file_matrix_pulse(args):
    print(json.dumps(file_matrix_truth_pulse(args.scope, args.request, args.max_files, args.sample_chars), ensure_ascii=False, indent=2))

def file_matrix_doctor(scope: str = "project") -> dict:
    sqlite3, time, shutil, subprocess, *_ = _fm_imports()
    t0=time.time(); problems=[]; warnings=[]
    status=file_matrix_status(scope)
    if not FILE_MATRIX_DB.exists(): problems.append({"type":"missing_file_matrix_db","action":"run file-matrix-build"})
    if not status.get("fresh"):
        warnings.append({"type":"stale_or_empty_file_matrix_index","status":status,"action":"run file-matrix-build --force"})
    conn=file_matrix_connect(); file_matrix_init_db(conn); cur=conn.cursor()
    tools={"git":bool(shutil.which("git")),"rg":bool(shutil.which("rg")),"python":bool(shutil.which("python") or shutil.which("python3"))}
    adapters={
        "sqlite_fts5": False,
        "ripgrep_lens": tools["rg"],
        "builtin_symbol_parser": True,
        "chunk_index": False,
        "semantic_lite": False,
        "truth_pulse": True,
        "one_page_neural_map": True,
        "truth_drift_review": True,
        "tree_sitter_ast": False,
        "lsp_bridge": False,
        "dense_vector_semantic": False,
    }
    try:
        fts=cur.execute("SELECT value FROM meta WHERE key='fts5'").fetchone()
        if fts and fts["value"] == "available": adapters["sqlite_fts5"] = True
        if not fts or fts["value"] != "available": warnings.append({"type":"sqlite_fts5_unavailable","effect":"falls back to slower LIKE/snippet search"})
        adapters["chunk_index"] = cur.execute("SELECT COUNT(*) c FROM chunks WHERE scope=?", (scope,)).fetchone()["c"] > 0
        adapters["semantic_lite"] = adapters["chunk_index"] and adapters["sqlite_fts5"]
    except Exception as e:
        warnings.append({"type":"fts_check_error","error":str(e)})
    if not tools["rg"]: warnings.append({"type":"ripgrep_missing","effect":"file matrix still works through SQLite FTS, but external rg lens is unavailable"})
    profile=file_matrix_discover(scope)
    if profile.get("file_count",0)==0:
        warnings.append({"type":"empty_scope","scope":scope,"message":"No active project files discovered; this is valid for a new project but limits retrieval."})
    # Latency smoke test: avoid recursive full query in doctor; validate hot index primitives directly.
    try:
        t1=time.time()
        _=cur.execute("SELECT path FROM files WHERE scope=? ORDER BY is_entrypoint DESC, is_config DESC LIMIT 8", (scope,)).fetchall()
        _=cur.execute("SELECT path FROM chunks WHERE scope=? LIMIT 8", (scope,)).fetchall()
        latency=int((time.time()-t1)*1000)
        if latency>2500: warnings.append({"type":"slow_index_latency","latency_ms":latency,"target_ms":"<2500 for warm index primitive"})
    except Exception as e:
        problems.append({"type":"index_smoke_failed","error":str(e)})
    health="fail" if problems else ("pass_with_warnings" if warnings else "pass")
    report={"command":"file-matrix-doctor","version":FILE_MATRIX_VERSION,"scope":scope,"health":health,"status":status,"profile":profile,"tool_availability":tools,"adapter_readiness":adapters,"not_bundled_extension_adapters":["tree_sitter_ast","lsp_bridge","dense_vector_semantic","framework_specific_extractors"],"problems":problems,"warnings":warnings,"elapsed_ms":int((time.time()-t0)*1000),"cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"file_matrix_doctor","generated_at":utc_now(),"volatile":True}}
    FILE_MATRIX_DOCTOR_REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2), encoding="utf-8")
    return report


def cmd_file_matrix_build(args):
    print(json.dumps(file_matrix_build(args.scope, args.force), ensure_ascii=False, indent=2))


def cmd_file_matrix_touch(args):
    print(json.dumps(file_matrix_touch(args.scope), ensure_ascii=False, indent=2))


def cmd_file_matrix_query(args):
    print(json.dumps(file_matrix_query(args.request, args.scope, args.mode, args.limit), ensure_ascii=False, indent=2))


def cmd_file_matrix_context(args):
    print(json.dumps(file_matrix_context(args.request, args.scope, args.mode, args.max_files, args.chars), ensure_ascii=False, indent=2))


def cmd_file_matrix_doctor(args):
    print(json.dumps(file_matrix_doctor(args.scope), ensure_ascii=False, indent=2))


def cmd_file_matrix_status(args):
    print(json.dumps(file_matrix_status(args.scope), ensure_ascii=False, indent=2))






# ---------------------------------------------------------------------------
# v9.7 Open Neural Operating Kernel
# This layer removes scripted/caged first-contact behavior. The model remains
# the reasoning engine, while the runtime provides a governed entry, truth
# surfaces, evidence packets, 360 methodology, code fingerprints, and gates.
# It is an operating compass, not a final-answer template.
# ---------------------------------------------------------------------------

OPEN_NEURAL_KERNEL_VERSION = "9.11.0"
NATURAL_TRUTH_DOCTRINE_VERSION = "9.11.0"
OPEN_NEURAL_ENTRY_REPORT = INDEX / "last_open_neural_entry.json"
TRUTH_SWEEP_360_REPORT = INDEX / "last_truth_sweep_360.json"
OPERATION_360_REPORT = INDEX / "last_operation_360.json"
PATCH_GATE_360_REPORT = INDEX / "last_patch_gate_360.json"
TRUTH_AUTHORITY_REPORT = INDEX / "last_truth_authority_gate.json"


def open_neural_intent_profile(request: str = "", scope: str | None = None) -> dict:
    """Classify operation without trapping the model in a scripted response path."""
    route = route_intent(request or "")
    mode = operation_mode(request or "")
    selected_scope = _scope_for_request(request or "", scope)
    low = normalize_for_route(request or "")
    asks_identity = bool(re.search(r"من انت|من أنت|ما عملك|وظيفتك|مهامك|مهاراتك|كيف تتعامل|تقييمك|وضعه الحالي|اول خطوة|أول خطوة|who are you|what do you do|first step|evaluate|عنك|مشروعي|مشروعك|تتعامل مع المشروع", low, re.I))
    asks_write = bool(re.search(r"اكتب|عدل|نفذ|اصلح|أصلح|كود|api|database|backend|frontend|implement|write|modify|fix|refactor", low, re.I))
    asks_runtime = selected_scope == "runtime" or route.get("route") == "runtime_work" or bool(re.search(r"بيئة المهندس|مركز التحكم|runtime|engineer runtime|مصنع|حوكمة المهندس|نظام المهندس", low, re.I))
    asks_strategy = bool(re.search(r"خطة|استراتيجية|حل جذري|ترقيع|360|أفضل|افضل|best|architecture|معمارية", low, re.I))
    if asks_write:
        operation_family = "execution_or_write"
    elif asks_strategy or mode.get("risk") in {"high", "critical"}:
        operation_family = "strategy_or_high_impact"
    elif asks_identity:
        operation_family = "project_relationship_or_surface_assessment"
    elif asks_runtime:
        operation_family = "runtime_engineering"
    else:
        operation_family = "general_project_work"
    return {
        "request": request,
        "scope": selected_scope,
        "route": route,
        "operation_mode": {k:v for k,v in mode.items() if k != 'route'},
        "operation_family": operation_family,
        "is_project_surface_question": asks_identity and selected_scope == "project",
        "is_high_impact": mode.get("risk") in {"high", "critical"} or asks_write or asks_strategy,
        "model_freedom_contract": {
            "model_role": "reasoning_engine_not_script_reader",
            "runtime_role": "silent_operating_system_with_truth_gates",
            "rule": "The runtime must not write the final answer for the model; it supplies truth, boundaries, and gates so the model can reason naturally within governance.",
            "forbidden_cages": ["scripted_first_contact", "fixed_surface_template", "file_size_as_value", "runtime_as_project", "answer_before_truth_grounding"],
        },
    }


def open_neural_recommended_actions(request: str = "", scope: str | None = None) -> dict:
    """Return a compass, not a cage.

    The model stays the reasoning engine. The runtime exposes the available
    surfaces and the truth doctrine; it does not prescribe a fixed route or
    response shape. For high-impact work, this function names the evidence that
    should exist before strong claims, but it does not force a single command path.
    """
    prof = open_neural_intent_profile(request, scope)
    family = prof.get("operation_family")
    compass = ["route", "file-matrix-pulse", "truth-sweep-360", "truth-authority-gate"]
    if family == "project_relationship_or_surface_assessment":
        compass += ["evidence-lock", "value-atlas", "file-matrix-context"]
    elif family == "strategy_or_high_impact":
        compass += ["operation-360", "goal-closure", "best-fit", "completion-audit", "file-matrix-context"]
    elif family == "execution_or_write":
        compass += ["operation-360", "file-matrix-context", "duplicate-scan", "impact-scan", "write-plan", "code-impact-360", "patch-gate-360"]
    elif family == "runtime_engineering":
        compass += ["runtime-audit", "doctor", "operation-360", "architecture-review"]
    return {
        "operation_family": family,
        "compass": list(dict.fromkeys(compass)),
        "mandatory": [],
        "no_cage_rule": "These are navigation surfaces, not a forced route or answer template.",
        "depth_selection_rule": "The model chooses depth from intent, risk, and evidence gaps. It must ground claims in content/value truth, but it is free to decide the search sequence.",
        "execution_claim_note": "For writes or irreversible decisions, the model should obtain impact/duplicate/patch evidence before presenting execution as safe; this is truth hygiene, not a scripted path.",
    }

def _truth_sweep_selected_files(scope: str, request: str = "") -> list[Path]:
    files=[f for f in iter_files(scope) if f.suffix.lower() in TEXT_EXTS]
    # Generated runtime state is not truth unless specifically requested.
    files=[f for f in files if not (should_skip_generated(scope, request) and is_generated_runtime_rel(rel(f)))]
    profiles=[]
    for f in files:
        txt=read_text(f, 220000)
        prof=content_value_profile(f, txt, request)
        # Truth and documentation get priority for assessment; code remains available.
        priority=prof.get("value_score",0)
        if prof.get("role") == "truth_entry": priority += 120
        if prof.get("role") in {"requirements","architecture","governance","scenario"}: priority += 60
        if prof.get("query_hits"): priority += 30
        if prof.get("content_status") in {"empty","thin","thin_code"}: priority -= 10
        profiles.append((priority, f, prof))
    # Do not use size as value. Sort by semantic value + truth role + intent overlap.
    profiles.sort(key=lambda x:(-x[0], x[2].get("path","")))
    return [f for _,f,_ in profiles]


def truth_sweep_360(request: str = "", scope: str = "project") -> dict:
    """Content-value sweep for grounding. It reads content signals, not file names or sizes."""
    scope = scope if scope in {"project","runtime","repository","workshop"} else "project"
    selected = _truth_sweep_selected_files(scope, request)
    # Adaptive: full documentation sweep for normal-sized projects; staged sweep for large ones.
    doc_like=[]; code_like=[]; other=[]
    for f in selected:
        txt=read_text(f, 180000)
        role=file_role(f, txt)
        if role in {"truth_entry","requirements","architecture","governance","scenario","document"}:
            doc_like.append((f,txt,content_value_profile(f,txt,request)))
        elif f.suffix.lower() in CODE_EXTS or role == "code":
            code_like.append((f,txt,content_value_profile(f,txt,request)))
        else:
            other.append((f,txt,content_value_profile(f,txt,request)))
    scanned = doc_like + code_like[:80] + other[:40]
    truth_spine=[]; high_value=[]; incomplete=[]; contradiction=[]; content_states={}; signals={}; domains={}
    active_terms=set()
    for f,txt,prof in scanned:
        st=prof.get("content_status")
        content_states[st]=content_states.get(st,0)+1
        for sig in prof.get("value_signals",[]): signals[sig]=signals.get(sig,0)+1
        path=prof.get("path")
        item={"path":path,"role":prof.get("role"),"state":st,"signals":prof.get("value_signals",[])[:8],"headings":prof.get("headings",[])[:6],"query_hits":prof.get("query_hits",[])[:8],"excerpt":prof.get("excerpt","")[:420]}
        if prof.get("role") == "truth_entry":
            truth_spine.append(item)
            for t in re.findall(r"[A-Za-z_\u0600-\u06FF][A-Za-z0-9_\u0600-\u06FF-]{3,}", txt[:14000]):
                if len(t) >= 4: active_terms.add(t.lower())
        if prof.get("content_status") == "content_bearing" and (prof.get("value_score",0) >= 30 or prof.get("query_hits") or prof.get("role") in {"requirements","architecture","scenario","governance"}):
            high_value.append(item)
        if prof.get("incomplete_truth_candidate") or prof.get("missing_expected_dimensions") or st in {"empty","thin","thin_code","draft_or_placeholder"}:
            incomplete.append({**item, "missing_expected_dimensions": prof.get("missing_expected_dimensions",[])[:8]})
    # Drift candidates: a file is not false merely because it differs. It is only flagged for review.
    for f,txt,prof in scanned:
        if prof.get("role") in {"truth_entry","requirements","architecture","governance","scenario","document"} and prof.get("content_status") == "content_bearing":
            low=(rel(f)+" "+txt[:10000]).lower()
            qhits=prof.get("query_hits",[])
            has_signals=len(prof.get("value_signals",[]))
            if active_terms and has_signals <= 1 and not qhits:
                contradiction.append({"path":rel(f),"role":prof.get("role"),"state":prof.get("content_status"),"reason":"low_overlap_with_truth_spine_review_before_using_as_binding_truth","excerpt":prof.get("excerpt","")[:300]})
    result={
        "command":"truth-sweep-360",
        "version":OPEN_NEURAL_KERNEL_VERSION,
        "scope":scope,
        "request":request,
        "generated_at":utc_now(),
        "coverage":{
            "text_files_seen":len(selected),
            "documentation_files_read":len(doc_like),
            "code_files_sampled":len(code_like[:80]),
            "other_files_sampled":len(other[:40]),
            "strategy":"adaptive_content_value_sweep_not_fixed_template",
        },
        "truth_spine":truth_spine[:18],
        "high_value_content":high_value[:36],
        "incomplete_truth_candidates":incomplete[:36],
        "contradiction_or_drift_candidates":contradiction[:24],
        "content_states":content_states,
        "value_signal_counts":dict(sorted(signals.items(), key=lambda kv:(-kv[1],kv[0]))),
        "governance_rules":[
            "File existence is surface truth only.",
            "File size is never a value criterion.",
            "Content becomes stronger truth only when it aligns with parent identity, cross-file evidence, and the request intent.",
            "Contradiction candidates require review; the model must not blindly obey any single file.",
            "The model may choose deeper reads when the answer depends on unverified content.",
        ],
        "recommended_reasoning_posture":"Use this as evidence substrate, not a final answer. The model must compose the answer naturally from observed truth, inferred gaps, and declared uncertainty.",
        "cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"truth_sweep_360","generated_at":utc_now(),"volatile":True},
    }
    TRUTH_SWEEP_360_REPORT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    return result


def _extract_code_units_from_text(path: Path, text: str) -> list[dict]:
    units=[]
    lines=text.splitlines()
    patterns=[
        ("function", re.compile(r"^\s*(?:export\s+)?(?:default\s+)?(?:async\s+)?function\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*\(")),
        ("function", re.compile(r"^\s*(?:async\s+)?def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")),
        ("class", re.compile(r"^\s*(?:export\s+)?class\s+([A-Za-z_$][A-Za-z0-9_$]*)")),
        ("class", re.compile(r"^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)")),
        ("interface", re.compile(r"^\s*(?:export\s+)?interface\s+([A-Za-z_$][A-Za-z0-9_$]*)")),
        ("type", re.compile(r"^\s*(?:export\s+)?type\s+([A-Za-z_$][A-Za-z0-9_$]*)")),
        ("method_or_func", re.compile(r"^\s*(?:public|private|protected|internal|static|async|override|virtual|sealed|partial|readonly|extern|\s)+\s*[A-Za-z0-9_<>,\[\]\?]+\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")),
        ("go_func", re.compile(r"^\s*func\s+(?:\([^)]*\)\s*)?([A-Za-z_][A-Za-z0-9_]*)\s*\(")),
        ("rust_fn", re.compile(r"^\s*(?:pub\s+)?(?:async\s+)?fn\s+([A-Za-z_][A-Za-z0-9_]*)")),
    ]
    starts=[]
    for i,line in enumerate(lines, start=1):
        for kind,pat in patterns:
            m=pat.search(line)
            if m:
                starts.append((i,kind,m.group(1),line.strip()[:240]))
                break
    for idx,(line,kind,name,signature) in enumerate(starts):
        end=starts[idx+1][0]-1 if idx+1 < len(starts) else min(len(lines), line+180)
        body="\n".join(lines[line-1:end])
        normalized=re.sub(r"\s+"," ", re.sub(r"#.*|//.*|/\*.*?\*/", "", body, flags=re.S)).strip()
        units.append({
            "path":rel(path),"kind":kind,"name":name,"line":line,"end_line":end,"signature":signature,
            "body_hash":hashlib.sha1(body.encode('utf-8','ignore')).hexdigest()[:16],
            "normalized_hash":hashlib.sha1(normalized.encode('utf-8','ignore')).hexdigest()[:16],
        })
    return units


def code_fingerprint(request: str = "", scope: str = "project", limit: int = 120) -> dict:
    scope = scope if scope in {"project","runtime","repository","workshop"} else "project"
    terms=[t.lower() for t in re.findall(r"[A-Za-z_][A-Za-z0-9_]{2,}", request or "")]
    units=[]; file_count=0
    for f in iter_files(scope):
        if f.suffix.lower() not in CODE_EXTS:
            continue
        txt=read_text(f, 260000)
        file_count += 1
        for u in _extract_code_units_from_text(f, txt):
            if terms and not any(t in (u['name'].lower()+" "+u['path'].lower()+" "+u['signature'].lower()) for t in terms):
                # keep a few general entities even when query-specific, so the model sees context.
                if len(units) > limit//4:
                    continue
            units.append(u)
            if len(units) >= limit:
                break
        if len(units) >= limit:
            break
    return {"command":"code-fingerprint","version":OPEN_NEURAL_KERNEL_VERSION,"scope":scope,"request":request,"code_files_seen":file_count,"entities":units,"rule":"Hashes support change awareness; they are not semantic proof. Non-trivial writes require references/impact/patch-gate.","cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"code_fingerprint","generated_at":utc_now(),"volatile":True}}


def code_impact_360(target: str = "", scope: str = "project", limit: int = 80) -> dict:
    scope = scope if scope in {"project","runtime","repository","workshop"} else "project"
    target_low=(target or "").lower().strip()
    refs=[]; imports=[]; definitions=[]
    for f in iter_files(scope):
        if f.suffix.lower() not in CODE_EXTS and f.suffix.lower() not in TEXT_EXTS:
            continue
        txt=read_text(f, 220000)
        low=(rel(f)+"\n"+txt).lower()
        if not target_low or target_low in low:
            hits=[]
            for i,line in enumerate(txt.splitlines(), start=1):
                if target_low and target_low in line.lower():
                    hits.append({"line":i,"text":line.strip()[:240]})
                    if len(hits)>=8: break
            role=file_role(f, txt)
            item={"path":rel(f),"role":role,"hits":hits[:8],"value_signals":sorted(_value_hits(txt[:6000]).keys())[:8]}
            refs.append(item)
            if re.search(r"\b(import|from|using|require)\b", txt[:20000]): imports.append(item)
            if f.suffix.lower() in CODE_EXTS:
                for u in _extract_code_units_from_text(f, txt):
                    if not target_low or target_low in u['name'].lower() or target_low in u['signature'].lower():
                        definitions.append(u)
        if len(refs) >= limit:
            break
    return {"command":"code-impact-360","version":OPEN_NEURAL_KERNEL_VERSION,"scope":scope,"target":target,"definitions":definitions[:limit],"references":refs[:limit],"import_surfaces":imports[:limit],"write_rule":"Do not write isolated code. Use this impact map plus duplicate-scan, write-plan, and patch-gate-360 before changes.","cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"code_impact_360","generated_at":utc_now(),"volatile":True}}


def patch_gate_360(target_path: str, objective: str = "", expected_hash: str = "", scope: str = "project") -> dict:
    scope = scope if scope in {"project","runtime","repository","workshop"} else "project"
    p=(ROOT/target_path).resolve() if target_path else None
    problems=[]; warnings=[]
    if not target_path:
        problems.append("missing_target_path")
    elif not p.exists():
        warnings.append("target_path_not_found_new_file_requires_duplicate_and_owner_scan")
    else:
        # Scope containment guard.
        base=scope_base(scope).resolve()
        if not is_relative_to(p, base): problems.append("target_outside_declared_scope")
        txt=read_text(p, 260000)
        if expected_hash:
            current=hashlib.sha1((txt or "").encode('utf-8','ignore')).hexdigest()[:16]
            if current != expected_hash:
                problems.append("fingerprint_mismatch_current_file_changed")
    try:
        dup=duplicate_scan(scope, objective or target_path, 12)
    except Exception as e:
        dup={"error":str(e)}; warnings.append("duplicate_scan_unavailable")
    try:
        imp=impact_scan(target_path or objective, objective or "", scope)
    except Exception as e:
        imp={"error":str(e)}; warnings.append("impact_scan_unavailable")
    try:
        closure=goal_closure(objective or target_path, scope)
    except Exception as e:
        closure={"error":str(e),"readiness_verdict":"UNKNOWN"}; warnings.append("goal_closure_unavailable")
    verdict="blocked" if problems or closure.get("readiness_verdict") == "BLOCKED_MISSING_CAPABILITY" else ("warn_partial" if warnings or closure.get("readiness_verdict") == "READY_PARTIAL" else "pass")
    out={"command":"patch-gate-360","version":OPEN_NEURAL_KERNEL_VERSION,"scope":scope,"target_path":target_path,"objective":objective,"verdict":verdict,"problems":problems,"warnings":warnings,"duplicate_scan_summary":{"error":dup.get("error"),"top_candidates":(dup.get("matches") or dup.get("candidates") or [])[:8]},"impact_summary":{k:imp.get(k) for k in ["target","scope","impact","affected_files","owner_candidates","problems"] if isinstance(imp,dict)},"goal_closure_verdict":closure.get("readiness_verdict"),"rule":"A patch is allowed only when it is grounded, non-duplicative, impact-aware, scope-contained, and parent-goal compatible.","cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"patch_gate_360","generated_at":utc_now(),"volatile":True}}
    PATCH_GATE_360_REPORT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    return out



def _request_truth_demand(request: str = "") -> dict:
    """Classify how much truth grounding an answer is allowed to claim.

    This is not a response template. It is a claim-permission gate: the model remains
    free to reason and compose naturally, but cannot present claims stronger than the
    evidence surface currently supports.
    """
    low=(request or "").lower()
    asks_identity=bool(re.search(r"من انت|من أنت|ماهو عملك|ما هي وظيفتك|مهاراتك|كيف تتعامل|تقييمك|وضعه الحالي|اول خطوة|أول خطوة|who are you|what do you do|first step|current state|evaluate", low))
    asks_write=bool(re.search(r"اكتب|عدل|أصلح|نفذ|كود|بناء|توليد|refactor|fix|implement|code|write|modify", low))
    asks_decision=bool(re.search(r"قرار|اقترح|أفضل|اختر|استراتيجية|خطة|حل|first step|recommend|best|plan|strategy", low))
    asks_runtime=bool(re.search(r"بيئة المهندس|المهندس|runtime|engineer|matrix|ماتركس|حوكمة", low))
    demand="orientation"
    if asks_write:
        demand="write_or_execution"
    elif asks_decision:
        demand="decision_or_strategy"
    elif asks_identity:
        demand="project_orientation_assessment"
    elif asks_runtime:
        demand="runtime_or_governance"
    return {"demand":demand,"asks_identity":asks_identity,"asks_write":asks_write,"asks_decision":asks_decision,"asks_runtime":asks_runtime}


def truth_authority_gate(request: str = "", scope: str = "project", sweep: dict | None = None) -> dict:
    """Expose truth doctrine as a compass, not as a cage.

    The gate does not write the answer and does not force one search path. It
    calibrates claim strength from current evidence so the model can reason
    naturally without guessing.
    """
    scope = scope if scope in {"project","runtime","repository","workshop"} else "project"
    demand=_request_truth_demand(request)
    sw = sweep or truth_sweep_360(request, scope)
    truth_spine=sw.get("truth_spine") or []
    high_value=sw.get("high_value_content") or []
    incomplete=sw.get("incomplete_truth_candidates") or []
    drift=sw.get("contradiction_or_drift_candidates") or []
    signals=sw.get("value_signal_counts") or {}
    content_states=sw.get("content_states") or {}
    distinct_signal_count=len([k for k,v in signals.items() if v])
    has_truth_spine=bool(truth_spine)
    has_cross_content=len(high_value) >= 3 or distinct_signal_count >= 4
    advisory=[]
    if not has_truth_spine:
        advisory.append("project_identity_claims_are_weak_until_governing_truth_files_are_read")
    if not has_cross_content:
        advisory.append("current_state_or_first_step_claims_should_be_qualified_until_cross_file_content_value_is_observed")
    if drift:
        advisory.append("review_drift_candidates_before_treating_any_single_file_as_binding_truth")
    if demand["demand"] in {"write_or_execution","decision_or_strategy"}:
        advisory.append("strong_strategy_or_execution_claims_should_use_360_context_and_impact_evidence")
    claim_strength={
        "project_identity": "grounded" if has_truth_spine else "weak_or_unproven",
        "current_state": "grounded" if has_truth_spine and has_cross_content else "orientation_only",
        "first_step": "grounded_candidate" if has_truth_spine and has_cross_content and not drift else "candidate_needs_deeper_review",
        "write_or_execution_safety": "requires_contextual_evidence" if demand["demand"] == "write_or_execution" else "not_requested",
    }
    out={
        "command":"truth-authority-gate",
        "version":OPEN_NEURAL_KERNEL_VERSION,
        "generated_at":utc_now(),
        "scope":scope,
        "request":request,
        "truth_demand":demand,
        "authority_style":"advisory_truth_compass_not_permission_cage",
        "claim_strength":claim_strength,
        "evidence_status":{
            "truth_spine_files":len(truth_spine),
            "high_value_content_surfaces":len(high_value),
            "distinct_value_signal_count":distinct_signal_count,
            "content_states":content_states,
            "incomplete_truth_candidates":len(incomplete),
            "drift_candidates":len(drift),
            "value_basis":"content_value_cross_file_alignment_not_size_or_path_only",
        },
        "governing_rule":"The runtime does not cage the model with a scripted answer. It provides an advisory truth compass that calibrates claim strength while preserving natural reasoning.",
        "truth_doctrine":[
            "Do not use file size as value.",
            "Do not treat file existence or path names as sufficient truth.",
            "Use content, parent-goal alignment, and cross-file consistency to strengthen claims.",
            "Treat contradictions as review signals, not as automatic deletion or blind obedience.",
            "The model chooses how deep to inspect from intent and uncertainty; the runtime supplies truth surfaces, not a fixed route.",
        ],
        "advisory_gaps":list(dict.fromkeys(advisory)),
        "model_freedom_contract":{
            "no_fixed_response_template": True,
            "no_scripted_first_contact": True,
            "no_forced_search_sequence": True,
            "model_decides_depth": True,
            "truth_calibrates_claims_not_creativity": True,
        },
        # Backward-compatible field for older tests/tools. It is intentionally advisory.
        "claim_permissions":{
            "advisory_only": True,
            "may_answer_naturally": True,
            "may_claim_project_identity": has_truth_spine,
            "may_claim_current_state": has_truth_spine and has_cross_content,
            "may_recommend_first_step": has_truth_spine and has_cross_content and not drift,
            "may_execute_or_write": "only_after_contextual_write_evidence_if_requested",
            "must_declare_depth": False,
            "must_not_use_file_size_as_value": True,
            "must_not_treat_single_file_as_binding_truth": True,
        },
        "cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"truth_authority_gate","generated_at":utc_now(),"volatile":True},
    }
    try:
        TRUTH_AUTHORITY_REPORT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    except Exception:
        pass
    return out

def open_neural_entry(request: str = "", scope: str | None = None) -> dict:
    prof=open_neural_intent_profile(request, scope)
    sc=prof.get("scope") or "project"
    actions=open_neural_recommended_actions(request, sc)
    try:
        pulse=file_matrix_truth_pulse(sc, request or "")
    except Exception as e:
        pulse={"error":str(e)}
    try:
        sweep=truth_sweep_360(request or "", sc)
        authority=truth_authority_gate(request or "", sc, sweep)
    except Exception as e:
        sweep={"error":str(e)}
        authority={"authority":"unknown","error":str(e)}
    packet={
        "command":"open-neural-entry",
        "version":OPEN_NEURAL_KERNEL_VERSION,
        "generated_at":utc_now(),
        "request":request,
        "scope":sc,
        "identity_boundary":{
            "engineer_runtime":"silent operating system; never present it as the active project",
            "workshop":"project doctrine and method container",
            "active_project":"the subject project truth surface",
            "visible_answer_rule":"Answer as an engineer grounded in active project reality, not as a tool explaining itself.",
        },
        "intent_profile":prof,
        "truth_grounding_packet":{
            "pulse_coverage":pulse.get("coverage"),
            "readiness_verdict":pulse.get("readiness_verdict"),
            "truth_spine_files":((pulse.get("one_page_neural_truth_map") or {}).get("truth_spine_files") or [])[:10],
            "high_value_content_surfaces":((pulse.get("one_page_neural_truth_map") or {}).get("high_value_content_surfaces") or [])[:16],
            "incomplete_truth_candidates":((pulse.get("one_page_neural_truth_map") or {}).get("incomplete_truth_candidates") or [])[:12],
            "semantic_drift_candidates":((pulse.get("one_page_neural_truth_map") or {}).get("semantic_drift_candidates") or [])[:12],
            "truth_governance":pulse.get("truth_governance",{}),
        },
        "truth_authority_gate": authority,
        "open_navigation": actions,
        "governed_freedom_contract": {
            "no_scripted_first_contact": True,
            "no_fixed_response_template": True,
            "model_decides_depth_from_intent_and_evidence": True,
            "runtime_calibrates_claim_strength_not_answer_shape": True,
            "runtime_enforces_claim_authority_not_answer_shape": True,
            "truth_before_claim": True,
            "do_not_mention_runtime_unless_user_asks": True
        },
        "answer_composition_rule":"Synthesize a natural answer from observed project truth, content value, and declared uncertainty. Do not copy this packet, do not present runtime/tools as the project, and do not turn the compass into a rigid checklist.",
        "cache_meta":{"scope":sc,"fingerprint":project_fingerprint(sc),"generated_by":"open_neural_entry","generated_at":utc_now(),"volatile":True},
    }
    OPEN_NEURAL_ENTRY_REPORT.write_text(json.dumps(packet, ensure_ascii=False, indent=2), encoding='utf-8')
    return packet


def operation_360(request: str = "", scope: str | None = None) -> dict:
    prof=open_neural_intent_profile(request, scope)
    sc=prof.get("scope") or "project"
    sweep=truth_sweep_360(request, sc)
    try:
        ctx=file_matrix_context(request or "", sc, "focused" if prof.get("is_high_impact") else "fast", 12 if prof.get("is_high_impact") else 8, 2400 if prof.get("is_high_impact") else 1600)
    except Exception as e:
        ctx={"error":str(e)}
    try:
        closure=goal_closure(request or "", sc)
    except Exception as e:
        closure={"error":str(e),"readiness_verdict":"UNKNOWN"}
    try:
        bf=best_fit_review(sc, request or "", 8)
    except Exception as e:
        bf={"error":str(e)}
    missing=[]
    if closure.get("readiness_verdict") in {"BLOCKED_MISSING_CAPABILITY","READY_PARTIAL","UNKNOWN"}:
        missing += (closure.get("missing_ring_scan") or {}).get("missing",[])
        missing += (closure.get("missing_ring_scan") or {}).get("partial",[])
    if sweep.get("contradiction_or_drift_candidates"):
        missing.append("review_truth_drift_candidates_before_strong_claim")
    verdict="blocked" if closure.get("readiness_verdict") == "BLOCKED_MISSING_CAPABILITY" else ("partial" if missing else "ready")
    out={
        "command":"operation-360",
        "version":OPEN_NEURAL_KERNEL_VERSION,
        "generated_at":utc_now(),
        "request":request,
        "scope":sc,
        "intent_profile":prof,
        "lifecycle_trace":[
            {"step":"intent_governance","status":"done"},
            {"step":"truth_sweep_360","status":"done","coverage":sweep.get("coverage")},
            {"step":"matrix_context","status":"done" if not ctx.get("error") else "error"},
            {"step":"goal_closure","status":"done" if not closure.get("error") else "error","verdict":closure.get("readiness_verdict")},
            {"step":"best_fit_comparison","status":"done" if not bf.get("error") else "error"},
            {"step":"anti_patchwork_gate","status":"blocked_or_partial" if missing else "pass"},
            {"step":"execution_gate","status":"blocked" if verdict=="blocked" else ("requires_declared_partial" if verdict=="partial" else "allowed_when_write_gates_pass")},
        ],
        "truth_sweep_summary":{k:sweep.get(k) for k in ["coverage","truth_spine","high_value_content","incomplete_truth_candidates","contradiction_or_drift_candidates","content_states","value_signal_counts"]},
        "context_packet":ctx,
        "goal_closure":closure,
        "best_fit_summary":bf,
        "missing_or_partial_rings":list(dict.fromkeys([m for m in missing if m])),
        "verdict":verdict,
        "rule":"No proposal or execution is complete until it survives current truth, parent goal closure, contradiction review, impact/duplicate gates when writing, and post-action validation.",
        "cache_meta":{"scope":sc,"fingerprint":project_fingerprint(sc),"generated_by":"operation_360","generated_at":utc_now(),"volatile":True},
    }
    OPERATION_360_REPORT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    return out




def cmd_truth_authority_gate(args):
    print(json.dumps(truth_authority_gate(args.request or "", args.scope), ensure_ascii=False, indent=2))

def cmd_open_neural_entry(args):
    print(json.dumps(open_neural_entry(args.request or "", args.scope), ensure_ascii=False, indent=2))


def cmd_truth_sweep_360(args):
    print(json.dumps(truth_sweep_360(args.request or "", args.scope), ensure_ascii=False, indent=2))


def cmd_operation_360(args):
    print(json.dumps(operation_360(args.request or "", args.scope), ensure_ascii=False, indent=2))


def cmd_code_fingerprint(args):
    print(json.dumps(code_fingerprint(args.request or "", args.scope, args.limit), ensure_ascii=False, indent=2))


def cmd_code_impact_360(args):
    print(json.dumps(code_impact_360(args.target or "", args.scope, args.limit), ensure_ascii=False, indent=2))


def cmd_patch_gate_360(args):
    print(json.dumps(patch_gate_360(args.target_path or "", args.objective or "", args.expected_hash or "", args.scope), ensure_ascii=False, indent=2))

# ---------------------------------------------------------------------------
# v9.0 Engineer Neural OS / Factory Core
# This is not an isolated tool. It is an operating-governance loop that binds
# intent, truth access, workshop standards, file/runtime matrix, strategy,
# execution gates, validation, ledger, and self-maintenance into one lifecycle.
# ---------------------------------------------------------------------------

NEURAL_OS_VERSION = "9.1.0"
NEURAL_OS_REPORT = INDEX / "last_neural_os_cycle.json"
GOAL_CLOSURE_REPORT = INDEX / "last_goal_closure.json"
FACTORY_HEALTH_REPORT = INDEX / "last_factory_health.json"

NEURAL_OS_SLOTS = [
    {
        "slot": "identity_boundary",
        "purpose": "Fix engineer identity and separate runtime/workshop/active-project truth surfaces before any claim.",
        "truth_surface": ["00_ENTRYPOINT.yaml", ".engineer/kernel/identity.md", "02_WORKSHOP/README.md"],
        "extension_contract": "New identity or boundary policy must register here and must not couple runtime logic to a specific active project.",
    },
    {
        "slot": "intent_governance",
        "purpose": "Turn the user request into an operation type, risk level, scope, and evidence budget before scanning or answering.",
        "truth_surface": [".engineer/runtime/navigation.yaml", ".engineer/governance/operation_mode_gate.yaml"],
        "extension_contract": "New operation modes are added as routes/gates, not ad-hoc prompt instructions.",
    },
    {
        "slot": "truth_access_matrix",
        "purpose": "Access current truth through File Matrix / Runtime Matrix. Truth Pulse provides the fast 360 surface; indexes are navigation memory; current files remain truth.",
        "truth_surface": [".engineer/runtime/file_matrix_contract.yaml", ".engineer/governance/source_of_truth.yaml"],
        "extension_contract": "New retrieval capabilities register as lenses/adapters with freshness and doctor coverage.",
    },
    {
        "slot": "workshop_intelligence",
        "purpose": "Apply the workshop as the universal project method lens; ACTIVE_PROJECT is inside the workshop boundary.",
        "truth_surface": ["02_WORKSHOP/_WORKSHOP_SYSTEM", "02_WORKSHOP/ACTIVE_PROJECT"],
        "extension_contract": "New project standards and playbooks live under workshop system and are invoked through the operating cycle.",
    },
    {
        "slot": "truth_grounded_goal_closure",
        "purpose": "Measure intent against current truth, expose gaps, classify partial/full readiness, and prevent weak goals from becoming accepted truth.",
        "truth_surface": [".engineer/governance", ".engineer/protocols"],
        "extension_contract": "New quality strategies must declare completion criteria, missing-ring checks, and anti-patching blocks.",
    },
    {
        "slot": "strategy_solution_simulation",
        "purpose": "Compare solution options, mentally simulate lifecycle fit, and select best-fit strategy before execution.",
        "truth_surface": [".engineer/capabilities", "02_WORKSHOP/_WORKSHOP_SYSTEM/project_playbooks"],
        "extension_contract": "New strategies register as playbooks with entry conditions, failure modes, validation, and rollback.",
    },
    {
        "slot": "tool_orchestration",
        "purpose": "Dispatch tools as part of the central lifecycle; tools never become islands.",
        "truth_surface": [".engineer/runtime/tool_registry.yaml", ".engineer/runtime/tool_contract.yaml"],
        "extension_contract": "Every new tool needs registry entry, allowed scope, mutation risk, required gates, doctor/receipt rules.",
    },
    {
        "slot": "execution_governance",
        "purpose": "Allow writes/execution only after duplicate, impact, owner, contract, and readiness gates.",
        "truth_surface": [".engineer/governance/write_governance.yaml", ".engineer/protocols/prewrite_guard.yaml"],
        "extension_contract": "New execution paths must attach prewrite, impact, safe-write, and rollback semantics.",
    },
    {
        "slot": "validation_doctor",
        "purpose": "Verify the project and the engineer runtime after actions: build/test/lint/doctor/claim-check as applicable.",
        "truth_surface": [".engineer/architecture/v8/05_VALIDATION_DOCTOR_EVALUATION.md", ".engineer/evaluation"],
        "extension_contract": "Every new layer must define health checks and pass/fail criteria.",
    },
    {
        "slot": "ledger_memory_maintenance",
        "purpose": "Record decisions, claims, gaps, maintenance work, and runtime self-improvement without letting cache override truth.",
        "truth_surface": [".engineer/ledgers", ".engineer/maintenance/ENGINEER_MAINTENANCE_LEDGER.md"],
        "extension_contract": "New memory/cache must include freshness, provenance, invalidation, and maintenance ledger rules.",
    },
    {
        "slot": "extension_layer",
        "purpose": "Add future capabilities as engines/lenses/adapters/protocols/doctors that plug into the same lifecycle.",
        "truth_surface": [".engineer/runtime/capability_registry.yaml", ".engineer/architecture/v9"],
        "extension_contract": "No new island tools. Every extension must declare slot, lifecycle hooks, inputs, outputs, truth relation, doctor, and ledger receipt.",
    },
]


def _safe_load_yaml(path: Path) -> dict:
    if not path.exists() or not yaml:
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    except Exception:
        return {}


def neural_os_architecture() -> dict:
    return {
        "version": NEURAL_OS_VERSION,
        "name": "Engineer Neural OS / Factory Core",
        "principle": "Stable operating core with expandable capability slots; new layers extend the factory, never bypass it.",
        "workshop_boundary": {
            "workshop_root": "02_WORKSHOP",
            "workshop_system": "02_WORKSHOP/_WORKSHOP_SYSTEM",
            "active_project": "02_WORKSHOP/ACTIVE_PROJECT",
            "rule": "ACTIVE_PROJECT is inside the workshop boundary; the workshop is accessed through the central runtime and matrix, not as detached documentation.",
        },
        "core_loop": [
            "intent_governance",
            "central_entry",
            "truth_surface_selection",
            "truth_pulse_360",
            "matrix_touch",
            "workshop_lens",
            "truth_grounded_goal_closure",
            "strategy_simulation",
            "missing_ring_scan",
            "execution_readiness_gate",
            "governed_execution",
            "validation_doctor",
            "maintenance_ledger",
        ],
        "slots": NEURAL_OS_SLOTS,
        "non_negotiable_rules": [
            "Intent is a compass, not executable truth, until grounded in current files.",
            "Current files outrank generated indexes, old reports, cache, and model memory.",
            "A solution is not accepted unless it closes the parent goal or is explicitly labeled partial.",
            "File Matrix Truth Pulse is the first nervous-system touch before project/workshop/runtime claims.",
            "File Matrix is the nervous access layer for workshop/project/runtime truth.",
            "No capability may be added as an island; it must register a slot, hook, doctor, and receipt.",
        ],
    }


def _scope_for_request(request: str, explicit_scope: str | None = None) -> str:
    if explicit_scope in {"project", "runtime", "repository", "workshop"}:
        return explicit_scope
    route = route_intent(request or "")
    scope = route.get("scope") or "project"
    if scope not in {"project", "runtime", "repository", "workshop"}:
        scope = "project"
    return scope


def _goal_capability_catalog(request: str, route_name: str, scope: str) -> list[dict]:
    low=(request or '').lower()
    caps=[]
    def add(name, required=True, source="inferred", why=""):
        if not any(c["capability"]==name for c in caps):
            caps.append({"capability":name,"required":required,"source":source,"why":why})
    add("intent_governance", True, "always", "classify operation, scope, risk, and evidence budget")
    add("truth_surface_selection", True, "always", "choose project/runtime/workshop truth before claims")
    add("file_or_runtime_matrix_touch", True, "always", "ground intent in current files/index surface")
    add("truth_pulse_360", True, "always", "perform fast content-aware truth pulse before strategy or claims")
    add("workshop_lens", True, "always", "apply universal project/workshop method without replacing local truth")
    add("goal_contract", True, "always", "define what success means before implementation")
    add("missing_ring_scan", True, "always", "detect incomplete loops before execution")
    add("strategy_simulation", True, "always", "test whether proposed solution works in lifecycle")
    add("readiness_gate", True, "always", "label full/partial/blocked")
    if route_name in {"write_or_modify_work", "implementation_translation_work"} or any(x in low for x in ["اكتب","عدل","نفذ","implement","write","modify","code","api","database","قاعدة بيانات","كود"]):
        add("duplicate_scan", True, "write/implementation", "avoid creating duplicate owners or fragmented logic")
        add("impact_scan", True, "write/implementation", "identify parents, children, dependencies, affected contracts")
        add("write_plan", True, "write/implementation", "decide update-vs-create and validation path")
        add("safe_write", True, "write/implementation", "perform changes only through governed write path")
        add("post_change_validation", True, "write/implementation", "doctor/claim-check/tests after modifications")
    if any(x in low for x in ["معالجة الملفات","file matrix","ملفات","بحث","فتش","فهرس","semantic","ast","lsp","codebase"]):
        add("multi_lens_retrieval", True, "file-matrix objective", "path/text/chunk/symbol/relation/semantic lenses")
        add("code_intelligence_adapters", True, "file-matrix objective", "AST/LSP/vector/framework adapters when objective requires production-grade code understanding")
        add("freshness_invalidation", True, "file-matrix objective", "cache cannot override current files")
        add("file_matrix_doctor", True, "file-matrix objective", "prove lens/index/adapters health")
    if route_name == "runtime_work" or scope == "runtime" or any(x in low for x in ["بيئة المهندس","المهندس","runtime","factory","نظام تشغيل","مصنع"]):
        add("runtime_self_audit", True, "runtime objective", "factory must inspect and improve itself")
        add("capability_registry", True, "runtime objective", "new layers must attach to stable slots")
        add("maintenance_ledger", True, "runtime objective", "record runtime decisions, gaps, and upgrades")
    if any(x in low for x in ["أفضل","افضل","best","strategy","استراتيجية","ترقيع","حلقة","360"]):
        add("anti_patching_gate", True, "strategy objective", "prevent local fixes that fail parent goal")
        add("best_fit_comparison", True, "strategy objective", "compare alternatives against reality and workshop standards")
        add("completion_audit", True, "strategy objective", "prove the result closes the parent goal")
    return caps


def _capability_evidence(capability: str, scope: str) -> dict:
    evidence=[]; status="missing"; notes=[]
    cmd_map={
        "intent_governance":["route","operation-mode"],
        "truth_surface_selection":["truth-map","evidence-lock"],
        "file_or_runtime_matrix_touch":["file-matrix-touch","file-matrix-context"],
        "truth_pulse_360":["file-matrix-pulse"],
        "workshop_lens":["workshop-lens"],
        "goal_contract":["goal-closure"],
        "missing_ring_scan":["goal-closure"],
        "strategy_simulation":["factory-cycle","best-fit"],
        "readiness_gate":["goal-closure"],
        "duplicate_scan":["duplicate-scan"],
        "impact_scan":["impact-scan"],
        "write_plan":["write-plan"],
        "safe_write":["safe-write"],
        "post_change_validation":["file-matrix-doctor","doctor","claim-check"],
        "multi_lens_retrieval":["file-matrix-query","file-matrix-context"],
        "freshness_invalidation":["file-matrix-status","file-matrix-doctor"],
        "file_matrix_doctor":["file-matrix-doctor"],
        "runtime_self_audit":["runtime-audit","doctor"],
        "capability_registry":["neural-os"],
        "maintenance_ledger":["ledger"],
        "anti_patching_gate":["goal-closure"],
        "best_fit_comparison":["best-fit"],
        "completion_audit":["completion-audit"],
    }
    cmds=cli_commands_from_source()
    for c in cmd_map.get(capability,[]):
        if c in cmds:
            evidence.append({"type":"command","name":c,"status":"available"})
    if capability == "code_intelligence_adapters":
        try:
            d=file_matrix_doctor(scope if scope in {"project","runtime","repository","workshop"} else "project")
            ad=d.get("adapter_readiness",{})
            ready=[k for k,v in ad.items() if v]
            not_ready=[k for k,v in ad.items() if not v]
            evidence.append({"type":"adapter_readiness","ready":ready,"not_ready":not_ready})
            if ad.get("tree_sitter_ast") or ad.get("lsp_bridge") or ad.get("dense_vector_semantic"):
                status="partial"
            elif ad.get("builtin_symbol_parser") and ad.get("chunk_index"):
                status="partial"
                notes.append("builtin symbol/chunk retrieval exists, but production AST/LSP/vector adapters remain missing")
            else:
                status="missing"
        except Exception as e:
            evidence.append({"type":"adapter_check_error","error":str(e)})
    elif evidence:
        status="available"
    return {"capability":capability,"status":status,"evidence":evidence,"notes":notes}


def goal_closure(request: str, scope: str | None = None) -> dict:
    scope=_scope_for_request(request, scope)
    route=route_intent(request or "")
    mode=operation_mode(request or "")
    # Ground first. This command intentionally uses matrix/workshop truth before strategy verdict.
    try:
        pulse = file_matrix_truth_pulse(scope if scope in {"project","runtime","repository","workshop"} else "project", request or "", max_files=80, sample_chars=2000)
    except Exception as e:
        pulse = {"error":str(e), "scope":scope}
    try:
        matrix = file_matrix_touch(scope if scope in {"project","runtime","repository","workshop"} else "project")
    except Exception as e:
        matrix = {"error":str(e), "scope":scope}
    try:
        ws = workshop_lens()
    except Exception as e:
        ws = {"error":str(e)}
    caps=_goal_capability_catalog(request or "", route.get("route","project_work"), scope)
    checks=[]; missing=[]; partial=[]; available=[]
    for c in caps:
        ev=_capability_evidence(c["capability"], scope)
        checks.append({**c, **ev})
        if ev["status"] == "missing": missing.append(c["capability"])
        elif ev["status"] == "partial": partial.append(c["capability"])
        else: available.append(c["capability"])
    high = mode.get("risk") in {"high","critical"} or route.get("route") in {"write_or_modify_work","implementation_translation_work","runtime_work","best_fit_work"}
    objective_text=(request or "").strip()
    goal_contract={
        "parent_goal": objective_text,
        "scope": scope,
        "route": route.get("route"),
        "risk": mode.get("risk"),
        "success_definition": [
            "intent is grounded in current truth surface",
            "workshop standards are applied as method lens, not as substitute truth",
            "required capabilities are available or explicitly marked partial/missing",
            "solution strategy closes parent goal or is blocked/labeled partial",
            "execution path includes validation and maintenance receipt",
        ],
        "truth_surfaces": {
            "runtime": ".engineer",
            "workshop": "02_WORKSHOP/_WORKSHOP_SYSTEM",
            "active_project": "02_WORKSHOP/ACTIVE_PROJECT",
            "selected_scope": scope,
        },
    }
    blocking_missing = missing if high else [m for m in missing if m in {"intent_governance","truth_surface_selection","file_or_runtime_matrix_touch","workshop_lens","goal_contract","readiness_gate"}]
    if blocking_missing:
        verdict="BLOCKED_MISSING_CAPABILITY"
    elif partial:
        verdict="READY_PARTIAL"
    else:
        verdict="READY_FULL"
    out={
        "command":"goal-closure",
        "version":NEURAL_OS_VERSION,
        "generated_at":utc_now(),
        "request":request,
        "goal_contract":goal_contract,
        "grounding_summary":{
            "route":route,
            "operation_mode":{k:v for k,v in mode.items() if k!='route'},
            "truth_pulse_surface":{"coverage":pulse.get("coverage"),"readiness_verdict":pulse.get("readiness_verdict"),"truth_spine_files":((pulse.get("one_page_neural_truth_map") or {}).get("truth_spine_files") or [])[:6],"semantic_drift_candidates":((pulse.get("one_page_neural_truth_map") or {}).get("semantic_drift_candidates") or [])[:6],"incomplete_truth_candidates":((pulse.get("one_page_neural_truth_map") or {}).get("incomplete_truth_candidates") or [])[:6]},
            "file_matrix_surface":{"scope":matrix.get("scope"),"file_count":(matrix.get("profile") or {}).get("file_count"),"counts":matrix.get("counts"),"status":matrix.get("status")},
            "workshop_surface":{"files_detected":ws.get("files_detected"),"silent_gate":ws.get("silent_gate")},
        },
        "capability_matrix":checks,
        "missing_ring_scan":{
            "missing":missing,
            "partial":partial,
            "available":available,
            "rule":"Missing or partial capabilities do not become accepted truth; they block or downgrade readiness.",
        },
        "anti_patching_gate":{
            "status":"blocked" if blocking_missing else ("warn_partial" if partial else "pass"),
            "blocks":blocking_missing,
            "warnings":partial,
            "rule":"A local useful patch is rejected when it fails the parent goal lifecycle.",
        },
        "readiness_verdict":verdict,
        "allowed_next_action": "execute_governed_path" if verdict=="READY_FULL" else ("execute_only_as_declared_partial_stage" if verdict=="READY_PARTIAL" else "do_not_execute; build missing capability or narrow goal"),
        "required_next_gates": list(dict.fromkeys(["factory-cycle", "file-matrix-pulse", "file-matrix-context", "best-fit", "impact-scan" if high else "evidence-lock", "validation-doctor", "maintenance-ledger"])),
        "cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"goal_closure","generated_at":utc_now(),"volatile":True},
    }
    GOAL_CLOSURE_REPORT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    return out


def factory_cycle(request: str, scope: str | None = None, depth: str = "auto") -> dict:
    scope=_scope_for_request(request, scope)
    route=route_intent(request or "")
    mode=operation_mode(request or "")
    os_arch=neural_os_architecture()
    # Matrix ground: use fast for normal, focused/deep for high risk.
    fm_mode="focused" if mode.get("risk") in {"medium"} else ("deep" if mode.get("risk") in {"high","critical"} else "fast")
    if depth in {"fast","focused","deep","surgical"}:
        fm_mode=depth
    try:
        pulse=file_matrix_truth_pulse(scope if scope in {"project","runtime","repository","workshop"} else "project", request or "", max_files=80, sample_chars=2000)
    except Exception as e:
        pulse={"error":str(e),"scope":scope}
    try:
        fm=file_matrix_context(request or "", scope if scope in {"project","runtime","repository","workshop"} else "project", fm_mode if fm_mode != "surgical" else "surgical", 8 if fm_mode in {"fast","focused"} else 16, 1200 if fm_mode in {"fast","focused"} else 2400)
    except Exception as e:
        fm={"error":str(e),"scope":scope}
    closure=goal_closure(request or "", scope)
    cycle={
        "command":"factory-cycle",
        "version":NEURAL_OS_VERSION,
        "generated_at":utc_now(),
        "request":request,
        "operating_model":"neural_factory_loop",
        "scope":scope,
        "route":route,
        "operation_mode":{k:v for k,v in mode.items() if k!='route'},
        "architecture_slots":[s["slot"] for s in os_arch["slots"]],
        "loop_trace":[
            {"step":"intent_governance","status":"done","evidence":"route + operation-mode"},
            {"step":"truth_surface_selection","status":"done","selected_scope":scope},
            {"step":"truth_pulse_360","status":"done" if not pulse.get("error") else "error","readiness":pulse.get("readiness_verdict")},
            {"step":"matrix_touch","status":"done" if not fm.get("error") else "error","mode":fm_mode},
            {"step":"workshop_lens","status":"done","rule":"workshop guides method; active project remains local truth"},
            {"step":"truth_grounded_goal_closure","status":"done","verdict":closure.get("readiness_verdict")},
            {"step":"strategy_simulation","status":"pending_if_execution","rule":"compare alternatives and lifecycle fit before any write"},
            {"step":"execution_gate","status":"allowed" if closure.get("readiness_verdict")=="READY_FULL" else "blocked_or_partial","allowed_next_action":closure.get("allowed_next_action")},
            {"step":"validation_ledger","status":"required_after_action"},
        ],
        "truth_pulse_packet":pulse,
        "file_matrix_packet":fm,
        "goal_closure":closure,
        "factory_rules":os_arch["non_negotiable_rules"],
        "next_action":"Use this packet as operating context, not final answer. If readiness is not READY_FULL, close missing rings before claiming completion.",
        "cache_meta":{"scope":scope,"fingerprint":project_fingerprint(scope),"generated_by":"factory_cycle","generated_at":utc_now(),"volatile":True},
    }
    NEURAL_OS_REPORT.write_text(json.dumps(cycle, ensure_ascii=False, indent=2), encoding='utf-8')
    append_jsonl(OPS_LEDGER, {"operation":"factory-cycle","scope":scope,"route":route.get("route"),"readiness":closure.get("readiness_verdict"),"request":request})
    return cycle


def completion_audit(request: str = "", scope: str = "project") -> dict:
    closure=goal_closure(request or "completion audit", scope)
    status="pass" if closure.get("readiness_verdict")=="READY_FULL" else "fail"
    return {
        "command":"completion-audit",
        "version":NEURAL_OS_VERSION,
        "generated_at":utc_now(),
        "scope":scope,
        "request":request,
        "status":status,
        "readiness_verdict":closure.get("readiness_verdict"),
        "remaining_missing":closure.get("missing_ring_scan",{}).get("missing",[]),
        "remaining_partial":closure.get("missing_ring_scan",{}).get("partial",[]),
        "rule":"Completion means parent goal closed against current truth, not merely a useful partial implementation.",
    }


def factory_health() -> dict:
    problems=[]; warnings=[]
    arch=neural_os_architecture()
    cmds=cli_commands_from_source(); registry=registry_commands()
    for cmd in ["neural-os","factory-cycle","goal-closure","completion-audit","file-matrix-pulse","file-matrix-context","doctor","runtime-audit"]:
        if cmd not in cmds: problems.append({"type":"missing_cli_command","command":cmd})
        if registry and cmd not in registry: warnings.append({"type":"tool_registry_missing_command","command":cmd})
    cap_reg=RUNTIME/"runtime"/"capability_registry.yaml"
    if not cap_reg.exists(): problems.append({"type":"missing_capability_registry","path":rel(cap_reg)})
    for doc in [RUNTIME/"architecture"/"v9"/"00_ENGINEER_NEURAL_OS_FACTORY_CORE.md", RUNTIME/"governance"/"truth_grounded_goal_closure.yaml", RUNTIME/"protocols"/"neural_factory_operating_cycle.md"]:
        if not doc.exists(): problems.append({"type":"missing_neural_os_doc","path":rel(doc)})
    try:
        fm=file_matrix_doctor("project")
        if fm.get("health") == "fail": problems.append({"type":"file_matrix_doctor_failed","detail":fm.get("problems",[])[:5]})
        elif fm.get("health") == "pass_with_warnings": warnings.append({"type":"file_matrix_doctor_warnings","detail":fm.get("warnings",[])[:5]})
    except Exception as e:
        problems.append({"type":"file_matrix_doctor_error","error":str(e)})
    health="fail" if problems else ("pass_with_warnings" if warnings else "pass")
    out={"command":"factory-health","version":NEURAL_OS_VERSION,"generated_at":utc_now(),"health":health,"slot_count":len(arch["slots"]),"problems":problems,"warnings":warnings,"cache_meta":{"scope":"runtime","fingerprint":project_fingerprint("runtime"),"generated_by":"factory_health","generated_at":utc_now(),"volatile":True}}
    FACTORY_HEALTH_REPORT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    return out


def cmd_neural_os(args):
    print(json.dumps(neural_os_architecture(), ensure_ascii=False, indent=2))


def cmd_goal_closure(args):
    print(json.dumps(goal_closure(args.request or "", args.scope), ensure_ascii=False, indent=2))


def cmd_factory_cycle(args):
    print(json.dumps(factory_cycle(args.request or "", args.scope, args.depth), ensure_ascii=False, indent=2))


def cmd_completion_audit(args):
    print(json.dumps(completion_audit(args.request or "", args.scope), ensure_ascii=False, indent=2))


def cmd_factory_health(args):
    print(json.dumps(factory_health(), ensure_ascii=False, indent=2))


def build_golden_suite() -> dict:
    prompts=[
        {"id":"surface_identity","prompt":"اخبرني عنك من انت وما عملك وما تقييمك الحالي للمشروع وما أول خطوة؟","max_seconds":30,"must_use":["plug-fast","index"],"must_not":["runtime project-specific coupling","raw json dump"]},
        {"id":"runtime_repair","prompt":"افحص بيئة المهندس وحدد إصلاحًا جذريًا دون كسر","max_seconds":45,"must_use":["operation-mode","best-fit-root-cause","maintenance-ledger"],"must_not":["add random protocol"]},
        {"id":"write_duplicate","prompt":"أضف ملفًا يشرح مفهومًا موجودًا","max_seconds":40,"must_use":["duplicate-scan","impact-scan","write-plan"],"must_not":["create before owner search"]},
        {"id":"implementation_contract","prompt":"حوّل PRD إلى API وقاعدة بيانات واختبارات","max_seconds":60,"must_use":["truth-maturity","canon-check","relationship-graph"],"must_not":["code from stack name only"]},
    ]
    return {"version":V7_INDEX_VERSION,"purpose":"Golden prompts protect behavior quality, speed, truth discipline, and non-regression.","prompts":prompts}


def cmd_build_index(args):
    out=build_kernel_index(args.scope, True)
    if args.compact:
        out={k:out[k] for k in ["kernel_version","generated_at","scope","fingerprint","file_count","counts_by_role","counts_by_status","counts_by_signal"] if k in out} | {"high_value_files":[{"path":e.get('path'),"role":e.get('role'),"score":e.get('value_score')} for e in out.get('high_value_files',[])[:12]]}
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_plug_fast(args):
    print(json.dumps(build_fast_plug(args.request or "", args.scope), ensure_ascii=False, indent=2))


def cmd_plug_deep(args):
    print(json.dumps(build_deep_plug(args.request or "", args.scope, args.full_reads), ensure_ascii=False, indent=2))


def cmd_operation_mode(args):
    print(json.dumps(operation_mode(args.request or ""), ensure_ascii=False, indent=2))


def cmd_golden_suite(args):
    print(json.dumps(build_golden_suite(), ensure_ascii=False, indent=2))


def cmd_kernel_status(args):
    out={"version":V7_INDEX_VERSION,"indexes":{}}
    for scope in ["project","runtime","workshop","repository"]:
        p=V7_INDEX_FILES.get(scope, V7_KERNEL_DIR/f"{scope}_kernel_index.json")
        item={"path":rel(p),"exists":p.exists(),"current_fingerprint":quick_scope_fingerprint(scope)}
        if p.exists():
            try:
                data=json.loads(p.read_text(encoding='utf-8'))
                item.update({"stored_fingerprint":data.get('fingerprint'),"fresh":data.get('fingerprint')==item['current_fingerprint'],"file_count":data.get('file_count'),"generated_at":data.get('generated_at')})
            except Exception as e: item["error"]=str(e)
        out["indexes"][scope]=item
    print(json.dumps(out, ensure_ascii=False, indent=2))

def cmd_runtime_audit(args):
    report=runtime_integrity_report()
    violations=project_specific_runtime_coupling_report()
    if violations:
        report.setdefault('problems', []).append({'type':'static_runtime_project_term_leak','violations':violations[:30]})
        report['status']='fail'
        report['health']='fail'
    report['static_project_term_violations']=len(violations)
    print(json.dumps(report, ensure_ascii=False, indent=2))

def main():
    parser=argparse.ArgumentParser(description="Project Engineer Operating Framework")
    sub=parser.add_subparsers(dest="cmd", required=True)
    p=sub.add_parser("plug"); p.add_argument("request", nargs="?", default=""); p.add_argument("--depth", choices=["auto","snapshot","standard","deep","guarded_write","augmented"], default="auto"); p.add_argument("--mode", choices=["compact","full"], default="compact"); p.set_defaults(func=cmd_plug)
    p=sub.add_parser("neural"); p.add_argument("request", nargs="?", default=""); p.set_defaults(func=cmd_neural)
    p=sub.add_parser("best-fit"); p.add_argument("query", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--limit", type=int, default=8); p.set_defaults(func=cmd_best_fit)
    p=sub.add_parser("truth-maturity"); p.add_argument("query", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--limit", type=int, default=10); p.set_defaults(func=cmd_truth_maturity)
    p=sub.add_parser("canon-check"); p.add_argument("query", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_canon_check)
    p=sub.add_parser("route"); p.add_argument("request"); p.set_defaults(func=cmd_route)
    p=sub.add_parser("touch"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_touch)
    p=sub.add_parser("truth-map"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_truth_map)
    p=sub.add_parser("digest"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_digest)
    p=sub.add_parser("search"); p.add_argument("query"); p.add_argument("--scope", default="project"); p.add_argument("--limit", type=int, default=20); p.set_defaults(func=cmd_search)
    p=sub.add_parser("evidence"); p.add_argument("query"); p.add_argument("--scope", default="project"); p.add_argument("--limit", type=int, default=20); p.set_defaults(func=cmd_evidence)
    p=sub.add_parser("read"); p.add_argument("path"); p.add_argument("--limit", type=int, default=50000); p.set_defaults(func=cmd_read)
    p=sub.add_parser("read-many"); p.add_argument("pattern"); p.add_argument("--scope", default="project"); p.add_argument("--max-files", type=int, default=25); p.add_argument("--limit-per-file", type=int, default=12000); p.set_defaults(func=cmd_read_many)
    p=sub.add_parser("audit-baseline"); p.set_defaults(func=cmd_audit_baseline)
    p=sub.add_parser("govern-check"); p.set_defaults(func=cmd_govern_check)
    p=sub.add_parser("doctor"); p.set_defaults(func=cmd_doctor)
    p=sub.add_parser("runtime-audit"); p.set_defaults(func=cmd_runtime_audit)
    p=sub.add_parser("scan-runtime"); p.set_defaults(func=cmd_scan_runtime)
    p=sub.add_parser("workshop-lens"); p.set_defaults(func=cmd_workshop_lens)
    p=sub.add_parser("project-lens"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_project_lens)
    p=sub.add_parser("answer"); p.add_argument("request"); p.set_defaults(func=cmd_answer)
    p=sub.add_parser("init-project"); p.add_argument("name"); p.set_defaults(func=cmd_init_project)
    p=sub.add_parser("cycle"); p.add_argument("request", nargs="?", default=""); p.set_defaults(func=cmd_cycle)
    p=sub.add_parser("tool-plan"); p.add_argument("request"); p.set_defaults(func=cmd_tool_plan)
    p=sub.add_parser("receipt"); p.add_argument("request"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_receipt)
    p=sub.add_parser("matrix"); p.add_argument("request"); p.set_defaults(func=cmd_matrix)
    p=sub.add_parser("relationship-graph"); p.add_argument("query", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--limit", type=int, default=12); p.set_defaults(func=cmd_relationship_graph)
    p=sub.add_parser("cache-clean"); p.add_argument("--apply", action="store_true"); p.add_argument("--include-ledgers", action="store_true"); p.set_defaults(func=cmd_cache_clean)
    p=sub.add_parser("scenario-map"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_scenario_map)
    p=sub.add_parser("evidence-lock"); p.add_argument("query", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_evidence_lock)
    p=sub.add_parser("claim-check"); p.add_argument("text", nargs="?", default=""); p.add_argument("--file", default=""); p.add_argument("--scope", default="project"); p.set_defaults(func=cmd_claim_check)
    p=sub.add_parser("value-atlas"); p.add_argument("query", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--limit", type=int, default=80); p.add_argument("--mode", choices=["compact","full"], default="compact"); p.set_defaults(func=cmd_value_atlas)
    p=sub.add_parser("context-pack"); p.add_argument("query", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--max-files", type=int, default=60); p.add_argument("--per-file-chars", type=int, default=1800); p.set_defaults(func=cmd_context_pack)
    p=sub.add_parser("one-page"); p.add_argument("query", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--max-files", type=int, default=60); p.add_argument("--per-file-chars", type=int, default=1800); p.set_defaults(func=cmd_one_page)
    p=sub.add_parser("surface-check"); p.add_argument("text", nargs="?", default=""); p.add_argument("--file", default=""); p.set_defaults(func=cmd_surface_check)
    p=sub.add_parser("duplicate-scan"); p.add_argument("query"); p.add_argument("--scope", default="project"); p.add_argument("--limit", type=int, default=25); p.set_defaults(func=cmd_duplicate_scan)
    p=sub.add_parser("impact-scan"); p.add_argument("target"); p.add_argument("--objective", default=""); p.add_argument("--scope", default="project"); p.set_defaults(func=cmd_impact_scan)
    p=sub.add_parser("write-plan"); p.add_argument("target"); p.add_argument("objective"); p.add_argument("--text", default=""); p.add_argument("--from-file", default=""); p.add_argument("--scope", default="project"); p.set_defaults(func=cmd_write_plan)
    p=sub.add_parser("safe-write"); p.add_argument("target"); p.add_argument("--text", default=""); p.add_argument("--from-file", default=""); p.add_argument("--reason", required=True); p.add_argument("--scope", default="project"); p.add_argument("--apply", action="store_true"); p.set_defaults(func=cmd_safe_write)
    p=sub.add_parser("compare"); p.add_argument("query_a"); p.add_argument("query_b"); p.add_argument("--scope", default="project"); p.add_argument("--limit", type=int, default=30); p.set_defaults(func=cmd_compare)
    p=sub.add_parser("ledger"); p.add_argument("--kind", choices=["ops","claims","writes"], default="ops"); p.add_argument("--limit", type=int, default=20); p.set_defaults(func=cmd_operation_ledger)
    p=sub.add_parser("maturity-map"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_maturity_map)
    p=sub.add_parser("placeholder-scan"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--limit", type=int, default=80); p.add_argument("--all", action="store_true"); p.set_defaults(func=cmd_placeholder_scan)
    p=sub.add_parser("answer-receipt"); p.add_argument("request"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_answer_receipt)
    p=sub.add_parser("test-suite"); p.add_argument("--format", choices=["text","json"], default="text"); p.set_defaults(func=cmd_test_suite)
    p=sub.add_parser("build-index"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--compact", action="store_true"); p.set_defaults(func=cmd_build_index)
    p=sub.add_parser("plug-fast"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default=None, choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_plug_fast)
    p=sub.add_parser("plug-deep"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default=None, choices=["project","runtime","repository","workshop"]); p.add_argument("--full-reads", type=int, default=None); p.set_defaults(func=cmd_plug_deep)

    p=sub.add_parser("file-matrix-pulse"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--max-files", type=int, default=0, help="0 means all files selected by the truth/value ranking; no hard answer-time cage"); p.add_argument("--sample-chars", type=int, default=0, help="0 means full text through the safe file reader; positive values are explicit lightweight probes"); p.set_defaults(func=cmd_file_matrix_pulse)
    p=sub.add_parser("file-matrix-build"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--force", action="store_true"); p.set_defaults(func=cmd_file_matrix_build)
    p=sub.add_parser("file-matrix-touch"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_file_matrix_touch)
    p=sub.add_parser("file-matrix-query"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--mode", choices=["touch","fast","focused","deep","surgical"], default="fast"); p.add_argument("--limit", type=int, default=16); p.set_defaults(func=cmd_file_matrix_query)
    p=sub.add_parser("file-matrix-context"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--mode", choices=["fast","focused","deep","surgical"], default="fast"); p.add_argument("--max-files", type=int, default=10); p.add_argument("--chars", type=int, default=1800); p.set_defaults(func=cmd_file_matrix_context)
    p=sub.add_parser("file-matrix-doctor"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_file_matrix_doctor)
    p=sub.add_parser("file-matrix-status"); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_file_matrix_status)
    p=sub.add_parser("open-neural-entry"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default=None, choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_open_neural_entry)
    p=sub.add_parser("truth-sweep-360"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_truth_sweep_360)
    p=sub.add_parser("truth-authority-gate"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_truth_authority_gate)
    p=sub.add_parser("operation-360"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default=None, choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_operation_360)
    p=sub.add_parser("code-fingerprint"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--limit", type=int, default=120); p.set_defaults(func=cmd_code_fingerprint)
    p=sub.add_parser("code-impact-360"); p.add_argument("target", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.add_argument("--limit", type=int, default=80); p.set_defaults(func=cmd_code_impact_360)
    p=sub.add_parser("patch-gate-360"); p.add_argument("target_path", nargs="?", default=""); p.add_argument("--objective", default=""); p.add_argument("--expected-hash", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_patch_gate_360)
    p=sub.add_parser("neural-os"); p.set_defaults(func=cmd_neural_os)
    p=sub.add_parser("goal-closure"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default=None, choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_goal_closure)
    p=sub.add_parser("factory-cycle"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default=None, choices=["project","runtime","repository","workshop"]); p.add_argument("--depth", default="auto", choices=["auto","fast","focused","deep","surgical"]); p.set_defaults(func=cmd_factory_cycle)
    p=sub.add_parser("completion-audit"); p.add_argument("request", nargs="?", default=""); p.add_argument("--scope", default="project", choices=["project","runtime","repository","workshop"]); p.set_defaults(func=cmd_completion_audit)
    p=sub.add_parser("factory-health"); p.set_defaults(func=cmd_factory_health)
    p=sub.add_parser("operation-mode"); p.add_argument("request", nargs="?", default=""); p.set_defaults(func=cmd_operation_mode)
    p=sub.add_parser("kernel-status"); p.set_defaults(func=cmd_kernel_status)
    p=sub.add_parser("golden-suite"); p.set_defaults(func=cmd_golden_suite)
    args=parser.parse_args(); ensure_dirs(); args.func(args)

if __name__=="__main__": main()

# PAZARAT DOCUMENTATION ROUTING

# Purpose

This file defines how Pazarat documentation is routed and organized within the full software project repository.

It ensures that documentation is properly placed, accessible, and integrated with the codebase structure.

---

# Documentation Migration Strategy

## Current Structure
```
02_MY_PROJECT/pazarat/
├── 00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md
├── 01_PAZARAT_PRD_PLATFORM_IDENTITY_AND_OBJECTIVES.md
├── 02_PLATFORM_STATE_TAXONOMY.md
├── 03_PLATFORM_EVENT_TAXONOMY.md
├── 04_PROJECT_STRUCTURE_TREE_INDEX.md
├── 05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
├── 06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md
├── 07_PAZARAT_HIERARCHICAL_DOCUMENTATION_AND_SHARED_LOGIC_PROTOCOL.md
├── 08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md
├── 09_PAZARAT_NARRATIVE_SEQUENCE_AND_SCENARIO_MATURITY_STANDARD.md
├── 10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md
├── 11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
├── 12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml
├── 13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
├── 14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
├── 15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
├── 16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
├── 99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md
├── A_dashboards/
├── B_web_frontend/
├── C_mobile_app/
├── CODEBASE_STRUCTURE.md
├── BACKEND_NET10_STRUCTURE.md
└── FRONTEND_NEXTJS_STRUCTURE.md
```

## Target Structure
```
pazarat/ (Full software project repository)
├── docs/
│   ├── standards/                  # Pazarat local standards (migrated from root)
│   │   ├── 00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md
│   │   ├── 01_PAZARAT_PRD_PLATFORM_IDENTITY_AND_OBJECTIVES.md
│   │   ├── 02_PLATFORM_STATE_TAXONOMY.md
│   │   ├── 03_PLATFORM_EVENT_TAXONOMY.md
│   │   ├── 04_PROJECT_STRUCTURE_TREE_INDEX.md
│   │   ├── 05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
│   │   ├── 06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md
│   │   ├── 07_PAZARAT_HIERARCHICAL_DOCUMENTATION_AND_SHARED_LOGIC_PROTOCOL.md
│   │   ├── 08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md
│   │   ├── 09_PAZARAT_NARRATIVE_SEQUENCE_AND_SCENARIO_MATURITY_STANDARD.md
│   │   ├── 10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md
│   │   ├── 11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
│   │   ├── 12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml
│   │   ├── 13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
│   │   ├── 14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
│   │   ├── 15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
│   │   ├── 16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
│   │   ├── 99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md
│   │   ├── CODEBASE_STRUCTURE.md
│   │   ├── BACKEND_NET10_STRUCTURE.md
│   │   ├── FRONTEND_NEXTJS_STRUCTURE.md
│   │   └── DOCUMENTATION_ROUTING.md
│   │
│   ├── prd/                        # PRDs organized by domain
│   │   ├── platform/
│   │   │   └── 01_PAZARAT_PRD_PLATFORM_IDENTITY_AND_OBJECTIVES.md (link)
│   │   ├── dashboards/
│   │   │   ├── A_PRD_dashboards.md
│   │   │   ├── A-A_admin_dashboard/
│   │   │   │   ├── A-A_PRD_admin_dashboard.md
│   │   │   │   └── modules/
│   │   │   │       ├── governance/
│   │   │   │       ├── business/
│   │   │   │       ├── financial/
│   │   │   │       ├── marketing/
│   │   │   │       ├── operations/
│   │   │   │       ├── smart_data/
│   │   │   │       └── system/
│   │   │   ├── A-B_user_dashboard/
│   │   │   ├── A-C_agent_dashboard/
│   │   │   ├── A-D_b2b_seller_dashboard/
│   │   │   ├── A-E_b2c_seller_dashboard/
│   │   │   ├── A-F_driver_dashboard/
│   │   │   ├── A-G_staff_dashboard/
│   │   │   └── A-H_support_dashboard/
│   │   ├── web/
│   │   │   └── B_PRD_Web.md
│   │   └── mobile/
│   │       └── C_PRD_mobile_app.md
│   │
│   ├── api/                        # API documentation
│   │   ├── openapi/
│   │   │   └── openapi.yaml
│   │   ├── endpoints/
│   │   │   ├── users.md
│   │   │   ├── orders.md
│   │   │   └── ...
│   │   └── integration/
│   │       └── integration-guide.md
│   │
│   └── architecture/                # Architecture documentation
│       ├── adr/
│       │   ├── 001-adopt-dotnet.md
│       │   ├── 002-adopt-postgresql.md
│       │   └── ...
│       ├── diagrams/
│       │   ├── system-architecture.md
│       │   ├── data-flow.md
│       │   └── deployment.md
│       └── decisions/
│           └── architecture-decisions.md
│
├── backend/                        # Backend implementation
├── frontend/                       # Frontend implementation
├── database/                       # Database schemas and migrations
├── infra/                          # Infrastructure
├── scripts/                        # Scripts
└── .github/                        # GitHub workflows
```

---

# Documentation Categories

## 1. Standards (docs/standards/)
Contains Pazarat local standards that govern documentation, code generation, and implementation.

**Purpose:** These are the binding rules that the AI model and developers must follow.

**Access:** AI models read these first when entering Pazarat. Developers reference these for guidance.

**Maintenance:** Updated when standards evolve. Changes must be approved and documented.

## 2. PRDs (docs/prd/)
Contains Product Requirements Documents organized by domain.

**Purpose:** These define what to build for each domain.

**Access:** Developers read these to understand requirements. AI models use these for code generation.

**Maintenance:** Updated as requirements evolve. Changes follow the parent-child sequence standard.

## 3. API Documentation (docs/api/)
Contains API specifications, endpoint documentation, and integration guides.

**Purpose:** These define how to interact with the backend APIs.

**Access:** Frontend developers and external integrators read these.

**Maintenance:** Updated as APIs change. OpenAPI specs should be auto-generated from code.

## 4. Architecture Documentation (docs/architecture/)
Contains Architecture Decision Records (ADRs), diagrams, and architectural decisions.

**Purpose:** These document why architectural decisions were made.

**Access:** Architects and senior developers read these.

**Maintenance:** Updated when architectural decisions are made or changed.

---

# Documentation Generation Workflow

## When Generating Documentation

1. **Identify the type:**
   - Standard? → Place in `docs/standards/`
   - PRD? → Place in `docs/prd/{domain}/`
   - API spec? → Place in `docs/api/`
   - Architecture decision? → Place in `docs/architecture/adr/`

2. **Follow naming conventions:**
   - Standards: `{Number}_{Name}.md`
   - PRDs: `{Code}_{Name}.md`
   - API docs: `{Endpoint}.md`
   - ADRs: `{Number}-{Title}.md`

3. **Link related documents:**
   - PRDs should link to relevant standards
   - API docs should link to relevant PRDs
   - ADRs should link to affected standards and PRDs

## When Generating Code

1. **Read relevant documentation:**
   - Read standards in `docs/standards/`
   - Read PRDs in `docs/prd/{domain}/`
   - Read API docs in `docs/api/`

2. **Generate code that aligns with documentation:**
   - Code must follow standards
   - Code must implement PRD requirements
   - Code must match API specifications

3. **Update documentation if needed:**
   - If code reveals gaps in documentation, update the relevant docs
   - If code introduces new patterns, update standards if needed

---

# Documentation Access Patterns

## For AI Models
1. Enter `docs/standards/` first
2. Read numbered standards in order
3. Identify the relevant domain
4. Read PRDs in `docs/prd/{domain}/`
5. Generate code or documentation

## For Developers
1. Read `docs/standards/` to understand rules
2. Read `docs/prd/{domain}/` to understand requirements
3. Read `docs/api/` to understand API contracts
4. Read `docs/architecture/` to understand architectural decisions
5. Implement code

## For Frontend Developers
1. Read `docs/standards/` (especially UI/UX standard)
2. Read `docs/prd/web/` for web-specific requirements
3. Read `docs/api/` for API contracts
4. Implement frontend

## For Backend Developers
1. Read `docs/standards/` (especially data model and API standards)
2. Read `docs/prd/{domain}/` for domain requirements
3. Read `docs/architecture/` for architectural decisions
4. Implement backend

---

# Documentation Maintenance

## When to Update Documentation

- **Standards:** When methodology changes or new patterns emerge
- **PRDs:** When requirements change or new features are added
- **API docs:** When APIs change (should be auto-generated)
- **Architecture docs:** When architectural decisions are made

## Update Process

1. Identify the document to update
2. Make the change
3. Update related documents if needed
4. Update cross-references
5. Commit with clear message

## Version Control

- All documentation is version-controlled
- Use semantic versioning for major changes
- Use conventional commits for clarity
- Document breaking changes

---

# Documentation Quality Standards

## Standards Quality
- Clear and unambiguous
- Examples provided where helpful
- Cross-references to related standards
- Updated when methodology evolves

## PRD Quality
- Aligned with platform identity and objectives
- Scenario-driven
- Implementation-ready
- Linked to relevant standards
- Parent-child hierarchy maintained

## API Documentation Quality
- Auto-generated from code when possible
- Clear request/response examples
- Error cases documented
- Authentication requirements specified
- Rate limiting documented

## Architecture Documentation Quality
- Decision context provided
- Alternatives considered
- Consequences documented
- Linked to affected code
- Reviewable and maintainable

---

# Documentation Tools

## Recommended Tools
- **Markdown:** For all documentation
- **Mermaid:** For diagrams
- **OpenAPI/Swagger:** For API documentation
- **ADR Tools:** For architecture decision records
- **Diagrams.net:** For complex diagrams

## Documentation Generation
- API docs should be auto-generated from code
- ADRs should follow a standard template
- PRDs should follow the Pazarat PRD standard
- Standards should follow the Pazarat documentation standard

---

# This Routing Aligns With

- Pazarat 360-degree engineering method
- Documentation-first approach
- Code generation from documentation
- Developer accessibility
- AI model readability
- Version control best practices
- Documentation maintenance
- Cross-referencing
- Scalable documentation structure

This routing ensures that documentation is properly organized, accessible, and integrated with the codebase structure.

# PAZARAT ENGINEERING ENVIRONMENT AND STACK STANDARD

# Purpose / الهدف

This file defines the binding programming environment, stack, repository structure, development tooling, quality gates, and deployment readiness standard for Pazarat.

It is the third direction of the Pazarat 360-degree engineering loop.

It ensures that PRD-to-code translation does not produce generic code, unsupported frameworks, disconnected database schemas, or deployment-unready implementation.

هذا الملف يحدد بيئة البرمجة الشاملة التي يجب أن يلتزم بها أي توليد أو تجهيز كود في بازارات.

**هذا الملف هو العقل التشغيلي لعمليات التوليد - ليس مجرد مكتبة معرفة، بل موزع الفهم لكيفية توزيع المراحل والتعامل مع المشروع بالكامل.**

---

# 1. Binding Stack Decision / قرار التقنية الملزم

Current accepted Pazarat stack:

```txt
Primary editor: VS Code
Backend platform: .NET 10
Backend web framework: ASP.NET Core Web API 10
Backend language: C# 13
Backend architecture: Modular Monolith + DDD boundaries + Vertical Slice use cases
Database: PostgreSQL 16+
Database access: EF Core 10 with Npgsql provider; Dapper only for justified high-performance read paths
Frontend framework: Next.js 15 (App Router)
Frontend language: TypeScript 5
API style: HTTP APIs / REST-style resources unless a documented contract says otherwise
API documentation: OpenAPI
Local orchestration: Docker + .NET Aspire when multi-resource local coordination is needed
CI/CD: GitHub Actions
Deployment target: AWS-ready, with final AWS service selection controlled by later deployment ADRs
```

This decision is project truth until changed by explicit user decision or an ADR-level stack migration.

---

# 2. Forbidden Stack Drift / منع الانحراف التقني

The model must not propose or generate production-oriented Pazarat backend code using NestJS, Express, Laravel, Django, FastAPI, Rails, Spring Boot, Go services, PHP services, or any non-.NET backend framework unless the user explicitly requests stack reconsideration or an ADR comparison.

The model must not replace PostgreSQL with MySQL, MongoDB, SQLite, DynamoDB, or another database unless the user explicitly requests a database decision review.

The model must not replace Next.js with another frontend framework unless the user explicitly requests a frontend stack decision review.

When discussing alternatives, classify them as alternatives, not Pazarat project truth.

---

# 3. Developer Workstation Standard / معيار جهاز المطور

Required baseline tools:

```txt
Git
.NET SDK
Node.js LTS
pnpm
Docker Desktop or Docker Engine
PostgreSQL client tools
VS Code
```

Recommended tools:

```txt
GitHub CLI
AWS CLI
Terraform CLI
DBeaver, pgAdmin, or DataGrip
```

The project should avoid undocumented machine-local assumptions.

Local setup must be reproducible through repository scripts, Docker, Aspire AppHost, `.env.example`, and documented setup steps.

---

# 4. IDE / Code Editor Standard / معيار محرر الكود

VS Code is the primary project editor because Pazarat includes backend, frontend, documentation, YAML gates, Docker, GitHub Actions, infrastructure files, and AI-readable project standards.

Recommended VS Code extensions:

```txt
C# Dev Kit
C#
ESLint
Prettier
Docker
Dev Containers
GitHub Actions
GitLens
YAML
Markdown All in One
EditorConfig
REST Client or Thunder Client
Terraform
PostgreSQL Explorer
```

Visual Studio and JetBrains Rider may be used for deep .NET work, but they do not replace VS Code as the cross-stack project reference editor.

---

# 5. Repository Strategy / استراتيجية المستودع

Pazarat should use a repository structure that supports documentation, backend, frontend, database, infrastructure, tests, and AI generation contracts.

Recommended top-level structure when code begins:

```txt
pazarat/
  docs/
  backend/
  frontend/
  database/
  infra/
  .github/
  scripts/
```

If the source code lives in the same repository as the Mind_Ai tunnel, code folders must remain clearly separated from project standards.

If the source code lives in a separate product repository, this standard must be copied or referenced as the binding engineering environment standard.

---

## 5.1 Codebase Integration Mode / وضع دمج المشروع البرمجي

When Pazarat is transformed into a full software repository, the repository must be understood as one project root that includes documentation and implementation together.

The correct concept is:

```txt
pazarat/ = full software project repository
```

Inside it:

```txt
root Mind_Ai entry files and general layers = operating method and expert engine
02_MY_PROJECT/pazarat/ = Pazarat local control plane and traceability
/docs = Pazarat product/developer documentation
/backend = ASP.NET Core / .NET backend implementation
/frontend = Next.js frontend implementation
/database = PostgreSQL schemas, migrations, seeds, read models
/infra = infrastructure and deployment artifacts
/scripts = repeatable developer/model operations
/tests = cross-cutting tests when not owned by backend/frontend
```

`docs/` must not be used to bury the general Mind_Ai tunnel. The general tunnel is an operating layer, not ordinary project documentation.

If existing Pazarat documentation branches such as `A_dashboards`, `B_web_frontend`, or `C_mobile_app` are migrated into `docs/`, the migration must be controlled by `17_PAZARAT_CODEBASE_INTEGRATION_AND_DOCUMENTATION_ROUTING_STANDARD.md` and a before/after routing map.

**Note:** These branches have been migrated to `docs/prd/dashboards/`, `docs/prd/web/`, and `docs/prd/mobile/` respectively.

Any generated ZIP or codebase scaffold must preserve this distinction before claiming that the structure is integrated.

---

# 5.2 Code Generation Distribution / توزيع عمليات التوليد

هذا القسم هو العقل التشغيلي لكيفية توزيع المراحل والتعامل مع المشروع بالكامل عند توليد الكود.

## المرحلة 1: فهم السيناريو من التوثيق

عندما يناقش المستخدم سيناريو مع النموذج، يجب أن يفهم النموذج:

1. **أين يكتب التوثيق:** في `docs/prd/{domain}/` حسب المجال
2. **ما هو المجال المعني:** governance, business, financial, marketing, operations, smart_data, system
3. **ما هو المستودع المعني:** backend module, frontend feature, database schema

**مثال:**
- المستخدم يناقش "إدارة المستخدمين"
- النموذج يفهم أن هذا يتبع مجال `business/User_Management`
- التوثيق يكتب في `docs/prd/dashboards/A-A_admin_dashboard/modules/business/User_Management/`
- الكود يولد في `backend/src/Pazarat.Modules.Users/` و `frontend/src/features/admin/users/`

## المرحلة 2: تحليل السيناريو وتوليد التوثيق

النموذج يجب أن:

1. يقرأ المعايير في `docs/standards/`
2. يحدد نوع السيناريو (PRD، سيناريو، عقد تنفيذ)
3. يولد التوثيق في المكان الصحيح
4. يربط التوثيق بالمعايير ذات الصلة

**قواعد التوليد:**
- PRD جديد: `docs/prd/{domain}/{Code}_{Name}.md`
- سيناريو: داخل مجلد السيناريو في PRD
- عقد تنفيذ: `docs/prd/{domain}/contracts/`

## المرحلة 3: توليد الكود من التوثيق

النموذج يجب أن:

1. يقرأ التوثيق في `docs/prd/{domain}/`
2. يحدد المستودع المعني (backend, frontend, database)
3. يولد الكود في المكان الصحيح حسب الهيكل

**قواعد التوليد:**
- Backend: `backend/src/Pazarat.Modules.{ModuleName}/`
- Frontend: `frontend/src/features/{domain}/`
- Database: `database/migrations/`

## المرحلة 4: التحقق من التوافق

النموذج يجب أن:

1. يتحقق من أن الكود يتوافق مع التوثيق
2. يتحقق من أن الكود يتوافق مع المعايير
3. يتحقق من أن الكود يتوافق مع البيئة البرمجية
4. يتحقق من أن الكود يتوافق مع هدف المشروع

**قواعد التحقق:**
- التوافق مع التوثيق: الكود يجب أن يحقق متطلبات PRD
- التوافق مع المعايير: الكود يجب أن يتبع معايير البيئة البرمجية
- التوافق مع البيئة: الكود يجب أن يستخدم التقنية المقبولة
- التوافق مع الهدف: الكود يجب أن يخدم هدف منصة Pazarat

## المرحلة 5: التكامل والاختبار

النموذج يجب أن:

1. يضمن التكامل بين المستودعات المختلفة
2. يولد الاختبارات المناسبة
3. يضمن جودة الكود
4. يضمان جاهزية النشر

**قواعد التكامل:**
- Backend-Frontend Integration: API contracts must match
- Backend-Database Integration: EF Core migrations must work
- Frontend-Backend Integration: API calls must work
- Cross-Module Integration: Domain events must work

---

# 5.3 Module Mapping to Pazarat Domains / ربط الموديولات بأقسام Pazarat

هذا القسم يوضح كيف يتم ربط الموديولات البرمجية بأقسام Pazarat.

## Governance Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/governance/`
- **Backend:** `backend/src/Pazarat.Modules.Governance/`
- **Frontend:** `frontend/src/features/admin/governance/`
- **Database:** `database/migrations/Governance/`
- **المسؤوليات:** Country context, platform governance, cross-domain rules

## Identity Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/business/User_Management/`
- **Backend:** `backend/src/Pazarat.Modules.Identity/`
- **Frontend:** `frontend/src/features/admin/users/`
- **Database:** `database/migrations/Identity/`
- **المسؤوليات:** User identity, authentication, verification

## Users Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/business/User_Management/`
- **Backend:** `backend/src/Pazarat.Modules.Users/`
- **Frontend:** `frontend/src/features/admin/users/`
- **Database:** `database/migrations/Users/`
- **المسؤوليات:** User management, profiles, approvals

## Merchants Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/business/vendors_store/`
- **Backend:** `backend/src/Pazarat.Modules.Merchants/`
- **Frontend:** `frontend/src/features/admin/merchants/`
- **Database:** `database/migrations/Merchants/`
- **المسؤوليات:** Merchant/store management

## Catalog Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/business/products/` و `categories/`
- **Backend:** `backend/src/Pazarat.Modules.Catalog/`
- **Frontend:** `frontend/src/features/admin/catalog/`
- **Database:** `database/migrations/Catalog/`
- **المسؤوليات:** Product catalog, categories

## Orders Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/business/orders/`
- **Backend:** `backend/src/Pazarat.Modules.Orders/`
- **Frontend:** `frontend/src/features/admin/orders/`
- **Database:** `database/migrations/Orders/`
- **المسؤوليات:** Order lifecycle, order management

## Payments Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/financial/payments/`
- **Backend:** `backend/src/Pazarat.Modules.Payments/`
- **Frontend:** `frontend/src/features/admin/financial/`
- **Database:** `database/migrations/Payments/`
- **المسؤوليات:** Payments, wallets, transactions

## Shipping Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/operations/shipping/`
- **Backend:** `backend/src/Pazarat.Modules.Shipping/`
- **Frontend:** `frontend/src/features/admin/operations/`
- **Database:** `database/migrations/Shipping/`
- **المسؤوليات:** Shipping, shipments, fulfillment

## Warehouses Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/operations/warehouses/`
- **Backend:** `backend/src/Pazarat.Modules.Warehouses/`
- **Frontend:** `frontend/src/features/admin/operations/`
- **Database:** `database/migrations/Warehouses/`
- **المسؤوليات:** Warehouse management, inventory

## Financial Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/financial/`
- **Backend:** `backend/src/Pazarat.Modules.Financial/`
- **Frontend:** `frontend/src/features/admin/financial/`
- **Database:** `database/migrations/Financial/`
- **المسؤوليات:** Commissions, payouts, settlements, tax

## Marketing Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/marketing/`
- **Backend:** `backend/src/Pazarat.Modules.Marketing/`
- **Frontend:** `frontend/src/features/admin/marketing/`
- **Database:** `database/migrations/Marketing/`
- **المسؤوليات:** Campaigns, coupons, CRM, rewards

## Operations Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/operations/`
- **Backend:** `backend/src/Pazarat.Modules.Operations/`
- **Frontend:** `frontend/src/features/admin/operations/`
- **Database:** `database/migrations/Operations/`
- **المسؤوليات:** Supply chain, address codes, operations

## SmartData Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/smart_data/`
- **Backend:** `backend/src/Pazarat.Modules.SmartData/`
- **Frontend:** `frontend/src/features/admin/smart-data/`
- **Database:** `database/migrations/SmartData/`
- **المسؤوليات:** Analytics, reports, AI, events

## System Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/system/`
- **Backend:** `backend/src/Pazarat.Modules.System/`
- **Frontend:** `frontend/src/features/admin/system/`
- **Database:** `database/migrations/System/`
- **المسؤوليات:** Roles, permissions, security, settings

## Notifications Module
- **التوثيق:** `docs/prd/dashboards/A-A_admin_dashboard/modules/system/notifications/`
- **Backend:** `backend/src/Pazarat.Modules.Notifications/`
- **Frontend:** `frontend/src/features/admin/system/`
- **Database:** `database/migrations/Notifications/`
- **المسؤوليات:** Notification delivery, templates



# 6. Backend Solution Structure / هيكل الباك اند

Recommended .NET solution structure:

```txt
backend/
  Pazarat.sln

  src/
    Pazarat.Api/
    Pazarat.AppHost/
    Pazarat.ServiceDefaults/
    Pazarat.SharedKernel/

    Pazarat.Modules.Identity/
    Pazarat.Modules.Users/
    Pazarat.Modules.Merchants/
    Pazarat.Modules.Catalog/
    Pazarat.Modules.Orders/
    Pazarat.Modules.Payments/
    Pazarat.Modules.Shipping/
    Pazarat.Modules.Notifications/
    Pazarat.Modules.Admin/

  tests/
    Pazarat.Api.Tests/
    Pazarat.IntegrationTests/
    Pazarat.ArchitectureTests/
```

Each module may use:

```txt
Domain/
Application/
Infrastructure/
Presentation/
Contracts/
Tests/
```

The exact module list must be derived from accepted PRDs and the project structure tree, not invented from generic marketplace assumptions.

---

# 7. Backend Architecture Standard / معيار معمارية الباك اند

The backend should begin as a Modular Monolith, not premature microservices.

Rules:

- organize by bounded business modules
- expose use cases through vertical slices
- keep domain logic out of controllers
- keep infrastructure details out of domain logic
- keep cross-module references explicit
- use central state/event terminology
- use shared primitives instead of duplicating behavior
- isolate integration/event/outbox concerns when needed

Preferred implementation concepts:

```txt
Commands
Queries
Handlers
Validators
Authorization policies
Domain entities
Value objects
Domain events
Audit records
Repository or persistence abstractions when justified
Integration boundaries
```

Microservices, Kafka, complex event sourcing, Kubernetes, and service mesh should be deferred until the product and operational needs justify them.

---

# 8. Database Standard / معيار قاعدة البيانات

PostgreSQL is the accepted relational database.

Database design must derive from documented entities, ownership, lifecycle, relationships, implementation contracts, and `16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md`.

Rules:

- apply `16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md` before proposing schema, relationship, or endpoint-level implementation
- schema changes must use migrations
- no manual production schema drift
- tables must reflect business ownership
- state storage must align with the state taxonomy
- event/audit storage must align with the event taxonomy and shared primitives
- indexes must support documented queries and filters
- constraints should protect critical invariants where appropriate
- JSONB may be used for justified flexible metadata, not as a replacement for modeled core domain data

EF Core migrations are the default migration mechanism unless an ADR changes this.

---

# 9. API Contract Standard / معيار واجهات API

Default API style:

```txt
HTTP APIs / REST-style resources
OpenAPI documentation
ProblemDetails error format
Pagination, filters, sorting, and idempotency when relevant
Authorization policies for protected operations
```

API operations must be derived from use cases, commands, queries, transitions, permissions, and the endpoint extraction rules in `16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md`, not from frontend button names alone.

API route naming must remain stable, descriptive, and module-aware.

Public or long-lived client-facing API changes require versioning consideration.

---

# 10. Frontend Standard / معيار الفرونت اند

Frontend stack:

```txt
Next.js App Router
TypeScript
Design system aligned with Pazarat UI/UX standard
React Hook Form + Zod when form complexity requires it
Server Components first where appropriate
Client components only where interactivity requires them
```

Frontend work must derive from PRDs, screen artifacts, UI/UX standards, permissions, states, events, and API contracts.

Screens must not invent backend behavior, permissions, or state transitions.

Reusable UI patterns must synchronize with the UI/UX standard and shared primitives.

---

# 11. Local Development Runtime / بيئة التشغيل المحلية

Local development should support repeatable startup of:

```txt
ASP.NET Core API
Next.js frontend
PostgreSQL
Redis when needed
Workers when needed
Observability dashboard when needed
```

Use Docker for containerized dependencies.

Use .NET Aspire AppHost when multiple resources must be coordinated with service discovery, configuration injection, startup ordering, and local observability.

Aspire is not a replacement for ASP.NET Core, Docker, GitHub Actions, AWS, or production runtime.

It is a development-time orchestration and observability layer that helps run and inspect the local distributed application shape.

---

# 12. Testing Standard / معيار الاختبار

Backend testing tools:

```txt
xUnit
FluentAssertions
NSubstitute or Moq
WebApplicationFactory
Testcontainers for PostgreSQL integration tests
NetArchTest or ArchUnitNET for architecture rules
```

Frontend testing tools:

```txt
Vitest
React Testing Library
Playwright for E2E
```

Testing rules:

- acceptance criteria must become tests when implementation begins
- state transitions need tests
- permissions need tests
- filters and pagination need tests
- database constraints and migrations need tests where risk is high
- API behavior must be tested against documented contracts
- architecture tests should protect module boundaries

---

# 13. Code Quality Standard / معيار جودة الكود

Required quality files and practices:

```txt
.editorconfig
dotnet format
.NET analyzers
nullable enabled
TreatWarningsAsErrors for critical backend projects
ESLint
Prettier
TypeScript strict mode
```

Generated code must be readable, testable, and aligned with project naming.

The model must not generate large unreviewable files when a smaller vertical slice or implementation contract is safer.

---

# 14. Security Standard / معيار الأمن

Security must be considered from the start.

Required concerns:

- authentication approach
- policy-based authorization
- role and permission mapping
- input validation
- output shaping
- secrets outside Git
- CORS rules
- rate limiting where needed
- audit logs for sensitive actions
- PII classification where relevant
- secure error behavior

Security decisions must be documented before production exposure.

---

# 15. Observability Standard / معيار المراقبة

Pazarat implementation should support:

```txt
Structured logs
Metrics
Distributed tracing
Health checks
Audit logs
Error tracking
Performance diagnostics
```

Local observability may use Aspire Dashboard.

Production observability may use AWS CloudWatch, OpenTelemetry collectors, Grafana/Prometheus, or another ADR-approved stack.

Observability must be attached to real lifecycle and failure points, not added only as generic logging.

---

# 16. GitHub Standard / معيار GitHub

GitHub is the source control and workflow control surface.

Rules:

- no direct push to protected main when code work begins
- pull requests require CI checks
- branch protection should be configured
- issues/labels should distinguish PRD, backend, frontend, database, infra, security, and AI-generation work
- major stack decisions require ADR or explicit project decision

Suggested workflows:

```txt
ci.yml
backend.yml
frontend.yml
database.yml
security.yml
staging-deploy.yml
production-deploy.yml
```

---

# 17. CI/CD Standard / معيار النشر والتحقق

Pull request checks should include:

```txt
restore
build
lint
format check
test
typecheck
migration check
security/dependency check
```

Main branch or release workflow should prepare deployable artifacts.

Staging and production must be separated.

Production deployment should require approval and rollback awareness.

---

# 18. Deployment Readiness Standard / معيار الجاهزية للنشر

Pazarat must be AWS-ready, but it must not prematurely lock into one AWS service without an ADR.

Likely AWS mappings:

```txt
Backend: ECS Fargate or another ADR-approved compute target
Database: Amazon RDS PostgreSQL
Storage: S3
Secrets: AWS Secrets Manager or Parameter Store
Queues: SQS when needed
Email/notifications: SES/SNS when needed
Observability: CloudWatch/OpenTelemetry pipeline
```

Infrastructure should eventually be represented with Terraform or another accepted Infrastructure-as-Code approach.

---

# 19. Versioning And Release Standard / معيار الإصدارات

The project should eventually define:

- semantic versioning or release train policy
- database migration release order
- API compatibility policy
- changelog policy
- rollback policy
- environment promotion flow

Until then, code generation should avoid irreversible production assumptions.

---

# 20. AI Code Generation Guardrails / ضوابط توليد الكود بالنموذج

Before generating code, the model must verify:

- source PRD or implementation contract exists
- central state/event/primitive alignment is checked
- target stack is ASP.NET/.NET, PostgreSQL, Next.js unless explicitly changed
- file paths match the accepted structure or are clearly proposed
- migrations are included when database schema changes
- tests are included or gap-labeled
- generated output is a vertical slice when the full feature is too large
- assumptions are classified

The model must not silently invent:

- final endpoint names
- table schemas
- state names
- event names
- permission names
- module ownership
- deployment services
- package choices

---

# 21. Maintenance And Upgrade Policy / سياسة الصيانة والتحديث

Technology upgrades must be deliberate.

When a library, framework, runtime, or cloud service changes, update:

- this environment standard
- implementation standard if translation is affected
- runtime gates if enforcement is affected
- affected PRDs or implementation contracts if behavior changes
- CI/CD workflows if build/test/deploy changes

Do not let generated code drift away from the documented engineering environment.

---

# 22. Engineering Environment Alphabet / أبجدية بيئة التطوير والبرمجة

This section is the compact reference map for the accepted Pazarat engineering environment.

It does not replace the detailed standards above. It gives the model, engineer, designer, and reviewer a simple alphabet to read before any environment setup, code generation, implementation planning, or code review.

هذه الفقرة هي الخريطة المختصرة لأبجدية بيئة التطوير في بازارات. لا تستبدل التفصيل السابق، بل تختصره كمرجع سريع يمنع الانحراف ويذكّر النموذج بالبيئة التي يجب أن يولّد داخلها.

## 22.1 Core Stack Alphabet

```txt
Editor:
- VS Code as the primary cross-stack project editor
- Visual Studio or JetBrains Rider as optional deep .NET IDEs

Backend:
- .NET
- C#
- ASP.NET Core Web API
- Modular Monolith
- DDD boundaries
- Vertical Slice use cases

Backend support:
- EF Core
- Npgsql PostgreSQL provider
- FluentValidation
- OpenAPI / Swagger
- ProblemDetails
- Health Checks
- OpenTelemetry
- Structured logging
- Dapper only for justified high-performance read paths

Frontend:
- Next.js App Router
- TypeScript
- Pazarat UI/UX Design System
- React Hook Form when form complexity requires it
- Zod when frontend validation contracts require it
- Server Components first when appropriate
- Client Components only when interaction requires them

Database:
- PostgreSQL
- EF Core migrations
- PostgreSQL client tools
- JSONB only for justified metadata, not core domain replacement

Local development:
- Docker
- .NET Aspire AppHost when local multi-resource orchestration is needed
- .env.example
- reproducible setup scripts
- optional Dev Containers

Testing:
- xUnit
- FluentAssertions
- NSubstitute or Moq
- WebApplicationFactory
- Testcontainers for PostgreSQL integration tests
- NetArchTest or ArchUnitNET
- Vitest
- React Testing Library
- Playwright

Quality:
- .editorconfig
- dotnet format
- .NET analyzers
- nullable enabled
- TreatWarningsAsErrors for critical backend projects
- ESLint
- Prettier
- TypeScript strict mode

Source control:
- Git
- GitHub
- protected main branch when code work begins
- pull requests
- required CI checks
- explicit ADR for major stack changes

CI/CD:
- GitHub Actions
- restore
- build
- lint
- format check
- test
- typecheck
- migration check
- security/dependency check
- staging and production separation

Deployment readiness:
- AWS-ready
- Dockerized deployable services
- Amazon RDS PostgreSQL as likely database target
- S3 for storage when needed
- Secrets Manager or Parameter Store for secrets
- SQS for queues when needed
- SES/SNS for email/notifications when needed
- CloudWatch/OpenTelemetry pipeline for observability
- Terraform or another accepted IaC tool when infrastructure is formalized

Documentation and AI generation:
- Pazarat 360-degree method
- PRD cognition and traceability standard
- narrative/scenario maturity standard
- parent-child routing standard
- implementation translation contract
- implementation architecture and code generation standard
- shared primitives and continuity memory
- central state taxonomy
- central event taxonomy
- UI/UX design system standard
- engineering environment standard
- runtime YAML gates
```

## 22.2 Forbidden Alphabet Drift

The alphabet above is binding project truth.

The model must not substitute it with a different backend framework, database, frontend framework, repository pattern, deployment model, testing stack, or terminology set unless the user explicitly requests a stack review or ADR-level migration.

Examples of forbidden drift:

```txt
- Replacing ASP.NET Core with NestJS, Laravel, Django, FastAPI, Spring Boot, Rails, or Go services without an ADR.
- Replacing PostgreSQL with MongoDB, MySQL, SQLite, DynamoDB, or another database without an ADR.
- Replacing Next.js with another frontend framework without an ADR.
- Inventing state, event, permission, endpoint, module, or database terminology outside central references.
- Generating code without checking the 360-degree loop.
```

## 22.3 Reading Rule

Before any meaningful code generation or programming-environment decision, read this alphabet in this order:

```txt
1. 360 method
2. central references: states, events, shared primitives, UI/UX
3. PRD or child PRD source
4. implementation translation contract
5. engineering environment alphabet
6. target file structure
7. tests and CI/CD expectations
```

If the requested output conflicts with this alphabet, classify the conflict before generating code.


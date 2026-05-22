# Pazarat - Commerce Operating Platform

## Overview

Pazarat is a large-scale multi-party commerce platform designed to support:
- B2C commerce
- B2B commerce
- Multi-vendor marketplace operations
- Seller and store management
- User account evolution
- Affiliate and partner models
- Product and catalog operations
- Order lifecycle operations
- Shipping and fulfillment
- Wallets and financial operations
- Commissions and settlements
- Taxes and customs logic when needed
- Approvals and governance
- Identity, verification, and trust systems
- Operational dashboards
- Advanced filtering and monitoring
- Support, notifications, and lifecycle tracking
- Future intelligent operational systems

## Technology Stack

### Backend
- .NET 10
- ASP.NET Core Web API 10
- C# 13
- PostgreSQL 16+
- EF Core 10
- Modular Monolith + DDD + Vertical Slice

### Frontend
- Next.js 15 (App Router)
- TypeScript 5
- Tailwind CSS
- React Hook Form + Zod

### Infrastructure
- Docker
- .NET Aspire
- GitHub Actions
- AWS-ready

## Project Structure

```
pazarat/
├── 00_PROJECT_TUNNEL/               # THIRD TUNNEL - Project operational tunnel (SINGLE SOURCE OF TRUTH for standards)
│   ├── README.md                   # Explains the three-tunnel sequence
│   ├── 00_PRD_COGNITION_AND_TRACEABILITY_STANDARD.md
│   ├── 01_PAZARAT_PRD_PLATFORM_IDENTITY_AND_OBJECTIVES.md
│   ├── 02_PLATFORM_STATE_TAXONOMY.md
│   ├── 03_PLATFORM_EVENT_TAXONOMY.md
│   ├── 04_PROJECT_STRUCTURE_TREE_INDEX.md
│   ├── 05_UI_UX_DESIGN_SYSTEM_AND_VISUAL_GENERATION_STANDARD.md
│   ├── 06_IMPLEMENTATION_ARCHITECTURE_AND_CODE_GENERATION_STANDARD.md
│   ├── 07_PAZARAT_HIERARCHICAL_DOCUMENTATION_AND_SHARED_LOGIC_PROTOCOL.md
│   ├── 08_PAZARAT_SHARED_PRIMITIVES_AND_CONTINUITY_MEMORY.md
│   ├── 09_PAZARAT_NARRATIVE_SEQUENCE_AND_SCENARIO_MATURITY_STANDARD.md
│   ├── 10_PAZARAT_PARENT_CHILD_SEQUENCE_AND_CROSS_ARTIFACT_ROUTING_STANDARD.md
│   ├── 11_PAZARAT_PRD_DOCUMENTATION_AND_IMPLEMENTATION_TRANSLATION_CONTRACT.md
│   ├── 12_PAZARAT_PRD_AND_CODE_RUNTIME_GATES.yaml
│   ├── 13_PAZARAT_360_DEGREE_ENGINEERING_METHOD.md
│   ├── 14_PAZARAT_ENGINEERING_ENVIRONMENT_AND_STACK_STANDARD.md
│   ├── 15_PAZARAT_RAW_TO_PROGRAMMATIC_NARRATIVE_WEAVING_STANDARD.md
│   ├── 16_PAZARAT_DATA_MODEL_DATABASE_API_AND_ENDPOINT_STANDARD.md
│   ├── 17_PAZARAT_CODEBASE_INTEGRATION_AND_DOCUMENTATION_ROUTING_STANDARD.md
│   └── 99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md
├── docs/                           # Product/developer documentation (SINGLE SOURCE OF TRUTH for PRDs)
│   ├── prd/                        # Product Requirements Documents
│   │   ├── platform/               # Platform PRDs
│   │   ├── dashboards/             # Dashboard PRDs (A-A_admin_dashboard)
│   │   ├── web/                    # Web frontend PRDs (B_web_frontend)
│   │   └── mobile/                 # Mobile app PRDs (C_mobile_app)
│   ├── api/                        # API documentation
│   └── architecture/               # Architecture documentation
│       ├── CODEBASE_STRUCTURE.md
│       ├── BACKEND_NET10_STRUCTURE.md
│       ├── FRONTEND_NEXTJS_STRUCTURE.md
│       └── DOCUMENTATION_ROUTING.md
├── backend/                        # ASP.NET Core / .NET backend
├── frontend/                       # Next.js frontend
├── database/                       # PostgreSQL schemas, migrations, seeds
├── infra/                          # Infrastructure and deployment
├── scripts/                        # Developer/model operations
└── .github/                        # GitHub workflows
```

## Getting Started

### Prerequisites

- .NET SDK 10
- Node.js LTS
- pnpm
- Docker Desktop
- PostgreSQL client tools
- VS Code

### Local Development

1. Clone the repository
2. Run setup scripts
3. Start PostgreSQL (Docker)
4. Run migrations
5. Start backend (dotnet run)
6. Start frontend (npm run dev)

## Documentation

**IMPORTANT: The project has TWO SINGLE SOURCES OF TRUTH:**

1. **`00_PROJECT_TUNNEL/` (Third Tunnel)** - Project operational tunnel - Defines engineering standards, PRD cognition, and project-specific 360-degree methods
2. **`docs/`** - Product/developer documentation - Defines what to build (PRDs) and how to structure code (architecture)

### Three-Tunnel Sequence

The model follows this sequence when working on the project:

1. **First Tunnel:** `g:\Mind_Ai_v7_1\00_COGNITIVE_RUNTIME\` - Native cognitive engines (360-degree thinking, project state awareness, deep inference, self-questioning)
2. **Second Tunnel:** `g:\Mind_Ai_v7_1\01_COGNITIVE_TUNNEL\` - Cumulative project tunnel (documentation, memory, context)
3. **Third Tunnel:** `00_PROJECT_TUNNEL/` - Project operational tunnel (standards 00-99)

The model reaches the Third Tunnel, then executes tasks dynamically based on its intent using the standards in this tunnel.

### Third Tunnel (00_PROJECT_TUNNEL/)

When generating code, fixing issues, or verifying implementation, always reference the standards in `00_PROJECT_TUNNEL/` first:

- `00_PROJECT_TUNNEL/README.md` - Explains the three-tunnel sequence
- `00_PROJECT_TUNNEL/00-17.md` - Engineering standards, PRD cognition, 360-degree methods
- `00_PROJECT_TUNNEL/99_PAZARAT_PROJECT_REINFORCEMENT_MEMORY.md` - Project reinforcement memory

### Documentation (docs/)

When discussing scenarios or defining what to build, reference the PRDs in `docs/`:

- `docs/prd/platform/` - Platform PRDs
- `docs/prd/dashboards/` - Dashboard PRDs (A-A_admin_dashboard)
- `docs/prd/web/` - Web frontend PRDs (B_web_frontend)
- `docs/prd/mobile/` - Mobile app PRDs (C_mobile_app)
- `docs/api/` - API documentation - OpenAPI specifications, endpoint documentation, integration guides
- `docs/architecture/` - Architecture documentation - Codebase structure, backend/frontend structure, documentation routing

**Never guess or assume requirements. Always read the relevant standards in `00_PROJECT_TUNNEL/` and PRDs in `docs/` before generating or modifying code.**

## Modules

The backend is organized into 14 modules:
- Governance
- Identity
- Users
- Merchants
- Catalog
- Orders
- Payments
- Shipping
- Warehouses
- Financial
- Marketing
- Operations
- SmartData
- System
- Notifications

## License

[License information]

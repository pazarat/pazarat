# Pazarat Documentation

**THIS IS THE SINGLE SOURCE OF TRUTH FOR PRODUCT REQUIREMENTS AND ARCHITECTURE.**

All documentation in this directory is the authoritative source for:
- What to build (PRDs)
- Code structure (Architecture)
- API contracts (API documentation)

**Note: Engineering standards (00-99) are now in `00_PROJECT_TUNNEL/` (Third Tunnel).**

When generating code, fixing issues, or verifying implementation:
1. First reference the standards in `00_PROJECT_TUNNEL/` (Third Tunnel)
2. Then reference the PRDs and architecture in this directory

Never guess or assume requirements.

## Structure

```
docs/
├── prd/                   # Product Requirements Documents
│   ├── platform/         # Platform PRDs
│   ├── dashboards/       # Dashboard PRDs (A-A_admin_dashboard)
│   ├── web/              # Web frontend PRDs (B_web_frontend)
│   └── mobile/           # Mobile app PRDs (C_mobile_app)
├── api/                   # API documentation
│   ├── openapi/          # OpenAPI specifications
│   ├── endpoints/        # Endpoint documentation
│   └── integration/      # Integration guides
└── architecture/          # Architecture documentation
    ├── CODEBASE_STRUCTURE.md
    ├── BACKEND_NET10_STRUCTURE.md
    ├── FRONTEND_NEXTJS_STRUCTURE.md
    └── DOCUMENTATION_ROUTING.md
```

## PRDs (docs/prd/)

Product Requirements Documents define what to build for each domain:
- `docs/prd/platform/` - Platform-level PRDs
- `docs/prd/dashboards/` - Dashboard PRDs (A-A_admin_dashboard)
- `docs/prd/web/` - Web frontend PRDs (B_web_frontend)
- `docs/prd/mobile/` - Mobile app PRDs (C_mobile_app)

**When discussing scenarios or generating code, always reference the relevant PRD first.**

## API Documentation (docs/api/)

API specifications, endpoint documentation, and integration guides.

## Architecture Documentation (docs/architecture/)

Codebase structure, backend/frontend structure, and documentation routing:
- `CODEBASE_STRUCTURE.md` - Complete codebase structure
- `BACKEND_NET10_STRUCTURE.md` - Backend .NET 10 structure
- `FRONTEND_NEXTJS_STRUCTURE.md` - Frontend Next.js structure
- `DOCUMENTATION_ROUTING.md` - Documentation routing and organization

**When generating code, always reference the relevant architecture documentation.**

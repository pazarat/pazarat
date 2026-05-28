# PAZARAT CODEBASE STRUCTURE

# Purpose

This file defines the complete codebase structure for Pazarat as a full software project repository.

It reflects the DDD (Domain-Driven Design), Modular Monolith, and Vertical Slice architecture that aligns with Pazarat's business domains.

This structure is the operational blueprint for code generation, implementation, and development workflow.

---

# Repository Root Structure

```
pazarat/
├── docs/                           # Pazarat product/developer documentation
│   ├── standards/                  # Pazarat local standards (migrated from root)
│   ├── prd/                        # PRDs organized by domain
│   ├── api/                        # API documentation
│   └── architecture/                # Architecture decisions and diagrams
│
├── backend/                        # ASP.NET Core / .NET backend implementation
│   ├── Pazarat.sln                 # Solution file
│   ├── src/                        # Source code
│   │   ├── Pazarat.Api/            # API Gateway / Entry point
│   │   ├── Pazarat.AppHost/        # .NET Aspire orchestration
│   │   ├── Pazarat.ServiceDefaults/# Shared service configuration
│   │   ├── Pazarat.SharedKernel/   # Shared kernel (cross-cutting concerns)
│   │   │
│   │   ├── Pazarat.Modules.Governance/      # Governance module
│   │   ├── Pazarat.Modules.Identity/        # Identity module
│   │   ├── Pazarat.Modules.Users/           # Users module
│   │   ├── Pazarat.Modules.Merchants/      # Merchants module
│   │   ├── Pazarat.Modules.Catalog/         # Catalog module
│   │   ├── Pazarat.Modules.Orders/          # Orders module
│   │   ├── Pazarat.Modules.Payments/        # Payments module
│   │   ├── Pazarat.Modules.Shipping/        # Shipping module
│   │   ├── Pazarat.Modules.Warehouses/      # Warehouses module
│   │   ├── Pazarat.Modules.Financial/       # Financial module
│   │   ├── Pazarat.Modules.Marketing/       # Marketing module
│   │   ├── Pazarat.Modules.Operations/      # Operations module
│   │   ├── Pazarat.Modules.SmartData/       # Smart Data module
│   │   ├── Pazarat.Modules.System/          # System module
│   │   └── Pazarat.Modules.Notifications/    # Notifications module
│   │
│   └── tests/                       # Tests
│       ├── Pazarat.Api.Tests/
│       ├── Pazarat.IntegrationTests/
│       └── Pazarat.ArchitectureTests/
│
├── frontend/                       # Next.js frontend implementation
│   ├── src/
│   │   ├── app/                    # App Router
│   │   ├── components/             # Shared components
│   │   ├── lib/                    # Utilities
│   │   ├── features/               # Feature modules
│   │   └── styles/                 # Global styles
│   └── public/
│
├── database/                       # PostgreSQL schemas, migrations, seeds
│   ├── migrations/                 # EF Core migrations
│   ├── seeds/                      # Seed data
│   ├── schemas/                    # Schema definitions
│   └── scripts/                    # Database scripts
│
├── infra/                          # Infrastructure and deployment artifacts
│   ├── terraform/                  # Infrastructure as Code
│   ├── docker/                     # Docker configurations
│   ├── kubernetes/                 # Kubernetes manifests (future)
│   └── scripts/                    # Infrastructure scripts
│
├── scripts/                        # Repeatable developer/model operations
│   ├── setup/                      # Setup scripts
│   ├── migration/                  # Migration helpers
│   └── generation/                 # Code generation helpers
│
├── .github/                        # GitHub workflows
│   └── workflows/                  # CI/CD workflows
│
└── README.md                       # Project README
```

---

# Module Structure (DDD + Vertical Slice)

Each module follows DDD boundaries with Vertical Slice Architecture:

```
Pazarat.Modules.{ModuleName}/
├── Domain/                         # Domain layer (DDD)
│   ├── Entities/                   # Domain entities
│   ├── ValueObjects/               # Value objects
│   ├── Events/                     # Domain events
│   ├── Interfaces/                 # Domain interfaces (repositories, services)
│   ├── Specifications/             # Specifications pattern
│   └── Constants/                  # Domain constants
│
├── Application/                    # Application layer (Use Cases)
│   ├── Commands/                   # Command handlers
│   ├── Queries/                    # Query handlers
│   ├── DTOs/                       # Data transfer objects
│   ├── Validators/                 # Input validation
│   ├── Behaviors/                  # Pipeline behaviors
│   └── Interfaces/                 # Application interfaces
│
├── Infrastructure/                 # Infrastructure layer
│   ├── Persistence/                # EF Core DbContext, repositories
│   ├── Migrations/                 # Module-specific migrations
│   ├── ExternalServices/           # External service clients
│   ├── Messaging/                  # Event bus, outbox
│   └── Caching/                    # Caching implementation
│
├── Presentation/                   # Presentation layer
│   ├── Controllers/                # API controllers
│   ├── Endpoints/                  # Minimal API endpoints
│   ├── Requests/                   # Request models
│   ├── Responses/                  # Response models
│   └── Mappers/                    # DTO mappers
│
├── Contracts/                      # Contracts for external integration
│   ├── Commands/                   # External commands
│   ├── Events/                     # External events
│   └── Queries/                    # External queries
│
└── Tests/                          # Module tests
    ├── Unit/
    ├── Integration/
    └── Functional/
```

---

# Module Mapping to Pazarat Domains

## Pazarat.Modules.Governance
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/governance/`
- Responsibilities: Country context, platform governance, cross-domain rules
- Entities: Country, Region, GovernanceRule, InteractionMatrix

## Pazarat.Modules.Identity
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/business/User_Management/`
- Responsibilities: User identity, authentication, verification
- Entities: User, Identity, Verification, Agent, Staff

## Pazarat.Modules.Users
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/business/User_Management/`
- Responsibilities: User management, profiles, approvals
- Entities: UserProfile, UserApproval, B2BSeller, B2CSeller

## Pazarat.Modules.Merchants
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/business/vendors_store/`
- Responsibilities: Merchant/store management
- Entities: Merchant, Store, StoreSettings

## Pazarat.Modules.Catalog
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/business/products/` and `categories/`
- Responsibilities: Product catalog, categories
- Entities: Product, Category, ProductVariant, ProductAttribute

## Pazarat.Modules.Orders
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/business/orders/`
- Responsibilities: Order lifecycle, order management
- Entities: Order, OrderItem, OrderStatus, OrderTimeline

## Pazarat.Modules.Payments
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/financial/payments/`
- Responsibilities: Payments, wallets, transactions
- Entities: Payment, Wallet, Transaction, Invoice

## Pazarat.Modules.Shipping
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/operations/shipping/`
- Responsibilities: Shipping, shipments, fulfillment
- Entities: Shipment, ShippingMethod, Fulfillment, Driver

## Pazarat.Modules.Warehouses
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/operations/warehouses/`
- Responsibilities: Warehouse management, inventory
- Entities: Warehouse, Inventory, StockMovement

## Pazarat.Modules.Financial
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/financial/`
- Responsibilities: Commissions, payouts, settlements, tax
- Entities: Commission, Payout, Settlement, TaxRecord

## Pazarat.Modules.Marketing
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/marketing/`
- Responsibilities: Campaigns, coupons, CRM, rewards
- Entities: Campaign, Coupon, Reward, CustomerSegment

## Pazarat.Modules.Operations
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/operations/`
- Responsibilities: Supply chain, address codes, operations
- Entities: SupplyChain, AddressCode, OperationLog

## Pazarat.Modules.SmartData
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/smart_data/`
- Responsibilities: Analytics, reports, AI, events
- Entities: Report, AnalyticsEvent, AIModel, EventLog

## Pazarat.Modules.System
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/system/`
- Responsibilities: Roles, permissions, security, settings, notifications
- Entities: Role, Permission, SecurityLog, SystemSetting, Notification

## Pazarat.Modules.Notifications
- Maps to: `A_dashboards/A-A_admin_dashboard/modules/system/notifications/`
- Responsibilities: Notification delivery, templates
- Entities: Notification, NotificationTemplate, NotificationChannel

---

# Backend Solution Structure Details

## Pazarat.Api
- ASP.NET Core Web API
- API Gateway / Entry point
- Authentication middleware
- Authorization policies
- API versioning
- OpenAPI/Swagger documentation
- Health checks
- ProblemDetails error handling

## Pazarat.AppHost
- .NET Aspire orchestration
- Service discovery
- Configuration injection
- Startup ordering
- Local observability dashboard
- Resource coordination

## Pazarat.ServiceDefaults
- Shared service configuration
- Logging configuration
- Health check defaults
- OpenTelemetry defaults
- CORS defaults
- Rate limiting defaults

## Pazarat.SharedKernel
- Cross-cutting concerns
- Shared value objects
- Domain events infrastructure
- Specifications base classes
- Result pattern
- Pagination helpers
- Audit trail base
- Event sourcing base (if needed)

---

# Database Structure

## PostgreSQL Database
- Single database for Modular Monolith
- Schema per module (optional, for isolation)
- EF Core migrations
- Connection string configuration
- Seed data for development

## Migration Strategy
- EF Core migrations in `database/migrations/`
- Module-specific migrations in each module's `Infrastructure/Migrations/`
- Migration naming convention: `{Timestamp}_{ModuleName}_{Description}.cs`
- Rollback support
- Migration testing

---

# Frontend Structure

## Next.js App Router
- TypeScript
- Server Components first
- Client Components where needed
- App Router structure
- API routes for server actions
- Route handlers

## Feature Modules
```
frontend/src/features/
├── auth/                    # Authentication
├── admin/                   # Admin dashboard
│   ├── governance/         # Governance
│   ├── users/              # User management
│   ├── merchants/          # Merchant management
│   ├── orders/             # Order management
│   ├── financial/          # Financial operations
│   ├── marketing/          # Marketing
│   ├── operations/         # Operations
│   ├── smart-data/         # Smart data
│   └── system/             # System settings
├── seller/                  # Seller dashboard
├── buyer/                   # Buyer dashboard
└── public/                  # Public pages
```

---

# Documentation Structure

## docs/standards/
- Migrated from `02_MY_PROJECT/pazarat/` root numbered files
- Maintains the Pazarat local tunnel
- Preserves PRD cognition and traceability

## docs/prd/
- Organized by module
- Parent PRDs and child PRDs
- Scenario documentation
- Implementation contracts

## docs/api/
- OpenAPI specifications
- API usage examples
- Integration guides

## docs/architecture/
- Architecture Decision Records (ADRs)
- System diagrams
- Data flow diagrams
- Deployment architecture

---

# Infrastructure Structure

## terraform/
- AWS infrastructure
- VPC configuration
- ECS/Fargate configuration
- RDS PostgreSQL configuration
- S3 buckets
- IAM roles
- Security groups

## docker/
- Docker Compose for local development
- Dockerfile for backend
- Dockerfile for frontend
- Multi-stage builds

## kubernetes/
- Kubernetes manifests (future)
- Helm charts (future)
- Service configurations
- Ingress configurations

---

# Scripts Structure

## setup/
- Database setup scripts
- Environment configuration
- Dependency installation
- Initial seed data

## migration/
- Migration helpers
- Data migration scripts
- Schema migration helpers

## generation/
- Code generation helpers
- Scaffold generators
- Boilerplate generators

---

# CI/CD Structure

## .github/workflows/
- ci.yml - Continuous integration
- backend.yml - Backend-specific pipeline
- frontend.yml - Frontend-specific pipeline
- database.yml - Database migration pipeline
- security.yml - Security scanning
- staging-deploy.yml - Staging deployment
- production-deploy.yml - Production deployment

---

# Development Workflow

## Local Development
1. Clone repository
2. Run `scripts/setup/local-setup.sh`
3. Start PostgreSQL (Docker)
4. Run migrations
5. Start backend (dotnet run)
6. Start frontend (npm run dev)
7. Access API at http://localhost:5000
8. Access frontend at http://localhost:3000

## Code Generation
1. Identify module from PRD
2. Generate domain entities
3. Generate use cases (commands/queries)
4. Generate API endpoints
5. Generate frontend components
6. Run tests
7. Verify integration

## Testing
- Unit tests per module
- Integration tests with Testcontainers
- Architecture tests with NetArchTest
- E2E tests with Playwright

---

# Module Communication

## Internal Module Communication
- Use domain events for cross-module communication
- Use message bus (outbox pattern)
- Avoid direct module-to-module dependencies
- Use interfaces for integration

## External Module Communication
- API contracts in `Contracts/`
- Event contracts in `Contracts/Events/`
- Version contracts for breaking changes
- Document integration points

---

# This Structure Aligns With

- Pazarat 360-degree engineering method
- DDD principles
- Modular Monolith architecture
- Vertical Slice pattern
- Clean Architecture
- SOLID principles
- Pazarat business domains
- Scalable development workflow
- AWS deployment readiness

This structure is the foundation for transforming Pazarat from documentation to a fully operational software platform.

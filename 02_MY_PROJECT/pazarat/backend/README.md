# Pazarat Backend

ASP.NET Core / .NET backend implementation for Pazarat.

## Technology Stack

- .NET 10
- ASP.NET Core Web API 10
- C# 13
- PostgreSQL 16+
- EF Core 10
- Modular Monolith + DDD + Vertical Slice

## Structure

```
backend/
├── src/
│   ├── Pazarat.Api/                    # API Gateway / Entry point
│   ├── Pazarat.AppHost/                # .NET Aspire orchestration
│   ├── Pazarat.ServiceDefaults/        # Shared service configuration
│   ├── Pazarat.SharedKernel/           # Cross-cutting concerns
│   ├── Pazarat.Modules.Governance/     # Governance module
│   ├── Pazarat.Modules.Identity/       # Identity module
│   ├── Pazarat.Modules.Users/          # Users module
│   ├── Pazarat.Modules.Merchants/     # Merchants module
│   ├── Pazarat.Modules.Catalog/        # Catalog module
│   ├── Pazarat.Modules.Orders/         # Orders module
│   ├── Pazarat.Modules.Payments/       # Payments module
│   ├── Pazarat.Modules.Shipping/       # Shipping module
│   ├── Pazarat.Modules.Warehouses/     # Warehouses module
│   ├── Pazarat.Modules.Financial/      # Financial module
│   ├── Pazarat.Modules.Marketing/      # Marketing module
│   ├── Pazarat.Modules.Operations/     # Operations module
│   ├── Pazarat.Modules.SmartData/      # Smart Data module
│   ├── Pazarat.Modules.System/         # System module
│   └── Pazarat.Modules.Notifications/  # Notifications module
└── tests/
    ├── Pazarat.Api.Tests/
    ├── Pazarat.IntegrationTests/
    └── Pazarat.ArchitectureTests/
```

## Running

```bash
cd backend
dotnet restore
dotnet build
dotnet run --project src/Pazarat.Api
```

## Testing

```bash
dotnet test
```

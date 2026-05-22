# Pazarat Database

PostgreSQL database schemas, migrations, seeds, and scripts for Pazarat.

## Structure

```
database/
├── migrations/           # EF Core migrations
├── seeds/                # Seed data
├── schemas/              # Schema definitions
└── scripts/              # Database scripts
```

## Running Migrations

```bash
cd backend
dotnet ef database update
```

## Creating a Migration

```bash
dotnet ef migrations add <MigrationName> --project src/Pazarat.Modules.<ModuleName>
```

## Database Schemas

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

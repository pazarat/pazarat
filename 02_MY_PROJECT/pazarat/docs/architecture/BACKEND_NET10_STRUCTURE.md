# PAZARAT BACKEND .NET 10 STRUCTURE

# Purpose

This file defines the detailed backend structure for Pazarat using .NET 10, ASP.NET Core, EF Core, PostgreSQL, and DDD principles.

It is the operational blueprint for backend code generation, implementation, and development workflow.

---

# Technology Stack

```txt
.NET Version: 10
Backend Framework: ASP.NET Core 10
Language: C# 13
Database: PostgreSQL 16+
ORM: Entity Framework Core 10
API Style: ASP.NET Core Web API + Minimal APIs
Authentication: ASP.NET Core Identity + JWT
Authorization: Policy-based authorization
Caching: Redis (optional)
Messaging: Outbox pattern with EF Core
Testing: xUnit, FluentAssertions, NSubstitute, WebApplicationFactory, Testcontainers
Architecture: Modular Monolith + DDD + Vertical Slice
```

---

# Solution Structure

```
backend/
├── Pazarat.sln
│
├── src/
│   ├── Pazarat.Api/
│   ├── Pazarat.AppHost/
│   ├── Pazarat.ServiceDefaults/
│   ├── Pazarat.SharedKernel/
│   │
│   ├── Pazarat.Modules.Governance/
│   ├── Pazarat.Modules.Identity/
│   ├── Pazarat.Modules.Users/
│   ├── Pazarat.Modules.Merchants/
│   ├── Pazarat.Modules.Catalog/
│   ├── Pazarat.Modules.Orders/
│   ├── Pazarat.Modules.Payments/
│   ├── Pazarat.Modules.Shipping/
│   ├── Pazarat.Modules.Warehouses/
│   ├── Pazarat.Modules.Financial/
│   ├── Pazarat.Modules.Marketing/
│   ├── Pazarat.Modules.Operations/
│   ├── Pazarat.Modules.SmartData/
│   ├── Pazarat.Modules.System/
│   └── Pazarat.Modules.Notifications/
│
└── tests/
    ├── Pazarat.Api.Tests/
    ├── Pazarat.IntegrationTests/
    └── Pazarat.ArchitectureTests/
```

---

# Pazarat.Api - API Gateway

## Structure
```
Pazarat.Api/
├── Controllers/                    # Traditional controllers (minimal use)
├── Endpoints/                      # Minimal API endpoints (preferred)
├── Middleware/                     # Custom middleware
├── Filters/                        # Action filters
├── Extensions/                     # Extension methods
├── Program.cs                      # Application entry point
├── appsettings.json               # Configuration
├── appsettings.Development.json
├── appsettings.Production.json
└── Properties/
    └── launchSettings.json
```

## Responsibilities
- API Gateway / Entry point
- Authentication middleware
- Authorization policies
- API versioning
- OpenAPI/Swagger documentation
- Health checks
- ProblemDetails error handling
- CORS configuration
- Rate limiting
- Request/response logging

## Key Components
```csharp
// Program.cs - Main configuration
var builder = WebApplication.CreateBuilder(args);

// Add service defaults
builder.AddServiceDefaults();

// Add authentication
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options => { /* JWT configuration */ });

// Add authorization
builder.Services.AddAuthorization(options => { /* Policy-based authorization */ });

// Add API explorer and Swagger
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options => { /* Swagger configuration */ });

// Add health checks
builder.Services.AddHealthChecks()
    .AddNpgSql(connectionString)
    .AddRedis(redisConnectionString);

// Register modules
builder.Services.RegisterPazaratModules();

var app = builder.Build();

// Use middleware
app.UseMiddleware<RequestLoggingMiddleware>();
app.UseMiddleware<ExceptionHandlingMiddleware>();

// Use authentication and authorization
app.UseAuthentication();
app.UseAuthorization();

// Map endpoints
app.MapEndpoints();

// Use Swagger
app.UseSwagger();
app.UseSwaggerUI();

// Use health checks
app.MapHealthChecks("/health");

app.Run();
```

---

# Pazarat.AppHost - .NET Aspire Orchestration

## Structure
```
Pazarat.AppHost/
├── Program.cs                      # Aspire orchestration
├── appsettings.json
└── Properties/
    └── launchSettings.json
```

## Responsibilities
- Service discovery
- Configuration injection
- Startup ordering
- Local observability dashboard
- Resource coordination
- Docker resource management

## Key Components
```csharp
// Program.cs - Aspire orchestration
var builder = DistributedApplication.CreateBuilder(args);

var postgres = builder.AddPostgres("postgres")
    .WithLifetime(ContainerLifetime.Persistent);

var redis = builder.AddRedis("redis")
    .WithLifetime(ContainerLifetime.Persistent);

var api = builder.AddProject<Projects.Pazarat_Api>("api")
    .WithReference(postgres)
    .WithReference(redis)
    .WithEnvironment("ASPNETCORE_ENVIRONMENT", "Development");

builder.Build().Run();
```

---

# Pazarat.ServiceDefaults - Shared Configuration

## Structure
```
Pazarat.ServiceDefaults/
├── Extensions/
│   └── ServiceDefaultsExtensions.cs
└── ServiceDefaults.cs
```

## Responsibilities
- Shared service configuration
- Logging configuration
- Health check defaults
- OpenTelemetry defaults
- CORS defaults
- Rate limiting defaults

## Key Components
```csharp
// Extensions/ServiceDefaultsExtensions.cs
public static IHostApplicationBuilder AddServiceDefaults(this IHostApplicationBuilder builder)
{
    builder.ConfigureOpenTelemetry();
    builder.AddDefaultHealthChecks();
    builder.ConfigureServices();
    
    return builder;
}
```

---

# Pazarat.SharedKernel - Cross-Cutting Concerns

## Structure
```
Pazarat.SharedKernel/
├── Domain/
│   ├── Events/
│   │   ├── IDomainEvent.cs
│   │   └── DomainEventBase.cs
│   ├── ValueObjects/
│   │   ├── ValueObject.cs
│   │   └── CommonValueObjects.cs
│   ├── Specifications/
│   │   ├── ISpecification.cs
│   │   └── Specification.cs
│   └── Primitives/
│       ├── Result.cs
│       ├── ResultT.cs
│       └── Pagination.cs
│
├── Application/
│   ├── Behaviors/
│   │   ├── ValidationBehavior.cs
│   │   ├── LoggingBehavior.cs
│   │   └── TransactionBehavior.cs
│   └── Interfaces/
│       ├── IUnitOfWork.cs
│       └── IRepository.cs
│
├── Infrastructure/
│   ├── Events/
│   │   ├── IDomainEventDispatcher.cs
│   │   └── InMemoryDomainEventDispatcher.cs
│   ├── Persistence/
│   │   ├── OutboxMessage.cs
│   │   └── IOutboxRepository.cs
│   └── Auditing/
│       ├── IAuditService.cs
│       └── AuditService.cs
│
└── Presentation/
    └── Extensions/
        └── ResultExtensions.cs
```

## Responsibilities
- Domain events infrastructure
- Value objects base classes
- Specifications pattern
- Result pattern
- Pagination helpers
- Audit trail base
- Pipeline behaviors
- Outbox pattern
- Domain event dispatcher

---

# Module Structure (DDD + Vertical Slice)

Each module follows this structure:

```
Pazarat.Modules.{ModuleName}/
├── Domain/
│   ├── Entities/
│   │   ├── {EntityName}.cs
│   │   └── {EntityName}Id.cs
│   ├── ValueObjects/
│   │   └── {ValueObjectName}.cs
│   ├── Events/
│   │   ├── {EventName}.cs
│   │   └── {EventName}Handler.cs
│   ├── Interfaces/
│   │   ├── I{EntityName}Repository.cs
│   │   └── I{EntityName}Service.cs
│   ├── Specifications/
│   │   └── {EntityName}Specifications.cs
│   └── Constants/
│       └── {ConstantName}.cs
│
├── Application/
│   ├── Commands/
│   │   ├── {CommandName}.cs
│   │   └── {CommandName}Handler.cs
│   ├── Queries/
│   │   ├── {QueryName}.cs
│   │   └── {QueryName}Handler.cs
│   ├── DTOs/
│   │   ├── {DtoName}.cs
│   │   └── {DtoName}Mapper.cs
│   ├── Validators/
│   │   └── {ValidatorName}.cs
│   ├── Behaviors/
│   │   └── {BehaviorName}.cs
│   └── Interfaces/
│       └── I{ServiceName}.cs
│
├── Infrastructure/
│   ├── Persistence/
│   │   ├── {ModuleName}DbContext.cs
│   │   ├── Configurations/
│   │   │   ├── {EntityName}Configuration.cs
│   │   │   └── {EntityName}Configuration.cs
│   │   ├── Repositories/
│   │   │   └── {EntityName}Repository.cs
│   │   └── Migrations/
│   │       └── {Timestamp}_{Description}.cs
│   ├── ExternalServices/
│   │   └── {ServiceName}Client.cs
│   ├── Messaging/
│   │   ├── OutboxMessage.cs
│   │   └── OutboxProcessor.cs
│   └── Caching/
│       └── {CacheName}Service.cs
│
├── Presentation/
│   ├── Controllers/
│   │   └── {ControllerName}Controller.cs
│   ├── Endpoints/
│   │   └── {EndpointName}Endpoint.cs
│   ├── Requests/
│   │   └── {RequestName}.cs
│   ├── Responses/
│   │   └── {ResponseName}.cs
│   └── Mappers/
│       └── {MapperName}.cs
│
├── Contracts/
│   ├── Commands/
│   │   └── {ExternalCommand}.cs
│   ├── Events/
│   │   └── {ExternalEvent}.cs
│   └── Queries/
│       └── {ExternalQuery}.cs
│
└── Tests/
    ├── Unit/
    │   ├── Commands/
    │   └── Queries/
    ├── Integration/
    │   └── {TestName}.cs
    └── Functional/
        └── {TestName}.cs
```

---

# Example Module: Pazarat.Modules.Users

## Domain Layer
```csharp
// Domain/Entities/User.cs
public class User : AggregateRoot<UserId>
{
    public string Email { get; private set; }
    public string FirstName { get; private set; }
    public string LastName { get; private set; }
    public UserStatus Status { get; private set; }
    public DateTime CreatedAt { get; private set; }
    public DateTime? UpdatedAt { get; private set; }
    
    private User() { }
    
    public static User Create(string email, string firstName, string lastName)
    {
        var user = new User
        {
            Id = UserId.New(),
            Email = email,
            FirstName = firstName,
            LastName = lastName,
            Status = UserStatus.Active,
            CreatedAt = DateTime.UtcNow
        };
        
        user.AddDomainEvent(new UserCreatedEvent(user.Id, user.Email));
        
        return user;
    }
    
    public void UpdateProfile(string firstName, string lastName)
    {
        FirstName = firstName;
        LastName = lastName;
        UpdatedAt = DateTime.UtcNow;
        
        AddDomainEvent(new UserUpdatedEvent(Id, Email));
    }
    
    public void Deactivate()
    {
        Status = UserStatus.Inactive;
        UpdatedAt = DateTime.UtcNow;
        
        AddDomainEvent(new UserDeactivatedEvent(Id, Email));
    }
}

// Domain/ValueObjects/UserId.cs
public record UserId(Guid Value)
{
    public static UserId New() => new(Guid.NewGuid());
    public static UserId From(Guid value) => new(value);
}

// Domain/Events/UserCreatedEvent.cs
public record UserCreatedEvent(UserId UserId, string Email) : IDomainEvent;

// Domain/Interfaces/IUserRepository.cs
public interface IUserRepository : IRepository<User>
{
    Task<User?> GetByEmailAsync(string email, CancellationToken cancellationToken = default);
    Task<bool> EmailExistsAsync(string email, CancellationToken cancellationToken = default);
}
```

## Application Layer
```csharp
// Application/Commands/CreateUserCommand.cs
public record CreateUserCommand(
    string Email,
    string FirstName,
    string LastName
) : ICommand<Result<UserId>>;

// Application/Commands/CreateUserCommandHandler.cs
public class CreateUserCommandHandler : ICommandHandler<CreateUserCommand, Result<UserId>>
{
    private readonly IUserRepository _userRepository;
    private readonly IUnitOfWork _unitOfWork;
    private readonly IDomainEventDispatcher _domainEventDispatcher;
    
    public CreateUserCommandHandler(
        IUserRepository userRepository,
        IUnitOfWork unitOfWork,
        IDomainEventDispatcher domainEventDispatcher)
    {
        _userRepository = userRepository;
        _unitOfWork = unitOfWork;
        _domainEventDispatcher = domainEventDispatcher;
    }
    
    public async Task<Result<UserId>> Handle(CreateUserCommand command, CancellationToken cancellationToken)
    {
        // Check if email already exists
        if (await _userRepository.EmailExistsAsync(command.Email, cancellationToken))
        {
            return Result.Failure<UserId>("Email already exists");
        }
        
        // Create user
        var user = User.Create(command.Email, command.FirstName, command.LastName);
        
        // Add to repository
        await _userRepository.AddAsync(user, cancellationToken);
        
        // Save changes
        await _unitOfWork.SaveChangesAsync(cancellationToken);
        
        // Dispatch domain events
        await _domainEventDispatcher.DispatchAsync(user.DomainEvents, cancellationToken);
        
        return Result.Success(user.Id);
    }
}

// Application/Queries/GetUserByIdQuery.cs
public record GetUserByIdQuery(UserId UserId) : IQuery<Result<UserDto>>;

// Application/Queries/GetUserByIdQueryHandler.cs
public class GetUserByIdQueryHandler : IQueryHandler<GetUserByIdQuery, Result<UserDto>>
{
    private readonly IUserRepository _userRepository;
    
    public GetUserByIdQueryHandler(IUserRepository userRepository)
    {
        _userRepository = userRepository;
    }
    
    public async Task<Result<UserDto>> Handle(GetUserByIdQuery query, CancellationToken cancellationToken)
    {
        var user = await _userRepository.GetByIdAsync(query.UserId, cancellationToken);
        
        if (user is null)
        {
            return Result.Failure<UserDto>("User not found");
        }
        
        var userDto = new UserDto(
            user.Id.Value,
            user.Email,
            user.FirstName,
            user.LastName,
            user.Status,
            user.CreatedAt,
            user.UpdatedAt
        );
        
        return Result.Success(userDto);
    }
}
```

## Infrastructure Layer
```csharp
// Infrastructure/Persistence/UsersDbContext.cs
public class UsersDbContext : DbContext
{
    public DbSet<User> Users => Set<User>();
    
    public UsersDbContext(DbContextOptions<UsersDbContext> options)
        : base(options) { }
    
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfigurationsFromAssembly(typeof(UsersDbContext).Assembly);
        base.OnModelCreating(modelBuilder);
    }
}

// Infrastructure/Persistence/Configurations/UserConfiguration.cs
public class UserConfiguration : IEntityTypeConfiguration<User>
{
    public void Configure(EntityTypeBuilder<User> builder)
    {
        builder.ToTable("Users", "Users");
        
        builder.HasKey(u => u.Id);
        
        builder.Property(u => u.Id)
            .HasConversion(
                id => id.Value,
                value => UserId.From(value));
        
        builder.Property(u => u.Email)
            .IsRequired()
            .HasMaxLength(256);
        
        builder.Property(u => u.FirstName)
            .IsRequired()
            .HasMaxLength(100);
        
        builder.Property(u => u.LastName)
            .IsRequired()
            .HasMaxLength(100);
        
        builder.Property(u => u.Status)
            .HasConversion<string>();
        
        builder.Property(u => u.CreatedAt)
            .IsRequired();
        
        builder.HasIndex(u => u.Email)
            .IsUnique();
    }
}

// Infrastructure/Persistence/Repositories/UserRepository.cs
public class UserRepository : Repository<User>, IUserRepository
{
    public UserRepository(UsersDbContext context) : base(context) { }
    
    public async Task<User?> GetByEmailAsync(string email, CancellationToken cancellationToken = default)
    {
        return await _context.Users
            .FirstOrDefaultAsync(u => u.Email == email, cancellationToken);
    }
    
    public async Task<bool> EmailExistsAsync(string email, CancellationToken cancellationToken = default)
    {
        return await _context.Users
            .AnyAsync(u => u.Email == email, cancellationToken);
    }
}
```

## Presentation Layer
```csharp
// Presentation/Endpoints/UsersEndpoints.cs
public static class UsersEndpoints
{
    public static void MapUsersEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/users")
            .WithTags("Users")
            .RequireAuthorization();
        
        group.MapPost("/", CreateUser)
            .WithName("CreateUser")
            .Produces<Result<UserId>>(StatusCodes.Status201Created)
            .Produces<ProblemDetails>(StatusCodes.Status400BadRequest);
        
        group.MapGet("/{id:guid}", GetUserById)
            .WithName("GetUserById")
            .Produces<Result<UserDto>>(StatusCodes.Status200OK)
            .Produces<ProblemDetails>(StatusCodes.Status404NotFound);
    }
    
    private static async Task<IResult> CreateUser(
        CreateUserCommand command,
        ISender sender,
        CancellationToken cancellationToken)
    {
        var result = await sender.Send(command, cancellationToken);
        
        if (result.IsFailure)
        {
            return Results.BadRequest(result.Error);
        }
        
        return Results.Created($"/api/users/{result.Value.Value}", result.Value);
    }
    
    private static async Task<IResult> GetUserById(
        Guid id,
        ISender sender,
        CancellationToken cancellationToken)
    {
        var query = new GetUserByIdQuery(UserId.From(id));
        var result = await sender.Send(query, cancellationToken);
        
        if (result.IsFailure)
        {
            return Results.NotFound(result.Error);
        }
        
        return Results.Ok(result.Value);
    }
}
```

---

# Database Structure

## PostgreSQL Database
```sql
-- Schema per module (optional)
CREATE SCHEMA IF NOT EXISTS Governance;
CREATE SCHEMA IF NOT EXISTS Identity;
CREATE SCHEMA IF NOT EXISTS Users;
CREATE SCHEMA IF NOT EXISTS Merchants;
CREATE SCHEMA IF NOT EXISTS Catalog;
CREATE SCHEMA IF NOT EXISTS Orders;
CREATE SCHEMA IF NOT EXISTS Payments;
CREATE SCHEMA IF NOT EXISTS Shipping;
CREATE SCHEMA IF NOT EXISTS Warehouses;
CREATE SCHEMA IF NOT EXISTS Financial;
CREATE SCHEMA IF NOT EXISTS Marketing;
CREATE SCHEMA IF NOT EXISTS Operations;
CREATE SCHEMA IF NOT EXISTS SmartData;
CREATE SCHEMA IF NOT EXISTS System;
CREATE SCHEMA IF NOT EXISTS Notifications;
```

## Migration Strategy
```csharp
// Program.cs - Migration configuration
builder.Services.AddDbContext<UsersDbContext>(options =>
    options.UseNpgsql(connectionString, 
        npgsqlOptions => npgsqlOptions
            .MigrationsAssembly(typeof(UsersDbContext).Assembly)));

// Run migrations
await context.Database.MigrateAsync();
```

## Connection String
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Host=localhost;Port=5432;Database=Pazarat;Username=postgres;Password=postgres"
  }
}
```

---

# Testing Structure

## Unit Tests
```csharp
// Tests/Unit/Commands/CreateUserCommandHandlerTests.cs
public class CreateUserCommandHandlerTests
{
    [Fact]
    public async Task Handle_WhenEmailExists_ReturnsFailure()
    {
        // Arrange
        var mockRepository = new Mock<IUserRepository>();
        var mockUnitOfWork = new Mock<IUnitOfWork>();
        var mockEventDispatcher = new Mock<IDomainEventDispatcher>();
        
        mockRepository.Setup(r => r.EmailExistsAsync(It.IsAny<string>(), It.IsAny<CancellationToken>()))
            .ReturnsAsync(true);
        
        var handler = new CreateUserCommandHandler(
            mockRepository.Object,
            mockUnitOfWork.Object,
            mockEventDispatcher.Object);
        
        var command = new CreateUserCommand("test@example.com", "John", "Doe");
        
        // Act
        var result = await handler.Handle(command, CancellationToken.None);
        
        // Assert
        Assert.True(result.IsFailure);
        Assert.Equal("Email already exists", result.Error);
    }
}
```

## Integration Tests
```csharp
// Tests/Integration/UsersIntegrationTests.cs
public class UsersIntegrationTests : IClassFixture<PazaratWebApplicationFactory>
{
    private readonly HttpClient _client;
    private readonly PazaratWebApplicationFactory _factory;
    
    public UsersIntegrationTests(PazaratWebApplicationFactory factory)
    {
        _factory = factory;
        _client = factory.CreateClient();
    }
    
    [Fact]
    public async Task CreateUser_WhenValid_ReturnsCreated()
    {
        // Arrange
        var command = new CreateUserCommand("test@example.com", "John", "Doe");
        
        // Act
        var response = await _client.PostAsJsonAsync("/api/users", command);
        
        // Assert
        response.StatusCode.Should().Be(HttpStatusCode.Created);
    }
}
```

## Architecture Tests
```csharp
// Tests/ArchitectureTests/ModuleArchitectureTests.cs
public class ModuleArchitectureTests
{
    [Fact]
    public void Domain_ShouldNotDependOnApplication()
    {
        var result = Types.InAssembly(typeof(User).Assembly)
            .Should()
            .NotHaveDependencyOn("Pazarat.Modules.Users.Application")
            .GetResult();
        
        result.IsSuccessful.Should().BeTrue();
    }
}
```

---

# This Structure Aligns With

- Pazarat 360-degree engineering method
- DDD principles
- Modular Monolith architecture
- Vertical Slice pattern
- Clean Architecture
- SOLID principles
- .NET 10 best practices
- EF Core 10 best practices
- PostgreSQL best practices
- ASP.NET Core 10 best practices
- Pazarat business domains
- Scalable development workflow
- Test-driven development
- CI/CD readiness

This structure is the foundation for building a robust, scalable, and maintainable backend for Pazarat.

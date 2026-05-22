using Pazarat.Modules.Identity;
using Pazarat.Modules.Users;
using Pazarat.Modules.CountryContext;
using Pazarat.Modules.Catalog;
using Pazarat.Modules.Orders;
using Pazarat.Modules.Payments;
using Pazarat.Modules.Shipping;
using Pazarat.Modules.Taxation;
using Pazarat.Modules.CustomsClearance;
using Pazarat.Modules.Admin;
using Pazarat.Modules.Audit;
using Pazarat.Modules.Notifications;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddIdentityModule();
builder.Services.AddUsersModule();
builder.Services.AddCountryContextModule();
builder.Services.AddCatalogModule();
builder.Services.AddOrdersModule();
builder.Services.AddPaymentsModule();
builder.Services.AddShippingModule();
builder.Services.AddTaxationModule();
builder.Services.AddCustomsClearanceModule();
builder.Services.AddAdminModule();
builder.Services.AddAuditModule();
builder.Services.AddNotificationsModule();

var app = builder.Build();

app.MapGet("/", () => Results.Ok(new { service = "Pazarat.Api", status = "ok" }));
app.MapGet("/health", () => Results.Ok(new { status = "healthy" }));

app.MapIdentityEndpoints();
app.MapUsersEndpoints();
app.MapCountryContextEndpoints();
app.MapCatalogEndpoints();
app.MapOrdersEndpoints();
app.MapPaymentsEndpoints();
app.MapShippingEndpoints();
app.MapTaxationEndpoints();
app.MapCustomsClearanceEndpoints();
app.MapAdminEndpoints();
app.MapAuditEndpoints();
app.MapNotificationsEndpoints();

app.Run();

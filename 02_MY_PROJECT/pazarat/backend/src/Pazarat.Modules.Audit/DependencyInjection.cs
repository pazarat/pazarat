using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Routing;
using Microsoft.Extensions.DependencyInjection;

namespace Pazarat.Modules.Audit;

public static class DependencyInjection
{
    public static IServiceCollection AddAuditModule(this IServiceCollection services)
    {
        return services;
    }

    public static IEndpointRouteBuilder MapAuditEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/audit").WithTags("Audit");
        group.MapGet("/health", () => Results.Ok(new { module = "audit", status = "ok" }));
        return app;
    }
}

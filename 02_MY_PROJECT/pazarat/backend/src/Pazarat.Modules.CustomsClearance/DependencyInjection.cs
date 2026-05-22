using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Routing;
using Microsoft.Extensions.DependencyInjection;

namespace Pazarat.Modules.CustomsClearance;

public static class DependencyInjection
{
    public static IServiceCollection AddCustomsClearanceModule(this IServiceCollection services)
    {
        return services;
    }

    public static IEndpointRouteBuilder MapCustomsClearanceEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/customs-clearance").WithTags("CustomsClearance");
        group.MapGet("/health", () => Results.Ok(new { module = "customs_clearance", status = "ok" }));
        return app;
    }
}

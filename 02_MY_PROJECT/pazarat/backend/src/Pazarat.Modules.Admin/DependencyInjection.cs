using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Routing;
using Microsoft.Extensions.DependencyInjection;

namespace Pazarat.Modules.Admin;

public static class DependencyInjection
{
    public static IServiceCollection AddAdminModule(this IServiceCollection services)
    {
        return services;
    }

    public static IEndpointRouteBuilder MapAdminEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/admin").WithTags("Admin");
        group.MapGet("/health", () => Results.Ok(new { module = "admin", status = "ok" }));
        return app;
    }
}

using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Routing;
using Microsoft.Extensions.DependencyInjection;

namespace Pazarat.Modules.Taxation;

public static class DependencyInjection
{
    public static IServiceCollection AddTaxationModule(this IServiceCollection services)
    {
        return services;
    }

    public static IEndpointRouteBuilder MapTaxationEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/taxation").WithTags("Taxation");
        group.MapGet("/health", () => Results.Ok(new { module = "taxation", status = "ok" }));
        return app;
    }
}

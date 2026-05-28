using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Routing;
using Microsoft.Extensions.DependencyInjection;

namespace Pazarat.Modules.Shipping;

public static class DependencyInjection
{
    public static IServiceCollection AddShippingModule(this IServiceCollection services)
    {
        return services;
    }

    public static IEndpointRouteBuilder MapShippingEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/shipping").WithTags("Shipping");
        group.MapGet("/health", () => Results.Ok(new { module = "shipping", status = "ok" }));
        return app;
    }
}

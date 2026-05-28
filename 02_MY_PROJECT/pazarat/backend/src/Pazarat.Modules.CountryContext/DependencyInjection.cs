using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Routing;
using Microsoft.Extensions.DependencyInjection;

namespace Pazarat.Modules.CountryContext;

public static class DependencyInjection
{
    public static IServiceCollection AddCountryContextModule(this IServiceCollection services)
    {
        return services;
    }

    public static IEndpointRouteBuilder MapCountryContextEndpoints(this IEndpointRouteBuilder app)
    {
        var group = app.MapGroup("/api/country-context").WithTags("CountryContext");
        group.MapGet("/health", () => Results.Ok(new { module = "country_context", status = "ok" }));
        return app;
    }
}

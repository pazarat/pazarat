FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS base
WORKDIR /app
EXPOSE 5000

FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src
COPY ["Pazarat.Api/Pazarat.Api.csproj", "Pazarat.Api/"]
RUN dotnet restore "Pazarat.Api/Pazarat.Api.csproj"
COPY . .
WORKDIR "/src/Pazarat.Api"
RUN dotnet build "Pazarat.Api.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Pazarat.Api.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Pazarat.Api.dll"]

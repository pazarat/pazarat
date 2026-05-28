param(
  [Parameter(Mandatory=$true)][string]$ModuleId,
  [Parameter(Mandatory=$true)][string]$FeatureId,
  [Parameter(Mandatory=$true)][string]$Slug
)
$target = "00_TUNNEL_ENTRY/02_MY_PROJECT/pazarat/00_PROJECT_TUNNEL/work_items/$ModuleId/$FeatureId-$Slug"
$template = "00_TUNNEL_ENTRY/02_MY_PROJECT/pazarat/00_PROJECT_TUNNEL/_templates/feature_packet.template"
New-Item -ItemType Directory -Force -Path $target | Out-Null
Copy-Item "$template/*" $target -Recurse -Force
Write-Host "Created feature packet: $target"

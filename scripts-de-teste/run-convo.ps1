param([string[]]$Utterances, [string]$Mode = "--simulate-actions")
$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")
Set-Location C:\Users\Ayumi\nu-explica
$sid = (sf agent preview start --authoring-bundle Nu_Explica -o minha-org $Mode --json | ConvertFrom-Json).result.sessionId
foreach ($u in $Utterances) {
    $r = sf agent preview send --authoring-bundle Nu_Explica -o minha-org --session-id $sid -u $u --json | ConvertFrom-Json
    $msg = ($r.result.messages | ForEach-Object { $_.message }) -join " / "
    $q = ([regex]::Matches($msg, '\?')).Count
    "USER: $u"
    "BOT ($q '?'): $msg"
    ""
}
$end = sf agent preview end --authoring-bundle Nu_Explica -o minha-org --session-id $sid --json | ConvertFrom-Json
"traces: " + ($end.result | ConvertTo-Json -Depth 3 -Compress)

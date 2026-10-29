param([string[]]$Utterances)
$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")
Set-Location C:\Users\Ayumi\nu-explica
$sid = (sf agent preview start --authoring-bundle Nu_Explica -o minha-org --use-live-actions --json | ConvertFrom-Json).result.sessionId
foreach ($u in $Utterances) {
    $r = sf agent preview send --authoring-bundle Nu_Explica -o minha-org --session-id $sid -u $u --json | ConvertFrom-Json
    $msg = ($r.result.messages | ForEach-Object { $_.message }) -join " / "
    $q = ([regex]::Matches($msg, '\?')).Count
    $trace = Get-ChildItem "C:\Users\Ayumi\nu-explica\.sfdx\agents\Nu_Explica\sessions\$sid\traces\*.json" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    $topic = if ((Get-Content $trace.FullName -Raw) -match '"topic": "([^"]+)"') { $Matches[1] } else { "?" }
    "USER: $u"
    "BOT [$topic] ($q '?'): $msg"
    ""
}
sf agent preview end --authoring-bundle Nu_Explica -o minha-org --session-id $sid --json | Out-Null

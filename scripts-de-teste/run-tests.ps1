param([string[]]$Utterances, [switch]$NewSessionEach)
$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")
Set-Location C:\Users\Ayumi\nu-explica
function Start-S { (sf agent preview start --authoring-bundle Nu_Explica_1 -o minha-org --simulate-actions --json | ConvertFrom-Json).result.sessionId }
$sid = Start-S
foreach ($u in $Utterances) {
    if ($NewSessionEach) { $sid = Start-S }
    $r = sf agent preview send --authoring-bundle Nu_Explica_1 -o minha-org --session-id $sid -u $u --json | ConvertFrom-Json
    $msg = ($r.result.messages | ForEach-Object { $_.message }) -join " / "
    $q = ([regex]::Matches($msg, '\?')).Count
    $w = ($msg -split '\s+' | Where-Object { $_ }).Count
    "USER: $u"
    "BOT ($w palavras, $q '?'): $msg"
    ""
}

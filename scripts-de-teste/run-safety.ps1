param([string[]]$Utterances, [int]$Runs = 3)
$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")
Set-Location C:\Users\Ayumi\nu-explica
foreach ($run in 1..$Runs) {
    $sid = (sf agent preview start --authoring-bundle Nu_Explica -o minha-org --simulate-actions --json | ConvertFrom-Json).result.sessionId
    foreach ($u in $Utterances) {
        $r = sf agent preview send --authoring-bundle Nu_Explica -o minha-org --session-id $sid -u $u --json | ConvertFrom-Json
        $m = $r.result.messages | Select-Object -First 1
        $trace = Get-ChildItem "C:\Users\Ayumi\nu-explica\.sfdx\agents\Nu_Explica\sessions\$sid\traces\*.json" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        $raw = Get-Content $trace.FullName -Raw
        $score = if ($raw -match '"safety_score": ([\d.e-]+)') { [double]$Matches[1] } else { -1 }
        $cats = ([regex]::Matches($raw, '"(\w+)": ([\d.]+)') | Where-Object { $_.Groups[1].Value -in 'toxicity','hate','identity','violence','physical','sexual','profanity','biased' -and [double]$_.Groups[2].Value -gt 0 } | ForEach-Object { "$($_.Groups[1].Value)=$($_.Groups[2].Value)" }) -join ","
        "run$run safe=$($m.isContentSafe) score=$score $cats :: $($m.message)"
    }
    sf agent preview end --authoring-bundle Nu_Explica -o minha-org --session-id $sid --json | Out-Null
    ""
}

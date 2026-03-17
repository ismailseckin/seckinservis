$sourceDir = "C:\Users\USER\.gemini\antigravity\brain\9f060131-156e-4007-9060-e98e63977942"
$destDir = "c:\Users\USER\.gemini\antigravity\scratch\seckin-servis\assets\logos"

if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force }

$mapping = @{
    "media__1773757158092.png" = "habas.png"
    "media__1773757158134.png" = "gage.png"
    "media__1773757158037.jpg" = "bisan.jpg"
    "media__1773757646874.jpg" = "ustunkarli.jpg"
    "media__1773757993065.jpg" = "inancelik.jpg"
    "media__1773757158108.png" = "cemer.png"
    "media__1773757158155.png" = "endosa.png"
    "media__1773758199275.jpg" = "kavurlar.jpg"
    "media__1773758210302.jpg" = "merka.jpg"
}

foreach ($src in $mapping.Keys) {
    $srcPath = Join-Path $sourceDir $src
    $destPath = Join-Path $destDir $mapping[$src]
    if (Test-Path $srcPath) {
        Write-Host "Copying $src to $($mapping[$src])..."
        [IO.File]::WriteAllBytes($destPath, [IO.File]::ReadAllBytes($srcPath))
    } else {
        Write-Warning "Source missing: $srcPath"
    }
}

Get-ChildItem $destDir

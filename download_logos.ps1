$logos = @{
    "ref-habas.png" = "https://www.habas.com.tr/Content/images/uploads/F300/e0dfec77-af46-499d-a064-6f2783d1f4be_habas--logo.png"
    "ref-bisan.png" = "https://www.bisan.com.tr/cdn/shop/files/bisan-400x100-white.png?v=1718739293&width=400"
    "ref-ustunkarli.png" = "https://ustunkarli.com/wp-content/uploads/logo_1_LOGO.png"
    "ref-gage.png" = "https://static.wixstatic.com/media/285971_60e3d97ca36f4956ac28a2b14fa8868e~mv2.png/v1/fill/w_268,h_268,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/285971_60e3d97ca36f4956ac28a2b14fa8868e~mv2.png"
    "ref-inan.png" = "https://www.inancelik.com.tr/site/o/107555/2026/02/logo-band-colored-2x.png"
    "ref-cemer.png" = "https://www.cemer.com.tr/assets/img/logo.png"
    "ref-endosa.png" = "https://endosa.com.tr/wp-content/uploads/2019/04/endosa-logo.png"
    "ref-kavurlar.png" = "https://www.kavurlar.com.tr/assets/front/style/assets/logo.png"
    "ref-merka.png" = "https://merkamakina.com/wp-content/uploads/2021/05/merka-logo.png"
}

$ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

foreach ($file in $logos.Keys) {
    $url = $logos[$file]
    $dest = Join-Path "assets\logos" $file
    Write-Host "Downloading $url to $dest..."
    try {
        Invoke-WebRequest -Uri $url -OutFile $dest -UserAgent $ua -ErrorAction Stop
        Write-Host "Success!"
    } catch {
        Write-Warning "Failed to download $url : $_"
    }
}

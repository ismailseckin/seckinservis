@echo off
set "DEST=assets\logos"
if not exist "%DEST%" mkdir "%DEST%"

echo Downloading Habaş...
curl -L -A "Mozilla/5.0" -o "%DEST%\ref-habas.png" "https://www.habas.com.tr/Content/images/uploads/F300/e0dfec77-af46-499d-a064-6f2783d1f4be_habas--logo.png"

echo Downloading Bisan...
curl -L -A "Mozilla/5.0" -o "%DEST%\ref-bisan.png" "https://www.bisan.com.tr/cdn/shop/files/bisan-400x100-white.png?v=1718739293&width=400"

echo Downloading Üstünkarlı...
curl -L -A "Mozilla/5.0" -o "%DEST%\ref-ustunkarli.png" "https://ustunkarli.com/wp-content/uploads/logo_1_LOGO.png"

echo Downloading Gage...
curl -L -A "Mozilla/5.0" -o "%DEST%\ref-gage.png" "https://static.wixstatic.com/media/285971_60e3d97ca36f4956ac28a2b14fa8868e~mv2.png/v1/fill/w_268,h_268,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/285971_60e3d97ca36f4956ac28a2b14fa8868e~mv2.png"

echo Downloading İnan...
curl -L -A "Mozilla/5.0" -o "%DEST%\ref-inan.png" "https://www.inancelik.com.tr/site/o/107555/2026/02/logo-band-colored-2x.png"

echo Downloading Cemer...
curl -k -L -A "Mozilla/5.0" -o "%DEST%\ref-cemer.png" "https://www.cemer.com.tr/assets/img/logo.png"

echo Downloading Endosa...
curl -L -A "Mozilla/5.0" -o "%DEST%\ref-endosa.png" "https://endosa.com.tr/wp-content/uploads/2019/04/endosa-logo.png"

echo Downloading Kavurlar...
curl -L -A "Mozilla/5.0" -o "%DEST%\ref-kavurlar.png" "https://www.kavurlar.com.tr/assets/front/style/assets/logo.png"

echo Downloading Merka...
curl -L -A "Mozilla/5.0" -o "%DEST%\ref-merka.png" "https://merkamakina.com/wp-content/uploads/2021/05/merka-logo.png"

dir "%DEST%"

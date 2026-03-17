@echo off
set "BRAIN=C:\Users\USER\.gemini\antigravity\brain\9f060131-156e-4007-9060-e98e63977942"
set "DEST=c:\Users\USER\.gemini\antigravity\scratch\seckin-servis\assets\logos"

echo Logolar kopyalaniyor...
if not exist "%DEST%" mkdir "%DEST%"

copy "%BRAIN%\media__1773757158092.png" "%DEST%\habas.png" /Y
copy "%BRAIN%\media__1773757158134.png" "%DEST%\gage.png" /Y
copy "%BRAIN%\media__1773757158037.jpg" "%DEST%\bisan.jpg" /Y
copy "%BRAIN%\media__1773757646874.jpg" "%DEST%\ustunkarli.jpg" /Y
copy "%BRAIN%\media__1773757993065.jpg" "%DEST%\inancelik.jpg" /Y
copy "%BRAIN%\media__1773757158108.png" "%DEST%\cemer.png" /Y
copy "%BRAIN%\media__1773757158155.png" "%DEST%\endosa.png" /Y
copy "%BRAIN%\media__1773758199275.jpg" "%DEST%\kavurlar.jpg" /Y
copy "%BRAIN%\media__1773758210302.jpg" "%DEST%\merka.jpg" /Y

echo.
echo Islem TAMAMLANDI! Sayfayi yenileyebilirsiniz.
pause

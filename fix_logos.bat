@echo off
set "BRAIN=C:\Users\USER\.gemini\antigravity\brain\9f060131-156e-4007-9060-e98e63977942"
set "LOGOS=c:\Users\USER\.gemini\antigravity\scratch\seckin-servis\assets\logos"

if not exist "%LOGOS%" mkdir "%LOGOS%"

copy "%BRAIN%\media__1773757158092.png" "%LOGOS%\habas.png" /Y
copy "%BRAIN%\media__1773757158134.png" "%LOGOS%\gage.png" /Y
copy "%BRAIN%\media__1773757158037.jpg" "%LOGOS%\bisan.jpg" /Y
copy "%BRAIN%\media__1773757646874.jpg" "%LOGOS%\ustunkarli.jpg" /Y
copy "%BRAIN%\media__1773757993065.jpg" "%LOGOS%\inancelik.jpg" /Y
copy "%BRAIN%\media__1773757158108.png" "%LOGOS%\cemer.png" /Y
copy "%BRAIN%\media__1773757158155.png" "%LOGOS%\endosa.png" /Y
copy "%BRAIN%\media__1773758199275.jpg" "%LOGOS%\kavurlar.jpg" /Y
copy "%BRAIN%\media__1773758210302.jpg" "%LOGOS%\merka.jpg" /Y

echo Contents of %LOGOS%:
dir "%LOGOS%"

@echo off
echo Dosya Yeniden Adlandirma Programi - EXE Derleme (Konsol)
echo ========================================================

echo.
echo PyInstaller kuruluyor...
pip install -r requirements.txt

echo.
echo EXE dosyasi derleniyor (konsol versiyonu)...
python -m PyInstaller --onefile --name="LeRename" --distpath=. --workpath=build --specpath=. file_renamer.py

echo.
echo Derleme tamamlandi!
echo EXE dosyasi: LeRename.exe
echo.
pause

@echo off
echo Dosya Yeniden Adlandirma Programi - EXE Derleme
echo ================================================

echo.
echo PyInstaller kuruluyor...
pip install -r requirements.txt

echo.
echo EXE dosyasi derleniyor...
python -m PyInstaller --onefile --windowed --name="LeRename" --distpath=. --workpath=build --specpath=. file_renamer.py

echo.
echo Derleme tamamlandi!
echo EXE dosyasi: LeRename.exe
echo.
pause

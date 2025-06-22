@echo off
REM Скрипт сборки приложения в один EXE файл

echo Проверка установки PyInstaller...
python -m pip show pyinstaller >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo PyInstaller не установлен. Устанавливаем...
    python -m pip install pyinstaller
) else (
    echo PyInstaller уже установлен
)

echo Начинаем сборку...
pyinstaller --onefile --noconsole --add-data "monkey780x450.jpg;." app.py

if %ERRORLEVEL% equ 0 (
    echo Сборка успешно завершена!
    echo Исполняемый файл находится в папке dist
) else (
    echo Ошибка при сборке
    exit /b 1
)

echo Очистка временных файлов...
rmdir /s /q build >nul 2>&1
del app.spec >nul 2>&1

echo Готово!
pause
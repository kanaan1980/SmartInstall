@echo off
chcp 65001 > nul
cls
echo ======================================================
echo    SmartInstall - نظام إدارة المبيعات بالتقسيط
echo ======================================================
echo.
echo جاري تشغيل التطبيق...
echo.

REM التحقق من Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ خطأ: Python غير مثبت!
    echo يرجى تثبيت Python 3.8+ من https://python.org
    pause
    exit /b 1
)

REM التحقق من المكتبات
echo 🔍 التحقق من المكتبات...
python -c "import PyQt5" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  المكتبات غير مثبتة. جاري التثبيت...
    pip install -r requirements.txt --break-system-packages
    if errorlevel 1 (
        echo ❌ فشل تثبيت المكتبات!
        pause
        exit /b 1
    )
)

REM تشغيل التطبيق
echo.
echo ▶️  بدء التشغيل...
echo.
python main.py

if errorlevel 1 (
    echo.
    echo ❌ حدث خطأ أثناء التشغيل!
    echo يرجى مراجعة ملف smartinstall.log للتفاصيل
    pause
)

# SmartInstall - run.ps1
# PowerShell startup script for Windows (PowerShell 5.1+)
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Clear-Host
Write-Host "======================================================"
Write-Host "   SmartInstall - نظام إدارة المبيعات بالتقسيط"
Write-Host "======================================================"
Write-Host "\nجاري تشغيل التطبيق...\n"

# التحقق من Python
try {
    & python -V > $null 2>&1
} catch {
    Write-Host "❌ خطأ: Python غير مثبت! يرجى تثبيت Python 3.8+ من https://python.org" -ForegroundColor Red
    exit 1
}

# التحقق من المكتبات
Write-Host "🔍 التحقق من المكتبات..."
python -c "import PyQt5" > $null 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  المكتبات غير مثبتة. جاري التثبيت..."
    pip install -r requirements.txt
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ فشل تثبيت المكتبات!" -ForegroundColor Red
        Read-Host -Prompt "اضغط Enter للمتابعة"
        exit 1
    }
}

# تشغيل التطبيق
Write-Host "\n▶️  بدء التشغيل...\n"
python main.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "\n❌ حدث خطأ أثناء التشغيل! الرجاء مراجعة ملف smartinstall.log للتفاصيل" -ForegroundColor Red
    Read-Host -Prompt "اضغط Enter للمتابعة"
}

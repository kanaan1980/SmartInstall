#!/usr/bin/env bash
# SmartInstall - run.sh
# Cross-platform startup script for Unix-like systems
set -e

echo "======================================================"
echo "   SmartInstall - نظام إدارة المبيعات بالتقسيط"
echo "======================================================"
echo
echo "جاري تشغيل التطبيق..."
echo

if ! command -v python >/dev/null 2>&1; then
  echo "❌ خطأ: Python غير مثبت! يرجى تثبيت Python 3.8+"
  exit 1
fi

# التحقق من المكتبات
echo "🔍 التحقق من المكتبات..."
python -c "import PyQt5" >/dev/null 2>&1 || {
  echo "⚠️  المكتبات غير مثبتة. جاري التثبيت..."
  pip install -r requirements.txt
}

# تشغيل التطبيق
echo
echo "▶️  بدء التشغيل..."
python main.py || {
  echo "\n❌ حدث خطأ أثناء التشغيل! الرجاء مراجعة ملف smartinstall.log للتفاصيل"
  exit 1
}

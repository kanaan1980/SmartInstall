"""
SmartInstall - Configuration
الإعدادات المركزية للتطبيق
"""

import os
from pathlib import Path

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent

# ============================================================================
# إعدادات التطبيق
# ============================================================================

class AppConfig:
    """إعدادات التطبيق الأساسية"""
    
    APP_NAME = "SmartInstall"
    APP_VERSION = "1.0.0"
    APP_DESCRIPTION = "نظام إدارة مبيعات الأجهزة الكهربائية بالتقسيط"
    
    # اللغة والتوطين
    LANGUAGE = "ar"  # Arabic
    TEXT_DIRECTION = "rtl"  # Right-to-Left
    
    # الخطوط
    FONT_FAMILY = "Cairo"  # يمكن استخدام: Cairo, Tajawal, Almarai
    FONT_SIZE_NORMAL = 11
    FONT_SIZE_HEADER = 14
    FONT_SIZE_TITLE = 16
    
    # الوضع
    DEBUG_MODE = False
    
    # Session
    SESSION_TIMEOUT = 1800  # 30 دقيقة بالثواني


# ============================================================================
# إعدادات قاعدة البيانات
# ============================================================================

class DatabaseConfig:
    """إعدادات قاعدة البيانات"""
    
    # ستُقرأ من ملف .env
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_NAME = os.getenv('DB_NAME', 'smartinstall_db')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_SSL_MODE = os.getenv('DB_SSL_MODE', 'prefer')
    
    # Connection Pool
    DB_POOL_MIN = 1
    DB_POOL_MAX = 10


# ============================================================================
# إعدادات الأمان
# ============================================================================

class SecurityConfig:
    """إعدادات الأمان والتشفير"""
    
    # مفتاح التشفير (Fernet)
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', '')
    
    # Secret Key للتطبيق
    APP_SECRET_KEY = os.getenv('APP_SECRET_KEY', '')
    
    # bcrypt rounds
    BCRYPT_ROUNDS = 12
    
    # تسجيل الخروج التلقائي
    AUTO_LOGOUT_ENABLED = True
    AUTO_LOGOUT_TIMEOUT = 1800  # 30 دقيقة


# ============================================================================
# إعدادات الصلاحيات
# ============================================================================

class PermissionsConfig:
    """إعدادات نظام الصلاحيات (RBAC)"""
    
    ROLES = {
        'admin': {
            'name_ar': 'مدير',
            'customers': ['view', 'add', 'edit', 'delete'],
            'inventory': ['view', 'add', 'edit', 'delete'],
            'contracts': ['view', 'add', 'edit', 'delete'],
            'payments': ['view', 'add', 'edit', 'delete'],
            'reports': ['view', 'export'],
            'settings': ['view', 'edit'],
            'users': ['view', 'add', 'edit', 'delete'],
            'auto_debit': ['view', 'execute']
        },
        'accountant': {
            'name_ar': 'محاسب',
            'customers': ['view'],
            'inventory': ['view'],
            'contracts': ['view'],
            'payments': ['view', 'add', 'edit'],
            'reports': ['view', 'export'],
            'settings': ['view'],
            'users': [],
            'auto_debit': ['view', 'execute']
        },
        'sales': {
            'name_ar': 'مبيعات',
            'customers': ['view', 'add', 'edit'],
            'inventory': ['view'],
            'contracts': ['view', 'add'],
            'payments': ['view'],
            'reports': [],
            'settings': [],
            'users': [],
            'auto_debit': []
        },
        'warehouse': {
            'name_ar': 'مخزن',
            'customers': [],
            'inventory': ['view', 'add', 'edit'],
            'contracts': [],
            'payments': [],
            'reports': [],
            'settings': [],
            'users': [],
            'auto_debit': []
        }
    }
    
    @staticmethod
    def check_permission(role, module, action):
        """
        التحقق من صلاحية المستخدم
        
        Args:
            role: دور المستخدم (admin, accountant, sales, warehouse)
            module: اسم الوحدة (customers, inventory, etc.)
            action: الإجراء (view, add, edit, delete)
        
        Returns:
            bool: True إذا كان لديه الصلاحية
        """
        if role not in PermissionsConfig.ROLES:
            return False
        
        role_perms = PermissionsConfig.ROLES[role]
        module_perms = role_perms.get(module, [])
        
        return action in module_perms


# ============================================================================
# إعدادات الملفات والموارد
# ============================================================================

class PathsConfig:
    """مسارات الملفات والمجلدات"""
    
    # المجلدات الأساسية
    BASE_DIR = BASE_DIR
    DATABASE_DIR = BASE_DIR / 'database'
    MODELS_DIR = BASE_DIR / 'models'
    CONTROLLERS_DIR = BASE_DIR / 'controllers'
    VIEWS_DIR = BASE_DIR / 'views'
    UTILS_DIR = BASE_DIR / 'utils'
    RESOURCES_DIR = BASE_DIR / 'resources'
    
    # المجلدات الفرعية
    ICONS_DIR = RESOURCES_DIR / 'icons'
    FONTS_DIR = RESOURCES_DIR / 'fonts'
    IMAGES_DIR = RESOURCES_DIR / 'images'
    TEMPLATES_DIR = RESOURCES_DIR / 'templates'
    
    # ملفات
    LOG_FILE = BASE_DIR / 'smartinstall.log'
    CONFIG_FILE = BASE_DIR / 'config.json'
    
    # التصدير
    EXPORT_DIR = BASE_DIR / 'exports'
    BACKUP_DIR = BASE_DIR / 'backups'


# ============================================================================
# إعدادات Logging
# ============================================================================

class LoggingConfig:
    """إعدادات نظام Logging"""
    
    LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_FILE = str(PathsConfig.LOG_FILE)
    LOG_MAX_BYTES = 10 * 1024 * 1024  # 10 MB
    LOG_BACKUP_COUNT = 5


# ============================================================================
# إعدادات الواجهة (PyQt5)
# ============================================================================

class UIConfig:
    """إعدادات الواجهة الرسومية"""
    
    # النوافذ
    WINDOW_MIN_WIDTH = 1024
    WINDOW_MIN_HEIGHT = 768
    WINDOW_TITLE = "SmartInstall - نظام إدارة المبيعات بالتقسيط"
    
    # الألوان (يمكن تخصيصها حسب الثيم)
    PRIMARY_COLOR = "#1976D2"  # أزرق
    SECONDARY_COLOR = "#424242"  # رمادي غامق
    SUCCESS_COLOR = "#4CAF50"  # أخضر
    WARNING_COLOR = "#FF9800"  # برتقالي
    DANGER_COLOR = "#F44336"  # أحمر
    INFO_COLOR = "#2196F3"  # أزرق فاتح
    
    # الثيمات
    THEME_LIGHT = "light"
    THEME_DARK = "dark"
    DEFAULT_THEME = THEME_LIGHT
    
    # QSS
    QSS_FILE = PathsConfig.VIEWS_DIR / 'styles.qss'

class FeatureFlags:
    """أعلام الميزات التجريبية والقابلة للتفعيل/التعطيل"""

    # تمكين Raptor mini (معاينة) لجميع العملاء
    # ملاحظة: وضع المعاينة قد يكون محدود المزايا؛ يمكن تعطيله بتعيين False
    RAPTOR_MINI_ENABLED = True
    RAPTOR_MINI_VERSION = 'preview'
    RAPTOR_MINI_DESCRIPTION = 'Raptor mini (Preview) — ميزة تجريبية لعرض تقارير سريعة'

# ============================================================================
# إعدادات التقارير والتصدير
# ============================================================================

class ReportConfig:
    """إعدادات التقارير والتصدير"""
    
    # الصيغ المدعومة
    EXPORT_FORMATS = ['PDF', 'Excel', 'Word']
    
    # PDF
    PDF_PAGE_SIZE = 'A4'
    PDF_ORIENTATION = 'portrait'  # أو 'landscape'
    PDF_FONT = 'Arial'  # خط يدعم العربية
    
    # Excel
    EXCEL_SHEET_NAME = 'التقرير'
    
    # Word
    WORD_FONT = 'Arial'
    WORD_FONT_SIZE = 11
    
    # شعار الشركة
    COMPANY_LOGO = PathsConfig.IMAGES_DIR / 'logo.png'


# ============================================================================
# إعدادات محاكاة السحب التلقائي
# ============================================================================

class AutoDebitConfig:
    """إعدادات محاكاة السحب التلقائي"""
    
    # نسبة النجاح الافتراضية (%)
    DEFAULT_SUCCESS_RATE = 70
    
    # رموز الأخطاء
    ERROR_CODES = {
        '05': 'رصيد غير كافٍ',
        '12': 'بطاقة منتهية الصلاحية',
        '51': 'خطأ في البطاقة',
        '91': 'مشكلة تقنية مؤقتة',
        '99': 'خطأ غير محدد'
    }


# ============================================================================
# إعدادات النسخ الاحتياطي
# ============================================================================

class BackupConfig:
    """إعدادات النسخ الاحتياطي"""
    
    # التفعيل
    AUTO_BACKUP_ENABLED = True
    
    # التكرار
    BACKUP_INTERVAL_HOURS = 24
    
    # المسار
    BACKUP_DIR = PathsConfig.BACKUP_DIR
    
    # الاحتفاظ
    BACKUP_RETENTION_DAYS = 30


# ============================================================================
# إعدادات الإشعارات
# ============================================================================

class NotificationConfig:
    """إعدادات نظام الإشعارات"""
    
    # التفعيل
    NOTIFICATIONS_ENABLED = True
    
    # الأنواع
    NOTIFICATION_TYPES = {
        'info': {'icon': 'info', 'color': UIConfig.INFO_COLOR},
        'success': {'icon': 'check_circle', 'color': UIConfig.SUCCESS_COLOR},
        'warning': {'icon': 'warning', 'color': UIConfig.WARNING_COLOR},
        'error': {'icon': 'error', 'color': UIConfig.DANGER_COLOR}
    }
    
    # المدة
    NOTIFICATION_DURATION = 5000  # 5 ثواني


# ============================================================================
# التحقق من صحة البيانات
# ============================================================================

class ValidationConfig:
    """إعدادات التحقق من البيانات"""
    
    # الرقم القومي
    NATIONAL_ID_LENGTH = 14
    NATIONAL_ID_PATTERN = r'^\d{14}$'
    
    # رقم الهاتف (مصري)
    PHONE_PATTERN = r'^01[0-2,5]\d{8}$'
    
    # البريد الإلكتروني
    EMAIL_PATTERN = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # كلمة المرور
    PASSWORD_MIN_LENGTH = 6
    PASSWORD_MAX_LENGTH = 100


# ============================================================================
# إعداد المجلدات عند أول تشغيل
# ============================================================================

def setup_directories():
    """إنشاء المجلدات المطلوبة إذا لم تكن موجودة"""
    directories = [
        PathsConfig.RESOURCES_DIR,
        PathsConfig.ICONS_DIR,
        PathsConfig.FONTS_DIR,
        PathsConfig.IMAGES_DIR,
        PathsConfig.TEMPLATES_DIR,
        PathsConfig.EXPORT_DIR,
        PathsConfig.BACKUP_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


# تشغيل الإعداد عند استيراد الملف
setup_directories()


# ============================================================================
# اختبار الوحدة
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("SmartInstall Configuration - Test")
    print("=" * 70)
    
    print(f"\n📱 التطبيق: {AppConfig.APP_NAME} v{AppConfig.APP_VERSION}")
    print(f"📝 الوصف: {AppConfig.APP_DESCRIPTION}")
    print(f"🌐 اللغة: {AppConfig.LANGUAGE} ({AppConfig.TEXT_DIRECTION})")
    
    print(f"\n🗄️ قاعدة البيانات:")
    print(f"   Host: {DatabaseConfig.DB_HOST}")
    print(f"   Port: {DatabaseConfig.DB_PORT}")
    print(f"   Database: {DatabaseConfig.DB_NAME}")
    
    print(f"\n👥 الأدوار المتاحة:")
    for role, config in PermissionsConfig.ROLES.items():
        print(f"   - {role}: {config['name_ar']}")
    
    print(f"\n✅ المجلدات تم إنشاؤها بنجاح")
    print(f"   Base: {PathsConfig.BASE_DIR}")
    print(f"   Resources: {PathsConfig.RESOURCES_DIR}")
    print(f"   Exports: {PathsConfig.EXPORT_DIR}")
    
    print("\n" + "=" * 70)

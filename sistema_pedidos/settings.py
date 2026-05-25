from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- MEDIA ----------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ---------------- AUTH ----------------
AUTH_USER_MODEL = 'users.User'

# ---------------- SECURITY ----------------
SECRET_KEY = 'django-insecure-pmd$48znr6ux*%i80a3u5_4s35ta2_fwh+q4c#6$ke=z4!n#cj'

DEBUG = False

ALLOWED_HOSTS = [
    "sistema-pedidos-rqhc.onrender.com",
    "front-end-sistema-pedidos-quxl-huo268ope.vercel.app",
]

# ---------------- APPS ----------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'users',
    'orders',
    'restaurants',
]

# ---------------- MIDDLEWARE (ORDEN IMPORTANTE) ----------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 👈 DEBE IR ARRIBA
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------- CORS CONFIG (CORREGIDO) ----------------

CORS_ALLOW_ALL_ORIGINS = True  # 🔥 CLAVE PARA TU CASO

CORS_ALLOWED_ORIGINS = [
    "https://front-end-sistema-pedidos-quxl-huo268ope.vercel.app",
]

CSRF_TRUSTED_ORIGINS = [
    "https://front-end-sistema-pedidos-quxl-huo268ope.vercel.app",
]

# ---------------- URL ROOT ----------------
ROOT_URLCONF = 'sistema_pedidos.urls'

WSGI_APPLICATION = 'sistema_pedidos.wsgi.application'

# ---------------- DATABASE ----------------
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL")
    )
}

# ---------------- REST FRAMEWORK ----------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

AUTHENTICATION_BACKENDS = [
    "users.auth_backend.EmailAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# ---------------- STATIC ----------------
STATIC_URL = 'static/'

# ---------------- DEFAULT ----------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
import os
from dotenv import load_dotenv
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
import dj_database_url
import stripe

# Load environment variables from .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "fallback_secret_key")

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

# os.getenv("DEBUG", "").lower() in ["true", "1"]

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "cloudinary",
    "cloudinary_storage",
    "home",
    "basket",
    "checkout",
    "products",
]

SITE_ID = 1

MIDDLEWARE = [
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cake_it_easy.urls"

# Templates Configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],  # Ensure BASE_DIR is correct
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",  # Required for Django Admin and Allauth
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "basket.contexts.basket_contents",  # Custom context processor for basket
            ],
        },
    },
]

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///db.sqlite3",
        engine="django.db.backends.postgresql"
    )
}

CSRF_TRUSTED_ORIGINS = ["https://*.codeinstitute-ide.net/", "https://*.herokuapp.com"]

# Static and Media Files
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Cloudinary Settings (Using Dummy Defaults)
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME", "dummy_cloud_name"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY", "dummy_api_key"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET", "dummy_api_secret"),
}

# DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

STRIPE_CURRENCY = "eur"
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "dummy_public_key")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "dummy_secret_key")
STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", "dummy_wh_secret")

STANDARD_DELIVERY_CHARGE = 15.00

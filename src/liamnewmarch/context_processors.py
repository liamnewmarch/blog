from django.conf import settings

from .constants import GOOGLE_FONTS_URL


def globals(request):
    return {
        'debug': settings.DEBUG,
        'google_cloud_project': settings.GOOGLE_CLOUD_PROJECT,
        'google_fonts_url': GOOGLE_FONTS_URL,
        'stackdriver_api_key': settings.STACKDRIVER_API_KEY,
    }

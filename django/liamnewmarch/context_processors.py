from .constants import GOOGLE_FONTS_URL


def globals(request):
    return {
        'google_fonts_url': GOOGLE_FONTS_URL,
    }

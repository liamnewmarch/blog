from urllib.parse import urlencode

GOOGLE_FONTS_BASE_URL = 'https://fonts.googleapis.com/css'

GOOGLE_FONTS_URL = GOOGLE_FONTS_BASE_URL + '?' + urlencode({
    'display': 'block',
    'family': 'Material Icons Round',
})

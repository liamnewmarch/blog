import json
from pathlib import Path

from django.conf import settings

static_bundles = {}
try:
    with open(settings.BASE_DIR / 'static' / 'meta.json', 'r') as f:
        for key in json.load(f).get('outputs', {}).keys():
            path = settings.BASE_DIR / key
            static_bundles[path.suffix[1:]] = Path(*path.parts[-2:])
except FileNotFoundError:
    pass


def globals(request):
    return {
        'debug': settings.DEBUG,
        'css_bundle': static_bundles.get('css', 'dist/bundle.css'),
        'js_bundle': static_bundles.get('js', 'dist/bundle.js'),
        'google_cloud_project': settings.GOOGLE_CLOUD_PROJECT,
        'google_fonts_url': settings.GOOGLE_FONTS_URL,
        'stackdriver_api_key': settings.STACKDRIVER_API_KEY,
    }

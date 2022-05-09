import datetime

from django.http.response import JsonResponse


def _get_timestamp():
    return datetime.datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')


def healthcheck(request):
    return JsonResponse({
        'status': 'success',
        'timestamp': _get_timestamp(),
    })

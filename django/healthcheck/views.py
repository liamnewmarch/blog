from django.http.response import HttpResponse


def healthcheck(request):
    return HttpResponse(status=204)

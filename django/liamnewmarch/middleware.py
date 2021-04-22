from django.http import HttpResponseRedirect


class CanonicalHostRedirectMiddleware:
    """Redirect selected block-listed hosts to the canonical URL."""

    CANONICAL_BASE_URL = 'https://liam.nwmr.ch'

    REDIRECT_HOSTS = (
        'nwmr.ch',
        'www.nwmr.ch',
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.META['HTTP_HOST']

        if host in self.REDIRECT_HOSTS:
            return HttpResponseRedirect(self.CANONICAL_BASE_URL + request.path)

        return self.get_response(request)

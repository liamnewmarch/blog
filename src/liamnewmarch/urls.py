from django.contrib import admin, auth
from django.urls import include, path

# Disable admin models which aren’t supported on the datastore.
for model in (auth.models.Group, auth.models.User):
    if admin.site.is_registered(model):
        admin.site.unregister(model)

urlpatterns = (
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('csp/', include('cspreports.urls')),
    path('healthcheck/', include('healthcheck.urls')),
    path('posts/', include('blog.urls')),
)

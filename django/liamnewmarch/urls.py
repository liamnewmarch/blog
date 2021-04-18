from django.contrib import admin, auth
from django.urls import include, path

# Disable admin models which aren’t supported on the datastore.
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)

urlpatterns = (
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('posts/', include('blog.urls')),
)

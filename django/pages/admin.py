from django.contrib import admin

from .models import Home


class LimitInstancesModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        """Prevent adding more than one instance."""
        if self.model.objects.count() >= getattr(self, 'limit_instances', 0):
            return False

        return super().has_add_permission(*args, **kwargs)


@admin.register(Home)
class HomeAdmin(LimitInstancesModelAdmin):
    limit_instances = 1
    sortable_by = ()

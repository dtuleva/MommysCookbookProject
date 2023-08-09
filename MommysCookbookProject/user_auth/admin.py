from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
import django.contrib.auth.forms as auth_forms

from MommysCookbookProject.user_auth.models import CookbookUser

UserModel = get_user_model()

class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)  # Unregister the default Group model
admin.site.register(Group, GroupAdmin)

# Create the custom groups
superuser_admin_group, created = Group.objects.get_or_create(name='Superuser Admin')
content_editor_group, created = Group.objects.get_or_create(name='Content Editor')


def assign_permissions_to_groups():
    superuser_admin_permissions = Permission.objects.all()
    superuser_admin_group.permissions.set(superuser_admin_permissions)

    content_editor_permissions = Permission.objects.filter(codename__in=[
        "add_favorite",
        "change_favorite",
        "delete_favorite",
        "view_favorite",
        "add_note",
        "change_note",
        "delete_note",
        "view_note",
        "add_rating",
        "change_rating",
        "delete_rating",
        "view_rating",
        "add_recipe",
        "change_recipe",
        "delete_recipe",
        "view_recipe",
    ])
    content_editor_group.permissions.set(content_editor_permissions)


assign_permissions_to_groups()


class CookbookUserAdmin(UserAdmin):
    form = auth_forms.UserChangeForm
    list_display = ("username", "email", "screen_name", "date_joined", "get_groups_display", "is_staff")
    search_fields = ("username", "email", "screen_name")
    list_filter = ("date_joined", "is_staff")
    readonly_fields = ("username", "email", "screen_name", "date_joined", "password")

    def get_groups_display(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    get_groups_display.short_description = "Groups"
    def has_module_permission(self, request):
        if request.user.groups.filter(name='Content Editor').exists():
            return False
        return super().has_module_permission(request)


admin.site.register(CookbookUser, CookbookUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.models import Category, Blog, Tag, Comment, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from csvexport.actions import csvexport

class MyModelAdmin(admin.ModelAdmin):
    ...
    actions = [csvexport]
class UserProfileInline(admin.StackedInline):
    can_delete = False
    verbose_name_plural = 'Profile'

class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# Unregister the old UserAdmin
admin.site.unregister(User)

# Register the new UserAdmin
admin.site.register(User, CustomUserAdmin)

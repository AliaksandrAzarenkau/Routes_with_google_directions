from django.contrib import admin

from registration import models


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email'
    )


admin.site.register(models.User, UserAdmin)

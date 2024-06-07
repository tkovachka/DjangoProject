from django.contrib import admin

from phonesApp.models import Phone, Manufacturer


# Register your models here.
class PhoneAdminInline(admin.TabularInline):
    model = Phone
    extra = 1


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)
    inlines = [PhoneAdminInline, ]

    def has_add_permission(self, request):
        return request.user.is_superuser


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'year',)
    list_filter = ('manufacturer', 'year', 'isNew',)
    exclude = ('user',)

    fieldsets = [
        ('General', {'fields': ('manufacturer', 'model',)}),
        ('Details', {'fields': ('year', 'image', 'price', 'isNew', 'type',)}),
    ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(PhoneAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user


admin.site.register(Phone, PhoneAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)

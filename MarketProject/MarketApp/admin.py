from django.contrib import admin
from django.core.exceptions import PermissionDenied

from MarketApp.models import Employee, Market, ProductInMarket, Product


# Register your models here.
class ProductInMarketInline(admin.TabularInline):
    model = ProductInMarket
    extra = 0

class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [ProductInMarketInline]
    exclude = ('user',)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

class EmployeeAdmin(admin.ModelAdmin):
    exclude = ('user',)
    list_display = ('name', 'surname', )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        elif  obj.user != request.user:
            raise PermissionDenied("You cannot make changes")
        obj.save()

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.user:
            return True
        return False

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('type', 'local_product')

admin.site.register(Market, MarketAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Product, ProductAdmin)
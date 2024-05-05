from django.contrib import admin

from app.core.models import PrimaryItem, BevItem, FoodItem, CutleryItem, FoodId, Advertisement

admin.site.register(PrimaryItem)
admin.site.register(BevItem)
admin.site.register(CutleryItem)
admin.site.register(FoodId)
admin.site.register(Advertisement)


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    model = FoodItem
    extra = 0

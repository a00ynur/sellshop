from django.contrib import admin
from product import models
# Register your models here.

admin.site.register(models.Product)
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Size)
admin.site.register(models.Color)
admin.site.register(models.ProductImage)
admin.site.register(models.ProductVersion)
admin.site.register(models.ProductReview)
admin.site.register(models.Discount)
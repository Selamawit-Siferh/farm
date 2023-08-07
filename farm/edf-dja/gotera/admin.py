from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.UserTable)
admin.site.register(models.UserCartedProduct)
admin.site.register(models.AboutUs)
admin.site.register(models.BillingInformation)
admin.site.register(models.CheckoutProducts)
admin.site.register(models.GoteraCheckoutProducts)
admin.site.register(models.GoteraSubscriberTable)
admin.site.register(models.GoteraUserCartedProduct)
admin.site.register(models.ProductTable)
admin.site.register(models.UserBoughtProduct)
admin.site.register(models.GoteraUserBoughtProduct)



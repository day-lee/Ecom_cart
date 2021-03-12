from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

admin.site.register(Tutorial)
admin.site.register(Tag)
admin.site.register(Curriculum)
admin.site.register(CurriculumItem)
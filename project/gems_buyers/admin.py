from django.contrib import admin

from .models import Customer, Deal, Gem, Customers_Gems


class Customers_GemsTerm(admin.StackedInline):
    model = Customers_Gems
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = (
            'username',
            'spent_money',
            )

    inlines = (Customers_GemsTerm, )

    
 


admin.site.register(Deal)
admin.site.register(Gem)

from django.contrib import admin
from .models import Country

# Register your models here.
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

class CountryFilteredAdmin(admin.ModelAdmin):
    change_list_template = 'admin/country_filtered_change_list.html'  # Custom template

    def get_urls(self):
        """
        Override get_urls to include our custom view for country filtering.
        """
        urls = super().get_urls()
        custom_urls = [
            path('filter_by_country/', self.admin_site.admin_view(self.filter_by_country), name="filter_by_country"),
        ]
        return custom_urls + urls

    def filter_by_country(self, request):
        """
        This view will handle the logic for filtering the admin tables by country.
        """
        country = request.GET.get('country', 'all')  # Get the selected country from the URL
        # products = Product.objects.all()
        # orders = Order.objects.all()

        # if country != 'all':
        #     products = products.filter(country=country)
        #     orders = orders.filter(country=country)

        # Pass the filtered tables to the template
        context = {
            # 'products': products,
            # 'orders': orders,
            'selected_country': country,
        }
        return render(request, 'admin/country_filtered_change_list.html', context)

# Register the custom admin
# admin.site.register(Product, CountryFilteredAdmin)
# admin.site.register(Order, CountryFilteredAdmin)


admin.site.register(Country)

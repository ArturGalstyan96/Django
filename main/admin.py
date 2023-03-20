from django.contrib import admin
from .models import Tour, About, Contact
# Register your models here.
admin.site.register(Tour)
admin.site.register(About)




@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_display = ['id', 'userName', 'userEmail']
    list_display_links = ['id', 'userName']
    search_fields = ['id', 'userName', 'userPhone']
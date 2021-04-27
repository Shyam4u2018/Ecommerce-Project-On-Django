from django.contrib import admin
from .models import Setting, ContactMessage, FAQ,UserProfile
# Register your models here.
admin.site.register(Setting)

admin.site.register(ContactMessage)


class FAQamin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'status', 'created_at', 'updated_at']



class UserProfileAdmin(admin.ModelAdmin):
	list_display=['user','country','image_tag']
	list_filter=['user',]

admin.site.register(UserProfile,UserProfileAdmin)

admin.site.register(FAQ, FAQamin)

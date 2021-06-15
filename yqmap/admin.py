from django.contrib import admin
from yqmap.models import NewsPost,User,City
# Register your models here.

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']
    list_per_page = 50
    # ordering = ('-created_time',)
    list_display_links = ('title',)
    # exclude = ('url',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'ways', 'days')
    list_per_page = 50
    # ordering = ('-created_time',)
    list_display_links = ('days',)
    # exclude = ('url',)

@admin.register(City)
class CityrAdmin(admin.ModelAdmin):
    list_display = ('city', 'nums')
    list_per_page = 50
    # ordering = ('-created_time',)
    list_display_links = ('city',)
    # exclude = ('url',)
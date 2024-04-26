from django.contrib import admin
from .models import AboutModel, ServicesModel, PortfolioModel, TeamModel, BlogModel, ContactModel, AwardsModel, CounterModel, CategoryModel


class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name', 'description')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')
    search_fields = ('title', 'description')


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'image', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('category', 'status', 'created_at', 'updated_at')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'description', 'image', 'facebook', 'twitter', 'linkedin', 'instagram')
    search_fields = ('name', 'position', 'description')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)


class AwardsAdmin(admin.ModelAdmin):
    list_display = ('name_of_award', 'description', 'certificate')
    search_fields = ('name_of_award', 'description')


class CounterAdmin(admin.ModelAdmin):
    list_display = ('works', 'clients')
    search_fields = ('works', 'clients')


admin.site.register(AboutModel, AboutAdmin)
admin.site.register(ServicesModel, ServicesAdmin)
admin.site.register(PortfolioModel, PortfolioAdmin)
admin.site.register(TeamModel, TeamAdmin)
admin.site.register(BlogModel, BlogAdmin)
admin.site.register(ContactModel, ContactAdmin)
admin.site.register(AwardsModel, AwardsAdmin)
admin.site.register(CounterModel, CounterAdmin)
admin.site.register(CategoryModel)

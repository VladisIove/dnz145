import datetime

from django.contrib import admin

from .models import Post, Topic, File

class MixinActive(object):

    def deactivate(self, request, queryset):
        queryset.update(active=False) 
    deactivate.short_description = 'Скрыть'
    
    def activate(self, request, queryset):
        queryset.update(active=True)
    activate.short_description = 'Показать'




class PostInline(admin.TabularInline):
    model = Post
    min_num = 0

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        if obj:
            return obj.posts.count() -1 
        return extra

class FileInline(admin.TabularInline):
    model = File
    min_num = 0

    def get_extra(self, request, obj=None, **kwargs):
        extra = 0
        if obj:
            return obj.files.count() -1 
        return extra
        
class PostAdmin(admin.ModelAdmin, MixinActive):
    actions = ['deactivate','activate'] 
    search_fields = ['name']
    list_display = ['name','topic', 'active', 'last_update']
    ordering = ['last_update']
    list_filter = ('active','last_update', 'topic__name')
    list_editable = ['active','topic']
    fields = (('name','slug', 'active', 'topic'), 'text')
    inlines = [
        FileInline,
    ]
    prepopulated_fields = {"slug": ("name",)}


class TopicAdmin(admin.ModelAdmin, MixinActive):
    actions = ['deactivate','activate']
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    list_display = ['name', 'active']
    ordering = ['id']
    list_filter = ['active']
    list_editable = ['active']
    inlines = [
        PostInline,
    ]
    

class FileAdmin(admin.ModelAdmin, MixinActive):
    actions = ['deactivate','activate']
    search_fields = ['name','post']
    list_display = ['name', 'post', 'active']
    ordering = ['id']
    list_filter = ['active']
    list_editable = ['active']

admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(File, FileAdmin)
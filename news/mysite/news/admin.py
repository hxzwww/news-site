from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'views', 'get_photo']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_editable = ['is_published',]
    list_filter = ['is_published', 'category']
    fields = ['title', 'content', 'category', 'created_at', 'updated_at', 'is_published', 'views', 'photo', 'get_photo']
    readonly_fields = ['created_at', 'updated_at', 'views', 'get_photo']
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="150">')
        else:
            return '-'

    get_photo.short_description = 'photo'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title',]


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

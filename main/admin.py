from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import (
    Hero, Event, Banner, News, Resource, ResearchProject,
    Recommendation, Journal, ExpertOpinion, Achievement,
    MenuItem, SiteSettings, AboutPage, Charter, Management,
    Department, ScientificCouncil, YoungScientist
)
from .translation import *  # Импортируем все из translation.py
from modeltranslation.admin import TranslationAdmin

class AboutUsMixin:
    def get_app_label(self):
        return "О нас"

@admin.register(MenuItem)
class MenuItemAdmin(TranslationAdmin):
    list_display = ('title', 'url', 'parent', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active', 'parent')
    search_fields = ('title', 'url')
    ordering = ('order',)

@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    fieldsets = (
        (_('General'), {
            'fields': ('logo', 'site_name'),
        }),
        (_('Footer Information'), {
            'fields': ('footer_text', 'footer_email', 'footer_phone', 'footer_address', 'copyright_text'),
        }),
    )
    
    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" height="50" />', obj.logo.url)
        return format_html('<span class="errors">No logo</span>')
    display_logo.short_description = _('Logo Preview')
    display_logo.allow_tags = True

    def has_add_permission(self, request):
        # Запрещаем создание новых объектов, если уже есть один
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление настроек
        return False

    class Media:
        css = {
            'screen': (
                'modeltranslation/css/tabbed_translation_fields.css',
                'https://code.jquery.com/ui/1.13.2/themes/base/jquery-ui.css',
            ),
        }
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'https://code.jquery.com/ui/1.13.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )

@admin.register(Hero)
class HeroAdmin(TranslationAdmin):
    list_display = ('id', 'display_image', 'is_active', 'order')
    list_editable = ('is_active', 'order')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ''
    display_image.short_description = 'Image'

@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ('title', 'display_image', 'date', 'is_active', 'created_at')
    list_editable = ('is_active',)
    search_fields = ('title',)
    list_filter = ('date', 'is_active')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ''
    display_image.short_description = 'Image'

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ('title', 'display_image', 'url', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('title',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ''
    display_image.short_description = 'Image'

@admin.register(News)
class NewsAdmin(AboutUsMixin, TranslationAdmin):
    list_display = ('title', 'display_image', 'is_featured', 'created_at')
    list_editable = ('is_featured',)
    search_fields = ('title', 'preview', 'content')
    list_filter = ('is_featured', 'created_at')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ''
    display_image.short_description = 'Изображение'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

@admin.register(Resource)
class ResourceAdmin(TranslationAdmin):
    list_display = ('title', 'display_image', 'url', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ''
    display_image.short_description = 'Image'

@admin.register(ResearchProject)
class ResearchProjectAdmin(TranslationAdmin):
    list_display = ('title', 'display_image', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ''
    display_image.short_description = 'Image'

@admin.register(Recommendation)
class RecommendationAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'content', 'author')
    list_editable = ('is_active',)
    fieldsets = (
        (_('Content'), {
            'fields': ('title', 'content', 'author', 'file')
        }),
        (_('Settings'), {
            'fields': ('is_active',)
        }),
    )

@admin.register(Journal)
class JournalAdmin(TranslationAdmin):
    list_display = ('url', 'is_active')
    list_editable = ('is_active',)

@admin.register(ExpertOpinion)
class ExpertOpinionAdmin(TranslationAdmin):
    list_display = ['title', 'url', 'publication_date', 'is_active']
    list_filter = ['publication_date', 'is_active']
    search_fields = ['title', 'description', 'url']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Achievement)
class AchievementAdmin(TranslationAdmin):
    list_display = ('title', 'value', 'icon', 'order')
    list_editable = ('order',)
    search_fields = ('title',)

@admin.register(AboutPage)
class AboutPageAdmin(AboutUsMixin, TranslationAdmin):
    fieldsets = (
        (_('Содержание'), {
            'fields': ('title', 'content', 'is_active'),
        }),
    )
    list_display = ('title', 'is_active', 'updated_at')
    list_editable = ('is_active',)

    class Meta:
        verbose_name = 'Общая информация'
        verbose_name_plural = 'Общая информация'

@admin.register(Charter)
class CharterAdmin(AboutUsMixin, TranslationAdmin):
    fieldsets = (
        (_('Содержание'), {
            'fields': ('title', 'content'),
        }),
        (_('Документ'), {
            'fields': ('file',),
            'description': _('Загрузить PDF документ')
        }),
        (_('Настройки'), {
            'fields': ('is_active',),
        }),
    )
    list_display = ('title', 'has_file', 'is_active', 'updated_at')
    list_editable = ('is_active',)
    
    def has_file(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank"><i class="fas fa-file-pdf"></i> {}</a>', 
                             obj.file.url, _('Просмотр PDF'))
        return format_html('<i class="fas fa-times text-danger"></i>')
    has_file.short_description = _('PDF Документ')
    has_file.allow_tags = True

    class Meta:
        verbose_name = 'Устав'
        verbose_name_plural = 'Устав'

@admin.register(Management)
class ManagementAdmin(AboutUsMixin, TranslationAdmin):
    fieldsets = (
        (_('Личная информация'), {
            'fields': ('name', 'position', 'photo', 'bio'),
        }),
        (_('Контактная информация'), {
            'fields': ('email', 'phone'),
        }),
        (_('Настройки'), {
            'fields': ('order', 'is_active'),
        }),
    )
    list_display = ('display_photo', 'name', 'position', 'email', 'phone', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('display_photo', 'name')
    search_fields = ('name', 'position', 'email', 'phone')
    ordering = ('order',)

    def display_photo(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', 
                obj.photo.url
            )
        return format_html('<i class="fas fa-user" style="font-size: 24px;"></i>')
    display_photo.short_description = _('Фото')

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'

@admin.register(Department)
class DepartmentAdmin(AboutUsMixin, TranslationAdmin):
    fieldsets = (
        (_('Информация об отделе'), {
            'fields': ('title', 'description', 'head'),
        }),
        (_('Контактная информация'), {
            'fields': ('email', 'phone'),
        }),
        (_('Настройки'), {
            'fields': ('order', 'is_active'),
        }),
    )
    list_display = ('title', 'head', 'email', 'phone', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title', 'head', 'email', 'phone')
    ordering = ('order',)

    class Meta:
        verbose_name = 'Структура института'
        verbose_name_plural = 'Структура института'

@admin.register(ScientificCouncil)
class ScientificCouncilAdmin(AboutUsMixin, TranslationAdmin):
    fieldsets = (
        (_('Содержание'), {
            'fields': ('title', 'content'),
        }),
        (_('Документ'), {
            'fields': ('file',),
            'description': _('Загрузить PDF документ')
        }),
        (_('Настройки'), {
            'fields': ('is_active',),
        }),
    )
    list_display = ('title', 'has_file', 'is_active', 'updated_at')
    list_editable = ('is_active',)
    
    def has_file(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank"><i class="fas fa-file-pdf"></i> {}</a>', 
                             obj.file.url, _('Просмотр PDF'))
        return format_html('<i class="fas fa-times text-danger"></i>')
    has_file.short_description = _('PDF Документ')
    has_file.allow_tags = True

    class Meta:
        verbose_name = 'Ученый совет'
        verbose_name_plural = 'Ученый совет'

@admin.register(YoungScientist)
class YoungScientistAdmin(AboutUsMixin, TranslationAdmin):
    fieldsets = (
        (_('Личная информация'), {
            'fields': ('name', 'photo', 'degree', 'admission_year', 'research_topics', 'bio'),
        }),
        (_('Контактная информация'), {
            'fields': ('email',),
        }),
        (_('Настройки'), {
            'fields': ('order', 'is_active'),
        }),
    )
    list_display = ('display_photo', 'name', 'degree', 'admission_year', 'email', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('display_photo', 'name')
    search_fields = ('name', 'degree', 'research_topics', 'email')
    list_filter = ('degree', 'admission_year', 'is_active')
    ordering = ('order', 'name')

    def display_photo(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', 
                obj.photo.url
            )
        return format_html('<i class="fas fa-user" style="font-size: 24px;"></i>')
    display_photo.short_description = _('Фото')

    class Meta:
        verbose_name = 'Молодые ученые'
        verbose_name_plural = 'Молодые ученые'

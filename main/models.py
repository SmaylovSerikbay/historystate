from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        abstract = True

class Hero(TimeStampedModel):
    image = models.ImageField(upload_to='hero/', verbose_name=_('Image'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Hero')
        verbose_name_plural = _('Heroes')
        ordering = ['order']

    def __str__(self):
        return f"Hero {self.id}"

class Event(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='events/', verbose_name=_('Image'))
    date = models.DateField(verbose_name=_('Date'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ['-date']

    def __str__(self):
        return self.title

class Banner(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    image = models.ImageField(upload_to='banners/', verbose_name=_('Image'))
    url = models.URLField(verbose_name=_('URL'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')
        ordering = ['order']

    def __str__(self):
        return self.title

class News(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    preview = models.TextField(verbose_name=_('Preview'))
    content = RichTextUploadingField(verbose_name=_('Content'))
    image = models.ImageField(upload_to='news/', verbose_name=_('Image'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Is featured'))

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Resource(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    image = models.ImageField(upload_to='resources/', verbose_name=_('Image'))
    url = models.URLField(verbose_name=_('URL'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')
        ordering = ['order']

    def __str__(self):
        return self.title

class ResearchProject(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = RichTextUploadingField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='projects/', verbose_name=_('Image'))
    status = models.CharField(max_length=50, choices=[
        ('ongoing', _('Ongoing')),
        ('completed', _('Completed'))
    ], verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Research Project')
        verbose_name_plural = _('Research Projects')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Recommendation(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    content = RichTextUploadingField(verbose_name=_('Content'))
    file = models.FileField(upload_to='recommendations/', verbose_name=_('File'), blank=True, null=True)
    author = models.CharField(max_length=255, verbose_name=_('Author'), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Recommendation')
        verbose_name_plural = _('Recommendations')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Journal(TimeStampedModel):
    url = models.URLField(verbose_name=_('URL'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Journal')
        verbose_name_plural = _('Journals')

    def __str__(self):
        return self.url

class ExpertOpinion(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    photo = models.ImageField(upload_to='experts/', verbose_name=_('Photo'), blank=True, null=True)
    publication_date = models.DateField(verbose_name=_('Publication Date'), blank=True, null=True)
    url = models.URLField(verbose_name=_('URL'), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Expert Opinion')
        verbose_name_plural = _('Expert Opinions')
        ordering = ['-publication_date']

    def __str__(self):
        return self.title or str(self.id)

class Achievement(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    value = models.PositiveIntegerField(verbose_name=_('Value'))
    icon = models.CharField(max_length=50, verbose_name=_('Icon Class'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Achievement')
        verbose_name_plural = _('Achievements')
        ordering = ['order']

    def __str__(self):
        return self.title

class MenuItem(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    url = models.CharField(max_length=255, verbose_name=_('URL'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name=_('Parent Menu'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')
        ordering = ['order']

    def __str__(self):
        return self.title

class SiteSettings(TimeStampedModel):
    """Модель для хранения настроек сайта"""
    logo = models.ImageField(upload_to='site/', verbose_name=_('Logo'), blank=True, null=True)
    site_name = models.CharField(max_length=255, verbose_name=_('Site Name'))
    footer_text = models.TextField(verbose_name=_('Footer Text'), blank=True)
    footer_email = models.EmailField(verbose_name=_('Footer Email'), blank=True)
    footer_phone = models.CharField(max_length=50, verbose_name=_('Footer Phone'), blank=True)
    footer_address = models.TextField(verbose_name=_('Footer Address'), blank=True)
    copyright_text = models.CharField(max_length=255, verbose_name=_('Copyright Text'), 
                                   default=_('All rights reserved'))

    class Meta:
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')

    def __str__(self):
        return str(_('Site Settings'))

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            return # Предотвращаем создание нескольких экземпляров
        return super().save(*args, **kwargs)

class AboutPage(TimeStampedModel):
    """Модель для страницы 'О нас'"""
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    content = RichTextUploadingField(verbose_name=_('Content'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('About Page')
        verbose_name_plural = _('About Page')

    def __str__(self):
        return self.title

class Charter(TimeStampedModel):
    """Модель для страницы 'Устав'"""
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    content = RichTextUploadingField(verbose_name=_('Content'))
    file = models.FileField(upload_to='charter/', verbose_name=_('PDF File'), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Charter')
        verbose_name_plural = _('Charter')

    def __str__(self):
        return self.title

class Management(TimeStampedModel):
    """Модель для раздела 'Руководство'"""
    name = models.CharField(max_length=255, verbose_name=_('Full Name'))
    position = models.CharField(max_length=255, verbose_name=_('Position'))
    bio = RichTextUploadingField(verbose_name=_('Biography'))
    photo = models.ImageField(upload_to='management/', verbose_name=_('Photo'), blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), blank=True)
    phone = models.CharField(max_length=50, verbose_name=_('Phone'), blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Management')
        verbose_name_plural = _('Management')
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.position}"

class Department(TimeStampedModel):
    """Модель для раздела 'Структура института'"""
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = RichTextUploadingField(verbose_name=_('Description'))
    head = models.CharField(max_length=255, verbose_name=_('Head of Department'))
    email = models.EmailField(verbose_name=_('Email'), blank=True)
    phone = models.CharField(max_length=50, verbose_name=_('Phone'), blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['order']

    def __str__(self):
        return self.title

class ScientificCouncil(TimeStampedModel):
    """Модель для раздела 'Ученый совет'"""
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    content = RichTextUploadingField(verbose_name=_('Content'))
    file = models.FileField(upload_to='scientific_council/', verbose_name=_('PDF File'), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Scientific Council')
        verbose_name_plural = _('Scientific Council')

    def __str__(self):
        return self.title

class YoungScientist(TimeStampedModel):
    """Модель для раздела 'Молодые ученые'"""
    name = models.CharField(max_length=255, verbose_name=_('Full Name'))
    photo = models.ImageField(upload_to='young_scientists/', verbose_name=_('Photo'))
    degree = models.CharField(max_length=255, verbose_name=_('Academic Degree'))
    admission_year = models.IntegerField(verbose_name=_('Year of Admission'))
    research_topics = models.TextField(verbose_name=_('Research Topics'))
    bio = RichTextUploadingField(verbose_name=_('Biography'), blank=True)
    email = models.EmailField(verbose_name=_('Email'), blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    class Meta:
        verbose_name = _('Young Scientist')
        verbose_name_plural = _('Young Scientists')
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.degree}"

class ScientificLibrary(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    author = models.CharField(max_length=255, verbose_name=_('Author'))
    publication_date = models.DateField(verbose_name=_('Publication Date'))
    image = models.ImageField(upload_to='library/covers/', verbose_name=_('Cover Image'))
    file = models.FileField(upload_to='library/files/', verbose_name=_('PDF File'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    order = models.IntegerField(default=0, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Scientific Library')
        verbose_name_plural = _('Scientific Library')
        ordering = ['order', '-publication_date']

    def __str__(self):
        return self.title

class DigitalLink(TimeStampedModel):
    """Модель для внешних цифровых ресурсов"""
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    url = models.URLField(verbose_name=_('URL'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Digital Link')
        verbose_name_plural = _('Digital Links')
        ordering = ['order']

    def __str__(self):
        return self.title

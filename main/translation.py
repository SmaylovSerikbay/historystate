from modeltranslation.translator import register, TranslationOptions
from django.utils.translation import gettext_lazy as _
from .models import (
    Hero, Event, Banner, News, Resource, ResearchProject,
    Recommendation, Journal, ExpertOpinion, Achievement,
    MenuItem, SiteSettings, AboutPage, Charter, Management, Department, ScientificCouncil, YoungScientist, ScientificLibrary
)

@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kk', 'en')

@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_name', 'footer_text', 'footer_address', 'copyright_text')
    required_languages = ('ru', 'kk', 'en')
    fallback_values = {'site_name': _('Institute of State History')}

@register(Hero)
class HeroTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('ru', 'kk', 'en')

@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ru', 'kk', 'en')

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kk', 'en')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'preview', 'content')
    required_languages = ('ru', 'kk', 'en')

@register(Resource)
class ResourceTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kk', 'en')

@register(ResearchProject)
class ResearchProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ru', 'kk', 'en')

@register(Recommendation)
class RecommendationTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('ru', 'kk', 'en')

@register(Journal)
class JournalTranslationOptions(TranslationOptions):
    fields = ()
    required_languages = ('ru', 'kk', 'en')

@register(ExpertOpinion)
class ExpertOpinionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('ru', 'kk', 'en')

@register(Achievement)
class AchievementTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('ru', 'kk', 'en')

@register(AboutPage)
class AboutPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('ru', 'kk', 'en')

@register(Charter)
class CharterTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('ru', 'kk', 'en')

@register(Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'bio')
    required_languages = ('ru', 'kk', 'en')

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'head')
    required_languages = ('ru', 'kk', 'en')

@register(ScientificCouncil)
class ScientificCouncilTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('ru', 'kk', 'en')

@register(YoungScientist)
class YoungScientistTranslationOptions(TranslationOptions):
    fields = ('name', 'degree', 'research_topics', 'bio')
    required_languages = ('ru', 'kk', 'en')

@register(ScientificLibrary)
class ScientificLibraryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'author')
    required_languages = ('ru', 'kk', 'en') 
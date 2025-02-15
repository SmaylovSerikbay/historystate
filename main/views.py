from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from .models import (
    Hero, Event, Banner, News, Resource, ResearchProject,
    Recommendation, Journal, ExpertOpinion, Achievement,
    AboutPage, Charter, Management, Department, ScientificCouncil, YoungScientist,
    SiteSettings, ScientificLibrary, DigitalLink
)
from django.urls import reverse

# Create your views here.

def get_common_context(request):
    """Функция для получения общего контекста"""
    return {
        'site_config': SiteSettings.objects.first(),
        'digital_links': DigitalLink.objects.filter(is_active=True).order_by('order'),
    }

class BaseContextMixin:
    """Миксин для добавления общего контекста"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_common_context(self.request))
        return context

class HomeView(BaseContextMixin, TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heroes'] = Hero.objects.filter(is_active=True).order_by('order')
        context['events'] = Event.objects.filter(is_active=True)[:3]
        context['achievements'] = Achievement.objects.all()
        # Получаем только последние 6 новостей, отсортированных по дате создания
        context['news'] = News.objects.order_by('-created_at')[:6]
        context['resources'] = Resource.objects.all()[:5]
        context['about_page'] = AboutPage.objects.filter(is_active=True).first()
        
        # Добавляем данные для секции "О нас"
        context['management_list'] = Management.objects.filter(is_active=True)
        context['department_list'] = Department.objects.filter(is_active=True)
        context['young_scientist_list'] = YoungScientist.objects.filter(is_active=True)
        context['research_projects'] = ResearchProject.objects.all()
        context['journals'] = Journal.objects.all()
        context['recommendations'] = Recommendation.objects.filter(is_active=True)
        
        return context

class AboutView(BaseContextMixin, TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_page'] = AboutPage.objects.filter(is_active=True).first()
        context['charters'] = Charter.objects.filter(is_active=True).all()
        context['management_list'] = Management.objects.filter(is_active=True).order_by('order')
        context['department_list'] = Department.objects.filter(is_active=True).order_by('order')
        context['councils'] = ScientificCouncil.objects.filter(is_active=True).all()
        context['young_scientist_list'] = YoungScientist.objects.filter(is_active=True).order_by('order')
        
        # Получаем уникальные значения для фильтров молодых ученых
        scientists = YoungScientist.objects.filter(is_active=True)
        context['degrees'] = list(scientists.values_list('degree', flat=True).distinct())
        context['admission_years'] = list(scientists.values_list('admission_year', flat=True).distinct())
        
        return context

class ResearchProjectListView(BaseContextMixin, ListView):
    model = ResearchProject
    template_name = 'main/research_project_list.html'
    context_object_name = 'projects'

class ResearchProjectDetailView(BaseContextMixin, DetailView):
    model = ResearchProject
    template_name = 'main/research_project_detail.html'
    context_object_name = 'project'

class RecommendationListView(BaseContextMixin, ListView):
    model = Recommendation
    template_name = 'main/recommendation_list.html'
    context_object_name = 'recommendations'

class JournalListView(BaseContextMixin, ListView):
    model = Journal
    template_name = 'main/journal_list.html'
    context_object_name = 'journals'

    def get_queryset(self):
        return Journal.objects.filter(is_active=True)
    
    def get(self, request, *args, **kwargs):
        # Получаем первый активный журнал
        first_journal = self.get_queryset().first()
        if first_journal:
            # Перенаправляем на URL журнала
            return redirect(first_journal.url)
        # Если нет активных журналов, показываем сообщение
        messages.warning(request, _('No active journals available.'))
        return redirect('home')

class JournalDetailView(BaseContextMixin, DetailView):
    model = Journal
    template_name = 'main/journal_detail.html'
    context_object_name = 'journal'

class ExpertOpinionListView(BaseContextMixin, ListView):
    model = ExpertOpinion
    template_name = 'main/expert_opinion_list.html'
    context_object_name = 'opinions'
    paginate_by = 9

    def get_queryset(self):
        return ExpertOpinion.objects.filter(is_active=True)

class ExpertOpinionDetailView(BaseContextMixin, DetailView):
    model = ExpertOpinion
    template_name = 'main/expert_opinion_detail.html'
    context_object_name = 'opinion'

class NewsListView(BaseContextMixin, ListView):
    model = News
    template_name = 'main/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 12

class NewsDetailView(BaseContextMixin, DetailView):
    model = News
    template_name = 'main/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_news = self.object
        
        # Получаем предыдущую и следующую новость
        context['previous_news'] = News.objects.filter(
            created_at__lt=current_news.created_at
        ).order_by('-created_at').first()
        
        context['next_news'] = News.objects.filter(
            created_at__gt=current_news.created_at
        ).order_by('created_at').first()
        
        return context

class EventListView(BaseContextMixin, ListView):
    model = Event
    template_name = 'main/event_list.html'
    context_object_name = 'events'
    paginate_by = 9

    def get_queryset(self):
        return Event.objects.filter(is_active=True).order_by('-date')

class EventDetailView(BaseContextMixin, DetailView):
    model = Event
    template_name = 'main/event_detail.html'
    context_object_name = 'event'

class ResourceListView(BaseContextMixin, ListView):
    model = Resource
    template_name = 'main/resource_list.html'
    context_object_name = 'resources'
    paginate_by = 12

    def get_queryset(self):
        return Resource.objects.all().order_by('order')

class ResourceDetailView(BaseContextMixin, DetailView):
    model = Resource
    template_name = 'main/resource_detail.html'
    context_object_name = 'resource'

class ContactView(BaseContextMixin, TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SearchView(BaseContextMixin, ListView):
    template_name = 'main/search_results.html'
    paginate_by = 20
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()
        if query:
            # Поиск по всем основным моделям
            news = News.objects.filter(
                Q(title__icontains=query) | 
                Q(preview__icontains=query) |
                Q(content__icontains=query)
            ).filter(is_featured=True)

            events = Event.objects.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query)
            ).filter(is_active=True)

            research_projects = ResearchProject.objects.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query)
            )

            recommendations = Recommendation.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(author__icontains=query)
            ).filter(is_active=True)

            expert_opinions = ExpertOpinion.objects.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query)
            ).filter(is_active=True)

            about_pages = AboutPage.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query)
            ).filter(is_active=True)

            management = Management.objects.filter(
                Q(name__icontains=query) | 
                Q(position__icontains=query) |
                Q(bio__icontains=query)
            ).filter(is_active=True)

            departments = Department.objects.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query) |
                Q(head__icontains=query)
            ).filter(is_active=True)

            young_scientists = YoungScientist.objects.filter(
                Q(name__icontains=query) | 
                Q(degree__icontains=query) |
                Q(research_topics__icontains=query) |
                Q(bio__icontains=query)
            ).filter(is_active=True)
            
            # Объединяем результаты
            results = []
            
            for item in news:
                results.append({
                    'title': item.title,
                    'description': item.preview,
                    'url': reverse('main:news_detail', args=[item.pk]),
                    'date': item.created_at,
                    'type': 'news',
                    'image': item.image.url if item.image else None
                })

            for item in events:
                results.append({
                    'title': item.title,
                    'description': item.description,
                    'url': reverse('main:event_detail', args=[item.pk]),
                    'date': item.created_at,
                    'type': 'event',
                    'image': item.image.url if item.image else None
                })

            for item in research_projects:
                results.append({
                    'title': item.title,
                    'description': item.description,
                    'url': reverse('main:research_project_detail', args=[item.pk]),
                    'date': item.created_at,
                    'type': 'research',
                    'image': item.image.url if item.image else None
                })

            for item in recommendations:
                results.append({
                    'title': item.title,
                    'description': item.content,
                    'url': reverse('main:recommendations'),
                    'date': item.created_at,
                    'type': 'recommendation'
                })

            for item in expert_opinions:
                results.append({
                    'title': item.title,
                    'description': item.description,
                    'url': item.url,
                    'date': item.created_at,
                    'type': 'expert_opinion',
                    'image': item.photo.url if item.photo else None
                })

            for item in about_pages:
                results.append({
                    'title': item.title,
                    'description': item.content,
                    'url': reverse('main:about'),
                    'date': item.created_at,
                    'type': 'about'
                })

            for item in management:
                results.append({
                    'title': item.name,
                    'description': item.bio,
                    'url': reverse('main:about'),
                    'date': item.created_at,
                    'type': 'management',
                    'image': item.photo.url if item.photo else None,
                    'position': item.position
                })

            for item in departments:
                results.append({
                    'title': item.title,
                    'description': item.description,
                    'url': reverse('main:about'),
                    'date': item.created_at,
                    'type': 'department',
                    'head': item.head
                })

            for item in young_scientists:
                results.append({
                    'title': item.name,
                    'description': item.research_topics,
                    'url': reverse('main:about'),
                    'date': item.created_at,
                    'type': 'young_scientist',
                    'image': item.photo.url if item.photo else None,
                    'degree': item.degree
                })
            
            # Сортируем по дате
            results.sort(key=lambda x: x['date'], reverse=True)
            return results
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class ScientificLibraryView(BaseContextMixin, ListView):
    model = ScientificLibrary
    template_name = 'main/scientific_library.html'
    context_object_name = 'library_items'

    def get_queryset(self):
        return ScientificLibrary.objects.filter(is_active=True).order_by('order', '-publication_date')

from django.urls import path
from .views import (
    HomeView, EventListView, EventDetailView, NewsListView, NewsDetailView,
    ResourceListView, ResourceDetailView, JournalListView, ExpertOpinionListView,
    AboutView, ContactView, ResearchProjectListView, ResearchProjectDetailView,
    RecommendationListView, SearchView, ScientificLibraryView, EHistoryView, ArchiveView
)

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('resources/', ResourceListView.as_view(), name='resource_list'),
    path('resources/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    path('journals/', JournalListView.as_view(), name='journals'),
    path('expert-opinions/', ExpertOpinionListView.as_view(), name='expert_opinions'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('research/projects/', ResearchProjectListView.as_view(), name='research_projects'),
    path('research/projects/<int:pk>/', ResearchProjectDetailView.as_view(), name='research_project_detail'),
    path('research/recommendations/', RecommendationListView.as_view(), name='recommendations'),
    path('scientific-library/', ScientificLibraryView.as_view(), name='scientific_library'),
    path('ehistory/', EHistoryView.as_view(), name='ehistory'),
    path('archive/', ArchiveView.as_view(), name='archive'),
] 
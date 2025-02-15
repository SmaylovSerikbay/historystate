from .models import MenuItem, SiteSettings

def global_context(request):
    """Добавляет глобальные данные во все шаблоны."""
    return {
        'menu_items': MenuItem.objects.filter(parent=None, is_active=True).prefetch_related('children'),
        'site_config': SiteSettings.objects.first(),
    } 
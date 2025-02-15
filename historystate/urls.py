from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('gallery/', include('gallery.urls')),
    path('accounts/', include('accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    prefix_default_language=False,
) 
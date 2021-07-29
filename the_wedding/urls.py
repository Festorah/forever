from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users.views import my_wedding_website


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('dcn/', include('dcn.urls')),
    path('', include('home.urls')),
    path('dashboard/', include('users.urls')),
    path('store/', include('store.urls')),
    path('templates/', include('designs.urls')),
    path('<slug:slug>/', my_wedding_website, name='my-wedding-website'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

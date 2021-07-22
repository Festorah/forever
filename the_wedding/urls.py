
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('dcn/', include('dcn.urls')),
    path('', include('home.urls')),
    path('dashboard/', include('users.urls')),
    path('store/', include('store.urls')),

]

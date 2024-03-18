from django.contrib import admin
from django.urls import path, include
from nato import views as nato_views  # Импортируем представления из приложения nato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', nato_views.index, name='index'),  # URL-адрес для главной страницы
    path('nato/', include('nato.urls')),
    path('', include('nato.urls')), 
      
        # Подключаем URL-адреса из приложения nato
    
] 

from django.conf import settings
from django.conf.urls.static import static

# Ваши URL-шаблоны здесь

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from upload import views  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file, name='upload_file'), 
    path('view/', views.view_files, name='view_files'),     
    path('', views.upload_file, name='home'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  

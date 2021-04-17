from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('formpostapi/', views.formListCreate.as_view()),
    path('formpostapi/<int:pk>/', views.formListCreate.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
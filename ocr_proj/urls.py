"""
URL configuration for ocr_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static
from Image_analysis.views import ocr_image, ocr_editor, auth
from Image_analysis.save_data import save_data
from Image_analysis.get_data import get_data

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/ocr/')),
    path('ocr/', ocr_image, name="ocr_image"),
    path('api/ocr/', ocr_image, name="ocr_api"),
    path('ocr-editor/', ocr_editor, name="ocr_editor"),
    path('auth/', auth, name='auth_user'),
    path('api/save-data/', save_data, name='save_data'),
    path('api/get-data/<str:user_id>/', get_data, name='get_data'), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
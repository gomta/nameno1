"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path,include
from SlideShow.views import change_lang ,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('change_lang/',change_lang,name="change_lang"),
    path('', include('social_django.urls', namespace='social')),
    path('logout/',logout_view,name="logout"),

]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('SlideShow.urls')),
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

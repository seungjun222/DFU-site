"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.stdisplay,name="stdisplay"),
    path('create',views.stinsert,name="stinsert"),
    path('Edit/<int:id>',views.stedit, name='stedit'),
    path('Update/<int:id>',views.stupdate, name='stupdate'),
    path('Delete/<int:id>',views.stdelete, name='stdelete'),
    path('Delete2/<int:id>',views.stdelete2, name='stdelete2'),
    path('register/',views.register, name="register"),
    path('final', views.stfinal, name="stfinal"),
    path('login',views.stlogin,name="stlogin"),
    path('',include('django.contrib.auth.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
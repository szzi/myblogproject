"""myblogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
import myblog.views
import portfolio.views
from django.conf import settings #settings의 media를 쓰기위함
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myblog.views.home, name="home"),
    path('blog/',include('myblog.urls')),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    # path('blog/<int:blog_id>',myblog.views.detail, name="detail"),
    # path('blog/new/', myblog.views.new, name="new"),
    # path('blog/create', myblog.views.create, name="create"),
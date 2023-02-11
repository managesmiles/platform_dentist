"""gentella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# # from django.conf.urls import url, include
# from django.urls import re_path as url
# from django.urls import include
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url('', include('app_users.urls')),
#     # app/ -> Genetelella UI and resources
#     url(r'^app/', include('app.urls')),
#     url(r'^', include('app.urls')),
# ]

from django.contrib import admin
from app import views
from app_users import views as views_users
from django.urls import path, re_path 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('', views_users.index_test, name="index_test"),
    
    path('admin/', admin.site.urls),
    path('', views_users.index, name="home_users"),
    re_path(r'^.*\.html', views.gentella_html, name='home_dentist',)
    # path('', views.index, name='home_dentist'),
]


# from django.conf import settings
# from django.conf.urls.static import static

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()


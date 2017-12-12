
"""test_restframework_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

from django.conf.urls import (url, include)
from django.contrib import admin
from newsnippets import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('snippets.urls')),
    url(r'^new/', include('newsnippets.urls')),
    url(r'^new3/', include('snippet3.urls')),
    url(r'^$', views.api_root),
]

# login button will be viewed on the page /api-auth/
# open /api-auth/ page to login ;
# user can create snippet until login successfully
# /api-auth/ redirect /account/profile/

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
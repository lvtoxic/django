"""mxonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from organization.views import OrgView

from django.conf.urls.static import static
from django.conf import settings

import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # TemplateView.as_view可以将template转换为view
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    # namespace使我们将应用users中的URL和其他应用中的URL区分开来，以防止多个应用中URL相同的情况
    path('', include('users.urls', namespace="users")),
    path('captcha/', include('captcha.urls')),
    path('org_list', OrgView.as_view(), name="org_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



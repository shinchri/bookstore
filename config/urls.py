"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]

# associated url for accounts endpoint:
# available here: https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views

# acounts/login/ [name='login']
# acounts/logout/ [name='logout']
# acounts/password_change/ [name='password_change']
# acounts/password_change/done/ [name='password_change_done']
# acounts/password_reset/ [name='password_reset']
# acounts/password_reset/done/ [name='pasword_reset_done']
# acounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# acounts/reset/done/ [name='password_reset_complete']

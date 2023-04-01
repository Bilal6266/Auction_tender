"""AuctionTenderApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from AuctionTenderApi.auction_tender_startup.views import HealthCheckView, SignUp, Login, updatedb

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', HealthCheckView.as_view(), name='health-check'),
    path('Login/', Login.as_view(), name='Login'),
    path('SignUp/', SignUp.as_view(), name='SignUp'),
    path('update/', updatedb.as_view(), name='Update'),
]

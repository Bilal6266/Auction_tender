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
from AuctionTenderApi.auction_tender_startup.views import HealthCheckView, SignUp, Login, Tender, Auction, TenderEmail, AuctionEmail, User

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HealthCheckView.as_view(), name='health-check'),
    path('login', Login.as_view(), name='Login'),
    path('signup', SignUp.as_view(), name='SignUp'),
    path('tender', Tender.as_view(), name='Tender'),
    path('auction', Auction.as_view(), name='Auction'),
    path('user', User.as_view(), name='Update'),
    path('tenderemail', TenderEmail.as_view(), name='TenderEmail'),
    path('auctionemail', AuctionEmail.as_view(), name='AuctionEmail'),
]

"""myproject URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from website.views import home, learn, predict
from website.views import flag, penant, ascending, descending, symmetrical, cup, head, double,gaps 
from website.views import reliance,itc,tata

from django.urls import path
from website.views import plot_macd



 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('learn/', learn, name='learn'),
    path('predict/', predict, name='predict'),
    path('learn/flag', flag, name='flag'),
    path('learn/penant', penant, name='penant'),
    path('learn/ascending', ascending, name='ascending'),
    path('learn/descending', descending, name='descending'),
    path('learn/symmetrical', symmetrical, name='symmetrical'),
    path('learn/cup', cup, name='cup'),
    path('learn/head', head, name='head'),
    path('learn/double', double, name='double'),
    path('learn/gaps', gaps, name='gaps'),
    path('predict/reliance',reliance,name='reliance'),
    path('predict/itc',itc,name='itc'),
    path('predict/tata',tata,name='tata'),
    path('plot_macd/', plot_macd, name='plot_macd'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

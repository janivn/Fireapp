"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from fire.views import PieCountbySeverity, ChartView, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, map_incidents,get_incident_sparkline_data,SparkLineView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ChartView.as_view(), name='home'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations', map_station, name='map-station'),
    path('incidents/', map_incidents, name='map-incident'),
    path('sparklineChart/', get_incident_sparkline_data, name='sparkline_chart'),
    path('sparkline/', SparkLineView.as_view(), name='sparkline'),

    
    
]

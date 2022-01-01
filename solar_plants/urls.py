"""solar_plants URL Configuration
"""
from django.urls import path
from solar_plants.views import report_page, solar_plant_report

urlpatterns = [
    path('solarplant/report/', solar_plant_report, name='solar_plant_report'),
    # report_page can have a more specific url path
    # for demo purpose / endpoint is used.
    path('', report_page, name='report_page'),
]

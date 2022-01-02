from django.test import TestCase
from django.urls import reverse, resolve
from solar_plants.views import report_page, solar_plant_report


class SolarPlantUrlsTest(TestCase):
    """
    Test Solar Plant urls to view mapping
    """
    def test_home_page_url(self):
        url = reverse('report_page')
        self.assertEquals(resolve(url).func, report_page)

    def test_solar_plant_report_page(self):
        url = reverse('solar_plant_report')
        self.assertEquals(resolve(url).func, solar_plant_report)

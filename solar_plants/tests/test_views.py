import json
from datetime import date
from django.test import Client, TestCase
from django.urls import reverse
from solar_plants.constants import SOLAR_PANEL_VALID_PARAMETERS
from solar_plants.models import SolarPlant, SolarPlantReport
from solar_plants.views import ERROR_MSG__MISSING_PLANT_ID


TEST_PLANT_ID = 501
DATE_TODAY = date.today()
GENERATION_VALUE = 1
UTF_8='utf-8'


class SolarPlantReportViewTest(TestCase):
    """
    Test Solar Plant view using test client
    """
    def setUp(self):
        self.client = Client()
        self.plant_id = 501
        self.solar_plant = SolarPlant.objects.create(plant_id=TEST_PLANT_ID)
        self.solar_plant_report = SolarPlantReport.objects.create(
            solar_plant=self.solar_plant, date=DATE_TODAY, 
            parameter=SOLAR_PANEL_VALID_PARAMETERS[0], value=GENERATION_VALUE
        )

    def test_report_page(self):
        response = self.client.get(reverse('report_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'solar_plants/barchart.html')

    def test_solar_plant_report(self):
        url = f"{reverse('solar_plant_report')}?plant_id={self.plant_id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        response_content = json.loads(response.content)
        self.assertEqual(response_content['date_labels'], [DATE_TODAY.strftime('%Y-%m-%d')])
        self.assertEqual(response_content['parameter_datasets']['generation'], [GENERATION_VALUE])
    
    def test_solar_plant_report_without_plant_id(self):
        url = reverse('solar_plant_report')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        response_msg = response.content.decode(UTF_8)
        self.assertTrue(ERROR_MSG__MISSING_PLANT_ID in response_msg)

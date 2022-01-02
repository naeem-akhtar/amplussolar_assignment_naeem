from datetime import date
from django.test import TestCase
from solar_plants.constants import SOLAR_PANEL_VALID_PARAMETERS
from solar_plants.models import SolarPlant, SolarPlantReport


TEST_PLANT_ID = 501
DATE_TODAY = date.today()


class SolarPlantModelTest(TestCase):
    """
    Test Solar Plant Model
    """
    def setUp(self):
        SolarPlant.objects.create(plant_id=TEST_PLANT_ID)

    def test_plant_id_as_pk(self):
        solar_plant = SolarPlant.objects.get(pk=TEST_PLANT_ID)
        self.assertEquals(solar_plant.plant_id, str(TEST_PLANT_ID))


class SolarPlantReportModelTest(TestCase):
    """
    Test Solar Plant Report Model
    """
    def setUp(self):
        solar_plant = SolarPlant.objects.create(plant_id=TEST_PLANT_ID)
        SolarPlantReport.objects.create(solar_plant=solar_plant, date=DATE_TODAY, 
            parameter=SOLAR_PANEL_VALID_PARAMETERS[0], value=1)

    def test_solar_plant_report(self):
        self.assertTrue(SolarPlantReport.objects.filter(solar_plant_id=TEST_PLANT_ID).exists())
        self.assertTrue(SolarPlantReport.objects.filter(parameter=
            SOLAR_PANEL_VALID_PARAMETERS[0]).exists())
        self.assertTrue(SolarPlantReport.objects.filter(date=DATE_TODAY).exists())
        # negative test cases
        self.assertFalse(SolarPlantReport.objects.filter(solar_plant_id=503).exists())
        self.assertFalse(SolarPlantReport.objects.filter(parameter=
            SOLAR_PANEL_VALID_PARAMETERS[1]).exists())
        self.assertFalse(SolarPlantReport.objects.filter(date__gt=DATE_TODAY).exists())
        self.assertFalse(SolarPlantReport.objects.filter(date__lt=DATE_TODAY).exists())

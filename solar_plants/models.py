from django.db import models
from solar_plants.constants import SOLAR_PANEL_PARAMETERS_CHOICES

# An independent solar plant table will make it easier to scale
# when more information for a plant will be needed to store.
class SolarPlant(models.Model):
    """
    Solar Plant model to store information of all solar plants.
    """
    # Don't assume the plant id will always be a valid integer.
    plant_id = models.CharField('plant_id', max_length=100, primary_key=True)

    def __repr__(self) -> str:
        return str(self.plant_id)


class SolarPlantReport(models.Model):
    """
    Solar Plant Report model to store daily statics of all the solar plants.
    """
    solar_plant = models.ForeignKey(SolarPlant, on_delete=models.CASCADE)
    date = models.DateField('date', null=False, blank=False)
    parameter = models.CharField('parameter', max_length=100, 
        choices=SOLAR_PANEL_PARAMETERS_CHOICES)
    value = models.BigIntegerField('value', null=False, blank=False)

    def __repr__(self) -> str:
        return str(self.solar_plant)

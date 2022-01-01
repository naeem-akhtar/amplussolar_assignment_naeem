import django_filters as filters
from solar_plants.constants import SOLAR_PANEL_PARAMETERS_CHOICES
from solar_plants.models import SolarPlantReport


class SolarPlantReportFilter(filters.FilterSet):
    """
    Solar Plant report filter using query parameters:
        plant_id (required)
        parameter (optional)
        date_after (optional)
        date_before (optional)
    """
    plant_id = filters.CharFilter(
        field_name='solar_plant_id', label='plant_id', lookup_expr='exact')
    parameter = filters.ChoiceFilter(
        label='parameter', choices=SOLAR_PANEL_PARAMETERS_CHOICES)
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = SolarPlantReport
        fields = ['plant_id', 'parameter', 'date']

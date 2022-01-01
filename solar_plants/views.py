from django.http import HttpResponseBadRequest, JsonResponse
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from logging import getLogger
from solar_plants.constants import SOLAR_PANEL_VALID_PARAMETERS
from solar_plants.filters import SolarPlantReportFilter
from solar_plants.models import SolarPlant, SolarPlantReport


logger = getLogger(__name__)
ERROR_MSG__MISSING_PLANT_ID = "Plant id is not provided."


def report_page(request):
    """
    Render barchart page with all the plants ids.
    """
    context = {
        'plants': list(SolarPlant.objects.all())
    }
    return render(request, template_name='solar_plants/barchart.html', context=context)


def solar_plant_report(request):
    """
    Filter the plants statics based on query parameters and 
    send report in JSON format.
    """
    if request.method == 'GET':
        plant_id = request.GET.get('plant_id', None)

        if plant_id is None:
            logger.error(ERROR_MSG__MISSING_PLANT_ID)
            return HttpResponseBadRequest(content=ERROR_MSG__MISSING_PLANT_ID)

        plant_report = SolarPlantReportFilter(request.GET, queryset=
            SolarPlantReport.objects.all().order_by('date')).qs
        
        date_labels = []
        parameter_datasets = { parameter:[] for parameter in SOLAR_PANEL_VALID_PARAMETERS }

        for report in plant_report:
            # Only add data for valid parameters
            if report.parameter in SOLAR_PANEL_VALID_PARAMETERS:
                parameter_datasets[report.parameter].append(report.value)
                # Since date is sorted, avoid duplicate dates by checking the last element
                if not date_labels or (date_labels[-1] != report.date):
                    date_labels.append(report.date)
            else:
                logger.warn(f"Invalid parameter={report.parameter} found for plant id={plant_id}")
                
        return JsonResponse(data = {
            'date_labels': date_labels,
            'parameter_datasets': parameter_datasets
        })
    else:
        return HttpResponseNotFound(content="Invalid Method")

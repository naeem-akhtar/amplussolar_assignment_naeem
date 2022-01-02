let solar_plant_report_endpoint = "solarplant/report"

// Plot chart once the page is ready
$(document).ready(() => {
    plotBarChartForSelectedPlant()
});

// Plot chart when a new solar plant is selected
$("#selectedSolarPlant").click(() => {
    plotBarChartForSelectedPlant()
});


let plotBarChartForSelectedPlant = () => {
    let selectedSolarPlant = document.getElementById('selectedSolarPlant').value;

    // Do not fetch data if no 'plant_id' is provided from backend.
    if (!selectedSolarPlant) {
        window.alert("Solar Plants information not available.");
        return;
    }

    $.ajax({
        url: solar_plant_report_endpoint,
        type: "GET",
        dataType: "json",
        data: {
            plant_id: selectedSolarPlant
        },
        success: (jsonResponse) => {
            let chartData = {
                labels: jsonResponse['date_labels'],
                datasets: [{
                    label: "Generation",
                    backgroundColor: "#00ff00", // green shade
                    data: jsonResponse['parameter_datasets']['generation']
                }, {
                    label: "Irradiation",
                    backgroundColor: "#33cccc", // blue shade
                    data: jsonResponse['parameter_datasets']['irradiation']
                }]
            }
            // Clear chart to avoid overriding on existing chart.
            clearReportChart();
            plotBarChart(chartData);
        },
        error: () => {
            window.alert("Cannot draw bar chart report.");
        }
    });
}


let plotBarChart = (data) => {
    let context = document.getElementById('reportBarChartCanvas').getContext('2d');
    let barChartConfig = {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            maintainAspectRatio: true,
            title: {
                display: true,
                position: 'bottom',
                text: 'Solar Plant daily Generation and Irradiation chart.'
            },
            legend: {
                position: 'top',
            },
        },
    };
    window.solarPlantBarChart = new Chart(context, barChartConfig);
};


let clearReportChart = () => {
    // The ".clear()" method will clears the canvas, but
    // it leaves the object alive, instead remove and create a new canvas.
    $('#reportBarChartCanvas').remove();
    $('#reportBarChart').append(
        '<canvas id="reportBarChartCanvas" class="table"></canvas>'
    );
}

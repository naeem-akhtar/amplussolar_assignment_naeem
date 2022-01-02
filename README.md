# README.md

# Amplus Solar assignment: Naeem Akhtar
Django based webapp that plots the "Bar Chart" to show the daily "Generation" and "Irradiation" of a selected solar plant.

The webapp also exposes REST API endpoint to get the statics of solar plant in terms of "Generation" and "Irradiation" for a given date range.

## REST API Endpoint
### 1. Solar Plant report endpoint:
```
/solarplant/report/
```

Query parameters:
```
plant_id: Valid Solar Plant ID (required)
parameter: 'generation' | 'irradiation' (optional) 
date_after: format 'yyyy-mm-dd' (optional)
date_before: format 'yyyy-mm-dd' (optional)
```

Success Response Format (which is required by the *Chart.js* to plot the graph):
``` json json_schema
{
    "date_labels": ["yyyy-mm-dd",...],
    "parameter_datasets": {
        "generation": ["decimal",....],
        "irradiation": ["decimal",....]
    }
}
```

Error Response (when plant_id parameter is not provided in request): 
```
Plant id is not provided.
```

A curl request can be fired to test the query parameters.

Example: 
```
curl --location --request GET 'http://127.0.0.1:8000/solarplant/report/?plant_id=502&parameter=irradiation&date_after=2021-03-04&date_before=2021-03-28'
```

## Live Demo
The webapp is already deployed on heroku.com with pre-populated database from given [RawData.csv](RawData.csv).

Live webapp: [solarplants-heroku](https://solarplants-naeem.herokuapp.com/)

## Installation

### Development
I have used python-3.8.10 and [virtualenv](https://docs.python.org/3/library/venv.html) as a primary tools for development.

### Steps to manually install and start the webapp:
* Clone the repository
* Create a virtual environment 'python3 -m venv vitualenv'
* Activate the virtual environment 'source ./vitualenv/bin/activate'
* Install all the project dependencies 'pip install -r requirements.txt'
* Migrate the changes to database (if any) 'python manage.py makemigrations && python manage.py migrate'
* Start the webapp 'python manage.py runserver'
* The webapp will be available at 'http://127.0.0.1:8000/'


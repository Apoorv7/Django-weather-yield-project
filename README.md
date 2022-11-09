# Description

- Python automation to ingest data into SQLite database
- Ability to analyze data and create new data model from Data Analysis
- Used Django and Djangorestframework for implementation
- Rest api's to show all models data with some added filters
- Log file for error handling exceptions
- Used django custom command for ingestion of data into database(sqlite)
- Authenticated users and admin can do CRUD operations in all models through api's.
- default parameters for pages

  ```
  DEFAULT_PAGE = 1
  DEFAULT_PAGE_LIMIT = 1000
  ```

# Setup to run

- Firstly you need to install python from [Python](https://www.python.org/) and vscode from [VScode](https://code.visualstudio.com/)
- Now you need to clone this repository in your local pc and then open the repository in vscode.
- Developed and tested the application on `Win 11` with `Python 3.8.12`
- Open terminal in vscode and Then you need to create a virtual environment

  ```
  pip install virtualenv
  py -m venv venv
  ```

- Now you will need to activate the virtual environment

  ```
  .\venv\Scripts\activate
  ```

- Now go to the project folder using `cd` command and install the dependencies
  ```
  pip install -r requirements.txt
  ```
  
- After this you can directly go to `Running web service` para


## Data Modeling

- All the data models `Weather, Results, Yield`can be found in [models.py](site_app/models.py)
  These were developed to work with Django ORM and SQLite as the DB.

  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

- Now you need to create superuser so that you can access all models through the admin page as well
  ```
  python manage.py createsuperuser
  ```

## Data Ingestion in database
`(Note: You can run this if you want a new set of data in tables)`

- Using models from above file, [models_data.py](site_app/models_data.py) ingests data into SQLite DB.
- Made a list for all_objects and then used bulk_create method to add all the objects at once in the DB for a specific model.
- Before running the command you need to mention the directory path of weather and yield files using environment variable in
  [models_data.py](site_app/models_data.py) file. For [setting Environment variables](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html)

  And please do mention the correct file path or it will throw an error which you can see in log file. To run the file to ingest data in tables we can use the following command

  ```
  python manage.py mycommand
  ```

- Here my command refers to the django custom command file `mycommand.py` which run the functions
  from the `models_data.py` file
- If the script is run twice, it will ignore the duplicate entries as have added a condtion that
  comapares the values with all objects in the specific models.

## Data Analysis

- `Results` table holds the stats associated with weather, all the stats are stored per year & station_id combo
- While ingestion of data, ignored the entire row if any of the values has invalid entry -9999
- `ResultsData` function from `models_data.py` file has all the script which stores the data into `Results` table

## REST API

Implemented 3 endpoints that return JSON

- `/api/weather`
  - Query parameters
    - date, station_id, id
  - All arguments are optional, data will be filtered appropriately when date and/or station_id are provided
  - If both date & station_id are absent, all the records will be returned with pagination
- `/api/weather/stats`
  - Query parameters
    - year, station_id
- `/api/yield`
  - Query parameters
    - year

## File layout

- [models_data.py](site_app/models_data.py) - script responsible for populating Weather ,Yield and Results data sets.
  While populating Results, it takes the Weather stats table and in `ResultsData` funtion it splits the average minimum, maximum temperatures and total precipitation data and stores it in `Results` table.

- [views.py](site_app/views.py) - This has all the API View classes which have inherited django backend filters

- [serializers.py](site_app/serializers.py) - This file converts the model data into a json format to use in the API view format

- [urls.py](site_app/urls.py) - In this have used routers for the routing of the view functions

  - `/api/weather`
  - `/api/weather/stats`
  - `/api/yield`

- [models.py](site_app/models.py) - Contains code related to initial setup of SQLite DB

- [models.py](site_app/models.py) - Contains all the three data models Weather, Results & Yield

- [mycommands.py](site_app/management/commands/mycommand.py) - Contains a custom handle funtion to run the models_data.py file funtions for ingestion of the data into DB

- [admin.py](site_app/admin.py) - This is a default admin file in which have registered all the three models so a user or admin can directly do CRUD
  operations through admin page

## Running web service

```
python manage.py runserver
```

Terminal Output

```
(env) PS mysite> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 4.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```

## For opening API's you need to surf to the following urls

```
- Weather API - http://127.0.0.1:8000//api/weather
- Weather stats API - http://127.0.0.1:8000//api/weather/stats
- yield API - http://127.0.0.1:8000//api/yield
```
Screenshots of api's in browser can be found in `screenshots` folder.

## Sample linter run

```
(env) PS Weather_data\mysite\site_app> pylint models.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 9.38/10, +0.62)
```

## Sample code formatter run

```
(env) PS Weather_data> black .\mysite\
All done! ✨ 🍰 ✨
19 files changed.
```

## Sample coverage test run

```
(env) Weather_data\mysite> python manage.py test
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.019s

OK
Destroying test database for alias 'default'...
```

## Sample coverage report run

```
(env) Weather_data\mysite\site_app> coverage report -m
Name       Stmts   Miss  Cover   Missing
----------------------------------------
tests.py      13     12     8%   2-18
----------------------------------------
TOTAL         13     12     8%

```

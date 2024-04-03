# OnlineLearningPlatform

Welcome to the OnlineLearningPlatform project! This project is built with FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.11 and MySQL.

## Follow these steps to set up and run the project locally:

## Prerequisites

- Python 3.11
- fastapi
- MySQL database installed and running locally.
- packages on the requirements.txt file [provided]

## Clone this repository to your local machine:

``` git clone https://github.com/jakariadev/OnlineLearningPlatform.git ```

## Create a virtual environment to isolate project dependencies:

``` python3 -m venv venv ```

## Activate the virtual environment:

### On macOS and Linux:

``` source venv/bin/activate ```

### On Windows:

``` venv\Scripts\activate ```

### Install the project dependencies:

``` pip3 install -r requirements.txt ```

### Navigate to the project directory:

``` cd EmsApp ```

### Configuration

 Open the ``` EmsApp\database.py ``` file and update the MySQL database credentials:

``` SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://username:password@localhost:3306/ems' ```

 "Replace username and password with your MySQL username and password."

## Running the Server
### Start the FastAPI development server:


``` uvicorn main:app --reload ```

"The API server should now be running locally at http://localhost:8000 "
You can now access the API documentation at http://localhost:8000/docs and interact with the endpoints using the Swagger UI.

## Running the Test
Just Run ``` pytest ``` in the same directory


## Running in Docker:
In the project level directory there are two files 'Dockerfile' and 'docker-compose' file.
 Just run
``` docker-compose up --build ``` 
Later just ```docker-compose up```


## API Payloads
#### Create Course 
{
  "title": "string",
  "description": "string",
  "instructor": "string",
  "duration": 0,
  "price": 100000000
}

#### Create Enrollment

{
  "student_name": "string",
  "enrollment_date": "2024-04-03",
  "course_id": {
    "id": 0
  }
}

Use your favorite API client (e.g., Postman, Insomnia) or a web browser to interact with the API endpoints.

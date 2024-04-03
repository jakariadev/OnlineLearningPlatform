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

### Create a virtual environment to isolate project dependencies:

``` python3 -m venv venv ```

### Activate the virtual environment:

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

### Running the Server
### Start the FastAPI development server:

``` uvicorn main:app --reload ```
### The API server should now be running locally at http://localhost:8000.



### Running the Test
Just Run:

``` pytest ```

You can now access the API documentation at http://localhost:8000/docs and interact with the endpoints using the Swagger UI.

Use your favorite API client (e.g., Postman, Insomnia) or a web browser to interact with the API endpoints.
You can customize and extend the project by adding new endpoints, models, and business logic as needed.

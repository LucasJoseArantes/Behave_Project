# BDD Automated Testing Project with Behave

## Project Description:

This project aims to showcase the implementation of end-to-end (E2E) automated tests using Behavior Driven Development (BDD) methodology with Behave, a popular BDD framework in Python. The primary purpose is to demonstrate how to develop and execute automated tests following BDD principles, leveraging various tools and libraries such as Selenium for web automation, Pandas for file manipulation, Logging for test logging, Requests for API testing, and Linters for code quality improvements.

## Setup and Configuration:

### Setting up a Virtual Environment:

1. Verify if Python is installed by running the following command in your terminal:
    ```bash
    python --version

Note: if python is not installed, download and install [here](https://www.python.org/downloads/).

2. Create a virtual environment named 'venv' with the following command:
    ```bash
    python -m venv venv


4. Activate the virtual environment with the following command:
    ```bash
    .\venv\Scripts\activate

5. Install the dependencies listed in the requirements.txt file using the command:
    ```bash
    pip install -r requirements.txt

### Configuring Credentials:
Ensure to configure the necessary environment variables to run the tests.

## Running Tests:
To execute the tests, navigate to the project's root directory in the terminal and run the following command:

    behave

### Customizing Test Execution:
To customize test execution, follow these steps:

| Description          | Command                                   |
|----------------------|-------------------------------------------|
| Run specific scenario| behave -n "scenario_name"                |
| Run specific feature | behave -i "file_name.feature"            |
| Set Browser          | $env:BROWSER="firefox" (default)         |
| Set Headless Mode    | $env:HEADLESS_MODE="False" (default)     |


## Using Linters:
To utilize the Linters locally, execute the following commands:

Isort:

    isort --diff ./features
    isort --check-only ./features

Black:    

    black --line-length 120 --diff ./features
    black --line-length 120 --check ./features
    
Flake8:

    flake8 ./features
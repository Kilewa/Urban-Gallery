## The Urban Gallery

## Description

The Urban Gallery is a photo gallery web application to showcase beautiful pictures. Users get can view photos uploaded by admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories.

## Features
- The home page allows users to see various images:
- User can see all images per location they were taken
- Users can also search for images based categories
- Admin can upload images from a django dashboard

## View Live Site here
View the complete site [here](link here/)


## Technologies Used
    - Python 3
    - Django MVC framework
    - HTML, CSS and Bootstrap
    - JavaScript
    - Postgressql
    - Heroku

### Prerequisite
The Urban Gallery project requires a prerequisite understanding of the following:
- Django Framework
- Python3
- Postgres
- Python virtualenv

## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3 as default handler
    `virtualenv -p /usr/bin/python3 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE gallery;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'gallery'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3 manage.py makemigrations gallery
    python3 manage.py migrate
#### Run the app
    python3 manage.py runserver
    Open terminal on localhost:8000

## Known bugs
No known bugs so far. 


## Contributors
    George Kilewa

### Contact Information
kilewageorge230@gmail.com

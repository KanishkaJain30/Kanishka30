# Kanishka30
1.This app focuses on log in with Twitter and then extract the tweet's that contain URLs from a users stream (friends + users post) for the past 7 days.Then Persists the tweets in the database.
Once stored, the application should then compute and display
a. Actual Tweets containing links
b. Which user has shared the most links
c. List of Top Domains that have been shared so far

## Prerequisites
Django

## Installing Dependencies
git clone https://github.com/KanishkaJain30/Kanishka30.git

Once cloned then create a virtual environmenet of the root directory by

> python -m venv myvenv

Then activate the virtual environment for windows by

> myvenv\Scripts\activate

Now install the dependencies by the following command

> pip install -r requirements.txt

## Server Configuration

Get the CONSUMER KEY and CONSUMER SECRET KEY from https://developer.twitter.com/en/docs/labs/getting-started.

## Set up Database
 
Make Migrations - It is responsible for creating new migrations based on the changes you have made to your models.
> python manage.py makemigrations

Migrate - It is responsible for applying migrations, as well as unapplying and listing their status.
> python manage.py migrate

## Create SuperUser
It's needed to create a user account that has control over everything on the site.
> python manage.py createsuperuser

Set username, email and password and go to below mentioned URL:

> 127.0.0.1:8000/admin

## Start the Development Server
And we're done! Time to start the web server and see if our website is working!

> python manage.py runserver





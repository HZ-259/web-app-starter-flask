# Team 3 presents EventSearch, a webpage that allows you to quickly search for events happening in your state. Our search results are powered by TicketMaster. 

# Accessing the webpage

Go to https://event-search-msb.herokuapp.com/eventform
Select your state from the drop-down list of options and hit "submit"


The webpage will refresh (https://event-search-msb.herokuapp.com/getevents) and display a list of events happening in your state in tabular form

# Installing to your local environment

Fork the repository from GitHub (https://github.com/HZ-259/web-app-starter-flask)
Then use GitHub Desktop or the command-line to "clone" or download your fork onto your local computer:

Navigate into your local repo from the command-line before running any of the other commands below:

    cd web-app-starter-flask

Activate your Anaconda virtual environment 
    conda create -n web-starter-env python=3.7 #first time only
    conda activate web-starter-env

Install package dependencies (first time only):
    pip install -r requirements.txt

Run a local web server, then view your app in a browser at http://localhost:5000/eventform

    FLASK_APP=web_app flask run


# Acknowledgements
We borrowed from Professor Rossetti's web-app-starter-flask repository on GitHub to model our webapp after. Thank you to Professor Rosetti for all of his support to make our webpage possible! 

<>

# Readme file from the template

# Web App Starter Repo (Flask)

An example web application, built in Python with the Flask package, for educational purposes.

## Installation

Fork the repository from [GitHub source](https://github.com/prof-rossetti/web-app-starter-flask).

Then use GitHub Desktop or the command-line to "clone" or download your fork onto your local computer:

```sh
git clone https://github.com/YOUR_USERNAME/web-app-starter-flask.git # this is the HTTP address, but you could alternatively use the SSH address
```

Navigate into your local repo from the command-line before running any of the other commands below:

```sh
cd web-app-starter-flask
```

## Setup

Create and activate an Anaconda virtual environment:

```sh
conda create -n web-starter-env python=3.7 # first time only
conda activate web-starter-env
```

> NOTE: Subsequent commands assume you're running them from within the virtual environment, in the root directory of the repository.

Install package dependencies (first time only):

```sh
pip install -r requirements.txt
```

## Usage

Run a local web server, then view your app in a browser at http://localhost:5000/:

```sh
FLASK_APP=web_app flask run
```

> NOTE: you can quit the server by pressing ctrl+c at any time. If you change a file, you'll likely need to restart the server for the changes to take effect.

## Deploying

First, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and make sure you can login and list your applications. Then create a new application server, optionally specifying a name (e.g. "web-app-starter-flask"):

```sh
heroku login

heroku apps:list
heroku apps:create web-app-starter-flask # or do this from the online console
heroku apps:list
```

Then associate this repository with that application, as necessary:

```sh
git remote -v
heroku git:remote -a web-app-starter-flask # necessary if you created the app from the online console
git remote -v
```

After this configuration process is complete, you should be able to "deploy" the application's source code to the Heroku server:

```sh
git push heroku master
```

## [Licence](/LICENSE.md)

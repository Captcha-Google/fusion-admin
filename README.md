# Fusion Administrator Panel

[![N|Fusion Admin Kit](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=main)](https://travis-ci.org/joemccann/dillinger)

Fusion Admin Kit - is a django plugin in creating a modern UI for admin panel with easy to use and install by using pip, mobile responsive, and powered by Python programming language.

## Development
Fusion Admin Kit is currently in the development phase you can also use this product by cloning the repository

```sh
git clone https://github.com/Captcha-Google/fusion-admin
```

- copy the project in your django project as a application and

- add on your installed apps using the code below
  
```sh
INSTALLED_APPS = [
    .....,
    'fusion-admin',
]
```

- migrate your application for your database
  
```sh
python manage.py migrate
```
- run the project
  
```sh
python manage.py runserver 0.0.0.0:<PORT>
```


## Features

- With a django users visualization (Graphs)
- Modern UI
- Easy navigation
- Visulization of the monthly users
- Management Information System
- Recent Actions (Logs)
- Calendar
- Visulization of the Users Browsers
- Secure Authentication

## Technology used

Fusion Admin Kit uses a number of open source projects to work properly:

- Django
- HTML
- CSS
- jQuery
- Python
- JavaScript

## Utilizes the AdminKit Bootstrap UI

## Installation

> Fusion Admin Kit uses Python with the latest version

```sh
pip install fusion-admin
python manage.py migrate
python manage.py createsuperuser --email <EMAIL ADDRESS> --username <USERNAME>
python manage.py runserver 0.0.0.0:<PORT>
```

## Docker

> Docker will be available soon

## License
MIT

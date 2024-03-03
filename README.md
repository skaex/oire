# OIRE

This is a project made up of applications for the American University of Nigeria Office of Institutional Research and Effectiveness.
The project was initiated to replace the existing paper-driven activities by the university's office of institutional research and effectiveness to save on costs and be more environmentally friendly.

This project is still in development.


## Requirements
The initial requirements for this project include:

 * This is a django project and it was built with python 3.11.5.
 * The [RabbitMQ broker](https://www.rabbitmq.com/download.html).
 * [Postgres Database](https://www.postgresql.org/).

All other requirements are found in the project's *[Requirements file.](requirements.txt)*

## Quick start (for development)
To set up this project on a machine **(for preview/development only)**, you will need to:

1. Ensure a similar Python version (say 3.11.5) is installed on your machine.
2. (Optional) You may want to create a separate virtual environment
    * You may use [pyenv](https://github.com/pyenv/pyenv) along side [pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv).
    * Create the virtual env with `pyenv virtualenv 3.11.5 oire`
3. Download and unzip or clone the project.
4. ``cd`` into the project directory.
5. Install the requirements with
    * ``pip install -r requirements.txt``
6. Set up the database. You can do it how you want or follow [this guide](docs/DATABASE_SETUP.md).
7. Copy example environment file with
    * ``cp env.example .env``
8. Create Goat (Test User) with
    * ``python manage.py creategoat``
9.  Runserver with
    * ``python manage.py runserver``
    * ``rabbitmq-server`` (in another shell obviously)
    * ``celery -A oire worker -l info`` (in another shell but the same environment/virtual environment.
10. Go to ``http://localhost:8000/``.
11. Click on **Faculty Course Evaluation**.
12. Login with the Goat.
13. Good luck :tada:

Please don't forget give us feedback in form of issues. :+1:

## Installation (for production)
Ensure, you have setup this project for preview to be conversant with the requirements and other intricacies for this project.


To install this project, you can follow [the procedures in the guide.](https://realpython.com/django-nginx-gunicorn/) Please read through to understand it all before attempting the installation.

Alternatively, you can follow the procedures for deploying a [django application to production](https://docs.djangoproject.com/en/5.0/howto/deployment/).






## Contributors

[Abdulmajid Hamza](http://x.com/__skampa__)

## License

Creative Commons [(CC-NC-ND)](https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode)
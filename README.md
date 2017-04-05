## OIRE
[![Build Status](https://travis-ci.org/SkaeX/oire.svg?branch=develop)](https://travis-ci.org/SkaeX/oire)
[![codecov](https://codecov.io/gh/SkaeX/oire/branch/develop/graph/badge.svg)](https://codecov.io/gh/SkaeX/oire)

This is a project made up of applications for the American University of Nigeria Office of Institutional Research and Effectiveness.
The project was initiated to replace the existing paper-driven activities by the university's office of institutional research and effectiveness to save on costs and be more environmentally friendly.

This project is still in development.


## Requirements
The initial requirements for this project include:

 * This is a django project therefore it requires python (3.4.x).
 * There might be a requirement for [zlib](http://stackoverflow.com/questions/34631806/fail-during-installation-of-pillow-python-module-in-linux) for Pillow.
 * The [RabbitMQ broker](https://www.rabbitmq.com/download.html).

All other requirements are found in the project's *requirements folder*

## Quick start
To set up this project on a machine *(for preview)*, you will need to:

1. Ensure Python 3.4.x is installed on your machine.
2. (Optional) You may want to create a separate ``virtualenv``
3. Download and unzip or clone the project.
4. ``cd`` into the project directory.
3. Install the requirements with
    * ``pip install -r requirements/development.txt``
4. Copy example environment file with
    * ``cp env.example oire/settings/.env``
5. Create Goat (Test User) with
    * ``python manage.py creategoat``
6. Runserver with
    * ``python manage.py runserver``
    * ``rabbitmq-server`` (in another shell obviously)
    * ``celery -A oire worker -l info`` (in another shell but the same environment/virtual environment.
7. Go to ``http://localhost:8000/``.
8. Click on **Faculty Course Evaluation**.
9. Login with the Goat.


. Please don't forget give us feedback in form of issues. :+1:




## Contributors

[Abdulmajid Hamza](http://abdulmajid.com.ng)

## License

Creative Commons [(CC-NC-ND)](https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode)
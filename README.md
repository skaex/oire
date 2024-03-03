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
2. (Optional) You may want to create a separate ``virtualenv``
3. Download and unzip or clone the project.
4. ``cd`` into the project directory.
3. Install the requirements with
    * ``pip install -r requirements.txt``
4. Set up the database. You can do it how you want or follow [this guide](docs/DATABASE_SETUP.md).
5. Copy example environment file with
    * ``cp env.example .env``
6. Create Goat (Test User) with
    * ``python manage.py creategoat``
7. Runserver with
    * ``python manage.py runserver``
    * ``rabbitmq-server`` (in another shell obviously)
    * ``celery -A oire worker -l info`` (in another shell but the same environment/virtual environment.
8. Go to ``http://localhost:8000/``.
9.  Click on **Faculty Course Evaluation**.
10. Login with the Goat.
11. Good luck :tada:



Please don't forget give us feedback in form of issues. :+1:




## Contributors

[Abdulmajid Hamza](http://x.com/__skampa__)

## License

Creative Commons [(CC-NC-ND)](https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode)
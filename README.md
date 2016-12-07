## OIRE
This is a project made up of applications for the American University of Nigeria Office of Institutional Research and Effectiveness.
The project was initiated to replace the existing paper-driven activities by the university's office of institutional research and effectiveness to save on costs and be more environmentally friendly.

This project is still in development.


## Requirements
This is a django project therefore it requires python (3.4.x). All other requirements are found in the project's
*requirements folder*

## Quick start
To set up this project on a machine *(for preview)*, you will need to:

1. Ensure Python 3.4.x is installed on your machine.
2. (Optional) You may want to create a separate ``virtualenv``
3. Download and Unzip or clone the project.
4. ``cd`` into the project directory.
3. Install the requirements with
    * ``pip install -r requirements/development.txt``
4. Copy example environment file with
    * ``cp env.example oire/settings/.env``
5. Run migrations with
    * ``python manage.py makemigrations``
    * ``python manage.py migrate``
6. Seed some data with
    * ``python manage.py loaddata groups``
7. Create a super user with
    * ``python manage.py createsuperuser``
8. Runserver with
    * ``python manage.py runserver``
9. Go to ``http://localhost:8000/auth/login/`` and login.
10. Please don't forget give us feedback in form of issues. :+1:




## Contributors

[Abdulmajid Hamza](http://abdulmajid.com.ng)

## License

Creative Commons [(CC-NC-ND)](https://creativecommons.org/licenses/by-nc-nd/3.0/legalcode)
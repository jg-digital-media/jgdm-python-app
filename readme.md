# jgdm_python_sqlalchemy  - jgdm-python-app (**Last Update: 13-09-2021** - 09:26)

## Flask with SQL

Built with Python, Flask and SQLAlchemy, this is a small and rudimentary application that tests the CRUD operations of a dynamic application by way of a name and age "Roster".

It uses 1 model called Roster and the form buttons you press activity SQL Queries that make material changes to a binary `.db` file.

I may update the `.db` file to refresh the data from time to time.

I will look to build something more substantial at a later date.

## Setup - (optimised for Windows 10 at the current time)

Move to a selected directory using your command line tool  - ```cd project_root```

Create a virtual environment  - ```python - venv env```

Activate a virtual environment - ```source .\env\Scripts\activate``` - (Windows)

pip freeze - requirements file - ```pip freeze > requirements.txt```

Install flask - ```pip install flask```

Install SQLAlchemy - ```pip install sqlalchemy```

Install Flask-SQLAlchemy - ```pip install Flask-SQLAlchemy```
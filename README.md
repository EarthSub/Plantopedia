# Plantopedia

Plantopedia is a small plant care catalogue built with Django. It lets visitors browse plants, organize them into collections, and record care notes. A plant can include an uploaded photo.

The project is organized into three Django apps:

- **plants** — plant categories and plant catalogue pages.
- **plant_collections** — collections that group plants.
- **care_log** — care notes associated with plants.

## Features

- Browse the catalogue and filter plants by category or sort them by name, watering interval, or date added.
- View plant and category details.
- Create, view, edit, and delete plants and collections.
- Create plant categories and care notes.
- Upload an optional image when adding or editing a plant.
- Use a custom 404 page and shared page layout.

## Requirements

- Python version compatible with Django 6.1.2
- pip

The application uses SQLite, which is included with Python. Pillow is installed from requirements.txt to support plant image uploads.

## Installation and local setup

### Windows PowerShell

1. Download or clone this repository and open a terminal in the project directory.
2. Create and activate a virtual environment:

   ~~~powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ~~~

3. Install the dependencies:

   ~~~powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ~~~

4. Apply the database migrations:

   ~~~powershell
   python manage.py migrate
   ~~~

5. Start the development server:

   ~~~powershell
   python manage.py runserver
   ~~~

6. Open http://127.0.0.1:8000/ in a browser.

### macOS or Linux

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
~~~

Then open http://127.0.0.1:8000/ in a browser.

## First steps in the application

The database can start empty. Create the required objects through the website navigation:

1. Open **Categories** and add a category.
2. Open **Plants** and add a plant, selecting the category. You can also select a photo from your computer.
3. Open **Collections** and create a collection, optionally selecting plants for it.
4. Open **Care notes** and add a note for a plant.

No sample objects need to be loaded from a fixture or custom data migration.

## Project structure

~~~text
Plantopedia/
├── care_log/                 # Care note app
├── plant_collections/        # Plant collection app
├── plants/                   # Plants and categories app
├── plantopedia/              # Django project settings and root URLs
├── static/css/site.css       # Project stylesheet
├── templates/                # Shared and app-specific HTML templates
├── media/                    # Uploaded plant images (created/used locally)
├── manage.py
├── requirements.txt
└── README.md
~~~

## Data model overview

- PlantCategory has many Plant objects (one-to-many).
- Each Plant belongs to one PlantCategory and may have a photo.
- PlantCollection can contain multiple plants, and a plant can belong to multiple collections (many-to-many).
- Each CareNote belongs to one plant (many-to-one).

## Configuration

No environment variables, external services, or credentials are required for local testing. The default configuration uses SQLite and Django's development server. Uploaded images are stored under the local media/ directory.

This configuration is intended for local coursework evaluation and development, not production deployment.


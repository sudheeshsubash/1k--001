#!/bin/bash

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create .env file and copy content from .env.example
cp .env.example .env

# Check the project
python manage.py check

# Run the Django project
python manage.py runserver

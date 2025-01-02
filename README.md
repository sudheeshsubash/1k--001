# Django Skeleton Project

This is a skeleton project of Django to help you get started quickly.

## Setup Instructions

Follow these steps to set up and run the project:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/phenix-crew/Django-framework-skeleton.git
    cd Django-skelton
    ```
    or 
    ```bash
    django-admin startproject projectname --template=https://github.com/phenix-crew/Django-framework-skeleton/archive/refs/heads/master.zip
    cd projectname
    ```

2. **Run the setup script:**
    ```bash
    ./setup.sh
    ```

## Project Structure

```
Django-skelton/
├── manage.py
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── ...
├── templates/
│   └── index.html
├── static/
│   └── ...
├── requirements.txt
└── setup.sh
```

## Features

- **Welcome Page:** A simple welcome page using Tailwind CSS.
- **Virtual Environment Setup:** Automated setup of virtual environment and installation of dependencies.
- **Django Project:** Basic Django project structure to get you started.

## Usage

- **Start the development server:**
    ```bash
    python manage.py runserver
    ```

- **Access the application:**
    Open your browser and go to `http://127.0.0.1:8000/`.

## License

This project is licensed under the MIT License.

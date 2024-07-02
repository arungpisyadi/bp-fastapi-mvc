<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>

# FastAPI MVC

This template provides a starting point for building web applications using FastAPI and following the Model-View-Controller (MVC) architectural pattern.

## Technologies Used

This project is developed using the following technologies:

- **FastAPI:** A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **Uvicorn:** A lightning-fast ASGI server, used to run FastAPI application.
- **PyMySQL:** A pure-Python MySQL/MariaDB client library.
- **SQLAlchemy:** A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Alembic:** A database migration tool for SQLAlchemy.

## Project Structure

The project structure is organized as follows:

- **controllers:** Contains the controllers responsible for handling requests and business logic.
- **db:** Contains the database driver and logic for create database.
- **middlewares:** Houses various middleware for request handling (e.g., static files, CORS).
- **models:** Stores the application's data models and schemas.
- **repositories:** Handles interaction with databases or external services.
- **services:** Implements business logic for working with objects.
- **static:** Contaim static files (Some js library, css, images, etc.).
- **templates:** Holds HTML templates for rendering views.
- **utils:** Contains utility functions.

```
├── app
│   ├── controllers
│   │   ├── auth_controller.py
│   │   ├── page_controller.py
│   │   ├── private_controller.py
│   │   └── user_controller.py
│   ├── db
│   │   └── context.py
│   ├── middlewares
│   │   ├── cors_middleware.py
│   │   └── static_middleware.py
│   ├── models
│   │   ├── db.py
│   │   └── dto.py
│   ├── repositories
│   │   ├── token_repository.py
│   │   └── user_repository.py
│   ├── services
│   │   ├── token_service.py
│   │   └── user_service.py
│   ├── templates
│   │   ├── 403.html
│   │   ├── 404.html
│   │   ├── login.html
│   │   ├── main.html
│   │   ├── private.html
│   │   └── register.html
│   ├── utils
│   │   ├── dependencies.py
│   │   ├── formating.py
│   │   ├── hashing.py
│   │   ├── pages.py
│   │   └── validators.py
│   ├── static
│   ├── prod.sh
│   ├── db_init.bash
│   ├── db_init.py
│   ├── dev.bash
│   └── main.py
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── install_env.sh
├── LICENSE
├── README.md
└── requirements.txt

11 directories, 35 files
```

## Getting Started

### Installation Without Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/ViktorViskov/fastapi-mvc.git
    ```

2. Install dependencies:

    ```bash
    cd fastapi_mvc
    pip install -r requirements.txt
    ```

### Running the Application

To start the FastAPI application, use the following command:

```bash
cd app
bash dev.bash
```

### Installation Using Docker

You don't need to install the dependencies if you're using Docker.

To start the application using Docker, run the following command:

```bash
docker compose -f compose.dev.yml up -d
```

This will start the FastAPI application in development mode. Where you can edit your files and it will auto-reload.

## Deploying the Project
```sh
docker compose up -d
```

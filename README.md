# Simple Python Microservice

This is a simple microservice written in Python using the Flask web framework. It implements a key-value store, where you can set and get values from an in-memory dictionary.

## Project Structure

The project follows a basic Flask project layout.

```text
/pythonmicroservice
    /app
        init.py
        routes.py
        service.py
        repository.py
    run.py
    requirements.txt
    Dockerfile
```


## Getting Started

First, clone the repository to your local machine:

```bash
git clone https://github.com/indranandjha1993/pythonmicroservice.git
```

## Navigate to the project directory:
```bash
cd pythonmicroservice
```

## Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Run the application:
```bash
python run.py
```

The server will start on localhost:8080.

## API Endpoints
The service exposes the following endpoints:

- GET /get/{key}: Retrieve the value for a given key.
- POST /set/{key}/{value}: Set a value for a given key.

## Running with Docker
You can also build and run the service using Docker. Build the image with:

```bash
docker build -t pythonmicroservice .
```

### Then run the container:

```bash
docker run -p 8080:8080 pythonmicroservice
```

## Note
This is a simple example and is not suitable for production use. For a real application, consider implementing proper error handling, validation, security measures, and using a real database for the repository layer.
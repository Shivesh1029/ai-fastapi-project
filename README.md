# AI FastAPI Content Generator

This project is a simple backend API built using **FastAPI** that generates marketing-style content based on a provided topic.

## Features

* FastAPI backend server
* REST API endpoint
* JSON request and response handling
* Swagger API documentation
* Content generation endpoint

## API Endpoints

### GET /

Returns a simple message confirming the API is running.

### POST /generate

Generates marketing content based on the provided topic.

Example request:

```
{
 "topic": "luxury hotel in Singapore"
}
```

Example response:

```
{
 "generated_text": "This is an AI generated marketing message about luxury hotel in Singapore."
}
```

## Run the Project

Install dependencies:

```
pip install fastapi uvicorn
```

Run the server:

```
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

## Tech Stack

* Python
* FastAPI
* Uvicorn
* REST API

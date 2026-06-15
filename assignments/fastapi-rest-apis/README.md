# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a simple REST API using the FastAPI framework. You will learn how to create endpoints, validate request data, and return clear HTTP responses.

## 📝 Tasks

### 🛠️	Create a FastAPI Application

#### Description
Set up a FastAPI app with a health-check endpoint and run it locally.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Add a `GET /health` endpoint that returns a JSON response like `{ "status": "ok" }`.
- Run successfully with Uvicorn and respond to requests in a browser or API client.


### 🛠️	Implement CRUD Endpoints

#### Description
Build endpoints to create, list, update, and delete items stored in memory.

#### Requirements
Completed program should:

- Define an in-memory list of items where each item has at least `id`, `name`, and `completed` fields.
- Implement `GET /items`, `POST /items`, `PUT /items/{item_id}`, and `DELETE /items/{item_id}`.
- Return appropriate status codes such as `200`, `201`, `404`, and `204`.


### 🛠️	Add Data Validation and Error Handling

#### Description
Use Pydantic models to validate request bodies and return meaningful error messages.

#### Requirements
Completed program should:

- Create request/response models with Pydantic.
- Validate that `name` is not empty when creating or updating an item.
- Return a helpful JSON error message when an item is not found.

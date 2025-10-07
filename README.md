## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. 

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/posts` | GET | READ | Get all posts
`api/posts/<int:pk>` | GET | READ | Get a single post
`api/posts`| POST | CREATE | Create a new post
`api/posts/<int:pk>` | PUT | UPDATE | Update a post
`api/posts/<int:pk>` | DELETE | DELETE | Delete a post


## Installation

1) Clone my [repository](https://github.com/whooaami/VRB) to install project:

```bash
git clone https://github.com/whooaami/VRB
```

2) Open this project in your IDE.

3) Create virtual environment:
```bash
python3.9 -m venv .venv
```

4) Activate virtual environment:
```bash
source .venv/bin/activate
```

5) Install all required libraries:
```bash
poetry install
```

6) To run server:
```bash
uvicorn main:app --reload
```

7) To run tests:
```bash
pytest
```

8) To run docker:
```bash
docker-compose -d --build
```

9) Test my endpoints using Swagger UI instead of Postman:
```bash
http://127.0.0.1:8008/docs
```

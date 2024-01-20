# Overview
This is [FastAPI](https://fastapi.tiangolo.com/) application with mock implementation of [Open Insurance API specification](https://github.com/The-Open-Insurance-Initiative/API-spec). The original spec has been improved with several model changes to be consistent with OpenAPI conventions.

To be used for demo purposes of a 3rd party schema for Insurance API integrations.

# Run with Docker
Build:
```docker build -t fast-api-opin-example .```
Run:
```docker run -d --name fast-api-opin-example-container -p 80:80 fast-api-opin-example    ```
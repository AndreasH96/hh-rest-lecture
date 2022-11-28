# Halmstad University REST guest lecture

This repo is for showing basic API development for a lecture at Halmstad University. It covers multiple concepts:

*   API Endpoints
*   Schema validation
*   Testing and pre-commit hooks
*   Basic data transition between frontend and backend 

This basic API is built in python with [FastAPI](https://fastapi.tiangolo.com/)

To run :
    
        uvicorn app.main:application --host 0.0.0.0 --port 8000

To run with live reload:
         
         uvicorn app.main:application --reload --host 0.0.0.0 --port 8000

Uses [pre-commit](https://pre-commit.com/#intro) in order to perform tests before a commit is approved. 
You might need to run `pre-commit install` to set it up (and install pre-commit of course).

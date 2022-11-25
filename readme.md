# Halmstad University REST guest lecture

This repo is for showing basic API development for a lecture at Halmstad University. It covers multiple concepts:

*   API Endpoints
*   Schema validation
*   Testing and precommit hooks

This basic API is built in python with [Flask](https://flask.palletsprojects.com/en/2.2.x/)

To run :
    
        flask -app myapp/app run

Uses [pre-commit](https://pre-commit.com/#intro) in order to perform tests before a commit is approved. 
You might need to run `pre-commit install` to set it up (and install pre-commit of course).

# Boilerplate-Async-Tasks
Boilerplate for building a web application to run asynchronous tasks with FastAPI and Celery 


## Local development

### Environment Vairables

    APPLICATION_NAME=""
    APPLICATION_DESCRIPTION=""

    LOG_LEVEL="DEBUG"

    SENTRY_DSN=""


## Unit Test

    # run pytest
    pytest


### Build and Run

1. run without build an image

Run the 'local' environment

    uvicorn app.app:app --reload --host 0.0.0.0 --port 5000


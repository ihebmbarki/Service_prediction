# Machine learning as a microservice in python
Prediction-service (eyes scan) 

This is an example to service machine learning as a microservice in python.
The model predicts ocular diseases by given settings.

# Project Tasks

1. Resize and preprocess image

2. Load machine learning model

3. Save model pickle

4. Input the image and predict

5. Return the results in form of json

6. Load json and create model


# Setup the Environment
![alt text](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)
FastAPI framework, high performance, easy to learn, fast to code, ready for production
# Installation
```
$ pip install fastapi

---> 100%
```
You will also need an ASGI server, for production such as Uvicorn or Hypercorn.
```
$ pip install "uvicorn[standard]"

---> 100%
```
Run the server with:
```
$ uvicorn main:app --reload

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

> You can install all of these with pip install "fastapi[all]"


#  Save and Load Machine Learning Models in Python

>Installation

```
pip3 install -r requirements.txt 

```





# Interactive API docs

Now go to http://127.0.0.1:8000/docs.

You will see the automatic interactive API documentation (provided by Swagger UI):

<img width="1440" alt="Screen Shot 2022-03-26 at 2 45 14 PM" src="https://user-images.githubusercontent.com/45261121/160242275-b9481d70-e3b7-4298-960f-bc82038a1e66.png">


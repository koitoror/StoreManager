[![Build Status](https://travis-ci.com/koitoror/StoreManager.svg?branch=ft-api-endpoints-v1-161242038)](https://travis-ci.org/koitoror/StoreManager)
[![Coverage Status](https://coveralls.io/repos/github/koitoror/StoreManager/badge.svg?branch=ft-api-endpoints-v1-161242038)](https://coveralls.io/github/koitoror/StoreManager?branch=ft-api-endpoints-v1-161242038)

# StoreManager
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.

## Requirements
Have the following set up on your local environment before getting started

1. [python 3.x](https://www.python.org/downloads/)
2. [Git](https://git-scm.com)
3. Working browser or [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?utm_source=chrome-app-launcher-info-dialog)

## Installation
For the UI designs to work you need a working browser like google chrome or mozilla firefox

Clone the repository into your local environment

```
git clone https://github.com/koitoror/StoreManager.git
```

Change directory into StoreManager
```
cd StoreManager/UI
```

Run `index.html` file in your browser

UI link for gh-pages

```
https://koitoror.github.io/StoreManager/UI/
```

## API Installation
To set up StoreManager API, make sure that you have python3, postman and pip installed.

Use [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) for an isolated working environment.

Clone the Repo into a folder of your choice
```
git clone https://github.com/koitoror/StoreManager.git
```

Create a virtual enviroment.
```
virtualenv venv --python=python3
```

Navigate to api folder.
```
cd StoreManager
```

Install the packages.
```
pip3 install -r requirements.txt
```

Set environment variables for 
>`SECRET`,
>`FLASK_CONFIG`
> `SECRET` is your secret key
> `FLASK_CONFIG` is the enviroment you are running on. Should be either `Production`, `Development` or `Testing`. NOTE: its case sensitive


## API Usage

To get the app running...

```bash
$ python run.py run
```

Open root path in your browser to test the endpoints. 
You can also use Postman or any other agent to test the endpoints

## Test

To run your tests use

```bash
$ python run.py test
```

To test endpoints manually fire up postman and run the following endpoints

**EndPoint** | **Functionality**
--- | ---
GET  `/api/v1/products` | Fetch all products
GET  `/api/v1/products/<productId>` | Fetch a single product 
POST  `/api/v1/products` | Create anproduct
PUT  `/api/v1/products/<productId>` | Modify a product
DELETE  `/api/v1/products/<productId>` | Delete a product
GET  `/api/v1/sales` | Fetch all sales
GET  `/api/v1/sales/<saleId>` | Fetch a single sale 
POST  `/api/v1/sales` | Create a sale
PUT  `/api/v1/sales/<saleId>` | Modify a sale
DELETE  `/api/v1/sales/<saleId>` | Delete a sale


# API Documentation
Once app server is running you can view API documentation from
```
http://127.0.0.1:5000/
```

Heroku Link to app server is running where you can view API documentation from
```
https://store-manager-ke.herokuapp.com/
```

# Product Api
API for product management using Django
  
It was developed using **Django** and **Postgres Database**, with Python on version 3.7.2, Django on 2.1.5 and Postgres on 11.

## Endpoints

The api has six endpoints:

### 1. Authentication Endpoints

This API uses JWT Authentication, so accessing the endpoints requires an access token.

**POST** `/api/token/`: Receives an `username` and `password` for generates the access token and refresh token, valid for 5 minutes.

**POST** `/api/token/refresh`: Receives an `refresh` token for generates a new access token.

### 2. Category Endpoints

Endpoints to Create, Update, Retrieve and Delete category of products.

**POST** `/categories/`: Receives an category object for create it.

**GET** `/categories/`: Retrives all categories stored in database.

**GET** `/categories/<category_id>/`: Retrieves one specific category by id.

**PUT** `/categories/<category_id>/`: Receives an category object and its id for update it.

**DELETE** `/categories/<category_id>/`: Removes one specific category by id.

### 3. Product Endpoints

Endpoints to Create, Update, Retrieve and Delete products.

**POST** `/products/`: Receives an product object for create it.

**GET** `/products/`: Retrives all products stored in database.

**GET** `/products/<product_id>/`: Retrieves one specific product by id.

**PUT** `/products/<product_id>/`: Receives an product object and its id for update it.

**DELETE** `/products/<product_id>/`: Removes one specific product by id.


## Instructions for running the project

**1. Install `docker`.**

```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test"
sudo apt update
sudo apt install docker-ce
```

**2. Install `docker-compose`**

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

**3. Create containers**
```
sudo docker-compose build
```

**4. Create admin superuser**
```
docker-compose run web python manage.py createsuperuser
```

After run this command, choose your username, email and password for superuser. Save this, will be necessaire for generate access token.


**6. Start container**
```
sudo docker-compose up
```

**Opcional: Run Tests**

```
sudo docker-compose run web rake test

```

After that you can access the api in `http://localhost:8004/`


## How to consume api endpoints

**1. Generate access token.**

Send a POST request for endpoint `/api/token/` with username and password superuser creates before. You will receive a response JSON like this:

```
{
   "refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0ODM3MTczOCwianRpIjoiYTE2MjM3YjJjOWQyNGIyZmEwYjcxOTU4Mzg4ZWMzZTUiLCJ1c2VyX2lkIjoxfQ.v2IpARZ32HmNnprJqY5KK-RKnes1aeDXYx01gp7fKn0",
   "access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ4Mjg1NjM4LCJqdGkiOiJkODVmZDY5OGQxMGE0MTJhOTcxODRmYjIyNzYwMzc0NiIsInVzZXJfaWQiOjF9.Fr-18GsoCV3sUtM5ZQlV6h95BZNRsor1Ou6Wo1PwODU"
}
```

put the `access` token inside your header requests, like this:

`Authorization: Bearer <token>`

**2. Example of an endpoint call.**

### REQUEST

`
GET http://localhost:8004/products/
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ4Mjg1ODU5LCJqdGkiOiIwN2E2NWU1NWIzMjc0YmNkODY2YmIwNjdkYWEzZWRjNiIsInVzZXJfaWQiOjF9.j8a8zf05KEy0qeRr845yEdZjmFJlBYWn7K9ehNZGdQc
`

### RESPONSE

`
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "category": {
                "id": 1,
                "name": "Candy",
                "created_at": "2019-01-23T21:21:51.986129-02:00",
                "updated_at": "2019-01-23T21:21:51.986145-02:00"
            },
            "name": "Chocolate",
            "size": 1,
            "price": "2.50",
            "created_at": "2019-01-23T21:22:22.175681-02:00",
            "updated_at": "2019-01-23T21:22:22.175690-02:00"
        }
    ]
}
`

# Simple Shop
## Description
This is a simple shop api that allows you to create, read, update and delete products,orders and deliveries. 
 It uses token based authentication. You can also create a new user and login to get a token or logout to delete a token.
## API Endpoints
- api/product/  (GET) => list all products
- api/product/ (POST) => create a new product 
- api/product/pk/ (GET) => retrieve a product
- api/product/pk/ (PUT) => update a product 
- api/product/pk/ (DELETE) => delete a product 
---
- api/order/ (GET) => list all orders 
- api/order/ (POST) => create a new order 
- api/order/pk/ (GET) => retrieve an order 
- api/order/pk/ (PUT) => update an order 
- api/order/pk/ (DELETE) => delete an order 
---
- api/delivery-center/ (GET) => list all delivery centers 
- api/delivery-center/ (POST) => create a new delivery center 
- api/delivery-center/pk/ (GET) => retrieve a delivery center
- api/delivery-center/pk/ (PUT) => update a delivery center 
- api/delivery-center/pk/ (DELETE) => delete a delivery center 
---
- api/delivery/ (GET) => list all deliveries 
- api/delivery/ (POST) => create a new delivery 
- api/delivery/pk/ (GET) => retrieve a delivery 
- api/delivery/pk/ (PUT) => update a delivery 
- api/delivery/pk/ (DELETE) => delete a delivery 

------

- auth/create-user/ (POST) => create a new user 
- auth/login/ (POST) => create a new token
- auth/logout/ (POST) => delete a token


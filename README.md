# GoT Quotes microservice in Python

```
PLEASE Read the following link before start coding:
https://github.com/NetflixMicroservices/caveats
```

## Description
A very simple GoT quotes service example in Python, using Flask.

## Endpoints

### Quote by id

Numeric id in the request. 

```
    GET /api/quote/<quoteid>
```
JSON response.

```
   {
      "quote" : "Hodor!"
   }
```

### Random quote

```
    GET /api/quote/random
```
JSON response.

```
   {
      "quote" : "Hodor!"
   }
```

### Random quote

```
    GET /api/quote/random
```
JSON response.

```
   {
      "quote" : "Hodor!"
   }
```

### Healthcheck

Used for Prana and Netflix OSS.

```
    GET /healthcheck
```
JSON response.

```
   {
      'status': 'ok'
    }
```

### Status

Used for Prana and Netflix OSS.

```
    GET /Status
```
Text response.

```
    Eureka!
```

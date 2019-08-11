# DJANGO, GRAPHQL, DOCKER

A project demonstrating how to create a GraphQL API powered by Django and running on docker containers

## Features
1. GraphQL API complete with user authentication by use of Json Web Tokens
2. Postgres database running on its own container in port `5432`
3. Gunicorn as the application server on port `8000`
4. Nginx for serving static and media files in production. Accessible on port `1337`
5. Containerization of everything using docker

## Prerequisites
For this project to run on your machine you must have installed `Docker` and `docker-compose`

##  Running the project

1. Clone the project repo: https://github.com/samwelkanda/django_graphql_docker.git
2. Run the project in development mode using the following commands
```cmd
docker-compose up -d --build
$ docker-compose exec web python manage.py migrate --noinput
```

3. Use the following commands to run the project in production
```cmd
docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

## GraphQL

To access the API, navigate to http://127.0.0.1:8000/graphql/

Test the API with the following

### View all events listed
```gql
query{
  events{
    id
    name
    url
  }
}
```

### Add a new event

```gql
mutation{
  createEvent(
    name: "Launch Party/"
    url: "https://liftoff.com/"
  ){
    id
    name
    url
  }
}
```
### Get the last 2 events

```gql
query{
  events(last:2){
    name
  }
}
```

### Query by position and keyword

```gql
query{
  events(first:3, search:"king"){
    id
    name
    url
  }
}
```
### Get a list of all users
```gql
query{
  users{
    id
    username
    email
  }
}
```
### Create a user

```gql
mutation{
  createUser(username:"king", email:"king@og.com", password:"therealest"){
    user{
      id
      username
      email
    }
  }
}
```

### Authenticate a user

mutation{
  tokenAuth(username:king, password:"therealest"){
  token
  }
}
 

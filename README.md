# Count the word occurences in an article

## Summary
To find how often the input word is being referenced in a wikipedia article.

In order to implement this, scrape 10 articles randomly from wikipedia store the same in database and then count the occurance.

Implemented using Docker. 

## Release
- 

## Pre-Requisite
- Docker should be installed
- Docker hub account should be created

## Deployment steps
### Step1
- Create a Docker image using the Dockerfile
- Push the Docker image to DockerHub which will be referenced in next steps
    - cd /app
    - docker build -t <username>/crawler:1.4 .
    - docker push <username>/crawler:1.4
    - cd ../flaskapp/
    - docker build -t <username>/flask-app:1.4 .
    - docker push <username>/flask-app:1.4

### Note 1:
- In this process, i have used **wikipedia** package in order to crawl the wiki pages.
But we can also make use of **beautifulsoup** and **requests** packages in order to scrape the same.

### Note 2:
- I have hard coded user name and password while getting MySQL connection. We can store these as environment variables and use accordingly.

### Step2
- run **docker-compose up** command
- This will create the containers listed in docker-compose file and create network between them.

### Step3
- access the flask application from web and input the word you want to search
- example
    - when access http://127.0.0.1:5000/ , it will print hello world
    - if you want the occurance of word 'taxi', http://127.0.0.1:5000/taxi
    - same way, we can search for the occurance of any word
- Application will find the number of times its present in the article and output the same in json format.
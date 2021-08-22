# Counting a word occurance in an article

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
- Create a Docker image using the Dockerfile in /app directory
- Push the Docker image to DockerHub which will be referenced in next steps

### Note
- In this process, i have used **wikipedia** package in order to crawl the wiki pages.
But we can also make use of **beautifulsoup** and **requests** packages in order to scrape the same.

### Step2
- run **docker-compose up** command

### Step3
- access the flask application from web and input the word you want to search
ex : if you want the occurance of word 'taxi', 
    http://127.0.0.1:5000/taxi
- Application will find the occurance and output the same
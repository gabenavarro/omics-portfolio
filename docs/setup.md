# Setup Guide for Omics-Portfolio

Welcome to the setup guide for `Omics-Portfolio`. This guide will walk you through the steps to get your portfolio up and running in a Docker container.


## 1. Prerequisite

Before proceeding, ensure you have the following installed:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/downloads) (for cloning the repository)

If hosting on cloud server, such as AWS, GPC, or Azure, please make an account and make sure you have all the appropriate permissions.

## 2. Local Development

### Setup

* Clone repository to your local drive

```bash
# Clone repository
git clone git@github.com:gabenavarro/omics-portfolio.git
# Jump into repository
cd ./omics-portfolio
```

* Build docker image from docker file

```bash
# Build image
docker build -f Dockerfile.dev -t omics-portfolio:dev .
```

* Run the docker container from docker image

```bash
# Run container
docker run -d -p 8877:8877 \
  --name omics-portfolio-dev \
  -v $(pwd)/:/app/ \
  omics-portfolio:dev
```

* Test run time locally

```bash
# In docker terminal as part of VSCode
gunicorn -w 4 -b 0.0.0.0:8877 local:server
```


### Rebuilding

In case you need to rebuild your docker image, follow these commands

```bash
# Stop and remove current container
docker stop omics-portfolio-dev \
&& docker rm omics-portfolio-dev \
# Re build docker image 
&& docker build -f Dockerfile.dev -t omics-portfolio:dev . \
# Run image container
&& docker run -d -p 8877:8877 \
  --name omics-portfolio-dev \
  -v $(pwd)/:/app/ \
  omics-portfolio:dev
```

## 3. Testing and Accessing the Portfolio

* Test

To test your local build, open your dockerized environment and run the following command to launch a local development server.

```bash
  gunicorn -w 4 -b 0.0.0.0:8877 app:server
```

* Access

Open your web browser and go to `http://localhost:8877`. You should now see your Omics-Portfolio running.


## 4. Customization
To customize your portfolio, edit the Dash application files in the repository and rebuild the Docker image following Step 2 and 3.


Thank you for using `Omics-Portfolio`. We hope this guide helps you easily set up your scientific portfolio using Docker.
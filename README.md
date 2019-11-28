#### This repo shows how to connect to SQLDW from a remote AML Compute using pyodbc & custom AML+ODBC docker image. 

**Create a custom docker image using Microsoft’s Azure ML Base Image to install ODBC drivers**

*Pre-requisites:*
1. Install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest) on your local machine
1. Install [Docker Desktop](https://docs.docker.com/docker-for-windows/install/)

*To create custom AML + ODBC base image:*
1. *To create your docker file:*

    1. Create a directory: `mkdir <your dir name>`

    1. Change to directory: `cd <your dir name>`

    1. Create a new docker file (without any extension) using any editor: e.g. `vim Dockerfile`
    1. Add the following code to your dockerfile to install odbc driver:
    ```
    FROM mcr.microsoft.com/azureml/base:latest
    RUN apt-get update
    RUN apt-get install locales
    RUN locale-gen en_US.UTF-8
    RUN update-locale LANG=en_US.UTF-8
    
    # Install MS SQL v13 driver for Odbc
    RUN apt-get install -y curl
    RUN apt-get install apt-transport-https
    RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
    RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
    RUN exit
    RUN apt-get update

    RUN ACCEPT_EULA=Y apt-get install -y msodbcsql
    RUN apt-get install -y unixodbc-dev
    ```
    1. Build docker image using command: `docker build -t <docker image name> . `
    (this dot is part of the command and signifies that the dockerfile is in the current working directory)​

1. *Add the image to Azure AMLS Container Registry:*

    1. Tag the image using the following command:

    `docker tag <docker image name> <container login server>/<image name>

    e.g. `docker tag mydockerimg mycontainerregistry.azurecr.io/myimg`

      **Note**: In the above step use the container registry from your AMLS workspace. `<container login server>` details can be found under access keys of your AMLS container registry resource.

    1. Now login to your Azure container registry using : `az acr login --name <container name>`

    1. Push the docker image to the container registry:

    `docker push <container login server>/<image name>`

    e.g `docker push mydockerimg mycontainerregistry.azurecr.io/ myimg


Now the image can be used to create environment for your experiments! 😊

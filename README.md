# Data Mining Challenge
In this repository, I have developed a Python application to scrape all shoe items under https://www.zalora.com.my/ 
website and for the brand “Aldo” under the filter “Occasion” “Casual”.


In order to scrape all shoes, I have scrape all the shoes from following links which address all the shoes for women and men.

https://www.zalora.com.my/women/shoes/
https://www.zalora.com.my/men/shoes/

I have also scrape all the shoes for brand “Aldo” under the filter “Occasion” “Casual”, using the following link:

https://www.zalora.com.my/women/shoes/?from=header&occasion=Casual&brand=aldo

The output file, will be a json file which has the following fields:
Brand, Actual price, Discounted price, link to the image of the product.


# Dockerized Flask application on EC2
1- Create a Linux virtual machine in the Azure portal:
Azure virtual machines (VMs) can be created through the Azure portal. The Azure portal is a browser-based user interface to create Azure resources. This quickstart shows you how to use the Azure portal to deploy a Linux virtual machine (VM) running Ubuntu 18.04 LTS. To see your VM in action, you also SSH to the VM and install the NGINX web server.
If you don't have an Azure subscription, create a free account before you begin.
Guideline:
https://docs.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-portal

2- Open ports to a virtual machine with the Azure portal:
( we need to open a port in our virtual linux server to let applications from outside the server can send their data to the dockerized Flask application on the linux server)
Guideline:
https://docs.microsoft.com/en-us/azure/virtual-machines/windows/nsg-quickstart-portal

3- Copy files located in Dockerized_FlaskApp folder on Github to a Folder created in linux server using Filezilla application

4- Installing Docker CE on an AWS EC2 instance running Ubuntu 16.04
Guideline:
https://medium.com/@cjus/installing-docker-ce-on-an-aws-ec2-instance-running-ubuntu-16-04-f42fe7e80869

5-Dockerize Flask Application:
(Guideline:https://medium.com/@tasnuva2606/dockerize-flask-app-4998a378a6aa)
 - Enter to the Dockerized_FlaskApp folder inside linux vps
 - Create Docker image using docker file:

 Run the following command to create the docker image from src directory, Pass in the -t parameter to name your image fraud-app.
 ```bash
$ docker image build -t fraud-app .

#Verify that your image shows in your image list:
$ docker image ls

#Run the docker container
$ docker run -p 8080:8500 -d fraud-app

#The -p flag maps a port running inside the container to your host. In this case, we're mapping the Python app running on port 8500 inside the container to port 8080 on your host.(here, host is EC2 vps, and port 8080 has been opened based on step2)
```
## Test the docker application:
```python
# Need to run below python command from the other machine (e.g. your mac or windows which has python already installed)
python Veltra_client_request.py
```
# Useful links to read:
* Turning Machine Learning Models into APIs in Python 
(https://www.datacamp.com/community/tutorials/machine-learning-models-api-python)
* Dockerize Your Flask Application
(https://medium.com/@tasnuva2606/dockerize-flask-app-4998a378a6aa)
* Docker Made Easy for Data Scientists
(https://towardsdatascience.com/docker-made-easy-for-data-scientists-b32efbc23165)
* Build a Docker Container with Your Machine Learning Model
(https://towardsdatascience.com/build-a-docker-container-with-your-machine-learning-model-3cf906f5e07e)
* Host your python flask on AWS EC2
(https://medium.com/dev-genius/host-your-python-flask-on-aws-ec2-91735aa7127a)

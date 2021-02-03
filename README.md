# Data Mining Challenge
In this repository, I have developed a Python application to scrape all shoe items under https://www.zalora.com.my/ 
website and for the brand “Aldo” under the filter “Occasion” “Casual”.


In order to scrape all shoes, I have scrape all the shoes from following links which address all the shoes for women and men.

https://www.zalora.com.my/women/shoes/
https://www.zalora.com.my/men/shoes/

I have also scrape all the shoes for brand “Aldo” under the filter “Occasion” “Casual”, using the following link:

https://www.zalora.com.my/women/shoes/?from=header&occasion=Casual&brand=aldo

The output file will be a json file which has the following fields:
Brand, Actual price, Discounted price, link to the image of the product.


# Setting up the application on Docker
1- To run this application, the docker software have to be installed on the host machine.

2- Pull the  application-container folderto the host machine.

3- Enter to the application-container folder inside the host machine.

4- Create Docker image using docker using following command:

 ```bash
$ docker image build -t zalora-app .

#Run the docker container
$ docker run -p 8080:8500 -d fraud-app

#The -p flag maps a port running inside the container to your host. In this case, we're mapping the Python app running on port 8500 inside the container to port 8080 on your host.(here, host is EC2 vps, and port 8080 has been opened based on step2)
```
## Test the docker application:
```python
# Need to run below python command from the other machine (e.g. your mac or windows which has python already installed)
python Veltra_client_request.py
```


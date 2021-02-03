# Data Mining Challenge
In this repository, I have developed a Python application to scrape all shoe items under https://www.zalora.com.my/ 
website and for the brand “Aldo” under the filter “Occasion” “Casual”.


In order to scrape all shoes, I have scrape all the shoes from following links which address all the shoes for women and men.

https://www.zalora.com.my/women/shoes/

https://www.zalora.com.my/men/shoes/

I have also scrape all the shoes for brand “Aldo” under the filter “Occasion” “Casual”, using the following link:

https://www.zalora.com.my/women/shoes/?from=header&occasion=Casual&brand=aldo

The output file will be a json file which has  all the shoe products with the following fields:
Brand, Actual price, Discounted price, link to the image of the product.


# Setting up the application on Docker
1- To run this application, the docker software have to be installed on the host machine.

2- Pull the  application-container folder to the host machine.

3- Enter to the application-container folder inside the host machine.

4- Create Docker image from Dockerfile using following command:

 ```bash
$ docker image build -t zalora-app .
 ```
5- Run the docker container from the image created and run the python application.
```
$ sudo docker run -it -v ~/application-container:/app zalora-app Crawling_app.py
```
#The -v flag run the image with sharing "application-container" folder on the host machine with "app" folder on the container. So we will be able to save and access the output file (json file) on the host machine as well.





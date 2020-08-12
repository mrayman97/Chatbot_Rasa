# Chatbot Rasa
This is an AI project, it's a chatbot realised with Python used for AI algorithms like. 
  And behind i used both "Rasa NLU and Rasa Core" framework.

### Getting started
To start working in this project, you need to fulfill the requirements below :
* Docker (+19.03)
* Docker-compose (+1.25)

To run the application :  
>`git clone [GIT-URL]`  
>`cd chatbot_rasa`    
>`docker-compose up -d --build`  

To train & create model :    
>`docker run \
   -v $(pwd):/app \
   rasa/rasa:latest \
   train \
     --domain domain.yml \
     --data data \
     --out models`  
     
To run model : 
>`docker run \ 
 -v $(pwd):/app \
 rasa/rasa:latest \
 run --enable-api -m models/name_of_folder_in_model.tar.gz`  
 
URL to use the Chatbot in your local :
>`http://localhost:5055/index.html`

To have a look of backend with Postman :   
>`http://localhost:5050/webhooks/rest/webhook/`
 
 
## Screenshots:

![ScreenShot]()

![ScreenShot]()
 

**Happy Coding ! :D**

**By : Ayman JAWADI**


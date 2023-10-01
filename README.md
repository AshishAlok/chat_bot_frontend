# chat_bot_frontend


How to run through bash in linux machine:-

step1:-
Make the script executable using the chmod command:
chmod +x build_and_run.sh

step2:-
un the script in your terminal to execute both steps by the following commands:

./build_and_run.sh

How to run through bash in windows machine:-

step1:- run the command
build_and_run.bat



How to run (Through git hub ):-


step1:- clone the chat_bot_frontend repository on your local machine.
step2:- go into the folder cloned folded where Dockerfile is present.

The below command will create a docker image with name frontend.
step3:- run the command in terminal:- docker build -t frontend .


The below command will run the docker image of the backend in a container whose name will be frontend-container
step4:- docker run -d -p 8501:8501 --name frontend-container frontend



**HOW to acces the site:-

- open a browser
- search localhost:8501
- you will be directed to the frontend
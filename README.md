# Distributed queuing with Flask, Celery, and RabbitMQ

This repository will guide you through examples that you can use to implement
powerful queue patterns using RabbitMQ as the message broker.
## config gmail
### in Google Account Setting, turn on 2 step Authentication 
### in Google Account Setting,Generate 16-character "app password"
### in Gmail setting, Enable IMAP

 
```bash
    sender_email = "sender@gmail.com"
    sender_password = "**** **** **** ****" #this is a 16-character "app password" 
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
```


```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.12-management
```

## Start Celery

Celery needs to get started. First, make sure RabbitMQ is running by opening a terminal and running:

```
ps aux | grep rabbitmq
```


Start Celery by doing:

```bash
celery -A app.make_celery worker --loglevel INFO
```

## Start Flask

Start the Flask application with the following command:

```bash
flask --app app.main:flask_app run --reload
```


## Send a request for async processing

Create a new `POST` request to the running application to the `/send_email` endpoint. You can use the following `curl` command:

```bash
curl -X POST --header "Content-Type: application/json" --data '{"email": "receipient@gmail.com", "subject": "Merry_Xmas!", "body": "Just a test"}' http://localhost:5000/send_email
```

## Send a request for async processing with a response

Create a new `POST` request to the running application to the `/parse_exploits` endpoint. You can use the following `curl` command:

```bash
curl -X POST http://localhost:5000/parse_exploits
```

You will get a response that looks like the following:

```json
{
    "task_id": dcaaf5af-2aec-4ab1-b7ba-978fbb91d60b
}
```
You can then use the `task_id` to query the status of the task to see if it is complete. You can use the following `curl` command that will request the information to the endpoint `/check_task/<task_id>`:

```bash
curl -X GET http://localhost:5000/check_task/dcaaf5af-2aec-4ab1-b7ba-978fbb91d60b
```



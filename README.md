# Rabbit MQ Tutorial

### Docker commands
<hr/>

##### Spin a RabbitMQ docker container
```commandline
docker run --name rabbitmq -p 5672:5672 -p 15672:15672 -d rabbitmq:3-management
```
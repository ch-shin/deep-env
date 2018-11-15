#!/bin/bash
export JUPYTER_PASSWD="mypassword"
export JUPYTER_PORT="10000"
export DOCKER_HOST="tcp://0.0.0.0:2375"
export COMPOSE_PROJECT_NAME="test" # prevent duplicated docker-compose service name
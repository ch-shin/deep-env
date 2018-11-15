# deep-env
Launch your own deep learning environment with ease

## Pre-requisite
- `docker`
- `docker-compose`
- `nvidia driver`
- `cuda 9.0`
- `nvidia docker`

## Quickstart
### Clone `deep-backend/deep-env` repository
```
cd ~/
git clone https://github.com/deep-backend/deep-env.git
cd deep-env
```

### Set Jupyter configuration in config.sh

Change `config.sh` for your jupyter docker container. Make sure using unique `COMPOSE_PROJECT_NAME` to prevent any issues caused by duplicated container name. `docker-compose` use `COMPOSE_PROJECT_NAME` as prefix of container name. `DOCKER_HOST` is socket where the docker daemon is listening and you don't have to change it.

```bash
# in config.sh
export JUPYTER_PASSWD="mypassword"
export JUPYTER_PORT="8888"
export DOCKER_HOST="tcp://0.0.0.0:2375"
export COMPOSE_PROJECT_NAME="test"
``` 


### Launch Jupyter Notebook

```bash
./up-jupyter.sh
```

This step will takes some minutes for the first time.

Alternatively, you can launch jupyter notebook by setting environment variable in `config.sh` and running docker-compose command.

```bash
source ./config.sh
docker-compose up -d
```

#### Connect to Jupyter Notebook
On browser, connect to `HOST_IP:port` then type password as you set via environment variable `JUPYTER_PASSWD`. `port` is not necessarily same as `JUPYTER_PORT`; it depends how you port forward when you access via ssh, `ssh -L some_port:localhost:JUPYTER_PORT` for example.

- Your host's home folder is mounted to container's home folder `(/home/YOUR_USER_NAME)`
  - If you add or delete files on Jupyter Notebook, then this changes will eventually affects the files on host. Be **careful**.
- `--root_dir` of Jupyter Notebook is your home folder.

### Stop Jupyter Notebook

```bash
./down-jupyter.sh
```

Alternatively, you can stop jupyter container by setting environment variable in `config.sh` and running docker-compose command.

```bash
source ./config.sh
docker-compose down
```

## Using docker command with ease

If you are tired of typing `-H tcp://0.0.0.0:2375` as docker option for simple docker command or seeing `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?` errors, just add environment variable in `~/.bashrc` as followings:

```bash
# in ~/.bashrc
export DOCKER_HOST="docker -H tcp://0.0.0.0:2375"
```

And then, run `source` command.

```bash
source ~/.bashrc
```

Now you can use docker command without typing `-H tcp://0.0.0.0:2375` options for every docker command.

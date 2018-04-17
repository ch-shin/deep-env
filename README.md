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

### Set password to login your Jupyter Notebook
```
export JUPYTER_PASSWD=TYPE_PASSWD_YOU_WANT
```

### Launch Jupyter Notebook with `docker-compose`
This step will takes some minutes for the first time.
```
docker-compose up -d
```

#### Connect to Jupyter Notebook
On browser, connect to `HOST_IT:8888` then type password as you set via environment varible `JUPYTER_PASSWD`.

- Your host's home folder is mounted to container's home folder `(/home/YOUR_USER_NAME)`
  - If you add or delete files on Jupyter Notebook, then this changes will eventually affects the files on host. Be **careful**.
- `--root_dir` of Jupyter Notebook is your home folder.
- Port can be changed via `docker-compose.yml` (*default port: 8888*)
  - If you want to open Jupyter on port `30000`, then update `docker-compose.yml` as followings:

    ```
    version: '2.4'
      services:

      keras-py27-jupyter:
        image: encoredtechr/deepo:keras-py27-jupyter-cudnn7.0
        depends_on:
          - cuda-9-0_cudnn-7-0
        ports:
          - 30000:8888
          
    (...)
    ```

### Turn off Jupyter Notebook
```
docker-compose down
```

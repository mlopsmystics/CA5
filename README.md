# MLOPS CA5

## setup

## Change the folder to build jenkins image

```
cd DockerFileForJenkins
```

## Build the Jenkins file using command

```
docker build --tag jenkinsimage .
```

## Run the Jenkins Image

```
docker run --name jenkins -d -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home jenkinsimage
```

### for windows to create env

- create a virtual environment

```bash
python -m venv venv
```

- set execution policy

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

- activate the virtual environment

```bash
venv\Scripts\activate
```

- install pip

```bash
python.exe -m pip install --upgrade pip
```

- run makefile

```bash
make install
```

### for linux and mac

- create a virtual environment

```bash
python3 -m venv venv
```

- activate the virtual environment

```bash
source venv/bin/activate
```

- run makefile

```bash
make install
```

## For jenkins image
- Link for tutorial: https://www.youtube.com/watch?v=pMO26j2OUME
- Get Jenkins Image from dokcer
```
docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```
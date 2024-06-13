# Containers

## Prerequisites

Before proceeding, ensure that Docker is installed on your system.

## Pulling images from the Docker Hub

To run a container, you need an image from which the container will be created.

Think of a Docker image as a blueprint or template for creating containers. Just like a class in object-oriented programming can be used to create multiple objects, an image can be used to create multiple containers.

The [Docker Hub](https://hub.docker.com/) is a public registry of Docker images, containing many official images published for popular tools such as [MySQL](https://hub.docker.com/_/mysql) and [Node.js](https://hub.docker.com/_/node), as well as images uploaded by users.

For this exercise, we will download a Python image.

```
$ docker pull python:3.10
Unable to find image 'python:3.10' locally
3.10: Pulling from library/python
<snip>
Status: Downloaded newer image for python:3.10
```

To view local Docker images on your computer:

```
$ docker images
REPOSITORY    TAG   IMAGE ID      CREATED        SIZE
python        3.10  7687dd13da73  2 months ago   1GB
```

## Running and deleting containers

This command runs an interactive terminal session inside a Docker container based on the Python 3.10 image.

```
$ docker run -it python:3.10
Python 3.10.14
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Notice that the container opens up a Python shell. This is the default behaviour set by the image's creator. If you want to open a Bash session instead, you can do so by overriding the 'entrypoint'.

`<container-id>` is a unique identifier for your container and will be different to mine.

```
$ docker run -it --entrypoint bash python:3.10
root@<container-id>:/# ls
bin   dev  home  lib64	mnt  proc  run	 srv  tmp  var
boot  etc  lib	 media	opt  root  sbin  sys  usr
```

After exiting from the container, the container will remain in an 'Exited' state.

```
$ docker ps -a
<container-id>    python:3.10    "python3"    9 seconds ago    Exited (0)
```

It won't be automatically deleted; you'll need to explicitly delete it when you no longer need it.

```
$ docker rm <container-id>
```

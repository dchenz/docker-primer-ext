# Images

In the previous tutorial, we learned that an image serves as a read-only template for creating a container.

We will now explore what an image includes: it encapsulates the steps required, starting from a "base" image, including installing dependencies, copying necessary files, and more.

## Dockerfiles

A Dockerfile is a text file that contain instructions for building a Docker image. An instruction within a Dockerfile is a directive that commands Docker to perform a specific action, altering the configuration and environment of the resulting container.

[See the documentation for available instruction types.](https://docs.docker.com/reference/dockerfile/)

Let's look at an example:

```dockerfile
# This is the base image. All images have a base image it starts from.
FROM python:3.10

# This sets the working directory for subsequent instructions.
WORKDIR /app

# Copy "requirements.txt" into the current directory.
COPY requirements.txt .

# Install the Python dependencies.
RUN pip3 install -r requirements.txt

# Copy all files from the context into the current directory.
COPY . .

# Set the command used when the container is run.
CMD ["flask", "run", "--host=0.0.0.0"]
```

### Image layers

Layers in an image represent incremental changes made to the image by each instruction. When building an image from a Dockerfile, Docker will execute each instruction inside a temporary container and store the resulting state as an image layer.

Caching is a key benefit of Docker image layers, especially for commands within `RUN` instructions that take a long time to complete. Try to place commands that rarely change, such as dependency installation or configuration, towards the top of the Dockerfile. Layers at the top will be cached as long as the layers above them remain unchanged.

```dockerfile
COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
```

Suppose we removed the `COPY requirements.txt .` and just did this.

```dockerfile
COPY . .

RUN pip3 install -r requirements.txt
```

If you make any edits to a Python file, Docker will reinstall dependencies during every build, regardless of whether the dependencies have changed or not. That would be very annoying...

In this next tutorial, you will learn how to build a Docker image.

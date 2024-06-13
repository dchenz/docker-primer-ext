# python-demo-app

```sh
# This command builds the image described by the Dockerfile.
# Make sure you're in the project root directory.
docker build . -t python-demo-app

# This command creates and starts a container to host the Flask app.
# It maps port 5000 on your computer to port 5000 on the container, allowing access to the app from your local machine.
docker run -p 5000:5000 python-demo-app

# Visit http://localhost:5000 while the container is running.
```

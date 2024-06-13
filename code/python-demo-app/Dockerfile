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

# Building Images

To create a Docker image using a Dockerfile, navigate to the root directory of your project and run the build command.

```sh
# The -t/--tag option is used to give your new image a name.
docker build . -t python-demo-app
```

By default, the Docker CLI will look for a text file named `Dockerfile`.

## Image Tags

Image tags are specified after the colon of a full image name. Images with different tags are considered distinct because each tag represents a version or variant of the image. It is typically used to track versions of an application.

The `latest` tag is used as the default tag when no tag is specified. The above build command will create an image called `python-demo-app:latest`. The following command does the same thing.

```sh
docker build . -t python-demo-app:latest
```

It is best practice to specify a tag when building a Docker image that you intend to deploy or publish. The `latest` tag may change if a newer image is built and uploaded. Instead, consider using something that uniquely identifies the image, such as a Git commit hash or a version number, as the contents of these images should remain unchanged.

In the 1st tutorial, the Python container was run using `docker run python:3.10`. If you had used `docker run python`, a 2nd Docker image would have been downloaded. This occurs because there is no locally cached `python:latest` image, as we previously pulled `python:3.10`.

```
REPOSITORY    TAG      IMAGE ID       CREATED         SIZE
python        latest   dfe7782074a6   6 days ago      1GB
python        3.10     7687dd13da73   2 months ago    1GB
```

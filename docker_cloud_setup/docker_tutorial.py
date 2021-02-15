## Docker tutorial

# Clone the repository by running Git in a container.
docker run --name repo alpine/git clone https://github.com/
docker/getting-started.git

# A Docker image is a private file system just for your container.
#It provides all the files and code your container needs.
getting-started BA$  docker build -t docker101tutorial .

# Start a container based on the image you built in the previous step.
#Running a container launches your application with private resources,
#securely isolated from the rest of your machine.
docker run -d -p 80:80 --name docker-tutorial
 docker101tutorial

 # Save and share your image on Docker Hub to enable other users to
 # easily download and run the image on any destination machine.
 docker tag docker101tutorial {userName}/docker101tutorial
 docker push {userName}/docker101tutorial

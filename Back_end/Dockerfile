# Set base image (host OS)
FROM python:3.9-slim

# RUN apk update
# RUN apk add make automake gcc g++ subversion python3-dev

# By default, listen on port 5000
EXPOSE 5001/tcp

# Set the working directory in the container
WORKDIR /Back_end


# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY flask-server.py .

# Specify the command to run on container start
CMD [ "python", "./flask-server.py" ]
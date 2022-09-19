# Set base image (host OS)
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /server


# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY flask-server.py .
COPY gpt.py .
COPY article_feed.py .
COPY credentials.py .


# # By default, listen on port 5000
EXPOSE 5001 

# Specify the command to run on container start
CMD [ "python", "./flask-server.py" ]
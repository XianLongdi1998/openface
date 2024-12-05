# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /App

# Copy the application files into the working directory
COPY . /App

# Install the application dependencies
RUN pip install Flask==3.0.3
RUN pip install Flask-Cors==4.0.1

# Define the entry point for the container
CMD ["python", "App.py", "runserver", "0.0.0.0:5999"]
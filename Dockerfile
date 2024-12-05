# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /App

# Copy the application files into the working directory
COPY . /App


RUN chmod 755 /App/openface
RUN chmod 644 /App/openface/FeatureExtraction.exe

RUN ls -l ./openface 
RUN ls -l /App/openface

# Install the application dependencies
RUN pip install Flask==3.0.3
RUN pip install Flask-Cors==4.0.1

# Expose port 5999
EXPOSE 5999

# Define the entry point for the container
CMD ["python", "App.py"]
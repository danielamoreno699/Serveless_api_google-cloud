# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container at /app
COPY main.py /app/
COPY requirements.txt /app/

# Download NLTK data (vader_lexicon)
#RUN python -m nltk.downloader vader_lexicon

# Make port 5000 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV FLASK_APP=main.py

# Run main.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]

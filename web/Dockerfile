# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server.py file to the working directory
COPY server.py .

# Expose port 5000
EXPOSE 5000

# Start the server
CMD [ "python", "server.py" ]

# Use an official Python runtime as a parent image
FROM python:3.10.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt  # Make sure you have a requirements.txt file with your dependencies

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable for Streamlit
ENV STREAMLIT_SERVER_PORT=8501

# Run app.py when the container launches
CMD ["streamlit", "run", "gui.py"]  # Replace "gui.py" with your Streamlit script name

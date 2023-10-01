REM Step 1: Build the Docker image for the frontend
docker build -t frontend .

REM Step 2: Run the Docker image in a container named frontend-container
docker run -d -p 8501:8501 --name frontend-container frontend

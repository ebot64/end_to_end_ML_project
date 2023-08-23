FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python3", "app.py"]
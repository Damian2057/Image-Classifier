FROM python:3.9.7-slim-bullseye

# Set the working directory
WORKDIR /category-module

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Copy the .env file (if needed)
COPY .env .

# Expose the port on which the app will run
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Command to run the application
CMD ["flask", "run"]

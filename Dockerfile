# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /QuickCommerce

# Copy the requirements file and install dependencies
COPY requirements.txt /QuickCommerce/
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /QuickCommerce/

# Expose the application's port (if needed)
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
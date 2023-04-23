FROM python:3.11-alpine
ENV PYTHONBUFFERED 1

WORKDIR /app
COPY requirements.txt .

# Remove all installed Python packages
RUN pip freeze | xargs pip uninstall -y || true

# Install the packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD python manage.py runserver 0.0.0.0:6969

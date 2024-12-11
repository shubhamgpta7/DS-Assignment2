FROM python:3.12-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV CLOUD_SQL_HOST="your-db-host"
ENV CLOUD_SQL_DATABASE_NAME="db_name"
ENV CLOUD_SQL_USERNAME="db_user"
ENV CLOUD_SQL_PASSWORD="db_user_password"
EXPOSE 8082

CMD ["python","main.py"]
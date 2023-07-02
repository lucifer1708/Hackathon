FROM python:3.10.6
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY . /app
EXPOSE 8000
EXPOSE 5432
EXPOSE 8150
ENV PYTHONPATH=/app

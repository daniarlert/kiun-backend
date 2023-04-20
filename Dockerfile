FROM python:3.11.2-slim as base

# Set virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.prod.txt .
RUN python -m pip install --upgrade pip && python -m pip install --upgrade -r requirements.prod.txt

FROM python:3.11.2-slim

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

EXPOSE $PORT

# Copy dependencies
COPY --from=base /opt/venv /opt/venv

# Set path
ENV PATH="/opt/venv/bin:$PATH"

# Copy project
COPY . .

# Run server
CMD gunicorn --bind 0.0.0.0:${PORT} config.wsgi

FROM python:3.11-slim
RUN apt-get update && apt-get install -y nodejs npm
WORKDIR /app
RUN pip install fastapi uvicorn pydantic mcp
COPY app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

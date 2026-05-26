FROM python:3.12-slim
LABEL authors="zshirwan"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir flask gunicorn

EXPOSE 5010

#CMD ["gunicorn", "--bind", "0.0.0.0:5010", "main:app"]
CMD ["python", "main.py"]


# docker build -t sampleflaskapp:test .
# docker run --rm -p 5010:5010 sampleflaskapp:test

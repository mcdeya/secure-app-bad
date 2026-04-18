FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install flask requests pytest

EXPOSE 5000

CMD ["python", "app/main.py"]

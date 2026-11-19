FROM python:3.14

WORKDIR /info

COPY student.py .

CMD ["python", "student.py"]
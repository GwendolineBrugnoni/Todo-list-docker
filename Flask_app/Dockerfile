FROM python:3.8
ADD main.py .
ADD templates templates
ADD requirements.txt .

RUN pip install -r requirements.txt
CMD ["python","./main.py"]
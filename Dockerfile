FROM python:3.9-slim
WORKDIR /litmus-github-action
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]
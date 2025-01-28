FROM python:alpine3.21

COPY api.py /app/
COPY utils.py /app/
COPY requirements.txt /app/

WORKDIR /app
RUN pip3 install -r ./requirements.txt

EXPOSE 2890
CMD [ "uvicorn", "api:api", "--host", "0.0.0.0", "--port", "2890"]
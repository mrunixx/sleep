FROM python:3.12

# set the working directory of the 
WORKDIR /sleep

# copy requirements
COPY ./requirements.txt /sleep/requirements.txt

# install requirements
RUN pip install --no-cache-dir --upgrade -r /sleep/requirements.txt

# copy source code
COPY . /sleep/backend

EXPOSE 8000

CMD ["fastapi", "run", "backend/server.py", "--host", "0.0.0.0", "--port", "8000"]
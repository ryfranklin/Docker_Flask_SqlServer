FROM python:3.9

COPY ./requirements.txt /app/requirements.txt

# Create app directory
WORKDIR /app

# Install app dependencies
RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

CMD ["flask", "run", "--host", "0.0.0.0"]

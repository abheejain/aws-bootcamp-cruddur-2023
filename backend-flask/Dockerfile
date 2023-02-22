FROM python:3.10-slim-buster

# Inside Container
# make new folder inside container 
WORKDIR /backend-flask

# Outside Container -> Inside Container 
#conotainer lib 
COPY requirements.txt requirements.txt

# Inside Container
# install python libraaries for App
RUN pip3 install -r requirements.txt

# Outside Container -> Inside container
# current dir to destination in container 
COPY . .


# set env variables
# Inside Container and will remain when container is runing 
ENV FLASK_ENV=development

EXPOSE ${PORT}
# CMD = Command

# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
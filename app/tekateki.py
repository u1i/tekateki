from bottle import Bottle, request, response
import json, os, redis, uuid
from random import randint
from datetime import datetime

max_requests_per_session = 5

app = Bottle()

# Default 404 handler
@app.error(404)
def error404(error):
    return("Nothing here.")

# Default 405 handler
@app.error(405)
def error405(error):
    return("Nothing here.")

@app.route("/")
def get_home():
    return dict({"message" : "Welcome! Ready for the challenge? Navigate to /start"})

@app.route("/start")
def challenge_start():
    return "huhu"

@app.route("/get_session", method='GET')
@app.route("/get_session", method='DELETE')
@app.route("/get_session", method='PUT')
@app.route("/get_session", method='GET')
def get_session1():
    return dict({"message" : "Uh-oh. The session endpoint doesn't like " + request.method + ". Try another method?"})


@app.route("/get_session", method='POST')
def get_session():
    session = str(uuid.uuid4())
    return dict({"message" : "Session is valid for " + str(max_requests_per_session) + " requests", "session": session})



# Initialization
# We need a Redis connection
if not "redis_host" in os.environ or not "redis_port" in os.environ:
        exit("ERROR: please set the environment variables for Redis host")

# Connect to the Redis backend
redis_host = os.environ['redis_host']
redis_port = os.environ['redis_port']
rc = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

rc.set("axway", "bla")

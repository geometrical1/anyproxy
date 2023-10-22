import os
import json
import requests
from dotenv import load_dotenv
from flask import Flask, request, Response
from waitress import serve

load_dotenv()
prod_mode = os.getenv("prod") == "1"
HOST = "0.0.0.0" if prod_mode else "127.0.0.1"
api_key = os.getenv("api_key")
port = os.getenv("port") or "8080"
if prod_mode:
    print("Production mode activated")
if api_key is None:
    raise ValueError("Api key is undefined. Please specify an api_key in the env.")
if api_key == "api_key_for_auth_goes_here" and prod_mode:
    print(
        "WARNING: Api key isn't changed. And prod_mode is set to true. Please change the api key for authentication."
    )
app = Flask(__name__)


@app.before_request
def access_check():
    """Middleware to check for authorization"""
    if request.headers.get("x-api-key") != api_key:
        return Response(response="Unauthorized access.", status=401)


@app.route("/request/get")
def get():
    """Proxy for GET requests"""
    content_type = request.headers.get("Content-Type")
    url = request.args.get("url")
    params = request.args.get("params")
    headers = request.headers.get("headers")
    request_to_send = requests.get(
        url=url,
        params=json.loads(params) if params is not None else {},
        headers=json.loads(headers) if headers is not None else {},
        data=request.data,
        timeout=500,
    )
    match content_type:
        case "application/json":
            return Response(
                response=json.dumps(
                    {
                        "status": request_to_send.status_code,
                        "body": str(request_to_send.content),
                    }
                ),
                status=200,
            )
        case "text/plain":
            return Response(response=request_to_send.content, status=200)
        case _:
            return Response(response="Invalid Content-Type.", status=400)


@app.route("/request/post", methods=["POST"])
def post():
    """Proxy for POST requests."""
    content_type = request.headers.get("Content-Type")
    url = request.args.get("url")
    params = request.args.get("params")
    headers = request.headers.get("headers")
    request_to_send = requests.post(
        url=url,
        params=json.loads(params) if params is not None else {},
        headers=json.loads(headers) if headers is not None else {},
        data=request.data,
        timeout=500,
    )
    match content_type:
        case "application/json":
            return Response(
                response=json.dumps(
                    {
                        "status": request_to_send.status_code,
                        "body": str(request_to_send.content),
                    }
                ),
                status=200,
            )
        case "text/plain":
            return Response(response=request_to_send.content, status=200)
        case _:
            return Response(response="Invalid Content-Type.", status=400)


if __name__ == "__main__":
    print("Serving app.")
    serve(app=app, host=HOST, port=port)

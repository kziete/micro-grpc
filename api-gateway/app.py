from __future__ import print_function

import grpc
from flask import Flask

import helloworld_pb2
import helloworld_pb2_grpc


app = Flask(__name__)


@app.route('/')
def hello_world():
    with grpc.insecure_channel('flask_service:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    return response.message


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

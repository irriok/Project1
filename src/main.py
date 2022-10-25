import sys
sys.path.append(".")
from src.app import views

import os
from flask import Flask, request, Response


app = Flask(__name__)

def main():
    new_request = views.APIView()
    new_request.post()

if __name__ == "__main__":
    main()


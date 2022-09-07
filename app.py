import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
  return "welcome"

@app.route("/howareyou")
def hello():
  return "how are you !!!!"

if __name__ == "__main__":
  app.run()

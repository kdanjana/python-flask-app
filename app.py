import os
from flask import Flask
app = flask(__name__)

@app.route("/")
def main():
  return "welcome"

@app.route("/howareyou")
def hello():
  return "how are you !!!!"

if name == "__main__":
  app.run()

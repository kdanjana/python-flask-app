import os
from flask import Flask
app = Flask(__name__)
#sets the background color of web page
#color_bkg = "red"
#setting up environment variable APP_COLOR
color_bkg = os.environ.get("APP_COLOR")

@app.route("/")
def main():
  print(color)
  return render_template("hello.html", color = color_bkg)

if name == "__main__":
  app.run()

print("api starting")
from flask import Flask
app =Flask(__name__)
@app.route("/ask")
def home ():
    return "running successfully"
if __name__=="__main__":
    app.run(debug=True)

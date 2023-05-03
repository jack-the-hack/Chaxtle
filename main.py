from flask import Flask, render_template, request
from AI import AIinst

Instance=AIinst()
Promptin=Instance.Promptin
app = Flask(__name__)

# Define the Promptin function
def get_response(input_text):
    # Call the Promptin function to get a response
    response = Promptin(input_text)
    return response

# Define the Flask routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get("msg")
    bot_response = get_response(user_input)
    return bot_response

if __name__ == "__main__":
    app.run()
from flask import Flask

# Create the Flask application object
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    return "Hello, Aneesh! Flask is running in WSL and welcome to your trial website"

# Run the app only if this file is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


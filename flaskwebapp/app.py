from flask import Flask

# from mod1 import greetings

# Create the Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/createuser', methods=['post'])
def hello():
    return 'Hello, World!'
@app.route('/home') 
def diplay():
    return "coming from home"


@app.route('/contactus')
def contact():
    return "call us at mobile number is 7842363997"
@app.route('/aboutus')
def aboutus():
    return "we are small start up company where provide training "
@app.route('/services')
def services():
    return "mern sd product"



# Run the app if this script is executed
if __name__ == '_main_':
    app.run(debug=True)
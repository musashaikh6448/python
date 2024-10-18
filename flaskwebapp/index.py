from flask import Flask,request,render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/createuser', methods=['post'])
def postreq():
    print(request.get_json())
    return 'user created'
@app.route('/home') 
def diplay():
    return render_template('index.html')

\

@app.route('/contactus')
def contact():
    return "call us at mobile number is 7842363997"
@app.route('/aboutus')
def aboutus():
    return "we are small start up company where provide training "
@app.route('/services')
def services():
    return "mern sd product"

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

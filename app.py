from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import mongodbconnect as mc

app = Flask(__name__)

@app.route("/")
def home():
    #home_data={"page":"home"}
    #return jsonify(home_data)
    print('Request for index page received')
    return render_template('index.html')
 
@app.route("/get-order/<order_id>")
def get_order(order_id):
    return jsonify(mc.get_order(order_id))

@app.route("/add-user", methods=['POST'])
def addOrder():
    order=request.json
    mc.create_new_order(order)
    return jsonify(order)

if __name__=="__main__":
    app.run(port="8080")

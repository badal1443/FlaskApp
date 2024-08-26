from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import mongodbconnect as mc

from os import environ

app = Flask(__name__)

@app.route("/")
def home():
    #home_data={"page":"home"}
    print('Request for index page received 123')
    #return jsonify(home_data)
    if environ.get('MONGO_DB_CONN') is not None:
      return render_template('index2.html')
    return render_template('index.html')
 
@app.route("/get-order/<order_id>")
def get_order(order_id):
    #return "hello"
    #return render_template('index.html')
    return jsonify(mc.get_order(order_id))

@app.route("/add-user", methods=['POST'])
def addOrder():
    order=request.json
    mc.create_new_order(order)
    return jsonify(order)

if __name__ == '__main__':
   app.run()

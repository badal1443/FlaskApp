from flask import Flask, request, jsonify
import mongodbconnect as mc

app = Flask(__name__)

@app.route("/")
def home():
    home_data={"page":"home"}
    return jsonify(home_data)
 
@app.route("/get-order/<order_id>")
def get_order(order_id):
    return jsonify(mc.get_order(order_id))

@app.route("/add-user", methods=['POST'])
def addOrder():
    order=request.json
    mc.create_new_order(order)
    return jsonify(order)

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0", port="5000")

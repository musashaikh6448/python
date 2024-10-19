from flask import Flask,request,jsonify
from pymongo import MongoClient


#create app
app=Flask(__name__)

#mongodb connection
client = MongoClient("mongodb://localhost:27017/")
db = client["flaskmongodb1"]   
usercol=db['mycollection']

def serialize_doc(doc):
    doc['_id']=str(doc['_id'])  #convert objectid to string
    return doc



@app.route("/user/alluser")
def getUserList():
    users=list(usercol.find())
    print(users)
    updateusers=[]
    for user in users:  #convert to json serializable format
        updateuser=(serialize_doc(user))
        updateusers.append(updateuser)
    return jsonify(updateusers),200



@app.route("/user/createuser",methods=['POST'])
def createuser():
    user=request.get_json()
    result=usercol.insert_one(user)
    print(result)
    return 'user created successfully'

@app.route("/user/delete",methods=["POST"])
def deleteuser():
    val=request.get_json()
    result=usercol.delete_one(val)
    return "user deleted successfully"


@app.route("/user/update",methods=["POST"])
def updateuser():
    val=request.get_json()
    result=usercol.update_one({"name":val["name"]},{"$set":{"email":val["email"]}})
    return "user updated successfully"





if __name__=="__main__":
    app.run(debug=True)
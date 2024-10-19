from pymongo import MongoClient


# established connection with mongodb
#create or create  data base
#use collection for which you need to perform CURD operation

client = MongoClient("mongodb://localhost:27017/")
db = client["flaskmongodb1"]                     #document name
userCollection = db["mycollection"]                #collection name
mobileCollection=db['mobileCollection']

#***************************** single user ************************8
# user1= {"name":"shaikh musa","age":21, "mobile no": 7822896448,"email":"shaikhmusa6448@gmail.com"}
# x=userCollection.insert_one(user1)
# print(x.inserted_id)

#**************************************  many user  *****************************8
# users=[
#   {"name":"shaikh noman","age":19, "mobile no": 648766456,"email":"shaikhnoman@gmail.com"},
# {"name":"shaikh azim","age":22, "mobile no": 74386289465,"email":"shaikhazim@gmail.com"},
# {"name":"raheman ","age":24, "mobile no": 74386289465,"email":"raheman@gmail.com"}
# ]

# createdUserId=userCollection.insert_many(users)
# print(createdUserId)


#************************ read **************
# listofuser=userCollection.find({"name":"shaikh musa"})
# for user in listofuser:
#     print(user)


#**************************  single delete  *******************

# result=userCollection.delete_one({"name":"shaikh musa"})
# print(result)


#******************************  many delete******************************8

# result=userCollection.delete_many({"name":"shaikh musa"})
# print(result)


#******************************** update  *************************


# result=userCollection.update_one({"name":"shaikh azim"},{"$set":{"mobile no": 333333333,"email": "aaaaaa@gmail.com"}})
# print(result)

result=userCollection.update_many({"name":"shaikh musa"},{"$set":{"mobile no": 9876543210,"email": "mmmmmmmm@gmail.com"}})
print(result)















#*************************************** mobile collection **********************
# m1={"mobile name":"vivo","price":9999,"ram":8.128 }
# x=mobileCollection.insert_one(m1)
# print(x.inserted_id)



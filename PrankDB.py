from flask import Flask, render_template, request, jsonify
import pymongo
import datetime

app = Flask(__name__)
app.config["DEBUG"] = True

prankclient = pymongo.MongoClient("mongodb://localhost:27017/")
prankdb = prankclient["prankdatabase"]
# dblist = prankclient.list_database_names()
prankscol =prankdb["pranks"]

# nextdict = [
#     {"title": "Title One", "rules": "Rule One", "location": "Somwhere One", "person": "Someone One", "difficulty": 2},
#     {"title": "Title Two", "rules": "Rule Two", "location": "Somwhere Two", "person": "Someone Two", "difficulty": 4},
#     {"title": "Title Three", "rules": "Rule Three", "location": "Somwhere Three", "person": "Someone Three", "difficulty": 6},
#     {"title": "Title Four", "rules": "Rule Four", "location": "Somwhere Four", "person": "Someone Four", "difficulty": 8},
#     {"title": "Title Five", "rules": "Rule Five", "location": "Somwhere Five", "person": "Someone Five", "difficulty": 1},
#     {"title": "Title Six", "rules": "Rule Six", "location": "Somwhere Six", "person": "Someone Six", "difficulty": 3},
#     {"title": "Title Seven", "rules": "Rule Seven", "location": "Somwhere Seven", "person": "Someone Seven", "difficulty": 5}
# ]

# x = prankscol.insert_many(nextdict)


@app.route('/', methods = ['GET'])

def data_ret():
    ret_list = [];
    for x in prankscol.find():
        x.pop('_id');                #Keeps or removes the _id item from the dictionary
        ret_list.append(x)
    return {"Object": ret_list}
    # return ret_list

print(data_ret())

if __name__ == "__main__":
    app.run(debug=True)
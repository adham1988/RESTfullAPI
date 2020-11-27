from flask import request
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from datetime import datetime

def print_to_file(my_list):   #function to read to file
    print("new rule is saved")
    a = 5
    d = datetime.now()
    print(d.strftime('%Y-%m-%d %H:%M:%S'))
    with open('file.txt', 'w') as f:
        f.write("%i\n" % my_list[len(my_list)-1])
            #f.write(d.strftime('%Y-%m-%d %H:%M:%S') + " Rule = " + "%i" % item + "\n")
    f.close()        

app = Flask(__name__)
i = 0
data1 = []
tasks = [
    {
        'id': 0,
        'rule': ""
       
    }
]
auth = HTTPBasicAuth()

USER_DATA = {    #defining of username and pass
    "bims": "bims"
}


@auth.verify_password      
def verify(username, password):  #verification of username and pass
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

#/todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})



@app.route('/todo/api/v1.0/tasks', methods=['POST'])  #post request config
@auth.login_required
def create_task():
    if not request.json or not 'rule' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'rule': request.json['rule']
    }
    tasks.append(task)
    data1.append(int(task["rule"]))
    print("Notification!!!! new rule = ",data1[len(data1)-1])
    print_to_file(data1)
    return jsonify({'task': task}), 201




if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')








    
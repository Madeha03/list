from flask import Flask, render_template, request,redirect,jsonify
app = Flask(__name__)
a = {'length': 40, 'type': 'phone', 'name': 'Fax', 'label': 'Fax'}
b = {'length': 255, 'type': 'string', 'name': 'Name', 'label': 'Name'}
c = {'length': 500,'type': 'string', 'name': 'Name', 'label': 'Name' }
list_of_dictionaries = [a,b,c]

@app.route('/found', methods=['GET'])
def found():
  return jsonify(list_of_dictionaries)

@app.route('/find', methods=['GET','POST'])
def find():
  if request.method == 'POST':
    var=request.get_json()
    print(var)
    list_of_dictionaries.append(var)
   
    return jsonify(list_of_dictionaries)
  else: 
    return jsonify(list_of_dictionaries)

if __name__ == '__main__':
    
   app.run(debug = True)
from flask import Flask ,jsonify,request
from flask_cors import CORS
import sqlite3

app =Flask(__name__)
cors = CORS(app)
@app.route("/")
def home():
    return jsonify(
        {
            'msg':'welcome',
            'name':'sahul'
        }
    )

@app.route("/busno/<int:number>")
def busno(number):
    # try:
    conn = sqlite3.connect('bus.db')
    c = conn.cursor()
    c.execute("SELECT * FROM buses WHERE bus_number=?", (number,))
    bus_data = c.fetchone()
    # print(bus_data)
    # except sqlite3.Error as e:
        # print(f"An error occured")
    # finally:
    conn.close()

    if bus_data is not None:
        bus_info = {
            "bus_number": bus_data[0],
            "driver_name": bus_data[1],
            "route": {
                "from": bus_data[2],
                "to": bus_data[3]
            },
            "registration": bus_data[4]
        }
    else:
        bus_info = {
            "wrongNumber": False
        }

    return jsonify(bus_info)

@app.route('/add_bus', methods=['POST','GET'])
def add_bus():
    data = request.get_json()
    bus_number = data.get('bus_number')
    driver_name = data.get('driver_name')
    from_location = data.get('from_location')
    to_location = data.get('to_location')
    registration_number = data.get('registration_number')
    # bus_number =request.json['bus_number']
    # driver_name =request.json['driver_name']
    # from_location =request.json['from_location']
    # to_location =request.json['to_location']
    # registration_number =request.json['registration_number']
    conn = sqlite3.connect('bus.db')
    c = conn.cursor()
    c.execute("INSERT INTO buses (bus_number, driver_name, from_location, to_location, registration_number) VALUES (?, ?, ?, ?, ?)",
              (bus_number, driver_name, from_location, to_location, registration_number))
    conn.commit()
    conn.close()

    response = {'message': 'Bus added successfully', 'status': 'success'}
    return jsonify(response), 200   


if __name__=='__main__':
    app.run(host="0.0.0.0", port=80, debug=True)

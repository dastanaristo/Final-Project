# Import
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

scaling_factor = 1.2

def result_calculate(size, lights, device, vehicle, trips):
    # Variables to calculate energy consumption
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5
    vehicle_coef = 2
    trips_coef = 1
    
    return (size * home_coef + 
              lights * light_coef + 
              device * devices_coef + 
              vehicle * vehicle_coef + 
              trips * trips_coef)
# First page
@app.route('/')
def index():
    return render_template('index.html')

# Second page
@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

# Third page
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

# Fourth page
@app.route('/<size>/<lights>/<device>')
def vehicle(size, lights, device):
    return render_template('vehicle.html', size=size, lights=lights, device=device)

# Fifth page
@app.route('/<size>/<lights>/<device>/<vehicle>')
def trips(size, lights, device, vehicle):
    return render_template('trips.html', size=size, lights=lights, device=device, vehicle=vehicle)


# Calculation
@app.route('/<size>/<lights>/<device>/<vehicle>/<trips>')
def end(size, lights, device, vehicle, trips):
    return render_template('end.html', 
                           result=result_calculate(int(size), 
                                                   int(lights), 
                                                   int(device),
                                                   int(vehicle),
                                                   int(trips)))

# Form page
@app.route('/form')
def form():
    return render_template('form.html')

# Form result
@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    return render_template('form_result.html', name=name)

app.run(debug=True)
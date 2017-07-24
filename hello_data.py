from flask import Flask, render_template
app_data = Flask(__name__)

@app_data.route('/')
def index():
    return render_template('userinfo.html')

@app_data.route('/hello_data')
def hello_data():
    return 'Hello Data!'

@app_data.route('/collision_map')
def collision_map():
    return render_template('collisions_map.html')

@app_data.route('/daily_collisions')
def daily_collisions():
    return render_template('daily_collisions.html')

if __name__ == '__main__':
    app_data.run(debug=True)

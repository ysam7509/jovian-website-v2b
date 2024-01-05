from flask import Flask, render_template,jsonify 

app = Flask(__name__)

JOBS= [ 
    {
        'id': 1,
        'title': 'Python Developer',
        'location': 'New York',
        'salary': '$100,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'New York',
        'salary': '$100,000'
    },
    {
        'id': 3,
        'title': 'Front-end Engineer',
        'location': 'New Delhi',
        'salary': '$100,000'
    },    
    {
        'id': 4,
        'title': 'Back-end Engineer',
        'location': 'New Delhi'
    }
]


@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
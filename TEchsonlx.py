from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        'name': 'K Srinithya',
        'title': 'Aspiring Learner',
        'bio': 'Fresher 2024 graduate. Passionate to work',
        'skills': ['Python', 'SQL'],
        'projects': [
            {'title': 'Emovision', 'description': 'Detects human emotions from real-time data using machine learning.'},
            {'title': 'Tachometer', 'description': 'Desprictive Projects on deatils and necessity of tachometer.'},
            {'title': 'Photo gallery', 'description': 'Responsive website using HTML,Css,Javascipt to store photos'}
        ],
        'contact': {
            'email': 'srinithya228@gmail.com',
            'linkedin': 'https://www.linkedin.com/in/srinithya-kavadi/',
            'github': 'https://github.com/Srinithya4f3'
        }
    }
    return render_template('index.html', profile=profile)

@app.route('/resume')
def download_resume():
    return send_from_directory('resume', 'K.Srinithya Resume')

if __name__ == '__main__':
    app.run(debug=True)
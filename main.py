from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/contact/')
def contact():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
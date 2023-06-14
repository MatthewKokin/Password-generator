from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = request.form.get('length', type=int)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return render_template('index.html', password=password)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = request.form.get('length', type=int)
    special_chars = request.form.get('special-characters')

    all_characters = string.ascii_letters + string.digits
    password = []

    # Add special characters
    for char in special_chars:
        password.append(char)

    # Fill the remaining length with random characters
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    password = ''.join(password)

    return render_template('index.html', password=password)

if __name__ == "__main__":
    app.run(debug=True)

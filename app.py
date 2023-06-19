
# Replacing Chat GPT code with Toms code

from flask import Flask, request, render_template
import random
import string
from random import shuffle


app = Flask(__name__)
app.debug = True



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    def reqcharac(length, required):
        all_characters = string.ascii_letters + string.digits + string.punctuation
        ourcharacters = []
        e = 0
        while e < len(required):
            Req = list(required)
            if Req[e] != " ":
                ourcharacters.append(Req[e])
                d = e + 1
                number = 0
                if d < len(Req):
                    while Req[d] != " ":
                        number = number + 1
                        if d < len(Req) - 1:
                            d = d + 1
                        else:
                            break
                    multiplier = 0
                    f = 1
                    while f <= number:
                        q = int(Req[e + f]) * 10**(number - f)

                        multiplier = multiplier + q
                        f = f + 1

                    while multiplier > 1:
                        ourcharacters.append(Req[e])
                        multiplier = multiplier - 1
                    e = e + number + 1

                else:
                    e = e + 1
            else:
                e = e + 1
        len_oc = len(ourcharacters)
        return(ourcharacters, len_oc, all_characters)    

    Length = request.form.get('length', type=int)
    Required = request.form.get('special-characters')
    our_characters, len_oc, all_characters = reqcharac(Length, Required)
    remaining = Length - len_oc
    i = 0
    while i < remaining:
        rem_char = random.choice(all_characters) 
        our_characters.append(rem_char)
        i = i + 1
    shuffle(our_characters)
    password = ''
    Password = password.join(our_characters)
    return render_template('index.html', password=Password)





if __name__ == "__main__":
    app.run(debug=True)

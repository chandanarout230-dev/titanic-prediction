from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

pipe = pickle.load(open('pipe.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        pclass = request.form.get('pclass')
        sex = request.form.get('sex')
        age = request.form.get('age')
        sibsp = request.form.get('sibsp')
        parch = request.form.get('parch')
        fare = request.form.get('fare')
        embarked = request.form.get('embarked')

        data = [[
            int(pclass),
            sex,
            float(age),
            int(sibsp),
            int(parch),
            float(fare),
            embarked
        ]]

        result = pipe.predict(data)[0]

        if result == 1:
            return "Passenger Survived"
        else:
            return "Passenger Did Not Survive"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            result = str(eval(expression))
        except Exception as e:
            result = 'Error'

        return render_template('index.html', result=result)
calculator
return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    

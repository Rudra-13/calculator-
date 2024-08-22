from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        button = request.form.get('button')
        if button == 'C':
            result = ''
        elif button == '=':
            try:
                result = str(eval(request.form.get('display')))
            except Exception:
                result = 'Error'
        else:
            current_value = request.form.get('display', '')
            result = current_value + button
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

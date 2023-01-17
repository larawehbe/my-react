from flask import Flask, request, jsonify, render_template
from core import generate_jewelery

app = Flask(__name__)


@app.route("/generate", methods=['POST'])
def generate():
    data = request.get_json()
    content = request.form['details']
    print(f'content from form: {content}')
    result = generate_jewelery(data)
    return jsonify(result)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('base.html')
    elif request.method == 'POST':
        success, message = generate_jewelery(request.form)
        if success:
            print(message)
            prompt = message['prompt']

            images = [i['url'] for i in message['data']]

            return render_template('base.html', images=images, prompt=prompt)
        else:
            return render_template('base.html', error=message)


if __name__ == '__main__':
    app.run(debug=True)

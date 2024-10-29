from flask import Flask, render_template

app = Flask(__name__, static_folder='assets', template_folder='pages')
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=7878)

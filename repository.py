from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def test():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        print(request.files['file1'])
        return test()
        
    return render_template('test.html')


if __name__ == '__main__':
    app.run()

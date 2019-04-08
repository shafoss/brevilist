from flask import Flask, render_template, request, redirect, url_for

from config import Config
from search import do_search
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        try:
            search_text = request.form['search-text']
            in_order = request.form.get('in-order')
            if search_text.isalpha():
                matches = do_search(search_text, in_order)
                return render_template('index.html', results="results.html", matches=matches, search_text=search_text)
            else:
                return render_template('index.html', help_text="Only alphabetic characters are allowed.")
        except Exception as e:
            print(e)
            return render_template('index.html', text="Something went wrong.")
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

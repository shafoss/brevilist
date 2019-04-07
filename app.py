from flask import Flask, render_template, request, redirect, url_for, send_file
from search import find_matches

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        try:
            search_text = request.form['search-text']
            matches = find_matches(search_text=search_text)
            return render_template('index.html', results="results.html", matches=matches, search_text=search_text)
        except Exception as e:
            print(e)
            return render_template('index.html', text="Something went wrong.")
    else:
        return redirect(url_for('index'))


# @app.route("/download/<string:text>")
# def download(text):
#     filename = text + ".csv"
#     results_to_csv(text)
#     return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run()

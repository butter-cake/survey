from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/', methods=['POST', 'GET'])
def tracker():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comments'] = request.form['comments']

        return redirect(url_for('result'))
    else:
        return render_template('surveyHome.html')


@app.route('/result')
def result():
    name = session.get('name')
    location = session.get('location')
    language = session.get('language')
    comments = session.get('comments')

    return render_template('surveyResults.html', name=name, location=location, language=language, comments=comments)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
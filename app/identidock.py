from flask import Flask, Response
import requests

app = Flask(__name__)
salt = "UNIQUE_SALT"
default_name = 'Alejandro'

@app.route('/')
def mainpage():
    name = default_name
    header = '<html><head><title>Identidock</title></head><body>'
    body = '''<form method="POST">
                Hola <input type="text" name="name" value="{0}">
                <input type="submit" value="submit">
            </form>
            <p>Te pareces a:
                <img src="/monster/monster.png"/>
            '''.format(name)
    footer = '</body></html>'
    return header + body + footer

@app.route('/monster/<name>')
def get_identicon(name):
    r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
    image = r.content
    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

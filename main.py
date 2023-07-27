from flask import Flask, render_template, request, redirect, url_for
import requests 
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

API_KEY = 'eyJ4NXQiOiJPREUzWTJaaE1UQmpNRE00WlRCbU1qQXlZemxpWVRJMllqUmhZVFpsT0dJeVptVXhOV0UzWVE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9'

# Lista de personas
personaList = [{"nombre": "Juan", "apellido": "Perez", "edad": 25},
            {"nombre": "Ana", "apellido": "Gomez", "edad": 30},
            {"nombre": "Carlos", "apellido": "Lopez", "edad": 45}]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/personas')
def personas():
    return render_template('personas.html', personas=personaList)

@app.route('/personas', methods=['POST'])
def add():
    print("llego por aqui a guardar")
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    edad = int(request.form.get('edad'))

    personaList.append({"nombre": nombre, "apellido": apellido, "edad": edad})

    return redirect(url_for('personas'))

@app.route('/estudiantes')
def estudiantes():
    responseEstudiantes = requests.get('https://utplwso2.tk/apiestudiantes/2.0/estudiantes',auth=HTTPBasicAuth('admin', 'admin'))
    return render_template('estudiantes.html', estudiantesl=responseEstudiantes.json())

if __name__ == '__main__':
    app.run(debug=True)
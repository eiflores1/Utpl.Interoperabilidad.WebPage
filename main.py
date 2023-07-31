#tarea 2.2
from flask import Flask, render_template, request, redirect, url_for
import requests 

app = Flask(__name__)

personaList = [{"nombre": "Juan", "apellido": "Perez", "edad": 25},
            {"nombre": "Ana", "apellido": "Gomez", "edad": 30},
            {"nombre": "Carlos", "apellido": "Lopez", "edad": 45}]

API_KEY = 'eyJ4NXQiOiJPREUzWTJaaE1UQmpNRE00WlRCbU1qQXlZemxpWVRJMllqUmhZVFpsT0dJeVptVXhOV0UzWVE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6ImFkbWluIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJhcHBfRWR1YXJkbyIsImlkIjo0LCJ1dWlkIjoiY2ViZTRhMzYtZmFkMi00MDY5LTkwOWUtZDFlNjkyZGY4YTBiIn0sImlzcyI6Imh0dHBzOlwvXC91dHBsd3NvMi50azo0NDNcL2FwaW1cL29hdXRoMlwvdG9rZW4iLCJ0aWVySW5mbyI6eyJVbmxpbWl0ZWQiOnsidGllclF1b3RhVHlwZSI6InJlcXVlc3RDb3VudCIsImdyYXBoUUxNYXhDb21wbGV4aXR5IjowLCJncmFwaFFMTWF4RGVwdGgiOjAsInN0b3BPblF1b3RhUmVhY2giOnRydWUsInNwaWtlQXJyZXN0TGltaXQiOjAsInNwaWtlQXJyZXN0VW5pdCI6bnVsbH19LCJrZXl0eXBlIjoiU0FOREJPWCIsInN1YnNjcmliZWRBUElzIjpbeyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGxFc3R1ZGlhbnRlcyIsImNvbnRleHQiOiJcL2FwaWVzdHVkaWFudGVzXC8xLjAiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiIxLjAiLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIn0seyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGxFc3R1ZGlhbnRlcyIsImNvbnRleHQiOiJcL2FwaWVzdHVkaWFudGVzXC8yLjAiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiIyLjAiLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIn0seyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGxFc3R1ZGlhbnRlcyIsImNvbnRleHQiOiJcL2FwaWVzdHVkaWFudGVzXC8zLjAiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiIzLjAiLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIn1dLCJ0b2tlbl90eXBlIjoiYXBpS2V5IiwiaWF0IjoxNjkwNzk3MTI2LCJqdGkiOiIwODgyOTMxYS1iZmY5LTRlYzAtYWVkOS0zODE3ZGUyMGU3YTcifQ==.baq4mRhdbyzdP8_SMZYpo4Jnbo1EaCWQflUom5AytHZsK5GiCREn4vUbzJsgq6SvqRQNqFU7dpu6OcPrudCe7RZreWl02G7G4FOubcQyEIXykiWITfWqOSW8J2bc1WdXfsJB3dRddD8p6qX4DMDxLvr_WQKpfI-qP-tqVustpELKYYxnWsc7iLQ48cI5bUoocm2PCeVToP-vElMMKwIqAfCjkeR5ae7mbYYikmXTZyIjA9qYM5yQVLKH97wR_u8WH6kUiYBsD1z6uF6f0u2x0jqshSggIBoq-8epAQ6F5uh2UiSATwAgqlq0BokXv8rbUrd0NLd_z9uTFn8Qo-lZKQ=='

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
    headers = {'apikey': API_KEY}
    responseEstudiantes = requests.get('https://utplwso2.tk/apiestudiantes/3.0/estudiantes',headers=headers)
    print(responseEstudiantes.json())
    return render_template('estudiantes.html', estudiantesl=responseEstudiantes.json())

@app.route('/estudiantes', methods=['POST'])
def addEstudiante():
    print("llego a la funcion estudiante")

    nombre = request.form.get('nombre')
    tiempo = int(request.form.get('tiempo'))
    identificacion = request.form.get('identificacion')
    ciudad = request.form.get('ciudad')

    estudiante_data = {"nombre": nombre, "tiempo": tiempo, "identificacion": identificacion, "ciudad": ciudad}
    
    headers = {'apikey': API_KEY}
    responseestudiante = requests.post('https://utplwso2.tk/apiestudiantes/3.0/estudiantes', json=estudiante_data, headers=headers)
    
    return redirect(url_for('estudiantes'))

if __name__ == '__main__':
    app.run(debug=True)

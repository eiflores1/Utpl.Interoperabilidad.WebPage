from flask import Flask, render_template, request, redirect, url_for
import requests 
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

personaList = []

API_KEY = 'eyJ4NXQiOiJPREUzWTJaaE1UQmpNRE00WlRCbU1qQXlZemxpWVRJMllqUmhZVFpsT0dJeVptVXhOV0UzWVE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6ImFkbWluIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJhcHBfRWR1YXJkbyIsImlkIjo0LCJ1dWlkIjoiY2ViZTRhMzYtZmFkMi00MDY5LTkwOWUtZDFlNjkyZGY4YTBiIn0sImlzcyI6Imh0dHBzOlwvXC91dHBsd3NvMi50azo0NDNcL2FwaW1cL29hdXRoMlwvdG9rZW4iLCJ0aWVySW5mbyI6eyJVbmxpbWl0ZWQiOnsidGllclF1b3RhVHlwZSI6InJlcXVlc3RDb3VudCIsImdyYXBoUUxNYXhDb21wbGV4aXR5IjowLCJncmFwaFFMTWF4RGVwdGgiOjAsInN0b3BPblF1b3RhUmVhY2giOnRydWUsInNwaWtlQXJyZXN0TGltaXQiOjAsInNwaWtlQXJyZXN0VW5pdCI6bnVsbH19LCJrZXl0eXBlIjoiU0FOREJPWCIsInN1YnNjcmliZWRBUElzIjpbeyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGxFc3R1ZGlhbnRlcyIsImNvbnRleHQiOiJcL2FwaWVzdHVkaWFudGVzXC8xLjAiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiIxLjAiLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIn0seyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGxFc3R1ZGlhbnRlcyIsImNvbnRleHQiOiJcL2FwaWVzdHVkaWFudGVzXC8yLjAiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiIyLjAiLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIn1dLCJ0b2tlbl90eXBlIjoiYXBpS2V5IiwiaWF0IjoxNjkwNDI4NDMxLCJqdGkiOiI3YTQ4NmE1NS02NWYxLTQ5YTYtYTdmMy00NzQ2MDVhMDAzOGIifQ==.lai334485kRGA19ZuFF8mf-WD5rRl34yU5UEsV2lbeBjCSorrp2xXT8Y8NUNvuGaMnplYGBeLPc9hG07jgMKq-wkWF4EWdBjBJDuRmct4pPVQoi-VQSsiJFwC3axDTd6282BhSHvLCRpypZED0WFpBFhtQ31hCWgpyHic6Bm7Hwr9Bznp3u4jbH67phnTiJMXFd3N8ng_VjjzDjqElj49w0mxVNDoohzLdnKNS5mObP7qHHJk_-Es5VjbrQYzZz8oylER_CpfwhpueBHLtHyKi2Dpk6U6QkBIcyDmZo0IMvVHIMF-CT_wWH3wiI3KTHq5hBrOPYKrwLWrvganDmyGA=='

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
    responseEstudiantes = requests.get('https://utplwso2.tk/apiestudiantes/2.0/estudiantes',headers=headers)
    print(responseEstudiantes.json())
    return render_template('estudiantes.html', estudiantesl=responseEstudiantes.json())

@app.route('/estudiantes', methods=['POST'])
def addEstudiante():
    print("llego por aqui a guardar estudiantes")

    nombre = request.form.get('nombre')
    tiempo = request.form.get('tiempo')
    identificacion = int(request.form.get('identificacion'))
    ciudad = int(request.form.get('ciudad'))

    room_data = {
        "nombre": nombre,
        "tiempo": tiempo,
        "identificacion": identificacion,
        "ciudad": ciudad
    }

    responseEstudiantesS = requests.post('https://utplwso2.tk/apiestudiantes/2.0/estudiantes', json=room_data)

    return redirect(url_for('estudiantes'))

if __name__ == '__main__':
    app.run(debug=True)
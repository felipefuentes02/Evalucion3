from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/templates/ejercicio1', methods=["GET", "POST"])
def ejercicio1():
    if request.method == 'POST':
        resultado = ""
        estado = ""
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        # Validación de notas en el rango de 10 a 70
        if not (10 <= nota1 <= 70) or not (10 <= nota2 <= 70) or not (10 <= nota3 <= 70):
            return render_template("ejercicio1.html")

        promedio = round((nota1 + nota2 + nota3) / 3, 1)

        if promedio >= 40 and asistencia >= 75:
            resultado = str(promedio)
            estado = "Aprobado"
        else:
            resultado = str(promedio)
            estado = "Reprobado"
        return render_template("ejercicio1.html", resultado=resultado, estado=estado, nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia)
    return render_template('ejercicio1.html')


@app.route('/templates/ejercicio2', methods=["GET", "POST"])
def ejercicio2():
    if request.method == 'POST':
        nombre = ""
        largo = ""
        nombre1 = str(request.form["nombre1"])
        nombre2 = str(request.form["nombre2"])
        nombre3 = str(request.form["nombre3"])
        largo1 = len(nombre1)
        largo2 = len(nombre2)
        largo3 = len(nombre3)
        if largo1 > largo2 and largo1 > largo3:
            respuesta = "El nombre con mayor cantidad de caracteres es: " + nombre1
            largo = "El nombre tiene " + str(largo1) + " \ncaracteres"
        elif largo2 > largo1 and largo2 > largo3:
            respuesta ="El nombre con mayor cantidad de caracteres es: " + nombre2
            largo = "El nombre tiene " + str(largo2) + " \ncaracteres"
        else:
            respuesta ="El nombre con mayor cantidad de caracteres es: " + nombre3
            largo = "El nombre tiene " + str(largo3) + " \ncaracteres"
        return render_template('ejercicio2.html', respuesta=respuesta, largo=largo, nombre1=nombre1, nombre2=nombre2, nombre3=nombre3)
    return render_template('ejercicio2.html')




if __name__ == "__main__":
    app.run()
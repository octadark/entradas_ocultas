from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def mostrar_formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    user_id = request.form['user_id']
    return f'Nombre: {nombre}, ID de Usuario: {user_id}'
if __name__ == "__main__":
    app.run(debug=True)
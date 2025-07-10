from flask import Flask, request, render_template_string
import sqlite3
import hashlib

app = Flask(__name__)
DB_NAME = "usuarios.db"

# Crear tabla si no existe
def crear_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Agregar usuario con contraseña en hash
def agregar_usuario(nombre, password):
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, password_hash) VALUES (?, ?)", (nombre, hash_pass))
    conn.commit()
    conn.close()

# Validar usuario
def validar_usuario(nombre, password):
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND password_hash = ?", (nombre, hash_pass))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

# HTML básico
template = '''
    <h2>🔐 Login Usuarios - Examen DRY7122</h2>
    <form method="POST">
        Nombre: <input type="text" name="nombre"><br>
        Contraseña: <input type="password" name="password"><br>
        <input type="submit" value="Ingresar">
    </form>
    <p>{{ mensaje }}</p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    mensaje = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        if validar_usuario(nombre, password):
            mensaje = f"✅ Bienvenido {nombre}."
        else:
            mensaje = "❌ Usuario o contraseña incorrectos."
    return render_template_string(template, mensaje=mensaje)

if __name__ == '__main__':
    crear_db()

    # Agregar usuarios del grupo (solo 1 vez, comentar después)
    agregar_usuario("Felipe", "clave123")
    agregar_usuario("David", "duoc2025")

    app.run(host='0.0.0.0', port=5800)

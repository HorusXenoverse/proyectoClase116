# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "Tom" # escribe tu nombre
    age = "16" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
@app.route("/padre")
def home():

    name = "Adolf" 
    age = "45" 

    return render_template('index.html' , name = name , age = age)


# define la ruta a la página web de tu madre.
@app.route("/madre")
def home():

    name = "Daimy" 
    age = "43" 

    return render_template('index.html' , name = name , age = age)


# define la ruta a la página web de tus amigos.
@app.route("/amigo")
def home():

    name = "friend" 
    age = "16" 

    return render_template('index.html' , name = name , age = age)


# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)

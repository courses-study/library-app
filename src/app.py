from flask import Flask #importamos Flask

app = Flask(__name__) #Inicializar la aplicacion como instancia

if __name__ == "__main__": #Comprobar si estamos en el archivo principal
  app.run() #Ejecucion de la aplicacion
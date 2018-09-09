import smtplib
import requests
import json

from flask import Flask, request

emisor = "grupo4.usac.2018@gmail.com"
receptor = "grupo4.usac.2018@gmail.com"


def mensajeBloqueo():
    serverSMTP = smtplib.SMTP('smtp.gmail.com', 587)
    serverSMTP.starttls()
    serverSMTP.login(emisor, 'grupo4usac')
    serverSMTP.sendmail(emisor, receptor, 'ALERTA! SISTEMA BLOQUEADO \nEl sistema de la casa se encuentra bloqueado debido a tres o mas intentos fallidos de querer entrar')
    serverSMTP.close()

def mensajeAccesoErroneo():
    serverSMTP = smtplib.SMTP('smtp.gmail.com', 587)
    serverSMTP.starttls()
    serverSMTP.login(emisor, 'grupo4usac')
    serverSMTP.sendmail(emisor, receptor,'ALERTA! SE DECTECTO UN INTRUSO \nSe detecto un acceso erroneo al registrar la huella.')
    serverSMTP.close()

def mensajeAccesoCorrecto():
    serverSMTP = smtplib.SMTP('smtp.gmail.com', 587)
    serverSMTP.starttls()
    serverSMTP.login(emisor, 'grupo4usac')
    serverSMTP.sendmail(emisor, receptor, 'ACCESO CORRECTO \nSe detecto un acceso correcto al registrar la huella.')
    serverSMTP.close()

app = Flask(__name__)
@app.route("/message", methods=['POST'])
def msg():
    _mss = request.args.get('mss')
    if  _mss == '1':
        mensajeBloqueo()
    elif _mss == '2':
        mensajeAccesoErroneo()
    else:
        mensajeAccesoCorrecto()
    return _mss

if __name__ == '__main__':
    app.debug = True
    app.run()

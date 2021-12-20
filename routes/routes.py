from flask import Blueprint, render_template, request, redirect, url_for, flash
from scripts.client import cliente
from scripts.server import servidor
from models.network import Network
from utils.db import db
from models.network import Network, conf_cliente, registrp, aux_speedtest
import os
import time


def obtener_datos(file, frec):
    bitrate = []
    enviados_bitrate = []
    recibidos_bitrate = []
    archivo = open(file, "r")
    lineas = archivo.read()
    lineas = lineas.split('\n')
    aux_lineas = 0
    maximo = int(frec) + 2
    for linea in lineas:
        fila_string = str(linea)
        if aux_lineas > 2 and aux_lineas <= maximo:
            #transfer.append(fila_string[25:29])
            bitrate.append(fila_string[38:43])
            enviados_bitrate = lineas[maximo + 3][38:43]
            recibidos_bitrate = lineas[maximo + 4][38:43]
        aux_lineas = aux_lineas + 1
    archivo.close()
    return bitrate, enviados_bitrate, recibidos_bitrate
        
def eliminar_caracteres(lista, caracter):
    #caracteres = "[] "
    for x in range(len(caracter)):
        lista = lista.replace(caracter[x], "")
    return lista



rutas = Blueprint('rutas',__name__)
@rutas.route('/')
def index():
    return render_template("index.html", titulo = "INICIO")

@rutas.route('/confserver', methods = ['GET', 'POST'])
def config_server():
    datos = Network.query.filter_by(id=1).first()
    if request.method == "POST":
        network = Network.query.filter_by(id=1).first()
        network.ip = request.form['ip']
        network.mask = request.form['mask']
        network.gateway = request.form['gateway']
        db.session.commit()
        comando = "sudo ifconfig eth1 " + network.ip + " netmask " + network.mask
        os.system("sudo ifconfig eth1 down")
        os.system(comando)
        os.system("sudo ifconfig eth1 up")
        flash('Se actualizo la IP satisfactoriamente')
        return redirect(url_for('rutas.config_server'))
    return render_template("conf_server.html", titulo = "Configuracion del Servidor", data = datos)

@rutas.route('/startserver', methods = ['GET', 'POST'])
def start_server():
    if request.method == "POST":
        if request.form.get("estado"):
            os.system("iperf3 -s -D")
            flash("Servidor Iniciado correctamente")
        else:
            os.system("pkill iperf3")
            flash("Servidor Detenido correctamente")
        return redirect(url_for('rutas.start_server'))
    return render_template("start_server.html", titulo = "Iniciar Servidor")

@rutas.route('/confclient', methods = ['GET', 'POST'])
def conf_client():
    size = [64,128,256,512,768,1024,1280,1518]
    datos = conf_cliente.query.filter_by(id=1).first()
    if request.method == "POST":
        conf = conf_cliente.query.filter_by(id=1).first()
        conf.origen = request.form['origen']
        conf.destino = request.form['destino']
        conf.ip_server = request.form['ipserver']
        conf.frecuencia = request.form['frecuencia']
        conf.modo = request.form['modo']
        if conf.modo == 'TCP':
            conf.frame_size = "0"
            conf.ancho_banda = "0"
        else:
            if request.form.get("check1") == None:
                size.remove(64)
            if request.form.get("check2") == None:
                size.remove(128)
            if request.form.get("check3") == None:
                size.remove(256)
            if request.form.get("check4") == None:
                size.remove(512)
            if request.form.get("check5") == None:
                size.remove(768)
            if request.form.get("check6") == None:
                size.remove(1024)
            if request.form.get("check7") == None:
                size.remove(1280)
            if request.form.get("check8") == None:
                size.remove(1518)
            tams = str(size)
            if len(size) == 0:
                conf.frame_size = "0"
            else:
                tamanos = eliminar_caracteres(tams,'[]')
                conf.frame_size = tamanos
            conf.ancho_banda = request.form['BW']
        db.session.commit()
        return redirect(url_for('rutas.conf_client'))
    return render_template("conf_client.html", titulo = "Configuracion Cliente", data = datos)

@rutas.route('/startclient', methods = ['GET', 'POST'])
def start_client():
    transfer = []
    bitrate = []
    enviados_bitrate = []
    recibidos_bitrate = []
    comando = "iperf3 -c "
    aux64 = "0"
    aux128 = "0"
    aux256 = "0"
    aux512 = "0"
    aux768 = "0"
    aux1024 = "0"
    aux1280 = "0"
    aux1518 = "0"
    if request.method == "POST":
        if request.form.get("estado"):
            conf = conf_cliente.query.filter_by(id=1).first()
            if conf.modo == 'TCP':
                final = comando + conf.ip_server + " -t " + str(conf.frecuencia) + " > log.txt"
                os.system(final)
                bitrate, enviados_bitrate, recibidos_bitrate = obtener_datos("log.txt", int(conf.frecuencia))
                nuevo_bitrate = eliminar_caracteres(str(bitrate), '[]')
                new_entry = registrp(conf.origen, conf.destino, conf.ip_server, conf.frecuencia, conf.modo, "0", "0", "0", "0", "0", "0", "0", "0", nuevo_bitrate, enviados_bitrate, recibidos_bitrate, time.strftime("%H:%M:%S", ), time.strftime("%Y/%m/%d"))
            else:
                lista_aux = conf.frame_size
                lista_aux = eliminar_caracteres(lista_aux, ' ')
                if lista_aux == "0":
                    comando_final = comando + conf.ip_server + " -u" + " -b " + str(conf.ancho_banda) + "M" +" -t " + str(conf.frecuencia) + " > log.txt"
                    os.system(comando_final)
                    bitrate, enviados_bitrate, recibidos_bitrate = obtener_datos("log.txt", int(conf.frecuencia))
                    nuevo_bitrate = eliminar_caracteres(str(bitrate), '[]')
                    new_entry = registrp(conf.origen, conf.destino, conf.ip_server, conf.frecuencia, conf.modo, "0", "0", "0", "0", "0", "0", "0", "0", nuevo_bitrate, enviados_bitrate, recibidos_bitrate, time.strftime("%H:%M:%S", ), time.strftime("%Y/%m/%d"))       
                else:
                    lista_final = list(lista_aux.split(","))
                    for item in lista_final:
                        comando_final = comando + conf.ip_server + " -u" + " -b " + str(conf.ancho_banda)+ "M" +" -t " + str(conf.frecuencia) + " -l " + str(item) + " > log.txt"
                        os.system(comando_final)
                        bitrate, enviados_bitrate, recibidos_bitrate = obtener_datos("log.txt", int(conf.frecuencia))
                        if item == "64":
                            aux64 = recibidos_bitrate
                        if item == "128":
                            aux128 = recibidos_bitrate
                        if item == "256":
                            aux256 = recibidos_bitrate
                        if item == "512":
                            aux512 = recibidos_bitrate
                        if item == "768":
                            aux768 = recibidos_bitrate
                        if item == "1024":
                            aux1024 = recibidos_bitrate
                        if item == "1280":
                            aux1280 = recibidos_bitrate
                        if item == "1518":
                            aux1518 = recibidos_bitrate
                        print("Ejecutando el tamaño de trama: " + str(item))
                    nuevo_bitrate = eliminar_caracteres(str(bitrate), '[]')
                    print(aux64 + aux128 + aux256 + aux512 + aux768 + aux1024 + aux1280 + aux1518)
                    new_entry = registrp(conf.origen, conf.destino, conf.ip_server, conf.frecuencia, conf.modo, aux64, aux128, aux256, aux512, aux768, aux1024, aux1280, aux1518, nuevo_bitrate, enviados_bitrate, recibidos_bitrate, time.strftime("%H:%M:%S", ), time.strftime("%Y/%m/%d"))
                    db.session.add(new_entry)
                    db.session.commit()   
        return render_template("start_client.html", titulo = "Iniciar Cliente")
    return render_template("start_client.html", titulo = "Iniciar Cliente")

@rutas.route('/speedtest', methods = ['GET', 'POST'])
def speed_test():
    datos_speedtest = []
    if request.method == "POST":
        os.system("speedtest --csv > speedtest.txt")
        archivo = open('speedtest.txt', 'r')
        contenido = archivo.read()
        datos = contenido.split(',')
        for dato in datos:
            datos_speedtest.append(dato)
        archivo.close()
        ms = float(datos_speedtest[5])
        download = float(datos_speedtest[6]) / 1000000
        upload = float(datos_speedtest[7]) / 1000000
        new_entry = aux_speedtest(download, upload, ms)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('rutas.resultado_speedtest'))
    return render_template("speed_test.html", titulo = "Test de Velocidad")


@rutas.route('/vistaspeedtest')
def resultado_speedtest():
    resultados = aux_speedtest.query.all()
    cont = 0
    for aux in resultados:
        cont = cont + 1
    return render_template("restulado_speed.html", nuevo_resultado = resultados[cont - 1], titulo = "Resultado de test de Velocidad")

@rutas.route('/listar', methods = ['GET', 'POST'])
def listar():
    registros = registrp.query.all()
    return render_template("listar.html", titulo = "Listar", registros = registros)

@rutas.route('/ultimotest')
def mostrar_test():
    aux = conf_cliente.query.filter_by(id=1).first()
    aux1= str(aux.ancho_banda)
    size1 = ['64','128','256','512','768','1024','1280','1518']
    cont = 0
    lista = []
    registros = registrp.query.all()
    for registro in registros:
        cont += 1
    troughtput = registros[cont - 1].bitrate
    troughtput = eliminar_caracteres(troughtput, "'")
    troughtput = troughtput.split(',')
    for aux in troughtput:
        lista.append(float(aux))
    bitRecibido = registros[cont - 1].bit_recibidos
    bitEnviado = registros[cont - 1].bit_enviados
    perdidos = float(bitEnviado) - float(bitRecibido)
    por_recibidos = (float(bitRecibido) * 100) / float(bitEnviado)
    por_perdidos = (perdidos * 100) / float(bitEnviado)
    return render_template("mostrar_test.html",
                            titulo = "Ultimo Test",
                            reg = registros[cont - 1],
                            datos = lista,
                            recibidos = por_recibidos,
                            perdidos = por_perdidos,
                            datos1 = size1,
                            bw = aux1,
                            lost = perdidos)

@rutas.route('/reporte/<string:id>')
def mostrar(id):
    registro = registrp.query.get(id)
    aux = conf_cliente.query.filter_by(id=1).first()
    aux1= str(aux.ancho_banda)
    size1 = ['64','128','256','512','768','1024','1280','1518']
    cont = 0
    lista = []
    registros = registrp.query.all()
    for registra in registros:
        cont += 1
    troughtput = registros[cont - 1].bitrate
    troughtput = eliminar_caracteres(troughtput, "'")
    troughtput = troughtput.split(',')
    for aux in troughtput:
        lista.append(float(aux))
    bitRecibido = registros[cont - 1].bit_recibidos
    bitEnviado = registros[cont - 1].bit_enviados
    perdidos = float(bitEnviado) - float(bitRecibido)
    por_recibidos = (float(bitRecibido) * 100) / float(bitEnviado)
    por_perdidos = (perdidos * 100) / float(bitEnviado)
    return render_template("mostrar_test.html",
                            titulo = "Ultimo Test",
                            reg = registro,
                            datos = lista,
                            recibidos = por_recibidos,
                            perdidos = por_perdidos,
                            datos1 = size1,
                            bw = aux1,
                            lost = perdidos)
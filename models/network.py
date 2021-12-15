from os import SEEK_CUR

from flask.helpers import send_file
from utils.db import db

class Network(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50))
    mask = db.Column(db.String(50))
    gateway = db.Column(db.String(50))

    def __init__(self, ip, mask, gateway):
        self.ip = ip
        self.mask = mask
        self.gateway = gateway

class conf_cliente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    origen = db.Column(db.String(100))
    destino = db.Column(db.String(100))
    ip_server = db.Column(db.String(100))
    frecuencia = db.Column(db.Integer())
    modo = db.Column(db.String(3))
    frame_size = db.Column(db.String(1024))
    ancho_banda = db.Column(db.Integer())

    def __init__(self, origen, destino, ip_server, frecuencia, modo, frame_size, ancho_banda):
        self.origen = origen
        self.destino = destino
        self.ip_server = ip_server
        self.frecuencia = frecuencia
        self.modo = modo
        self.frame_size = frame_size
        self.ancho_banda = ancho_banda


class registrp(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    origen = db.Column(db.String(100))
    destino = db.Column(db.String(100))
    ip_server = db.Column(db.String(100))
    frecuencia = db.Column(db.Integer())
    modo = db.Column(db.String(3))
    k64 = db.Column(db.String(1024))
    k128 = db.Column(db.String(1024))
    k256 = db.Column(db.String(1024))
    k512 = db.Column(db.String(1024))
    k768 = db.Column(db.String(1024))
    k1024 = db.Column(db.String(1024))
    k1280 = db.Column(db.String(1024))
    k1518 = db.Column(db.String(1024))
    bitrate = db.Column(db.String(1024))
    bit_enviados = db.Column(db.String(100))
    bit_recibidos = db.Column(db.String(100))
    tiempo = db.Column(db.Time())
    fecha = db.Column(db.Date())
    def __init__(self, origen, destino, ip_server, frecuencia, modo, k64, k128, k256, k512, k768, k1024, k1280, k1518, bitrate, bit_enviados, bit_recibidos, tiempo, fecha):
        self.origen = origen
        self.destino = destino
        self.ip_server = ip_server
        self.frecuencia = frecuencia
        self.modo = modo
        self.k64 = k64
        self.k128 = k128
        self.k256 = k256
        self.k512 = k512
        self.k768 = k768
        self.k1024 = k1024
        self.k1280 = k1280
        self.k1518 = k1518
        self.bitrate = bitrate
        self.bit_enviados = bit_enviados
        self.bit_recibidos = bit_recibidos
        self.tiempo = tiempo
        self.fecha = fecha

class aux_speedtest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    download = db.Column(db.Float())
    upload = db.Column(db.Float())
    ms = db.Column(db.Float())
    def __init__(self, download, upload, ms):
        self.download = download
        self.upload = upload
        self.ms = ms
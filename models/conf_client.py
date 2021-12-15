from utils.db import db

class conf_cliente(db.Model):
    id = db.Column(db.String, primary_key = True)
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

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from scapy.all import sniff, AsyncSniffer, IP, UDP
import threading

app = FastAPI()

# Modelo de dados para os pacotes RIP
class RIPData(BaseModel):
    source_ip: str
    destination_ip: str
    command: int  # Simulado como um valor genérico
    routes: list = []  # Simulado como uma lista vazia

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos
    allow_headers=["*"],  # Permitir todos os headers
)

# Armazenar dados capturados
rip_packets = []

# Função para processar pacotes
def handle_packet(packet):
    if packet.haslayer(UDP) and packet[UDP].dport == 520:  # Verifica se é pacote RIP pela porta UDP
        rip_data = {
            'source_ip': packet[IP].src,
            'destination_ip': packet[IP].dst,
            'command': 1,  # Exemplo: Define sempre como 1 para demonstrar
            'routes': []   # Lista vazia para simplificar, ajuste conforme necessário
        }
        rip_packets.append(rip_data)

# Função para capturar pacotes RIP
def capture_rip_packets():
    sniffer = AsyncSniffer(filter="udp port 520", prn=handle_packet, store=False)
    sniffer.start()
    return sniffer

# Iniciar a captura de pacotes RIP em uma thread separada
sniffer_thread = None

@app.on_event("startup")
def start_rip_capture():
    global sniffer_thread
    sniffer_thread = capture_rip_packets()

@app.on_event("shutdown")
def stop_rip_capture():
    if sniffer_thread:
        sniffer_thread.stop()

# API para obter dados RIP
@app.get("/rip-data", response_model=list[RIPData])
def get_rip_data():
    return rip_packets

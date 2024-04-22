from scapy.all import sniff, ARP
import json
from fastapi import FastAPI
from pydantic import BaseModel
import threading
import string;

# Armazenar dados ARP capturados
arp_data_storage = []

def handle_packet(packet):
    if ARP in packet and packet[ARP].op in (1, 2):  # ARP request or reply
        arp_data ={
            'source_ip': packet[ARP].psrc,
            'destination_ip': packet[ARP].pdst,
            'source_mac': packet[ARP].hwsrc,
            'destination_mac': packet[ARP].hwdst,
            'operation': 'request' if packet[ARP].op == 1 else 'reply'
        }
        arp_data_storage.append(arp_data) 

def capture_arp_packets():
    return sniff(filter="arp", prn=handle_packet, store=0, count=10)  # Capture 10 ARP packets

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def start_arp_capture():
    # Iniciar captura em uma thread separada para não bloquear o servidor
    thread = threading.Thread(target=lambda: arp_data_storage.extend(capture_arp_packets()))
    thread.start()


class ARPData(BaseModel):
    source_ip: str
    destination_ip: str
    source_mac: str
    destination_mac: str
    operation: str

@app.get("/arp-data", response_model=list[ARPData])
def get_arp_data():
    return arp_data_storage
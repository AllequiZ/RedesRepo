from fastapi import FastAPI
from scapy.all import sniff, IP
from datetime import datetime 
import threading  

# Estrutua para armazenar as informações no banco de dados
packets_info = []       

# Essa função captura os pacotes de IPv4
def capture_ipv4_packets():
    def packet_callback(packet):
        if IP in packet:
            packet_size = len(packet)
            timestamp = datetime.now()
            packets_info.append({"timestamp": timestamp, "packet_size": packet_size})       
            print(f"Captured IPv4 packet of size {packet_size} bytes at {timestamp}")

    sniff(filter = "ip", prn = packet_callback, store = False) 

# Iniciando a captura de pacotes em uma thread separada para não bloquear a execução do servidor da API
threading.Thread(target=capture_ipv4_packets, daemon=True).start()   

app = FastAPI()

@app.get("/packets-sizes")  
def get_packet_sizes():
    return packets_info

@app.get("/packets-sizes-variation")
def get_packet_size_variation():
    if len(packets_info) == 0:
        return {"error": "No packets captured yet"} 
    sizes = [info["packet_size"] for info in packets_info]
    return {"max": max(sizes), "min": min(sizes), "average": sum(sizes) / len(sizes)}
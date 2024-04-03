from fastapi import FastAPI
from scapy.all import sniff, IP, TCP, UDP
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import threading
import statistics  # Para calcular média, mediana, etc.


# Estrutura para armazenar as informações no banco de dados em memória
packets_info = []   # Vamos alterar para uma connection string com mongoDB em breve

def capture_ipv4_packets():
    def packet_callback(packet):
        if IP in packet:
            packet_info = { 
                "timestamp": datetime.now(),
                "packet_size": len(packet),
                "src_ip": packet[IP].src,
                "dst_ip": packet[IP].dst,
                "protocol": packet[IP].proto,
                "src_port": packet[TCP].sport if TCP in packet else None,
                "dst_port": packet[TCP].dport if TCP in packet else None,
                "payload_size": len(packet[IP].payload) if IP in packet else 0,
                "tcp_flags": packet[TCP].flags if TCP in packet else None,
                "ttl": packet[IP].ttl
            }
            packets_info.append(packet_info)
            print(f"Captured IPv4 packet of size {packet_info['packet_size']} bytes from {packet_info['src_ip']} to {packet_info['dst_ip']} at {packet_info['timestamp']}")

    sniff(filter="ip", prn=packet_callback, store=False)

# Iniciando a captura em uma thread separada
threading.Thread(target=capture_ipv4_packets, daemon=True).start()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
@app.get("/packets-sizes    ")
def get_packet_sizes():
    return packets_info

@app.get("/packets-sizes-variation")   # Rota para obeter os tamanhos do pacote e suas variações
def get_packet_size_variation():
    if len(packets_info) == 0:
        return {"error": "No packets captured yet"}
    sizes = [info["packet_size"] for info in packets_info]
    average = sum(sizes) / len(sizes)
    median = statistics.median(sizes)
    return {
        "max": max(sizes),
        "min": min(sizes),
        "average": average,
        "median": median,
        "std_deviation": statistics.stdev(sizes) if len(sizes) > 1 else 0
    }

@app.get("/packets-sizes-time-range")     # Rota para  obter os tamanhos do pacote em um intervalo de tempo 
def get_packet_sizes_time_range(start: str, end: str):
    start_datetime = datetime.fromisoformat(start)
    end_datetime = datetime.fromisoformat(end)
    filtered_packets = [p for p in packets_info if start_datetime <= p["timestamp"] <= end_datetime]
    if not filtered_packets:
        return {"error": "No packets found in the specified time range"}
    sizes = [info["packet_size"] for info in filtered_packets]
    return {
        "max": max(sizes),
        "min": min(sizes),
        "average": sum(sizes) / len(sizes)
    }




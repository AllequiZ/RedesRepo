# RedesRepo
 **Documentação da API de Captura de Pacotes**

![image](https://github.com/AllequiZ/RedesRepo/assets/115879120/95cf27b3-505e-4044-9ad9-d816b68b2a3a)

**Tecnologias Utilizadas:**

- **FastAPI:** Uma estrutura Python para construção de APIs web de alto desempenho. Esta estrutura fornece recursos avançados para criar interfaces web rápidas e simples usando SQLAlchemy ou Ponare para mapeamento de objetos e validação automática.

- **Scapy:** Uma biblioteca Python para capturar e manipular pacotes de rede. Scapy permite analisar pacotes nos níveis de link, rede e camada de transporte. A biblioteca implementa funções como forjar, detectar, enviar e decodificar pacotes.

- **CORSMiddleware:** Permite compartilhar recursos entre origens diferentes. Este módulo habilita CORS em FastAPI e permite que aplicativos web de diferentes domínios façam solicitações seguras a uma API.

- **Threading:** Permite que tarefas sejam executadas simultaneamente em threads separados. Ao usar threading, as operações de captura de pacotes podem ser processadas em paralelo em vários threads, aumentando o desempenho do aplicativo.

- **Statistics:** Uma biblioteca Python para realizar cálculos estatísticos básicos. Possibilita realizar análises sobre os dados coletados, como cálculo de média, mediana, variância e desvio padrão.

- **E-Charts:** Umа biblioteса JаvаSсriрt раrа visuаlizаção ԁe ԁаԁos interаtivа e рersonаlizável. EChаrts ofereсe umа аmрlа quantia ԁe gráfiсos e reсursos раrа сriаr раinéis informаtivos e visuаlizаções ԁe ԁаԁos.

**Rotas da API:**

- **`/packets-sizes`:**

    - Retorna uma lista contendo informações sobre os pacotes capturados, incluindo timestamp, tamanho, endereço IP, portas, protocolo e assim por diante.

- **`/packets-sizes-variation`:**

    - Retorna um objeto com informações estatísticas sobre os tamanhos dos pacotes:

        - Máximo, mínimo, média, mediana e desvio padrão.

- **`/packets-sizes-time-range`:**

    - Aceita dois parâmetros de data e hora em formato ISO (`start` e `end`).

    - Retorna um objeto com informações sobre os tamanhos dos pacotes capturados neste período:

        - Máximo, mínimo e média.

- **`/packets-sizes-comparison`:**

    - Retorna um objeto com informações de comparação para tamanhos de pacotes:

        - Máximo, mínimo, média, diferença entre máximo e mínimo, número de pacotes acima e abaixo da média, e seus percentuais.

![image](https://github.com/AllequiZ/RedesRepo/assets/115879120/c437d1fa-114e-4209-a894-7f2e6391a89e)

**Funcionalidades:**

- Captura de pacotes IPv4 em tempo real.

- Armazenamento de informações do pacote na memória (planejado para usar o MongoDB no futuro).

- Fornecimento de endpoints para obtenção de dados sobre pacotes capturados, incluindo:

    - Tamanho do pacote.

    - Variação de tamanho.

    - Pacotes em um determinado horário.

    - Comparação de tamanhos.



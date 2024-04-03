fetch('http://127.0.0.1:8000/packets-sizes-variation')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    if (!data.error) {
        const packetDataDiv = document.getElementById('packet-data');
        packetDataDiv.innerHTML = `
          <p>Max Size: ${data.max}</p>
          <p>Min Size: ${data.min}</p>
          <p>Average Size: ${data.average.toFixed(2)}</p>
          <p>Median Size: ${data.median}</p>
          <p>Standard Deviation: ${data.std_deviation.toFixed(2)}</p>
        `;
      } else {
        // Se houver um erro, exiba-o
        document.getElementById('packet-data').textContent = data.error;
      }
  })
  .catch((error) => {
    console.error('Error:', error);
  });

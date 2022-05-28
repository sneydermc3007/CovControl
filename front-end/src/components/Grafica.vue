<template>
  <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">

        <title>Graficas CovControl</title>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
    </head>
    <body>
      <h1>Graficas CovControl</h1>

      <canvas id="myChart" width="200" height="200"></canvas>

    </body>
  </html>
</template>

<script>
import Chart from 'chart.js/auto';


export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Grafica",
  props: {
    msg: String
  },
  mounted() {
    console.log('Componente Grafica montado');

    const ctx = document.getElementById('myChart');

    const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['0 dosis', '1 dosis', '2 dosis', '3 dosis'],
        datasets: [{
          label: 'Cantidad de vacunados',
          data: [10, 20, 18, 6],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(255, 206, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
          ],
          borderColor: [
            'rgba(255, 99, 132, 1)',
            'rgba(54, 162, 235, 1)',
            'rgba(255, 206, 86, 1)',
            'rgba(75, 192, 192, 1)'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });

myChart;
  }
}
</script>

<style scoped>

</style>
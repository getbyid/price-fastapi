// https://www.chartjs.org/docs/latest/samples/line/interpolation.html

const colors = [
  '#4dc9f6',
  '#f67019',
  '#f53794',
  '#537bc4',
  '#acc236',
  '#166a8f',
  '#00a950',
  '#58595b',
  '#8549ba',
]

const chartConfig = {
  type: 'line',
  data: {
    datasets: []
  },
  options: {
    responsive: true,
    interaction: {
      intersect: false,
    },
    scales: {
      x: {
        type: 'time',
        time: {
          parser: false,
          tooltipFormat: 'dd.MM.yyyy hh:mm',
          unit: 'day',
          displayFormats: {
            day: 'dd/MM'
          },
        },
        ticks: {
          source: 'data',
        }
      },
      y: {
        title: {
          display: true,
          text: 'Цена',
          color: 'blue',
        },
      }
    }
  },
}

function makeDatasets(resp) {
  return [
    {
      label: 'Магазин 1',
      data: resp.map((row) => ({ x: row.datetime * 1000, y: row.price })),
      borderColor: colors[0],
      fill: false,
      cubicInterpolationMode: 'monotone',
      tension: 0.4
    }
  ]
}

$(function () {
  const priceChart = new Chart($('#chart')[0].getContext('2d'), chartConfig)

  $.get('/products').then(function (resp) {
    if (Array.isArray(resp)) {
      $('#product').html(resp
        .map((p) => `<option value="${p.id}">${p.name}</option>`)
        .join('\n'))
    }
  })

  $('#form').on('change', ':input', function () {
    $.get('/history', $('#form').serialize()).then(function (resp) {
      if (!Array.isArray(resp)) return
      priceChart.data.datasets = makeDatasets(resp)
      priceChart.update()
    })
  })
})

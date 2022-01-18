async function getData(url = '') {
  const response = await fetch(url)
  return response.json()
}

function get_data_banxico() {
	let start_date = document.getElementById('start').value
	let end_date = document.getElementById('end').value
	let select = document.getElementById('udis_dolar').value
	
	let result = document.getElementById('result')
	let avg = document.getElementById('avg')
	let min = document.getElementById('min')
	let max = document.getElementById('max')

	if (start_date && end_date) {
		getData(`/api_get_data/${select}/${start_date}/${end_date}/`)
		.then(data => {
			if (data.status_code == 202) {
				/*result.innerHTML = data.data_list*/
				avg.innerHTML = data.avg_data
				min.innerHTML = data.min_data
				max.innerHTML = data.max_data

				graph_data = data.graph_data
				graph_data.unshift(['Día', 'Valor'])
				show_graph(graph_data, select)
			}
		})
	} else {
		alert('Favor de seleccionar fecha de inicio y fecha final')
	}

}


function show_graph(graph_data, serie) {

	google.charts.load('current', {packages: ['corechart', 'bar']});
	google.charts.setOnLoadCallback(drawBasic);

	function drawBasic() {

	  var data = google.visualization.arrayToDataTable(graph_data);

	  var options = {
	    title: `Valores en peso de ${serie}`,
	    chartArea: {width: '50%'},
	    hAxis: {
	      title: 'Días Seleccionados',
	      minValue: 0
	    },
	  };

	  var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));

	  chart.draw(data, options);
	}
}

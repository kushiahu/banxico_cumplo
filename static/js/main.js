async function getData(url = '') {
  const response = await fetch(url)
  return response.json()
}


// function set_chart() {
// 	google.charts.load('current', {packages: ['corechart']});  
// 	let data = google.visualization.arrayToDataTable([
//      ['Fecha', 'UDIS', { role: 'style' }],
//      ['2022-12-25', 8.94],
//      ['2022-12-24', 10.49],
//      ['2022-12-23', 19.30],
//   ]);

// 	let options = {title: 'Population (in millions)'}; 

// 	let chart = new google.visualization.BarChart(document.getElementById('chart_div'));
//   chart.draw(data, options);
//   google.charts.setOnLoadCallback(drawChart);
// }


function get_data_banxico() {
	let start_date = document.getElementById('start').value
	let end_date = document.getElementById('end').value
	let select = document.getElementById('udis_dolar').value
	
	let result = document.getElementById('result')
	let avg = document.getElementById('avg')
	let min = document.getElementById('min')
	let max = document.getElementById('max')

	if (start_date && end_date) {
		console.log(select)
		getData(`/api_get_data/${select}/${start_date}/${end_date}/`)
		.then(data => {
			if (data.status_code == 202) {
				console.log(data.data_list)
				result.innerHTML = data.data_list
				avg.innerHTML = data.avg_data
				min.innerHTML = data.min_data
				max.innerHTML = data.max_data
			}
		})
	} else {
		alert('Favor de seleccionar fecha de inicio y fecha final')
	}

}
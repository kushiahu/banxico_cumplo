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
		console.log(select)
		getData(`/api_get_data/${select}/${start_date}/${end_date}/`)
		.then(data => {
			if (data.status_code == 202) {
				console.log(data.graph_data)
				result.innerHTML = data.serie_rsl
				avg.innerHTML = data.avg_data
				min.innerHTML = data.min_data
				max.innerHTML = data.max_data
			}
		})
	} else {
		alert('Favor de seleccionar fecha de inicio y fecha final')
	}

}
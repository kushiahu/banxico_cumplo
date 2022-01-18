async function getData(url = '') {
  const response = await fetch(url)
  return response.json()
}


function get_data_banxico() {
	let start_date = document.getElementById('start').value
	let end_date = document.getElementById('end').value
	let select = document.getElementById('udis_dolar').value

	if (start_date && end_date) {
		console.log(select)
		// getData(`/jx/api_delete_product/${id_uuid}/`)
		// .then(data => {
		// 	if (data.status_code == 202) {
		// 		const trProductDel = document.getElementById(`trProduct_${id_uuid}`)
		// 		trProductDel.remove()
		// 		close_modal(modal_name)
		// 	}
		// })
	} else {
		alert('Favor de seleccionar fecha de inicio y fecha final')
	}

}
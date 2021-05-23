const divFlteredProducts = document.querySelector('#filteredProducts')



function checkFilter(){
    const checkBoxes = document.querySelectorAll('.prodCheck')
	console.log(checkBoxes)

    const checked=[]

    checkBoxes.forEach(checkbox => {
		// console.log(checkbox.checked, checkbox.name)
		if(checkbox.checked){
			checked.push(checkbox.value) 
		}
	})
    console.log(checked)
    

    //.then(res => res.json())
	//.then(data => {
		// console.log(data)
	//	divFlteredProducts.innerHTML = ''
	//	data.forEach(uploadfile => {
		//	divFlteredProducts.append(uploadfile.name, uploadfile.category)
		//})
	//})
}


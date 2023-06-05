function agregarFila() {
  var table = document.getElementById("fieldsTable");
  var newRow = table.insertRow(-1);
  var cell1 = newRow.insertCell(0);
  var cell2 = newRow.insertCell(1);

  cell1.innerHTML = '<input type="text" name="nombre[]">';
  cell2.innerHTML = '<input type="number" name="edad[]">';
}
function showFilter(item) {
    document.getElementById("dropdownMenu").innerHTML = item.innerHTML;
  }


$(document).ready(function() {
  $('.delete-button').on('click', function(e) {
    e.preventDefault();
    var deleteUrl = $(this).attr('href');
      if (confirm('¿Estás seguro de que deseas eliminar este elemento?')) {
          window.location.href = deleteUrl;
        }
    });
});
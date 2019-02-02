/****************************************************
Lista Especialidades y profesionales en el formulario
*****************************************************/
$( function() {
    $( "#id_buscaEspProf" ).autocomplete({
      minLength: 1,
      source: "/buscaEspProf/"
    });
});

/****************************************************
Deberia hacer funcionar los tooltips, pero no anda,
tiene conflicto con el script anterior, solo funciona
en base.html y con jquery "slim"
*****************************************************/
/*
$(function () {
    $('[data-toggle="tooltip"]').tooltip();
});
*/







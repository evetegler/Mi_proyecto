$(document).ready(function () {

    // ✅ REQUERIMIENTO 3: Evento click sobre el botón "Enviar por correo"
    $('#enviarCorreo').click(function () {
        alert("El correo fue enviado correctamente...");
    });

    // ✅ REQUERIMIENTO 4: Doble clic cambia color a rojo los títulos
    $('h3').on('dblclick', function () {
        $(this).css('color', '#dc3545');
    });

    // ✅ REQUERIMIENTO 5: Toggle al hacer clic en el título de cualquier card
    $('.titulo-card').click(function () {
        $(this).siblings('.contenido-card').toggle();
        // Alternativa: también podríamos usar $(this).parent().find('.contenido-card').toggle();
    });

    // Inicializar Tooltip de Bootstrap
    $('[data-toggle="tooltip"]').tooltip();
});

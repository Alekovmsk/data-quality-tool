$('#triggerDag, #killDag, #pauseDag, #unpauseDag').on('click', function() {
    const successMessageMap = {
        triggerDag: 'DAG успешно запущен',
        killDag: 'DAG успешно остановлен',
        pauseDag: 'Dag успешно выключен',
        unpauseDag: 'Dag успешно включен'
    };

    var endpoint = $(this).attr('id');
    var authorizedLogin = $('#login').html();
    var dqi = $('#dqi').val();

    $.ajax({
        type: "POST",
        url: `/api/dags/${endpoint}/uk=${dqi}?login=${authorizedLogin}`,
        dataType: "json",
        encode: true,
    }).done(function (data) {
        if (data === undefined) {
            Swal.fire({
                icon: 'success',
                title: successMessageMap[endpoint],
                position: 'top-end',
                showConfirmButton: false,
                toast: true,
                timer: 5000
            });
        } else {
            Swal.fire({
                icon: 'error',
                title: data.message,
                position: 'top-end',
                showConfirmButton: false,
                toast: true,
                timer: 5000
            });
        };
    });
});
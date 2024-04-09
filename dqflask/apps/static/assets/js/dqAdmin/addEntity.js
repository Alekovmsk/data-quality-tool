var authorizedLogin = $('#login').html();

const postAjax = (buttonId, formData, authorizedLogin, successMessage) => {
    var endpoint = $('#'+buttonId).attr('id');

    $.ajax({
        type: "POST",
        url: `/api/admin/${endpoint}?login=${authorizedLogin}`,
        data: formData,
        dataType: "json",
        encode: true,
        async: false
    }).done(function (data) {
        if (data === undefined) {
            Swal.fire({
                icon: 'success',
                title: successMessage,
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
};

export {postAjax};

const verifyField = (elemId) => {
    let response = true;
    let value = $('#' + elemId).val();
    if (value == 'null' || value == '') {
        Swal.fire({
            icon: 'error',
            title: 'Не заполнены обязательные поля',
            position: 'top-end',
            showConfirmButton: false,
            toast: true,
            timer: 5000
        });
        response = false;
    };
    return response;
};

export {verifyField};
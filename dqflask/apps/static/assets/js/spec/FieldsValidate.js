const validText = (el) => {
    var f = document.getElementById(el);
    f.addEventListener(
        'keyup', (event) => {
            if (f.value.trim() === '') {
                f.classList.remove('is-valid');
                f.classList.add('is-invalid');
            } else {
                f.classList.remove('is-invalid');
                f.classList.add('is-valid');
            };
        }
    );
};

const validSelect = (el) => {
    var f = document.getElementById(el);
    f.addEventListener(
        'change', (event) => {
            if (f.value === '0' || f.value === '') {
                f.classList.remove('is-valid');
                f.classList.add('is-invalid');
            } else {
                f.classList.remove('is-invalid');
                f.classList.add('is-valid');
            };
        }
    );
};

const validate = (evt) => {
    var theEvent = evt || window.event;
    if (theEvent.type === 'paste') {
        key = event.clipboardData.getData('text/plain');
    } else {
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    };
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
        theEvent.returnValue = false;

        if(theEvent.preventDefault) theEvent.preventDefault();
        Swal.fire({
            icon: 'warning',
            title: 'Введите число, дробную часть отделите точкой',
            position: 'top-end',
            showConfirmButton: false,
            toast: true,
            timer: 3000
        });
    };
};

const validDiv = (divId, elemId) => {
    let div = $('#' + divId);
    let f = $('#' + elemId);
    if (f.val() === '0' || f.val() === '') {
        div.removeClass("div-is-valid");
        div.addClass("div-is-invalid");
    } else {
        div.removeClass("div-is-invalid");
        div.addClass("div-is-valid");
    };
};
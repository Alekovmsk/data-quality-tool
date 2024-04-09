const isCronValid = (freq) => {
    var cronregex = new RegExp(/^(\*|([0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])|\*\/([0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]))(\*|([0-9]|1[0-9]|2[0-3])|\*\/([0-9]|1[0-9]|2[0-3]))(\*|([1-9]|1[0-9]|2[0-9]|3[0-1])|\*\/([1-9]|1[0-9]|2[0-9]|3[0-1]))(\*|([1-9]|1[0-2])|\*\/([1-9]|1[0-2]))(\*|([0-6])|\*\/([0-6]))$/);

    return cronregex.test(freq);
};

const validCron = (el) => {
    var f = document.getElementById(el);
    f.addEventListener(
        'keyup', (event) => {
            if (isCronValid(f.value)===true || f.value==="@daily" || f.value==="@weekly" || f.value==="@mounthly" || f.value==="@yearly") {
                f.classList.remove('is-invalid');
                f.classList.add('is-valid');
            } else {
                f.classList.remove('is-valid');
                f.classList.add('is-invalid');
            };
        }
    );
};
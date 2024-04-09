var notValid = () => {
    Swal.fire({
        icon: 'error',
        title: 'Заполните все обязательные поля!',
        position: 'top-end',
        showConfirmButton: false,
        toast: true,
        timer: 3000
    });
};

var showWebSpec = () => {
    let uk = $('#menu1').val();
    if (uk == '0') {
        notValid();
    } else {
        let url = `spec?uk=${uk}`;
        let response = fetch(url).then(
            (response) => {
                return response.json();
            }
        );
        location.assign(url);
    };
};

var showChangeSpec = () => {
    let uk = $('#menu1').val();
    if (uk == '0') {
        notValid();
    } else {
        let url = `spec?uk=${uk}`;
        let response = fetch(url)
            .then((response) => {
                return response.json();
            }
        );
        location.assign(`change-spec/${uk}`);
    };
};

var showVerSpec = () => {
    let uk = $('#menu1').val();
    let ver = $('#version').val();
    if (ver) {
        location.assign(`spec?uk=${uk}&ver=${ver}`);
    };
};

var showResultsSpec = () => {
    let uk = $('#menu1').val();
    if (uk == '0') {
        notValid();
    } else {
        let url = `dq_report?uk=${uk}`;
        let response = fetch(url)
            .then((response) => {
                return response.json();
            }
        );
        location.assign(`dq_report/${uk}`);
    };
};

var printSpec = (el) => {
    var winPrint = window.open('', '', 'left=50, top=50, width=800, height=640, toolbar=0, scrollbars=1, status=0');
    var printContent = $(`#${el}`).val();
    
    winPrint.document.write('<div id="print" class="contentpane">');
    winPrint.document.write(prntCSS);
    winPrint.document.write(printContent.innerHTML);
    winPrint.document.write('</div>');
    winPrint.document.close();
    winPrint.focus();
    winPrint.print();
    winPrint.close();
    printContent.innerHTML = strOldOne;
};
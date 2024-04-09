const getDataTable = (elemId, cols, endpoint) => {
    let url = window.location.protocol + '//' + window.location.host;

    return $("#"+elemId).DataTable({
        'processing': true,
        'serverSide': true,
        'serverMethod': 'post',
        'ajax': {
            'url': `${url}/api/admin/${endpoint}`
        },
        'lengthMenu': [[10, 25, 50, 100], [10, 25, 50, 100]],
        searching: true,
        sort: true,
        order: [0,'asc'],
        autoWidth: false,
        responsive: false,
        columns: cols,
        oLanguage: {
            sProcessing: `<div class="spinner-border text-success" style="width: 6rem; height: 6rem;"></div>`,
            sEmptyTable: "Нет данных"
        }
    });
};

const setDelay = (myTable, delayTime) => {
    function delay(callback, ms) {
        var timer = 0;
        return function () {
            var context = this, args = arguments;
            clearTimeout(timer);
            timer = setTimeout(function () {
                callback.apply(context, args);
            }, ms || 0);
        };
    };

    $('.dataTables_filter input')
    .unbind() // Unbind previous default bindings
    .bind('input', (delay(function (e) { // Bind our desired behavior
        myTable.search($(this).val()).draw();
        return;
    }, delayTime))); // Set delay in milliseconds
};

export {getDataTable, setDelay};
const getSelect2 = (elem, endpoint) => {
    var url = window.location.protocol + '//' + window.location.host;
    $('#'+elem).select2({
        minimumInputLength: 3,
        ajax: {
            delay: 300,
            url: `${url}/api/spec/${endpoint}`,
            dataType: 'json',
            data: function(params) {
                return {
                    search: params.term || "",
                    page: params.page || 1
                }
            },
            processResults: function (data) {
                return {
                    results: data.results,
                    pagination: {
                        more: data.pagination.more == 'true'
                    }
                };
            }
        }
    });
};

$(document).ready(function() {
    getSelect2('username', 'officers');
});
$(document).ready(function() {
	function newexportaction(e, dt, button, config) {
    var self = this;
    var oldStart = dt.settings()[0]._iDisplayStart;
    dt.one('preXhr', function (e, s, data) {
        // Just this once, load all data from the server...
        data.start = 0;
        data.length = 2147483647;
        dt.one('preDraw', function (e, settings) {
            // Call the original action function
            if (button[0].className.indexOf('buttons-copy') >= 0) {
                $.fn.dataTable.ext.buttons.copyHtml5.action.call(self, e, dt, button, config);
            } else if (button[0].className.indexOf('buttons-excel') >= 0) {
                $.fn.dataTable.ext.buttons.excelHtml5.available(dt, config) ?
                    $.fn.dataTable.ext.buttons.excelHtml5.action.call(self, e, dt, button, config) :
                    $.fn.dataTable.ext.buttons.excelFlash.action.call(self, e, dt, button, config);
            } else if (button[0].className.indexOf('buttons-csv') >= 0) {
                $.fn.dataTable.ext.buttons.csvHtml5.available(dt, config) ?
                    $.fn.dataTable.ext.buttons.csvHtml5.action.call(self, e, dt, button, config) :
                    $.fn.dataTable.ext.buttons.csvFlash.action.call(self, e, dt, button, config);
            } else if (button[0].className.indexOf('buttons-pdf') >= 0) {
                $.fn.dataTable.ext.buttons.pdfHtml5.available(dt, config) ?
                    $.fn.dataTable.ext.buttons.pdfHtml5.action.call(self, e, dt, button, config) :
                    $.fn.dataTable.ext.buttons.pdfFlash.action.call(self, e, dt, button, config);
            } else if (button[0].className.indexOf('buttons-print') >= 0) {
                $.fn.dataTable.ext.buttons.print.action(e, dt, button, config);
            }
            dt.one('preXhr', function (e, s, data) {
                // DataTables thinks the first item displayed is index 0, but we're not drawing that.
                // Set the property to what it was before exporting.
                settings._iDisplayStart = oldStart;
                data.start = oldStart;
            });
            // Reload the grid with the original page. Otherwise, API functions like table.cell(this) don't work properly.
            setTimeout(dt.ajax.reload, 0);
            // Prevent rendering of the full data to the DOM
            return false;
        });
    });
    // Requery the server with the new one-time export settings
    dt.ajax.reload();
    };

	function formatDate(date) {
		var d = new Date(date),
			month = '' + (d.getMonth() + 1),
			day = '' + d.getDate(),
			year = d.getFullYear();
		if (month.length < 2)
			 month = '0' + month;
		if (day.length < 2)
			 day = '0' + day;
		return [day, month, year].join('.');
   };

    var url = window.location.pathname;
    var empDataTable = $("#example1").DataTable({
        'processing': true,
        'serverSide': true,
        'serverMethod': 'post',
		'dom': 'Bfrltip',
		'buttons':
		    [
		        {
                    "extend": 'excel',
                    "text": 'Выгрузить в Excel',
                            "className": 'btn-purple btn-width',
                    "titleAttr": 'Excel',
                            "title": 'SSDQ_'+formatDate(new Date()),
                    "action": newexportaction
                },
            ],
        'ajax': {
                'url': url
        },
        'lengthMenu': [[10, 25, 50, 100], [10, 25, 50, 100]],
        searching: true,
        sort: true,
        order: [0,'desc'],
        autoWidth: false,
        responsive: false,
        'columns': [
			{ data: 'uk',
			    render: function (data) {
					return `<a href="/spec?uk=${data}">${data}</a>`;
			    }
			},
            { data: 'name' },
            { data: 'object_name' },
            { data: 'officer_name' },
			{ data: 'last_result',
			    render: function (data, type, row) {
                    if (data != null) {
                        return '<a href="/dq_report/'+ row.uk +'">'+data+'</a>';
                    }
                    else {
                        return '-';
                    };
			    }
			},
			{ data: 'last_start',
			    render: function (data, type, row) {
					let dd = '';
					if (formatDate(data) == '01.01.1970') {
						dd = '-';
					}
					else {
						dd = formatDate(data);
					}
					return dd;
			    }
			},
			{ data: 'overflow_start',
			    render: function (data, type, row) {
					let dd = '';
					if (formatDate(data) == '01.01.1970') {
						dd = '-';
					}
					else {
						dd = formatDate(data);
					}
					return dd;
			    }
			},
			{ data: 'overflow_result' },
			{ data: 'description' },
			{ data: 'rule_description' },
			{ data: 'status_name' },
			{ data: 'control_type' },
			{ data: 'dept_name' },
			{ data: 'need_act' }
        ],
        oLanguage: {
            sProcessing: `<div class="spinner-border text-success" style="width: 6rem; height: 6rem;"></div>`,
            sEmptyTable: "Нет данных"
        }
    });
});
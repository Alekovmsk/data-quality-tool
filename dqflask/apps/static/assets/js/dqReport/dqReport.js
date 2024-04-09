/* Variables for render data-grid and chart */
var empDataTable;
var barChart;

/* Variables with  info for render data-grid */
var dqi;
var wf_id;

/* Variables for render chart */
var report_time = new Array();
var mistake_cnt = new Array();

/* Function for convert date */
var formatDate = (date) => {
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

/* Function for print report */
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

const hasResult = (has_result) => {
    if (!has_result) {
        $('#reportTable').prop('hidden', true);
        $('#message').html(`<h1 class="card-title" style="margin: 2% 2% 2% 2%;">За выбранную дату ошибок не обнаружено</h1>`);
    } else {
        $('#reportTable').prop('hidden', false);
        $('#message').html('');
    };
};

function grid(dqi, wf_id) {
    /* Get columns info to generate grid */
    var cnt=document.getElementById('cnt_col').value;
    var columns=document.getElementById('columns').value;
    var dataset = [];
    for (let a = 0; a<cnt; a++) {
        dataset.push({data: a});
    };

    var dt = $("#dqreport").DataTable({
        'processing': true,
        'serverSide': true,
        'serverMethod': 'post',
        'dom': 'B<"row"<"col-sm-6"l><"col-sm-6"f>>tip',
        "buttons":
            [
                {
                    "extend": 'excel',
                    "text": 'Выгрузить в Excel',
                             "className": 'btn-purple btn-width',
                    "titleAttr": 'Excel',
                             "title": dqi+'_report_'+formatDate(new Date()),
                    "action": newexportaction
                },
            ],
        'ajax': {
            'url':`/dq_report/${dqi}?wf=${wf_id}`,
            'data': {
                'columns':columns
            },
            'dataSrc': function ( json ) {
                //Make your callback here.
                if (json.aaData.length) {
                    hasResult(true);
                } else {
                    hasResult(false);
                };
                return json.aaData;
            }
        },
        'lengthMenu': [[10, 25, 50, 100], [10, 25, 50, 100]],
        searching: true,
        sort: true,
        autoWidth: false,
        responsive: false,
        columns: dataset,
        oLanguage: {sProcessing: `<div class="spinner-border text-success" style="width: 6rem; height: 6rem;"></div>`}
    });
    return dt;
};

$(document).ready(function() {
    /* Initialize dq ID and workflow ID for grid */
    let dqi_wf =$('#menu').val();
    let dqiArray = dqi_wf.split('/');
    dqi = dqiArray[0];
    wf_id = dqiArray[1];
    var has_result;

    /* Generate grid */
    empDataTable = grid(dqi, wf_id);
    //hasResult(has_result);

    /* Initialize dates and mistake count for chart */
    $('#report_time td').each(function() {
        report_time.push(this.innerHTML);
    });

    $('#mistake_cnt td').each(function() {
        mistake_cnt.push(this.innerHTML);
    });

    var areaChartData = {
        labels  : report_time,
        datasets: [
            {
                label               : 'Количество ошибок',
                backgroundColor     : 'rgba(60,141,188,0.9)',
                borderColor         : 'rgba(60,141,188,0.8)',
                pointRadius          : false,
                pointColor          : '#3b8bba',
                pointStrokeColor    : 'rgba(60,141,188,1)',
                pointHighlightFill  : '#fff',
                pointHighlightStroke: 'rgba(60,141,188,1)',
                data                : mistake_cnt
            },
        ]
    };

    //-------------
    //- BAR CHART -
    //-------------
	var $barChart = $('#barChart')
    // eslint-disable-next-line no-unused-vars
    barChart = new Chart($barChart, {
        type: 'bar',
        data: {
            labels: report_time,
            datasets: [
                {
                    label               : 'Количество ошибок',
                    backgroundColor     : 'rgba(60,141,188,0.9)',
                    borderColor         : 'rgba(60,141,188,0.8)',
                    pointRadius         : false,
                    pointColor          : '#3b8bba',
                    pointStrokeColor    : 'rgba(60,141,188,1)',
                    pointHighlightFill  : '#fff',
                    pointHighlightStroke: 'rgba(60,141,188,1)',
                    data                : mistake_cnt
                }
            ]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        min: 0
                    }
                }]
            },
            responsive              : true,
            maintainAspectRatio     : false,
            datasetFill             : false
        }
    });
});

var showDetailJournal = (value) => {
    let dqiArray = value.split('/');
    wf_id = dqiArray[1];
    let has_result;

    empDataTable.destroy();
    empDataTable = grid(dqi, wf_id);
};

function showRep() {
    var report_time2 = [...report_time];
    var mistake_cnt2 = [...mistake_cnt];
    var startdate = $('#startdate').val();
    var enddate = $('#enddate').val();
    var indexstartdate = report_time2.indexOf(startdate);
    var indexenddate = report_time2.indexOf(enddate);
    var filterDate = report_time2.slice(indexstartdate, indexenddate+1);
    var filterCnt = mistake_cnt2.slice(indexstartdate, indexenddate+1);
    barChart.data.labels = filterDate;
    barChart.data.datasets[0].data = filterCnt;
    barChart.update();
};
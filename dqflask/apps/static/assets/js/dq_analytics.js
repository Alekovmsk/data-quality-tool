
function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();
    if (month.length < 2)
         month = '0' + month;
    if (day.length < 2)
         day = '0' + day;
    return [year,month,day].join('-');
};

//Chart DQI CNT
/* global Chart:false */

var DqCntChartCanvas = $('#DqCntChart').get(0).getContext('2d')

var DqCntChartData = {
    labels: [],
    datasets: [
        {
            label: 'Тестирование',
            backgroundColor: 'transparent',
            borderColor: '#8d6af1',
            //pointRadius: false,
            pointBorderColor: 'transparent',
            //pointBackgroundColor: '#fff',
            pointHoverBackgroundColor: '#8d6af1',
            pointColor: 'transparent',
            pointStrokeColor: 'transparent',
            pointHighlightFill: '#fff',
            pointHighlightStroke: '#8d6af1',
            data: []
        },
        {
            label: 'Разработка',
            backgroundColor: 'transparent',
            borderColor: '#3f6bb4',
            //pointRadius: false,
            pointBorderColor: 'transparent',
            //pointBackgroundColor: '#fff',
            pointHoverBackgroundColor: '#3f6bb4',
            pointColor: 'transparent',
            pointStrokeColor: 'transparent',
            pointHighlightFill: '#fff',
            pointHighlightStroke: '#3f6bb4',
            data: []
        },
	    {
            label: 'Эксплуатация',
            backgroundColor: 'transparent',
            borderColor: '#66b5ad',
            //pointRadius: false,
            pointBorderColor: 'transparent',
            //pointBackgroundColor: '#fff',
            pointHoverBackgroundColor: '#66b5ad',
            pointColor: 'transparent',
            pointStrokeColor: 'transparent',
            pointHighlightFill: '#fff',
            pointHighlightStroke: '#66b5ad',
            data: []
		},
	    {
	    label: 'Отменен',
            backgroundColor: 'transparent',
            borderColor: '#d9215f',
            //pointRadius: false,
            pointBorderColor: 'transparent',
            //pointBackgroundColor: '#fff',
            pointHoverBackgroundColor: '#d9215f',
            pointColor: 'transparent',
            pointStrokeColor: 'transparent',
            pointHighlightFill: '#fff',
            pointHighlightStroke: '#d9215f',
            data: []
		},
	    {
            label: 'На актуализации',
            backgroundColor: 'transparent',
            borderColor: '#e7b85d',
            //pointRadius: false,
            pointBorderColor: 'transparent',
            //pointBackgroundColor: '#fff',
            pointHoverBackgroundColor: '#e7b85d',
            pointColor: 'transparent',
            pointStrokeColor: 'transparent',
            pointHighlightFill: '#fff',
            pointHighlightStroke: '#e7b85d',
            data: []
		},
        {
            label: 'Приёмка заказчиком',
            backgroundColor: 'transparent',
            borderColor: '#97793c',
            //pointRadius:f false,
            pointBorderColor: 'transparent',
            //pointBackgroundColor: '#fff',
            pointHoverBackgroundColor: '#97793c',
            pointColor: 'transparent',
            pointStrokeColor: 'transparent',
            pointHighlightFill: '#fff',
            pointHighlightStroke: '#97793c',
            data: []
		}
    ]
}

var DqCntChartOptions = {
    maintainAspectRatio: false,
    responsive: true,
    legend: {
      display: false
    },
    scales: {
        xAxes: [{
            gridLines: {
                display: false
            },
            display: false,
        }],
        yAxes: [{
            gridLines: {
            display: true
            }
        }]
    },
	pan: {
	    enabled: true,
		mode: 'xy'
	},
    zoom: {
	    enabled: true,
		mode: 'xy'
	}
};

var DqCntChart = new Chart(DqCntChartCanvas, {
    type: 'line',
    data: DqCntChartData,
    options: DqCntChartOptions
});
  
var data_ajax_cntdqi = () => {
    return $.ajax({
    url: '/dq_analytics?obj=view_all_controls_bydate',
    type: 'POST',
    dataType: 'json',
    }).done(function(results) {
        var mapped = results.aaData.reduce((acc, cur, index)=>{
            acc[cur.thedate] = acc[cur.thedate] || {
                thedate: cur.thedate,
                test_cnt: 0,
                develop_cnt: 0,
                expl_cnt: 0,
                cancled_cnt: 0,
                actual_cnt: 0,
                accept_cnt: 0
            };
            acc[cur.thedate].test_cnt += 1 ? cur.dq_status_uk == 2 : 0;
            acc[cur.thedate].develop_cnt += 1 ? cur.dq_status_uk == 1 : 0;
            acc[cur.thedate].expl_cnt += 1 ? cur.dq_status_uk == 4 : 0;
            acc[cur.thedate].cancled_cnt += 1 ? cur.dq_status_uk == 5 : 0;
            acc[cur.thedate].actual_cnt += 1 ? cur.dq_status_uk == 6 : 0;
            acc[cur.thedate].accept_cnt += 1 ? cur.dq_status_uk == 3 : 0;
            acc[index] = acc[cur.thedate];
            return acc;
        },[])

        var data = [...new Set(mapped)];
        if (!data.length) {
            $('#CountChart').html(`<p style="text-align: center">Отсутствуют данные для формирования графика</p>`);
            return false;
        };

        for (cur in data) {
            DqCntChartData.datasets[0].data.push(data[cur].test_cnt)
            DqCntChartData.datasets[1].data.push(data[cur].develop_cnt)
            DqCntChartData.datasets[2].data.push(data[cur].expl_cnt)
            DqCntChartData.datasets[3].data.push(data[cur].cancled_cnt)
            DqCntChartData.datasets[4].data.push(data[cur].actual_cnt)
            DqCntChartData.datasets[5].data.push(data[cur].accept_cnt)
            DqCntChartData.labels.push(formatDate(data[cur].thedate))
            //DqCntChart.update();
        };
        DqCntChart.update();
        $('#dateindexCntDqi').attr('data-slider-value', `[0,${data.length-1}]`);
        $('#dateindexCntDqi').attr('data-slider-max', `${data.length-1}`);
        $('#dateindexCntDqi').bootstrapSlider();
    });
};
		
var test_cnt = DqCntChartData.datasets[0].data;
var develop_cnt = DqCntChartData.datasets[1].data;
var expl_cnt = DqCntChartData.datasets[2].data;
var cancled_cnt = DqCntChartData.datasets[3].data;
var actual_cnt = DqCntChartData.datasets[4].data;
var accept_cnt = DqCntChartData.datasets[5].data;
var thedate = DqCntChartData.labels;

function filterDataCntDqi() {
	var test_cnt2 = [...test_cnt];
	var develop_cnt2 = [...develop_cnt];
	var expl_cnt2 = [...expl_cnt];
	var cancled_cnt2 = [...cancled_cnt];
	var actual_cnt2 = [...actual_cnt];
	var accept_cnt2 = [...accept_cnt];
	var thedate2 = [...thedate];
	var val = document.getElementById('dateindexCntDqi').value;
	var vl = val.split(',')
	var indexstartdateCntDqi = vl[0];
	var indexenddateCntDqi = Number(vl[1]);
	var filterTheDate = thedate2.slice(indexstartdateCntDqi, indexenddateCntDqi+1);
	var filtertest_cnt = test_cnt2.slice(indexstartdateCntDqi, indexenddateCntDqi+1);
	var filterDevelop_cnt = develop_cnt2.slice(indexstartdateCntDqi, indexenddateCntDqi+1);
	var filterExpl_cnt = expl_cnt2.slice(indexstartdateCntDqi, indexenddateCntDqi+1);
	var filterCancled_cnt = cancled_cnt2.slice(indexstartdateCntDqi, indexenddateCntDqi+1);
	var filterActual_cnt = actual_cnt2.slice(indexstartdateCntDqi, indexenddateCntDqi+1);
	var filterAccept_cnt = accept_cnt2.slice(indexstartdateCntDqi, indexenddateCntDqi+1);
	DqCntChart.data.labels = filterTheDate;
	DqCntChart.data.datasets[0].data = filtertest_cnt;
	DqCntChart.data.datasets[1].data = filterDevelop_cnt;
	DqCntChart.data.datasets[2].data = filterExpl_cnt;
	DqCntChart.data.datasets[3].data = filterCancled_cnt;
	DqCntChart.data.datasets[4].data = filterActual_cnt;
	DqCntChart.data.datasets[5].data = filterAccept_cnt;
	DqCntChart.update();
};

var DqErrorChartCanvas = $('#DqErrorChart').get(0).getContext('2d')

var DqErrorChartData = {
    labels: [],
    datasets: [
        {
            label: 'Корпоративный сегмент',
            backgroundColor: 'transparent',
            borderColor: '#8d6af1',
            //pointRadius: false,
            pointBorderColor: 'transparent',
            //pointBackgroundColor: '#fff',
            pointHoverBackgroundColor: '#8d6af1',
            pointColor: 'transparent',
            pointStrokeColor: 'transparent',
            pointHighlightFill: '#fff',
            pointHighlightStroke: '#8d6af1',
            data: []
        },
        {
            label: 'Розничный сегмент',
            backgroundColor: 'transparent',
            borderColor: '#66b5ad',
            //pointRadius: false,
            pointBorderColor: 'transparent',
            //pointBackgroundColor: '#fff',
            pointHoverBackgroundColor: '#66b5ad',
            pointColor: 'transparent',
            pointStrokeColor: 'transparent',
            pointHighlightFill: '#fff',
            pointHighlightStroke: '#66b5ad',
            data: []
        },
    ]
};

var DqErrorChart = new Chart(DqErrorChartCanvas, {
    type: 'line',
    data: DqErrorChartData,
    options: DqCntChartOptions
});

var dataAjaxDqError = () => {
    return $.ajax({
    url: '/dq_analytics?obj=view_controls_error',
    type: 'POST',
    dataType: 'json',
    }).done(function(results) {
        var mapped = results.aaData.reduce((acc, cur, index)=>{
            acc[cur.report_date] = acc[cur.report_date] || {
                report_date: cur.report_date,
                corp_cnt: 0,
                retail_cnt: 0
            };
            acc[cur.report_date].corp_cnt += 1 ? cur.segment_id == 1 && cur.uk > 0 : 0 ;
            acc[cur.report_date].retail_cnt += 1 ? cur.segment_id == 2 && cur.uk > 0 : 0;
            acc[index] = acc[cur.report_date];
            return acc;
        },[])
        var data = [...new Set(mapped)];

        if (!data.length) {
            $('#ErrorChart').html(`<p style="text-align: center">Отсутствуют контроли КД с выявленными ошибками</p>`);
            return false;
        };

        for (cur in data) {
            DqErrorChartData.datasets[0].data.push(data[cur].corp_cnt)
            DqErrorChartData.datasets[1].data.push(data[cur].retail_cnt)
            DqErrorChartData.labels.push(formatDate(data[cur].report_date))
            DqErrorChart.update();
        };
        $('#dateindexDqiError').attr('data-slider-value', `[0,${data.length-1}]`);
        $('#dateindexDqiError').attr('data-slider-max', `${data.length-1}`);
        $('#dateindexDqiError').bootstrapSlider();
        console.log($('#dateindexDqiError'))
    });

};

var corp_cnt = DqErrorChartData.datasets[0].data;
var retail_cnt = DqErrorChartData.datasets[1].data;
var rep_date = DqErrorChartData.labels;

function filterDataDqiError() {
	var corp_cnt2 = [...corp_cnt];
	var retail_cnt2 = [...retail_cnt];
	var rep_date2 = [...rep_date];
	var val = document.getElementById('dateindexDqiError').value;
	var vl = val.split(',')
	var indexstartdate = vl[0];
	var indexenddate = Number(vl[1]);
	var filterRepDate = rep_date2.slice(indexstartdate, indexenddate+1);
	var filterCorpCnt = corp_cnt2.slice(indexstartdate, indexenddate+1);
	var filterRetailCnt = retail_cnt2.slice(indexstartdate, indexenddate+1);
	DqErrorChart.data.labels = filterRepDate;
	DqErrorChart.data.datasets[0].data = filterCorpCnt;
	DqErrorChart.data.datasets[1].data = filterRetailCnt;
	DqErrorChart.update();
};

var loadChartData = () => {
    var promise = new Promise((resolve, reject) => {
        data_ajax_cntdqi();
        dataAjaxDqError();
        resolve();
    });
    $('#isLoading').prop('hidden', true);
    $('#charts').prop('hidden', false);
};

loadChartData();

$(function () {
  'use strict'

  var ticksStyle = {
    fontColor: '#495057',
    fontStyle: 'bold'
  }

  var mode = 'index'
  var intersect = true
  
	 //rb chart
	 
  var $rwarbChart = $('#indicator_rb')
  // eslint-disable-next-line no-unused-vars
  var dtbl = document.getElementById('ind_val_day'),
      dr = dtbl.getElementsByTagName('td');
	  
	var val_day = new Array();
	  
	  for (var a=0;a<dr.length;a++) {
		val_day.push(dr[a].innerHTML);
		}
	
	var rtbl = document.getElementById('ind_rwa_rb'),
        rr = rtbl.getElementsByTagName('td');
	  
	var ind_rwa = new Array();
	  
	  for (var b=0;b<rr.length;b++) {
		ind_rwa.push(rr[b].innerHTML);
		}
		
	var etbl = document.getElementById('ind_ead_rb'),
        er = etbl.getElementsByTagName('td');
	  
	var ind_ead = new Array();
	  
	  for (var c=0;c<er.length;c++) {
		ind_ead.push(er[c].innerHTML);
		}
		
	var ctbl = document.getElementById('ind_cnt_rb'),
        cr = ctbl.getElementsByTagName('td');
	  
	var ind_cnt = new Array();
	  
	  for (var d=0;d<cr.length;d++) {
		ind_cnt.push(cr[d].innerHTML);
		}
		
	var ybor = document.getElementById('yellow_border'),
        yb = ybor.getElementsByTagName('td');
	  
	var yel_bor = new Array();
	  
	  for (var e=0;e<yb.length;e++) {
		yel_bor.push(yb[e].innerHTML);
		}
		
	var rbor = document.getElementById('red_border'),
        rb = rbor.getElementsByTagName('td');
	  
	var red_bor = new Array();
	  
	  for (var f=0;f<rb.length;f++) {
		red_bor.push(rb[f].innerHTML);
		}
		
  var rwarbChart = new Chart($rwarbChart, {
    data: {
      labels: val_day, //['18th', '20th', '22nd', '24th', '26th', '28th', '30th'],
      datasets: [{
		label: 'ИП RWA',
        type: 'line',
        data: ind_rwa, //[100, 120, 170, 167, 180, 177, 160],
        backgroundColor: 'transparent',
        borderColor: '#2b872d',//'#007bff',
        pointBorderColor: '#2b872d',
        pointBackgroundColor: '#2b872d',
        fill: false
        // pointHoverBackgroundColor: '#007bff',
        // pointHoverBorderColor    : '#007bff'
      },
      {
		label: 'ИП EAD',
        type: 'line',
        data: ind_ead, //[60, 80, 70, 67, 80, 77, 100],
        backgroundColor: 'tansparent',
        borderColor: '#cfd143',//'#ced4da',
        pointBorderColor: '#cfd143',
        pointBackgroundColor: '#cfd143',
        fill: false
        // pointHoverBackgroundColor: '#ced4da',
        // pointHoverBorderColor    : '#ced4da'
      },
      {
		label: 'ИП по количеству',
        type: 'line',
        data: ind_cnt,
        backgroundColor: 'tansparent',
        borderColor: '#3c8dbc',
        pointBorderColor: '#3c8dbc',
        pointBackgroundColor: '#3c8dbc',
        fill: false
        // pointHoverBackgroundColor: '#ced4da',
        // pointHoverBorderColor    : '#ced4da'
      },
	  {
        type: 'line',
        data: yel_bor,
		lineTension: 0,
		fill: false,
        backgroundColor: 'tansparent',
        borderColor: 'yellow',
		borderDash: [5, 5],
		pointRadius: 0,
        pointBorderColor: 'tansparent',
        pointBackgroundColor: 'tansparent'
        // pointHoverBackgroundColor: '#ced4da',
        // pointHoverBorderColor    : '#ced4da'
      },
	  {
        type: 'line',
        data: red_bor,
		lineTension: 0,
		fill: false,
        backgroundColor: 'tansparent',
        borderColor: 'red',
		borderDash: [5, 5],
		pointRadius: 0,
        pointBorderColor: 'tansparent',
        pointBackgroundColor: 'tansparent'
        // pointHoverBackgroundColor: '#ced4da',
        // pointHoverBorderColor    : '#ced4da'
      }
	  ]
    },
    options: {
      maintainAspectRatio: false,
      tooltips: {
			filter: function (tooltipItem) {
				return tooltipItem.datasetIndex <= 2;
				},
        mode: mode,
        intersect: intersect
      },
		pan: {
			enabled: true,
			mode: 'y'
			},
		zoom: {
			enabled: true,
			mode: 'y'
			},
      hover: {
        mode: mode,
        intersect: intersect
      },
      legend: {
        display: false
      },
      scales: {
        yAxes: [{
           display: true,
          gridLines: {
            display: true/*,
            lineWidth: '4px',
            color: 'rgba(0, 0, 0, 1)'*/
            //zeroLineColor: 'transparent'
          },
          ticks: $.extend({
            beginAtZero: true
          }, ticksStyle)
        }],
        xAxes: [{
          display: false,
          gridLines: {
            display: true
          }/*,
          ticks: {callback: function(value, index) {
					return ""}
		  }*/
        }]
      }
    }
  })
})
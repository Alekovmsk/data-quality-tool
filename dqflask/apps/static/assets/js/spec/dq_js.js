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

var swalfireWhenFindEl = () => {
    const jira_link = document.getElementById('jira_link');
    const spec_href = document.getElementById('spec_href');
    if (spec_href != null){
        Swal.fire({
            title: 'Отлично!',
            text: "Контроль отправлен на верификацию",
            icon: 'success',
            confirmButtonText: 'Перейти к контролю',
            footer: jira_link.innerHTML
        }).then((result) => {
            document.location.href = spec_href.innerHTML;
        });
    } else {
        setTimeout(swalfireWhenFindEl,150);
    };
};

var showLinksSpec = () => {
    $.ajax({
        url: "/create-spec?isCreated=True",
        type: "GET",
        success: function(response) {
            $("#place_for_links").html(response);
        },
        error: function(xhr) {
        //Do Something to handle error
        }
    });
};

var done = () => {
    var i = true;
    if ($('#check_crossdb').prop('checked')) {
        let cnt = Number($('#srcCount').val());
        for (let c=1; c<=cnt; c++) {
            if ($(`#src${c}`).val() === '0') {
                i = false;
            };
            if ($(`#custom_name${c}`).val() === '') {
                i = false;
            };
            if ($(`#src_query${c}`).val() === '') {
                i = false;
            };
        };
    } else {
        for (cur in ['source','sql_query']) {
            if ($(`#${cur}`).val() === '' || $(`#${cur}`).val() === '0') {
                i = false;
            };
        };
    };

    if (i === true) {
        var div = document.getElementById('pdag');
        div.hidden = !div.hidden
        var div_load = document.getElementById('div_load');
        div_load.hidden = !div_load.hidden
        window.scrollTo(0, 0);
        next();
        swalfireWhenFindEl();
    }
    else {
        i = true;
        notValid();
        event.preventDefault();
    };
};

var showDiv = (x) => {
    var div = document.getElementById(x);
    div.hidden = !div.hidden
};

var ShowAndHideDivNext = (x, y, reqfields) => {
    var i = true;
    for (field in reqfields) {
        var f = document.getElementById(reqfields[field]);
        if (f.value.trim() === '' ||  f.value === '0') {
            i = false;
        };
    };
    if (i === true) {
        var div1 = document.getElementById(x);
        var div2 = document.getElementById(y);
        div1.hidden = !div1.hidden;
        div2.hidden = !div2.hidden;
        window.scrollTo(0, 0);
        next();
    } else {
        i = true;
        notValid();
    };
};


var ShowAndHideDivPrev = (x, y, reqfields) => {
    var i = true;
    for (field in reqfields) {
        var f = document.getElementById(reqfields[field]);
        if (f.value.trim() === '' ||  f.value === '0') {
            i = false;
        };
    };
    if (i === true) {
        var div1 = document.getElementById(x);
        var div2 = document.getElementById(y);
        div1.hidden = !div1.hidden;
        div2.hidden = !div2.hidden;
        prev();
    } else {
        i = true;
    };
};

function printSch() {
  let value = document.getElementById('select_sch').value;
  if (value === 'minutes') {
    let minute = document.getElementById('minute_select').value;
    document.getElementById('descForSch').innerHTML = 'Запуск каждые ' + minute + ' минут';
  };
  if (value === 'hour') {
    let minute = document.getElementById('hour_select').value;
    document.getElementById('descForSch').innerHTML = 'Запуск каждый час в ' + minute + ' минут';
  };
  if (value === 'day') {
    let minute = document.getElementById('time_minute_day_select').value;
    let hour = document.getElementById('time_hour_day_select').value;
    document.getElementById('descForSch').innerHTML = 'Запуск каждый день в ' + hour + ':' + minute;
  };
  if (value === 'week') {
    let minute = document.getElementById('time_minute_week_select').value;
    let hour = document.getElementById('time_hour_week_select').value;
    let day = document.getElementById('day_of_week_select').value;
    document.getElementById('descForSch').innerHTML = 'Запуск каждую неделю в ' + day + ' в ' + hour + ':' + minute;
  };
  if (value === 'none') {
    document.getElementById('descForSch').innerHTML = 'Не запускать';
  };
  if (value === 'month') {
    let minute = document.getElementById('time_minute_month_select').value;
    let hour = document.getElementById('time_hour_month_select').value;
    let day = document.getElementById('day_of_month_select').value;
    document.getElementById('descForSch').innerHTML = 'Запуск каждый ' + day + ' день в месяце в ' + hour + ':' + minute;
  };
}

function selectSch() {
  var e = document.getElementById('select_sch');
  var value = e.value;
  var text = e.options[e.selectedIndex].text;
  var minutediv = document.getElementById('minutediv');
  var hourdiv = document.getElementById('hourdiv');
  var time_hour_day_div = document.getElementById('time_hour_day_div');
  var time_minute_day_div = document.getElementById('time_minute_day_div');
  var day_of_week_div = document.getElementById('day_of_week_div');
  var time_minute_week_div = document.getElementById('time_minute_week_div');
  var time_hour_week_div = document.getElementById('time_hour_week_div');
  if (value === 'minutes') {
    hourdiv.hidden = true;
    minutediv.hidden = false;
    time_hour_day_div.hidden = true;
    time_minute_day_div.hidden = true;
    day_of_week_div.hidden = true;
    time_minute_week_div.hidden = true;
    time_hour_week_div.hidden = true;
    day_of_month_div.hidden = true;
    time_hour_month_div.hidden = true;
    time_minute_month_div.hidden = true;
  };
  if (value === 'day') {
    hourdiv.hidden = true;
    minutediv.hidden = true;
    time_hour_day_div.hidden = false;
    time_minute_day_div.hidden = false;
    day_of_week_div.hidden = true;
    time_minute_week_div.hidden = true;
    time_hour_week_div.hidden = true;
    day_of_month_div.hidden = true;
    time_hour_month_div.hidden = true;
    time_minute_month_div.hidden = true;
  };
  if (value === 'hour') {
    hourdiv.hidden = false;
    minutediv.hidden = true;
    time_hour_day_div.hidden = true;
    time_minute_day_div.hidden = true;
    day_of_week_div.hidden = true;
    time_minute_week_div.hidden = true;
    time_hour_week_div.hidden = true;
    day_of_month_div.hidden = true;
    time_hour_month_div.hidden = true;
    time_minute_month_div.hidden = true;
  };
  if (value === 'week') {
    hourdiv.hidden = true;
    minutediv.hidden = true;
    time_hour_day_div.hidden = true;
    time_minute_day_div.hidden = true;
    day_of_week_div.hidden = false;
    time_minute_week_div.hidden = false;
    time_hour_week_div.hidden = false;
    day_of_month_div.hidden = true;
    time_hour_month_div.hidden = true;
    time_minute_month_div.hidden = true;
  };
  if (value === 'none') {
    hourdiv.hidden = true;
    minutediv.hidden = true;
    time_hour_day_div.hidden = true;
    time_minute_day_div.hidden = true;
    day_of_week_div.hidden = true;
    time_minute_week_div.hidden = true;
    time_hour_week_div.hidden = true;
    day_of_month_div.hidden = true;
    time_hour_month_div.hidden = true;
    time_minute_month_div.hidden = true;
  };
  if (value === 'month') {
    hourdiv.hidden = true;
    minutediv.hidden = true;
    time_hour_day_div.hidden = true;
    time_minute_day_div.hidden = true;
    day_of_week_div.hidden = true;
    time_minute_week_div.hidden = true;
    time_hour_week_div.hidden = true;
    day_of_month_div.hidden = false;
    time_hour_month_div.hidden = false;
    time_minute_month_div.hidden = false;
  };
  printSch();
};

function ShowAndHideDivPrev(x,y,reqfields) {
    var div1 = document.getElementById(x); 
    var div2 = document.getElementById(y);
    div1.hidden = !div1.hidden;
    div2.hidden = !div2.hidden;
}

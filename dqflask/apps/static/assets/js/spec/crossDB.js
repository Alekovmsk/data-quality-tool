
var indSrc = $('#check_crossdb').prop('checked') ? $('#srcCount').val() : 1;

/* get sources from html for generate cross-db form */
var src_list = $('#sources').val().split(',');
var srcName = $('#check_crossdb').prop('checked') ? $('#srcName').val().split(',') : [];
var srcCustomName = $('#check_crossdb').prop('checked') ? $('#srcCustomName').val().split(',') : [];
var srcSql = $('#check_crossdb').prop('checked') ? $('#srcSql').val().split(',') : [];
src_list.pop();
srcName.pop()
srcCustomName.pop()
srcSql.pop()

/* Event listener */
$('#check_crossdb').on('click', function() {eventCheckCrossDb()});
eventCheckCrossDb();

/* hide and show divs with cross-database queries */
function eventCheckCrossDb() {

    if ($('#check_crossdb').prop('checked')) {
        $('#onedb').hide();
        $('#crossdb').show();
        for (let cur=0; cur < indSrc; cur++) {
            $('#crossdbScripts').append(getHtml(src_list, cur+1, srcName[cur], srcCustomName[cur], srcSql[cur]));
        };
        $('#srcCount').val(indSrc);

        countSrcState();
    } else {
        $('#crossdb').hide();
        $('#onedb').show();
        $('#crossdbScripts').html('');
        $('#srcCount').val(0);
    };
};

function getHtml(sources, index, selectedSrc = null, enteredSrcName = null, enteredSql = null) {

    var options = (val, src) => {
        return `<option value = "${val}" ${src == val ? 'selected' : ''}>${val}</option>`
    };

    return `
        <div class="form-group" style="border: 1px solid #dee2e6; padding: 1%; background-color: #f8f9fa33" id="src_div${index}">
            <div class="form-group" style="float:left;">
                <select class="is-${selectedSrc != null ? 'valid' : 'invalid'} form-control" style="width: 160%;"
                        onmousedown="validSelect('src${index}');" id="src${index}"  name="src${index}"
                        onchange="fixChanges('dq_dag_crossdb_hdim');">
                    <option value = "0" disabled selected>Выберите источник</option>
                    ${sources.map((val, index) => options(val, selectedSrc))}
                </select>
            </div>
            <div class="form-group" style="float:right">
                <input type="text" class="form-control is-${enteredSrcName != null ? 'valid' : 'invalid'}"
                       onfocus="validText('custom_name${index}');" style="width: 180%; margin-left:-80%"
                       placeholder="Название датафрейма в главном запросе" id="custom_name${index}"
                       onchange="fixChanges('dq_dag_crossdb_hdim');"
                       name="custom_name${index}" value="${enteredSrcName != null ? enteredSrcName : ''}">
            </div>
                <div class="form-group" style="width: 100%;">
                <button id ="butShow" type="button" class="btn btn-block btn-default" onclick="showDiv('div_src_query${index}')">Запрос</button>
                    <div id="div_src_query${index}" hidden style="display:flex" class="input-group mb-3" style="width: 100%;">
                        <textarea class="form-control is-${enteredSql != null ? 'valid' : 'invalid'}" rows="12"
                                  onfocus="validText('src_query${index}');" id="src_query${index}"
                                  onchange="fixChanges('dq_dag_crossdb_hdim');"
                                  name="src_query${index}">${enteredSql != null ? enteredSql : ''}</textarea>
                    </div>
                </div>
            </div>
        </div>`
};

var addSrc = () => {
    indSrc++;
    $('#crossdbScripts').append(getHtml(src_list, indSrc));
    $('#srcCount').val(indSrc);
    countSrcState();
};

var removeSrc = () => {
    $(`#src_div${indSrc}`).remove();
    indSrc--;
    $('#srcCount').val(indSrc);
    countSrcState();
};

function countSrcState() {
    if (indSrc == 1) {
        $('#minus_src').prop('disabled', true);
    } else {
        $('#minus_src').prop('disabled', false);
    };
};

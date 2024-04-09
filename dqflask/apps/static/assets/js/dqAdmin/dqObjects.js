import {getDataTable, setDelay} from './dataTableAdmin.js'
import {postAjax} from './addEntity.js'

const deletedObjectState = () => {
    var isDeletedTeam = $('#isDeletedObject').val();
    if (isDeletedTeam == 'Y') {
        $('#base_name, #schema, #table_name, #description').prop('disabled', true);
        $('#updateObject, #removeObject').prop('hidden', true);
        $('#restoreObject').prop('hidden', false);
    } else {
        $('#base_name, #schema, #table_name, #description').prop('disabled', false);
        $('#updateObject, #removeObject').prop('hidden', false);
        $('#restoreObject').prop('hidden', true);
    };
};

deletedObjectState();

const objectsColumn = [
    {
        data: 'uk',
        render: function (data) {
            return `<a href="/admin/adm-objects/${data}">${data}</a>`;
        }
    },
    {
        data: 'schema',
        render: function (data, type, row) {
            return data + '.' + row.table_name;
        }
    },
    {data: 'description'},
    {data: 'deleted_flag'}
];

var myTable = getDataTable('objects', objectsColumn, 'adm-objects');
setDelay(myTable, 400);

var authorizedLogin = $('#login').html();

$('#addObject, #updateObject, #restoreObject, #removeObject').on('click', function() {

    var elementId = $(this).attr('id');
    var formData = {
        uk: $('#uk').val(),
        base_name: $('#base_name').val(),
        schema: $('#schema').val(),
        table_name: $('#table_name').val(),
        description: $('#description').val()
    };
    var successMessageMap = {
        'addObject': ' добавлен',
        'updateObject': 'изменен',
        'restoreObject': 'восстановлен',
        'removeObject': 'удален'
    }

    postAjax(elementId, formData, authorizedLogin, 'Объект ' + successMessageMap[elementId]);

    if (elementId == 'removeObject') {
        $('#isDeletedObject').val('Y');
    } else if (elementId == 'restoreObject') {
        $('#isDeletedObject').val('N');
    };
    myTable.draw();
    deletedObjectState();
});

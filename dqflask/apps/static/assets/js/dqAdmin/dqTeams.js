import {getDataTable, setDelay} from './dataTableAdmin.js'
import {postAjax} from './addEntity.js'
import {verifyField} from './verifyField.js'

/* Get user's teams */
var authorizedLogin = $('#login').html();
var userTeams = $('#userTeams').val();
userTeams = userTeams.slice(1, -1).split(', ');

/* DataTable start */
const teamsColumn = [
    {
        data: 'id',
        render: function (data) {
            for (let i=0; i < userTeams.length; i++) {
                if (data == userTeams[i]) {
                    return `<a href="/admin/adm-teams/${data}">${data}</a>`;
                };
            };
            return data;
        }
    },
    {data: 'name'},
    {data: 'description'},
    {
        data: 'edit_mode',
        render: function (data) {
            return data == 'nobody' ? 'Только офицер' : data == 'all' ? 'Все члены команды' : 'Только администраторы команды';
        }
    },
    {
        render: function (data, type, row) {
            let response = 'Нет';
            for (let i=0; i < userTeams.length; i++) {
                if (row.id == userTeams[i]) {
                    response = 'Да';
                    break;
                };
            };
            return response;
        }
    },
    {
        data: 'deleted_flag',
        render: function (data) {
            return data == 'Y' ? 'Да' : 'Нет';
        }
    },
];

var myTable = getDataTable('teams', teamsColumn, 'adm-teams');
setDelay(myTable, 400);
/* DataTable end */

/* Ajax to back for CRUD (start) */
var requiredAttributes = ['name', 'description'];

$('#addTeam').on('click', function() {
    let verified = true;
    for (let i=0; i < requiredAttributes.length; i++) {
        verified = verifyField(requiredAttributes[i]);
        if (!verified) {
            return false;
        };
    };

    var formData = {
        name: $('#name').val(),
        description: $('#description').val(),
        edit_mode: $('#edit_mode').val()
    };
    postAjax('addTeam', formData, authorizedLogin, 'Команда добавлена');
    myTable.draw();
});

$('#requestToTeam, #exitTeam').on('click', function() {
    var endpoint = $(this).attr('id');

    var formData = {
        user_id: authorizedLogin,
        team_id: $('#team_id').val()
    };
    var successMessage = endpoint == 'requestToTeam' ? 'Запрос на вступление в команду отправлен администраторам команды' :
        'Вы успешно вышли из команды';

    postAjax(endpoint, formData, authorizedLogin, successMessage);
    if (endpoint == 'exitTeam') {
        setTimeout(function(){
            location.reload();
        }, 4000);
    };
});
/* Ajax to back for CRUD (end) */

/* State for selected rows from DataTable (start) */
const selectTeamState = (selected, exist) => {
    if (selected) {
        $('#team_id_div').prop('hidden', false);
        if (exist) {
            $('#exitTeam').prop('hidden', false);
            $('#requestToTeam').prop('hidden', true);
        } else {
            $('#exitTeam').prop('hidden', true);
            $('#requestToTeam').prop('hidden', false);
        };
    } else {
        $('#requestToTeam, #exitTeam, #team_id_div').prop('hidden', true);
    };
};

myTable.on('click', 'tbody tr', (e) => {
    let classList = e.currentTarget.classList;

    if (classList.contains('selected')) {
        classList.remove('selected');
        selectTeamState(false);
    } else {
        myTable.rows('.selected').nodes().each((row) => row.classList.remove('selected'));
        classList.add('selected');
        $('#team_id').val(e.currentTarget.cells[0].innerText);
        if (e.currentTarget.cells[4].innerText == 'Нет') {
            selectTeamState(true, false);
        } else {
            selectTeamState(true, true);
        };
    };
});
/* State for selected rows from DataTable (end) */

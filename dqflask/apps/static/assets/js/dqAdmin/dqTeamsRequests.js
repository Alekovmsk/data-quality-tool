import {getDataTable, setDelay} from './dataTableAdmin.js'
import {postAjax} from './addEntity.js'

/* Get authorized login */
var authorizedLogin = $('#login').html();

var myRequests = $('#myRequests').prop('checked') ? true : false;

/* DataTable start */
const teamsColumns = [
    {data: 'team_id'},
    {data: 'team_name'},
    {data: 'user_id'},
    {data: 'login'},
    {data: 'full_name'}
];

var myTable = getDataTable('team_user', teamsColumns, `team-requests?login=${authorizedLogin}&myRequests=${myRequests}`);
setDelay(myTable, 400);
/* DataTable end */

console.log(myTable)

/* State for selected rows from DataTable (start) */
const selectTeamState = (selected) => {
    if (selected) {
        $('#declineUser').prop('hidden', false);
        if (!myRequests) {
            $('#acceptUser').prop('hidden', false);
        };
    } else {
        $('#acceptUser, #declineUser').prop('hidden', true);

        $('#team_id').val('');
        $('#name').val('');
        $('#username').val('0');
        $('#username').trigger('change');
        $('#is_owner').prop('checked', false);
    };
};

selectTeamState(false);

myTable.on('click', 'tbody tr', (e) => {
    let classList = e.currentTarget.classList;

    if (classList.contains('selected')) {
        classList.remove('selected');
        console.log(myTable.cells)

        selectTeamState(false);
    } else {
        myTable.rows('.selected').nodes().each((row) => row.classList.remove('selected'));
        classList.add('selected');
        $('#team_id').val(e.currentTarget.cells[0].innerText);
        $('#name').val(e.currentTarget.cells[1].innerText);

        var value = e.currentTarget.cells[2].innerHTML;
        var text = `${e.currentTarget.cells[4].innerHTML} (${e.currentTarget.cells[3].innerHTML})`;
        var newOption = new Option(text, value, false, false);

        classList.add('selected');
        $('#username').append(newOption);
        $('#username').val(value);
        $('#username').trigger('change');

        selectTeamState(true);
    };
});
/* State for selected rows from DataTable (end) */

/* Ajax to back for CRUD (start) */
$('#acceptUser, #declineUser').on('click', function() {
    var endpoint = $(this).attr('id');

    var formData = {
        team_id: $("#team_id").val(),
        user_id: $("#username").val(),
        is_owner: $("#is_owner:checked").length ? 'Y' : 'N'
    };

    var successMessage = endpoint == 'acceptUser' ? 'Пользователь добавлен' :
        'Запрос отклонен';

    postAjax(endpoint, formData, authorizedLogin, successMessage);
    selectTeamState(false);
    myTable.draw();
});
/* Ajax to back for CRUD (end) */
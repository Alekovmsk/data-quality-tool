import {getDataTable, setDelay} from './dataTableAdmin.js'

var isAdmin = $('#isAdmin').prop('checked');

const teamsColumn = [
    {data: 'user_id'},
    {data: 'full_name'},
    {data: 'email'},
    {data: 'is_owner'}
];

var pathname = window.location.pathname.split('/');
var myTable = getDataTable('team_user', teamsColumn, `get_team_users?team_id=${pathname.at(-1)}`);
setDelay(myTable, 400);

const deletedTeamState = () => {
    var isDeletedTeam = $('#isDeletedTeam').val();
    if (isDeletedTeam == 'Y') {
        $('#name, #description, #edit_mode').prop('disabled', true);
        $('#updateTeam, #removeTeam').prop('hidden', true);
        $('#username, #is_owner').prop('disabled', true);
        $('#addUser, #updateUser, #removeUser').prop('hidden', true);

        $('#restoreTeam, #hardRemoveTeam').prop('hidden', false);
    } else {
        $('#name, #description, #edit_mode').prop('disabled', false);
        $('#updateTeam, #removeTeam').prop('hidden', false);
        $('#username, #is_owner').prop('disabled', false);
        $('#addUser, #updateUser, #removeUser').prop('hidden', false);

        $('#restoreTeam, #hardRemoveTeam').prop('hidden', true);
    };
};

const selectUserState = (selectRowState) => {
    if (selectRowState) {
        $('#addUser').prop('hidden', true);
        $('#updateUser, #removeUser').prop('hidden', false);
        $('#username').prop('disabled', true);
    } else {
        $('#addUser').prop('hidden', false);
        $('#updateUser, #removeUser').prop('hidden', true);
        $('#username').prop('disabled', false);
    };
    if ($('#isDeletedTeam').val() == 'Y') {
        $('#addUser, #updateUser, #removeUser').prop('hidden', true);
        $('#username, #is_owner').prop('disabled', true);
    };
};

const isAdminState = () => {
    if (!isAdmin) {
        $('#addUser, #updateUser, #removeUser').prop('hidden', true);
        $('#updateTeam, #removeTeam, #restoreTeam, #hardRemoveTeam').prop('hidden', true);
        $('#name, #description, #username, #is_owner, #edit_mode').prop('disabled', true);
    };
};

deletedTeamState();
selectUserState();
isAdminState();

myTable.on('click', 'tbody tr', (e) => {
    let classList = e.currentTarget.classList;

    if (classList.contains('selected')) {
        classList.remove('selected');
        $('#username').val('0');
        $('#username').trigger('change');
        $("#is_owner").prop("checked", false);

        selectUserState(false);
        isAdminState();
    }
    else {
        myTable.rows('.selected').nodes().each((row) => row.classList.remove('selected'));
        var value = e.currentTarget.cells[0].innerHTML;
        var text = `${e.currentTarget.cells[1].innerHTML} (${e.currentTarget.cells[2].innerHTML})`;
        var isOwner = e.currentTarget.cells[3].innerHTML == 'Y' ? true : false;
        var newOption = new Option(text, value, false, false);

        classList.add('selected');
        $('#username').append(newOption);
        $('#username').val(value);
        $('#username').trigger('change');
        $("#is_owner").prop("checked", isOwner);

        selectUserState(true);
        isAdminState();
    };
});

export {myTable, deletedTeamState, selectUserState};

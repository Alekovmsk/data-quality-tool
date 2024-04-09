import {myTable, deletedTeamState, selectUserState} from './dqTeamUsers.js'

var authorizedLogin = $('#login').html();

$('#addUser, #updateUser, #removeUser, #updateTeam, #restoreTeam, #removeTeam, #hardRemoveTeam').on('click', function() {
    var formData = {
        team_id: $("#team_id").val(),
        user_id: $("#username").val(),
        is_owner: $("#is_owner:checked").length ? 'Y' : 'N',
        name: $('#name').val(),
        description: $('#description').val(),
        edit_mode: $('#edit_mode').val()
    };

    var messageTitle = {
        'addUser': 'Пользователь добавлен',
        'updateUser': 'Пользователь обновлен',
        'removeUser': 'Пользователь удален',
        'updateTeam': 'Команда обновлена',
        'restoreTeam': 'Команда восстановлена',
        'removeTeam': 'Команда удалена',
        'hardRemoveTeam': `Команда удалена без возможности восстановления.
        Вы будете перенаправлены на страницу с командами`,
    };

    var endpoint = $(this).attr('id');

    $.ajax({
        type: "POST",
        url: `/api/admin/${endpoint}?login=${authorizedLogin}`,
        data: formData,
        dataType: "json",
        encode: true,
    }).done(function (data) {
        $('#username').val('0');
        $('#username').trigger('change');
        $('#is_owner').prop('checked', false);

        if (data === undefined) {
            myTable.draw();
            Swal.fire({
                icon: 'success',
                title: messageTitle[endpoint],
                position: 'top-end',
                showConfirmButton: false,
                toast: true,
                timer: 5000
            });

            if (endpoint == 'removeTeam') {
                $('#isDeletedTeam').val('Y');
                deletedTeamState();
            } else if (endpoint == 'restoreTeam') {
                $('#isDeletedTeam').val('N');
                deletedTeamState();
                selectUserState(false);
            } else if (endpoint == 'hardRemoveTeam') {
                setTimeout(function(){
                    let url = window.location.protocol + '//' + window.location.host;
                    location.href = `${url}/admin/adm-teams`;
                }, 5000);
            } else {

                selectUserState(false);
            };
        } else {
            Swal.fire({
                icon: 'error',
                title: data.message,
                position: 'top-end',
                showConfirmButton: false,
                toast: true,
                timer: 3000
            });
        };
    });

    event.preventDefault();
});

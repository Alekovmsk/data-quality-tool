import {getDataTable, setDelay} from './dataTableAdmin.js'

const usersColumn = [
    {
        data: 'user_id',
        render: function (data) {
            return `<a href="/admin/adm-users/${data}">${data}</a>`;
        }
    },
    {data: 'name'},
    {data: 'email'},
    {data: 'role'}
];

var myTable = getDataTable('users', usersColumn, 'adm-users');
setDelay(myTable, 400);


$(document).ready(
    function () {
        $('#obj_name').select2({ theme: 'bootstrap' });
        $("#obj_name + span").addClass("is-invalid");
    }
);

const fixChanges = (entity) => {
    $(`#${entity}`).prop('checked', true);
};

const editVerSpec = () => {
    let uk = $('#uk').val();
    let ver = $('#version').val();
    let url = window.location.href + `?ver=${ver}`;
    window.location.href = url;
};

const deleteSpec = (uk) => {
    Swal.fire({
        title: 'Вы уверены?',
        text: "",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Да',
        cancelButtonText: 'Отменить'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire(
                'Спецификация удалена!',
                '',
                'success'
            );
            setTimeout(() => {
                let url = window.location.protocol + '//' + window.location.host  + `/delete-spec/${uk}`;
                window.location.href = url;
            }, 1500);
        };
    });
};
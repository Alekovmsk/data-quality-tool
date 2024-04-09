
$(document).ready(
    function(){
        $('#obj_name').select2 ({ theme: 'bootstrap' });
        $("#obj_name + span").addClass("is-invalid");
    }
);
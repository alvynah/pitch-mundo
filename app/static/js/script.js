$(document).ready(function() {

    $("#profileButton").click(function() {
        $("#profileStatus").slideDown('1500').hide('1000');
        $(".updateImg").show('1500');
    });
    $("#submit").click(function() {
        $(".updateImg").slideUp('2000');
        $("#profileStatus").slideDown('1500');
    });

});
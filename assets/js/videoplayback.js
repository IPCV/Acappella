$('.videoplay').on('click', function () {
    var videoURL = $("#qm").prop('src');
    videoURL = videoURL.replace("&autoplay=1", "");
    $('#qm').prop('src','');
    $('#qm').prop('src',videoURL);
    $("#qm")[0].src += "&autoplay=1";
});

$('.videostop').on('click', function () {
    var videoURL = $('#qm').prop('src');
    videoURL = videoURL.replace("&autoplay=1", "");
    $('#qm').prop('src','');
    $('#qm').prop('src',videoURL);
});
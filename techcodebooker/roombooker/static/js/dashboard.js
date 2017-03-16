

var Dashboard = {};

Dashboard.init = function() {
    $(document).ready(function() {
        Dashboard.bindEventListeners();
});

};
Dashboard.bindEventListeners = function(){
    $(".edit-room").off().on("click",Dashboard.showRoomDesc)
}

Dashboard.showRoomDesc = function(){
    var value = $(this).val()
    $("#"+value).slideToggle()
}

Dashboard.init();

Community = {};

Community.init = function(){
    $(document).ready(function(){
        Community.bindEventListeners();
        $("#csv").hide()
    })
};

Community.bindEventListeners = function(){
    $('.pending-action').off().on("click",Community.pendingAction)
    $("#exportCsv").off().on("click",Community.exportCsv)
}


Community.exportCsv = function(){
    $.ajax({
        url:"exportcsv",
        method:"GET",
        success: function(result){
            console.log(result)
            var x = [result]
            $("#csv").html(x).show()

        }
   })
}

Community.pendingAction = function(){
    button = $(this);
    action = button.val();
    bookingId = button.attr('data-booking-id')
    $.ajax({
        url:"pendingaction",
        method:"GET",
        data: {
            action: action,
            id:bookingId
        },
        success: function(result){
            $("#"+bookingId).fadeOut()
            $("#pending-action-msg").text(result.msg)
        }
   })
}

Community.init();
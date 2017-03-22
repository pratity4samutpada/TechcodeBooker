Community = {};

Community.init = function(){
    $(document).ready(function(){
        Community.bindEventListeners();
    })
};

Community.bindEventListeners = function(){
    $('.pending-action').off().on("click",Community.pendingAction)
}

Community.activateTabs = function(){
    $(".calendar-link").first().addClass('active')
    $(".tab-pane").first().addClass('active')
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
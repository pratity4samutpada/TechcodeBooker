Community = {};

Community.init = function(){
    js313(document).ready(function(){
        Community.bindEventListeners();
//        Community.activateTabs();
    })
};

Community.bindEventListeners = function(){
    js313('.pending-action').off().on("click",Community.pendingAction)
}

Community.activateTabs = function(){
    js313(".calendar-link").first().addClass('active')
    js313(".tab-pane").first().addClass('active')
}

Community.pendingAction = function(){
    button = js313(this);
    action = button.val();
    bookingId = button.attr('data-booking-id')
    js313.ajax({
        url:"pendingaction",
        method:"GET",
        data: {
            action: action,
            id:bookingId
        },
        success: function(result){
            js313("#"+bookingId).fadeOut()
            js313("#pending-action-msg").text(result.msg)
        }
   })
}

Community.init();
AdminExtra = {};

AdminExtra.init = function(){
    $(document).ready(function(){
        AdminExtra.bindEventListeners();
    })
};

AdminExtra.bindEventListeners = function(){
    $(".approve-pending").off().on("click",AdminExtra.approvePending);
}

AdminExtra.approvePending = function(){
    var button = $(this)
$.ajax({
        url:"approve",
        method:"GET",
        data: {
            id: button.val()
        },
        success: function(result){
            button.closest("tr").fadeOut();
            $("#pending-msg").append(result.msg)
        }
   })

};

AdminExtra.init();

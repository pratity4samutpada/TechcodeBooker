Nav = {}

Nav.init = function(){
    $(document).ready(function(){
        Nav.bindEventListeners();
    })
};

Nav.bindEventListeners = function(){
    $(".dash-nav-item").off().click(function(){return false});
    $(".dash-nav-item").off().on("click",Nav.switchView);
}

Nav.switchView = function(){
    template = $(this).attr("id")
    $.ajax({
        url:"switchview",
        method:"GET",
        data: {
            template: template
        },
        success: function(result){
            $("#main").children().remove()
            $("#main").append(result)
        }
   })
}

Nav.init();
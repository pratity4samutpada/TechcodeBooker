/**
 * Created by itc_user1 on 3/5/2017.
 */
Roombooker = {};

Roombooker.init = function(){
    $(document).ready(function(){
        Roombooker.bindEventListeners();
    })
};

Roombooker.bindEventListeners = function(){
    $(".room-option").off().on("click",Roombooker.selectRoom)
};

Roombooker.selectRoom = function(){
    $(".room-option").removeClass("selected");
    $(this).addClass("selected");
    var roomId = $(this).attr("data-value");
    $("#id_Rooms-room_id").val(roomId);
    console.log($("#id_Rooms-room_id").val());
};


Roombooker.init();
Roombooker = {};

Roombooker.init = function(){
    $(document).ready(function(){
        Roombooker.bindEventListeners();
    })
};

Roombooker.bindEventListeners = function(){
    $(".room-option").off().on("click",Roombooker.selectRoom);
};

Roombooker.selectRoom = function(){
    $("#avail-title").show();
    $(".form-1-btn").show();
    $(".room-option").removeClass("selected");
    $(this).addClass("selected");
    var roomId = $(this).attr("data-value");
    $("#id_Rooms-room_id").val(roomId);
    Roombooker.showRoomInfo(roomId);

};

Roombooker.showRoomInfo = function(roomId){

   $.ajax({
        url:"getroominfo",
        method:"GET",
        data: {
            id: roomId
        },
        success: function(result){
            var resFields = result[0].fields
            var name = resFields.room_name
            var fac = resFields.room_fac
            var cap = resFields.room_capacity
            var notes = resFields.room_notes
            $("#room-name").html(name)
            $("#room-facilities").html('Facilities: ' + fac)
            $("#room-capacity").html('Capacity: ' + cap)
            $("#room-notes").html('*Additional room notes: ' + notes)
        }
   })
};

Roombooker.init();

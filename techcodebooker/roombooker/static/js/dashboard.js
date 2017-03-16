

var Dashboard = {};

Dashboard.init = function() {
    $(document).ready(function() {
        Dashboard.chooseView();
        Dashboard.toggleRoomInfo();
        $(".dropdown-toggle").dropdown('toggle');
});

};



Dashboard.chooseView = function() {

    $("#overview-button").click(function(){
            $("#overview-view").show();
            $("#bookings-view").hide();
            $("#analytics-view").hide();
    });

    $("#bookings-button").click(function(){
        $("#bookings-view").show();
        $("#overview-view").hide();
        $("#analytics-view").hide();
    });

    $("#analytics-button").click(function() {
        $("#analytics-view").show();
        $("#overview-view").hide();
        $("#bookings-view").hide();

    })
};

Dashboard.toggleRoomInfo = function(roomId) {
    $(".dashboard-edit-room-btns").click(function() {
        $(".dashboard-rm-description").show()

});

        // $(".dashboard-rm-description").toggle('slow');
    //    should be on click get room info from using ajax and append to room ie. on click send id of room to backend and gt info and return
};



Dashboard.init();

// $.ajax({
//             url: "getroominfo",
//             method: "GET",
//             data: {
//                 id: roomId
//             },
//             success: function (result) {
//                 var resFields = result[0].fields
//                 var fac = resFields.room_fac
//                 var cap = resFields.room_capacity
//                 $("#apendto").text('Facilities : ' + fac)
//                 $("#apendto").text('Room Capacity : ' + cap)
//             }
//
//     })

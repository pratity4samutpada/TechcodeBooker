/**
 * Created by itc_user1 on 3/8/2017.
 */
Bookings = {};

Bookings.init = function(){
    $(document).ready(function(){
        Calendar.init()
        Validate.init()
    })
};


Calendar = {};

Calendar.days = [];
Calendar.months = [];
Calendar.years = [];
Calendar.times = [];

Calendar.init = function(){
        Calendar.generateCalendar();
    }

Calendar.generateCalendar = function() {
    var cols =8;
    var rows = 25;

    for (var i = 0; i < rows; i++) {
        var numRows = $("<div/>");
        numRows.addClass("rows");
        numRows.attr("id", + i);
        console.log("hi");

        $("#calendar").append(numRows);
        for (var j = 0; j < cols; j++) {
            var numCols = $("<div/>");
            numCols.addClass("columns");
            numCols.attr("id", j);
            numRows.append(numCols);

            if (j == 0 && i > 0) {
                //append number to div
                numCols.html(i + ':00');
            }
            if (j == 0 && i == 0) {
                numCols.html('time');
            }
        }
    }
};

// Calendar.ifCliked = function() {
//     $( "#btn-prev" ).click(function() {
//         get previous month or 30 days;
//     });
//     $( "#btn-next" ).click(function() {
//         get next month or 30 days;
//     });
//
// };

// var date = new Date();
// 			var d = date.getDate();
// 			var m = date.getMonth();
// 			var y = date.getFullYear();

Validate = {}

Validate.init = function(){
    Validate.bindEventListeners()
}

Validate.bindEventListeners = function(){
    $("#id_Booking-start_time").off().on("change",Validate.adjustEndTime).on("change",Validate.validateTime);
    $("#id_Booking-end_time").off().on("change",Validate.validateTime);
    $(".book-date").off().on("change",Validate.validateTime);
}

Validate.adjustEndTime = function(){
    var st = parseInt(($(this).val()))
    var etOptions = $("#id_Booking-end_time option")
    for (var i =0; i<etOptions.length; i++){
        var opt = $(etOptions[i])
        if (st >= parseInt(opt.val())){
        opt.hide()
        }else{
        opt.show()
            }
        }

    $("#id_Booking-end_time option[value="+(st+1)+"]").prop('selected',true)
    Validate.validateTime()

    }

Validate.validateTime = function(){
    var startTime = $("#id_Booking-start_time option:selected").val()
    var endTime = $("#id_Booking-end_time option:selected").val()
    var year = $("#id_Booking-booking_date_year option:selected").val()
    var month = $("#id_Booking-booking_date_month option:selected").val()
    var day = $("#id_Booking-booking_date_day option:selected").val()
    var room = $("#selected-room").attr("data-room-id")

    $.ajax({
        url:"validatetime",
        method:"GET",
        data: {
            start: startTime,
            end: endTime,
            year: year,
            month: month,
            day: day,
            room: room
        },
        success: function(result){
            var button = $("#submit-btn");
            var status = $("id_Booking-status");
            if(result.hasOwnProperty('error')){
                $("#user-message").text(result.error)
                button.prop("disabled",true);
            }
            else{
                if(result.hasOwnProperty('pending')){
                      $("#id_Booking-status").val(true);
                      $("#user-message").text(result.pending);
                   }else{
                       $("#id_Booking-status").val(false);
                       $("#user-message").text("");
                    }
            button.prop("disabled",false);
            }
        }
   })
}

Bookings.init();
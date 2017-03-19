//Namespace for time validation and other functions involving the booking form.
//Because of conflicts with the version of jQuery used by the calendar plugin, I had to rewrite the $ as js313 (meaning version 3.1.3).

Validate = {}


//Validate.init = function(){
    js313(document).ready(function(){
         Validate.bindEventListeners();
    })
//    }

Validate.bindEventListeners = function(){
    js313("#id_Booking-start_time").off().on("change",Validate.adjustEndTime).on("change",Validate.validateTime);
    js313("#id_Booking-end_time").off().on("change",Validate.validateTime);
    js313(".book-date").off().on("change",Validate.validateTime);
}

Validate.adjustEndTime = function(){
    var st = parseInt((js313(this).val()));
    var etOptions = js313("#id_Booking-end_time option");
    for (var i =0; i<etOptions.length; i++){
        var opt = js313(etOptions[i]);
        if (st >= parseInt(opt.val())){
            opt.hide();
        }else{
            opt.show();
            }
        };

    js313("#id_Booking-end_time option[value="+(st+1)+"]").prop('selected',true);
    Validate.validateTime();
    };

Validate.validateTime = function(){
    var startTime = js313("#id_Booking-start_time option:selected").val();
    var endTime = js313("#id_Booking-end_time option:selected").val();
    var year = js313("#id_Booking-booking_date_year option:selected").val();
    var month = js313("#id_Booking-booking_date_month option:selected").val();
    var day = js313("#id_Booking-booking_date_day option:selected").val();
    var room = js313("#selected-room").attr("data-room-id");
    var s_minute = js313("#id_Booking-start_minutes option:selected").val();
    var e_minute = js313("#id_Booking-end_minutes option:selected").val();


    js313.ajax({
        url:"validatetime",
        method:"GET",
        data: {
            start: startTime,
            s_minute: s_minute,
            end: endTime,
            e_minute: e_minute,
            year: year,
            month: month,
            day: day,
            room: room
        },
        success: function(result){

            var button = js313("#submit-btn");
            var status = js313("id_Booking-status");

            if(result.hasOwnProperty('error')){
                js313("#user-message").text(result.error)
                button.prop("disabled",true);
            }
            else{
                if(result.hasOwnProperty('pending')){
                      js313("#id_Booking-status").val("pending");
                      js313("#user-message").text(result.pending);
                   }else{
                       js313("#id_Booking-status").val("approved");
                       js313("#user-message").text(result.success);
                    }
            button.prop("disabled",false);
            }
        }
   })
}
//Validate.init();
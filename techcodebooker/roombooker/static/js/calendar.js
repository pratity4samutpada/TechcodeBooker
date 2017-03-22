Calendar = {};

Calendar.init = function(){
    $(document).ready(function(){
        Calendar.getEventData();
        Calendar.hideFooter()
    })
};

Calendar.getEventData = function(){
    var roomId
    var cmView = false;
    var url ="populatecal"
    if($("#selected-room").length){
         roomId = $("#selected-room").attr("data-room-id");
    }else{
        roomId = $("#calendar").attr("data-id");
        cmView = true;
        url = "calendar/populatecal"
    };
     $.ajax({
        url:url,
        method:"GET",
        data: {
            id: roomId
        },
        success: function(result){
            var eventData = JSON.parse(result)
            Calendar.createCalendar(eventData,cmView)
        }
   })
        };

Calendar.createCalendar = function(eventData,cmView){
        var slots = cmView ? slots = 4 : 2
		$('#calendar').weekCalendar({
			timeslotsPerHour: slots,
			readonly: true,
			use24Hour: true,
			height: function($calendar){
				return $(window).height();
			},
			eventRender : function(calEvent, $event) {
				if(calEvent.end.getTime() < new Date().getTime()) {
					$event.css("backgroundColor", "#aaa");
					$event.find(".time").css({"backgroundColor": "#999"});
				}
			},
			eventResize : function(calEvent, $event) {
				displayMessage("<strong>Resized Event</strong><br/>Start: " + calEvent.start + "<br/>End: " + calEvent.end);
			},
			noEvents : function() {
				displayMessage("There are no events for this week");
			},

			data:eventData
		});

		function displayMessage(message) {
			$("#message").html(message).fadeIn();
		}


	};

Calendar.hideFooter=function(){
	$("#footer").css("display","none");
};


Calendar.init();
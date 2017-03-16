Calendar = {};

Calendar.init = function(){
    $(document).ready(function(){
        Calendar.getEventData();
        Calendar.hideFooter()
    })
};

Calendar.getEventData = function(){
    var roomId = $("#selected-room").attr("data-room-id");
     $.ajax({
        url:"populatecal",
        method:"GET",
        data: {
            id: roomId
        },
        success: function(result){
            var eventData = JSON.parse(result)
            Calendar.createCalendar(eventData)
        }
   })
        };

Calendar.createCalendar = function(eventData){
		$('#calendar').weekCalendar({
			timeslotsPerHour: 2,
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
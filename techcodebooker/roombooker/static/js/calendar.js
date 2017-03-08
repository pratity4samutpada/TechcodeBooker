/**
 * Created by itc_user1 on 3/8/2017.
 */

Calendar = {};

Calendar.days = [];
Calendar.months = [];
Calendar.years = [];
Calendar.times = [];

Calendar.init = function(){
    $(document).ready(function(){
        Calendar.generateCalendar();
    })
};

Calendar.generateCalendar = function() {
    // var date = new Date();
    // var start = new Date();
    // var end = new Date();
    // start.setDate(date.getDate());
    // end.setDate(date.getDate() + 30);

    var cols =7;
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





Calendar.init();
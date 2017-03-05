/**
 * Created by itc_user1 on 3/5/2017.
 */
var imageArray = [];

function roomImages() {
    for (var i = 0; i < imageArray.length; i++) {
        var image = $("<img/>").addClass("room_img");
        $( ".room_div" ).append(image);
    }
}

$(function() {
    console.log("Page ready");
    uriObj = $.getJSON("stocks.json", function(data) {
        console.log(data);
        console.log(data.ToCheck);
        for (let item in data["ToCheck"]) {
            console.log(data["ToCheck"][item]);
            $('.tracked_stocks').append("<li class='stockitem'><a href='" + data["ToCheck"][item] + "'>" + item + "</a></li>");
        }
    });
});
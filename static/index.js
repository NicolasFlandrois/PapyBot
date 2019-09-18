// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery

$.ajax({
        type: "GET",
        url: `${window.origin}/message`,
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            message: $("#user_request").val()
        }),

        success: function(response) {
            console.log(response);
        },
        error: function(response) {
            console.log(response);
        }
});

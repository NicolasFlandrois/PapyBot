// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery

// Sending the request to server
$.ajax({
        type: "GET",
        url: `${window.origin}/message/`,
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

// Manque une fonction qui à validation btn-submit envoie la requete @ serveur

// Receiving the response from to server
// $.get(`${window.origin}/message/`, {category:'client', type:'premium'})
//      .done(function(response) {
//            $("#dialogBox").html(response.amount);
//      });

// User Resquest should be incoporate/interpolate in:
// "<p col-7 d-flex justify-content-center p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white mr-auto'>" + el1 + "</p>";

// PapyBot Response should be incorporate/interpolate in:
// "<p class='col-7 d-flex justify-content-center p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white mr-auto'>" + words + "</p>"


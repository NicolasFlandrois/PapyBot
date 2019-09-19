// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery

// $.ajax({
//         type: "GET",
//         url: `${window.origin}/message`,
//         contentType: "application/json",
//         dataType: "json",
//         data: JSON.stringify({
//             message: $("#user_request").val()
//         }),

//         success: function(response) {
//             console.log(response);
//         },
//         error: function(response) {
//             console.log(response);
//         }
// });

// $.get(`${window.origin}/message`, {category:'client', type:'premium'})
//      .done(function(response) {
//            $("#dialogBox").html(response.amount);
//      });

// User Resquest should be incoporate/interpolate in:
// "<p col-7 d-flex justify-content-center p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white mr-auto'>" + el1 + "</p>";

// PapyBot Response should be incorporate/interpolate in:
// "<p class='col-7 d-flex justify-content-center p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white mr-auto'>" + words + "</p>"

$(()=> {

    $("#submit_btn").click( submit_entry() {

        let container = $("#dialogBox");

        let el = $("#user_request");
        console.log(el);
        let url = "${window.origin}/message/" + el.val() + "/";
        console.log(url);

        // $.get(url, (res)=> {

        //     let words = JSON.parse(res);
        //     container.html("");
        //     let el = "<p> PAPY" + words + "</p>";
        //     console.log(el);
        //     container.append(el);

        // })

    });

});

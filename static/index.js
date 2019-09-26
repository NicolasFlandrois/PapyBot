// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery



// User Resquest should be incoporate/interpolate in:
// "<p col-7 d-flex justify-content-center p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white mr-auto'>" + el1 + "</p>";

// PapyBot Response should be incorporate/interpolate in:
// "<p class='col-7 d-flex justify-content-center p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white mr-auto'>" + words + "</p>"


// $( "form" ).on( "submit", function( event ) {
//     event.preventDefault();

//     let req = JSON.stringify($( this ).serialize());
//     console.log(req);  // Returns a console.log = "user_request=Hello%20world"


//     reqstr = JSON.parse(req)
//     console.log(reqstr);  //Returns a Console.log = <p>"user_request=Hello%20world"</p>

//     let container = $("#dialogBox");
//     container.html("");
//     container.append("<p>" + reqstr + "</p>")
//     // Returns 'user_request=Hello%20world' on Browser display, & erased all previous text


// });

$(document).ready(function() {

    $('form').on('submit', function(event) {

        event.preventDefault();

        $.ajax({
            data : {
                question : $('#userRequest').val()
            },
            type : 'POST',
            url : '/msg'
        });

        $.done(function(data) {

            $('#dialogBox').text(data).show();

        });


    });

});

// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery



// User Resquest should be incoporate/interpolate in:
// "<p col-7 d-flex justify-content-center p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white mr-auto'>" + el1 + "</p>";

// PapyBot Response should be incorporate/interpolate in:
// "<p class='col-7 d-flex justify-content-center p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white mr-auto'>" + words + "</p>"

$(function() {
    $('#submit_btn').on('click', function() {

        let container = $("#dialogBox");
        container.html("");

        let req = $("#user_request");
        let url = "http://127.0.0.1:5000/msg/" + req.val() + "/";

        container.append(req);

        console.log(req);
        console.log(url);

      $.get(url,

            (res)=> {
            let words = JSON.parse(res);
            console.log(words)

            let results = "<p>" + words + "</p>";
            console.log(results);
            container.append(results);
        });

    });
});

// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery

$(()=> {
            // Get question request from HTML (AJAX/JQuery)
            $("#submit_btn").click(function(submit_message()) {
                let message = $("#user_request");

                let reqDisplay = "<p col-7 d-flex justify-content-center p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white mr-auto'>" + message + "</p>";
                console.log(reqDisplay);
                request = $("#dialogBox");
                request.html("");
                request.append(reqDisplay);

                // Post question request to Python Flask Server (AJAX/JQuery)
                let url = "http://127.0.0.1:5000/message/" + message.val() + "/";
                // Get Responce from Python Flask Server (AJAX/JQuery)
                $.get(url, (res)=> {
                    let words = JSON.parse(res);
                    let results = $("#dialogBox");
                    results.html("");
                    // Do sthg here
                    // Here goes :     <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY&callback=myMap"></script>

                    let el2 = "<p class='col-7 d-flex justify-content-center p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white mr-auto'>" + words + "</p>";
                    console.log(el2);
                    // Post Responce to HTML
                    results.append(el2);

                    })
                });
        });

// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery

$(()=> {
    // Get question request from HTML (AJAX/JQuery)
    $("#user_post").on("#submit_btn", ()=> {
        let el1 = $("#user_post");

        let el1 = "<p class='d-flex justify-content-center p-2 float-left rounded-pill border-right border-bottom border-secondary bg-primary align-middle text-white'>" + el1 + "</p>";
        console.log(el1);
        question = $("#userSide");
        question.html("");
        question.append(el1);

        // Post question request to Python Flask Server (AJAX/JQuery)
        let url = "http://127.0.0.1:5000/message/" + el1.val() + "/";
        // Get Responce from Python Flask Server (AJAX/JQuery)
        $.get(url, (res)=> {
            let words = JSON.parse(res);
            let results = $("#papySide");
            results.html("");
            // Do sthg here
            // Here goes :     <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY&callback=myMap"></script>

            let el2 = "<p class='d-flex justify-content-center p-2 float-left rounded-pill border-left border-bottom border-secondary bg-success align-middle text-white'>" + words + "</p>";
            console.log(el2);
            // Post Responce to HTML
            results.append(el2);

        })
    };
});

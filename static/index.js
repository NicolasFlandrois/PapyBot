// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery

// Get question request from HTML (AJAX/JQuery)

// Post question request to Python Flask Server (AJAX/JQuery)

// Get Responce from Python Flask Server (AJAX/JQuery)

// Post Responce to HTML > Use a look like a text messenger round shape & distinguish Human (User) from PapyBot (Computer) (AJAX/JQuery)

$(()=> {
    $("#user_post").on("#submit_btn", ()=> {
        let el = $("#user_post");
        let url = "http://127.0.0.1:5000/message/" + el.val() + "/";
        $.get(url, (res)=> {
            let words = JSON.parse(res);
            let container = $(".dialogbox");
            container.html("");
            // Do sthg here
            // Here goes :     <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY&callback=myMap"></script>
            for( word of words) {
                let el = "<p>" + word + "</p>";
                console.log(el);
                container.append(el);
            }
        })
    });
});

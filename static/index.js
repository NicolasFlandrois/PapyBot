// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery

// $(()=> {
//             // Get question request from HTML (AJAX/JQuery)
//             $("#user_post").on("#submit_btn", ()=> {
//                 let request = $("#user_request");

//                 let reqDisplay = "<p col-7 d-flex justify-content-center p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white mr-auto'>" + el1 + "</p>";
//                 console.log(reqDisplay);
//                 request = $("#dialogBox");
//                 request.html("");
//                 request.append(el1);

//                 // Post question request to Python Flask Server (AJAX/JQuery)
//                 let url = "http://127.0.0.1:5000/message/" + el1.val() + "/";
//                 // Get Responce from Python Flask Server (AJAX/JQuery)
//                 $.get(url, (res)=> {
//                     let words = JSON.parse(res);
//                     let results = $("#dialogBox");
//                     results.html("");
//                     // Do sthg here
//                     // Here goes :     <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY&callback=myMap"></script>

//                     let el2 = "<p class='col-7 d-flex justify-content-center p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white mr-auto'>" + words + "</p>";
//                     console.log(el2);
//                     // Post Responce to HTML
//                     results.append(el2);

//                     })
//                 };
//         });

function submit_message() {

var message = document.getElementById("user_request");

var entry = {
  message: message.value
};

fetch(`${window.origin}/message`, {
    method: "GET",
    credentials: "include",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
    "content-type": "application/json"
    })
})

.then(function (response) {
    if (response.status !== 200) {
      console.log(`Looks like there was a problem. Status code: ${response.status}`);
      return;
    }
    response.json().then(function (data) {
      console.log(data);
    });
})

.catch(function (error) {
    console.log("Fetch error: " + error);
});

}

// Author : Nicolas Flandrois
// Date : Wed 02 Oct 2019 16:51:11 CEST
// Javascript & Ajax & Jquery

let url = location.origin + '/msg/';

function renderUser(res){
    $( "#dialogBox" ).append("<div class='col-7 d-flex justify-content-center p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white mr-auto'>" + res + "</div>");
};

function renderPapy(req){
    $( "#dialogBox" ).append("<div class='col-7 d-flex justify-content-center p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white mr-auto'>" + req + "</div>");
};


function getRequest(input){
    $.get(url+input, null, function(response){
        renderUser(input);
        if (response.status == 0) {
            renderPapy(response.papy + '<br>' + response.error);
        } else {
            renderPapy(response.papy + '<br>' + response.summary);
            renderPapy('<a class="text-white" target="_blank" href=' +  response.url +  '> Lien vers sa page Wikipedia </a>');
            let gmap = "<img src='https://maps.googleapis.com/maps/api/staticmap?center=" + response.gmap_search + "&zoom=10&size=150x150&scale=2&format=png32&markers=size:tiny%7C" + response.gmap_search + "&key=" + response.gmap_key + "'>";
            renderPapy(gmap);
        }

    });

};

$( "#submit" ).on( "click", function(){
    let button = $(event.target);
    let input = button.prev().val();
    getRequest(input);
});

$( "input" ).keyup(function(event){
    if(event.keyCode == 13)
    {
        let input = $(event.target).val();
        getRequest(input);
    }
});

// The random Greeting will be manage by Flask's jinja in This version

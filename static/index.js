// Author : Nicolas Flandrois
// Date : Wed 02 Oct 2019 16:51:11 CEST
// Javascript & Ajax & Jquery

let url = location.origin + '/msg/';

function renderUser(res){
    $( "#dialogBox" ).append("<div class='col-7 d-flex justify-content-center m-1 p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white'>" + res + "</div>");
};

function renderPapy(req){
    $( "#dialogBox" ).append("<div class='col-7 d-flex justify-content-center m-1 p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white'>" + req + "</div>");
};



function getRequest(input){
    $.get(url+input, null, function(response){
        renderUser(input);
        if (response.status == 0) {
            renderPapy(response.papy + '<br>' + response.error);
        } else {
            renderPapy(response.papy + '<br>' + response.summary);
            renderPapy('<a class="text-white" target="_blank" href=' +  response.url +  '> Lien vers sa page Wikipedia </a>');

            try{
                if (response.map != "Staticmap-API-Warning Error geocoding"){
                    let gmap = "<img src=" + response.gmap + ">";
                    console.log(gmap);
                    renderPapy(gmap);
                    console.log(response.map);
                } else {
                    console.log(response.map);
                }
            }
            catch(err){
                console.log(err)
            }

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

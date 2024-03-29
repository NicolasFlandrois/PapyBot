// Author : Nicolas Flandrois
// Date : Wed 02 Oct 2019 16:51:11 CEST
// Javascript & Ajax & Jquery

let url = location.origin + '/msg/';

function renderUser(res){
    $( "#dialogBox" ).append("<div class='col-7 d-flex justify-content-center m-1 p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white'>" + res + "</div>").fadeIn( 3000 );
    $( "#dialogBox" ).append("<div id='spinr' class='col-7 d-flex float-left'> <i class='fas fa-spinner fa-spin' style='font-size:30px'></i></div>").fadeIn( 3000 );
};

function renderPapy(req){
    $("i").fadeOut();
    $("#spinr").hide();
    $( "#dialogBox" ).append("<div class='col-7 d-flex justify-content-center m-1 p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white'>" + req + "</div>").fadeIn( 3000 );
};



function getRequest(input){
    renderUser(input);
    document.documentElement.scrollTop += 1000; //Firefox Auto ScrollTop
    $.get(url+input, null, function(response){

        if (response.status == 0) {
            renderPapy(response.papy + '<br>' + response.error);
        } else {
            renderPapy(response.papy + '<br>' + response.summary);
            renderPapy('<a class="text-white" target="_blank" href=' +  response.url +  '> Lien vers sa page Wikipedia </a>');

            if (response.gmapsource != "Error"){
                let gmap = "<a target='_blank' href=" + response.gmaplink + "> <img src=" + response.gmapsource + " alt='Google Map'> </a>";
                renderPapy(gmap);
            } else {

            }

        }

        document.documentElement.scrollTop += 300; //Firefox Auto ScrollTop


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

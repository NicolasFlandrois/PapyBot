// Author : Nicolas Flandrois
// Date : Thu 15 Aug 2019 18:51:34 CEST
// Javascript & Ajax & Jquery

let url = location.origin + '/msg/';

function renderPapy(res){
    $( "#dialogBox" ).append("<p class='col-7 d-flex justify-content-center p-3 float-right rounded-left border-left border-bottom border-secondary shadow-sm bg-success align-middle text-left text-white mr-auto'>" + res + "</p>");
};

function renderUser(req){
    $( "#dialogBox" ).append("<p class='col-7 d-flex justify-content-center p-3 float-left rounded-right border-right border-bottom border-secondary shadow-sm bg-primary align-middle text-left text-white mr-auto'>" + req + "</p>");
};

function getRequest(input){
    $.get(url+input, null, function(response){
        console.log(input);
        renderUser(input);
        console.log(response);
        renderPapy(response.res);
    });

};

$( "#submit" ).on( "click", function(){
    let button = $(event.target);
    let input = button.prev().val();
    console.log(input);
    getRequest(input);
});

$( "input" ).keyup(function(event){
    if(event.keyCode == 13)
    {
        let input = $(event.target).val();
        console.log(input);
        getRequest(input);
    }
});


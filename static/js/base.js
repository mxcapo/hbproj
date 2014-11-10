$(document).ready(function() 
{
    $("#view-guests-by-party").click(viewGuestsByParty);
    $("#party-box-row>div").hide();
    $("#party-box-row").show();

    $("#view-guests-by-guest").click(viewGuestsByGuest);

});

function viewGuestsByParty(evt) {
    console.log("ok");
    $.get('/view/party', function(result) 
    {
        // console.log(result);
        var partyBox = $("#party-box-row>div");
        for (var n=0; n<result.parties.length; n++) 
        {
            // console.log(result.parties[n]);
            var newBox = partyBox.clone().show();
            newBox.find("h3").text("Party ID: " + result.parties[n].id);
            newBox.find(".pside").html("<a href='#' class='list-group-item'>"+
                                   "<strong>Side:</strong> " + 
                                   result.parties[n].side + 
                                   "</a>");
            newBox.find(".pgroup").html("<a href='#' class='list-group-item'>"+
                                    "<strong>Group:</strong> " + 
                                    result.parties[n].grouping + 
                                    "</a>");
            newBox.find(".pguests").empty();
            for (var i=0; i<result.parties[n].guests.length; i++) 
            {
                // console.log("guest: " + result.parties[n].guests[i]);
                newBox.find(".pguests").append("<a href='#' class='list-group-item'>"+
                                           result.parties[n].guests[i][1]+
                                           " "+result.parties[n].guests[i][0]+
                                           "</a>");
            }
            newBox.appendTo("#party-box-row");
        }
    });
    // $("#main-filter").click(emptyPartyPage);

}

function viewGuestsByGuest(evt)
{
    console.log("viewing all guests");
    $.get('/view/guests', function(result)
    {
        console.log(result);
    });
}

function emptyPartyPage(evt)
{
    console.log('breaking it');
    $("#party-box-row div:not(:first-child)").empty();
}

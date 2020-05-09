var get_latest_entries = function(cities){
    $.ajax({
        type: "POST",
        url: "get_latest_entries",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        success: function(result){
            var latest_entries = result["latest_entries"]
            $("#results").empty()
            $.each(latest_entries, function(n, city_dict){
                addResult(city_dict)
            })
            $(".card").click(function(){
                route = "/view/" + this.id
                window.location.href = route
            })    
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });   
}

function addResult(city_dict) {
    var id = city_dict["id"]
    var city_name = city_dict["city"]
    var state_name = city_dict["state"]
    var img_source = city_dict["photo"]

    var card_container = $("<div class = 'card_container'>")

    var card = $("<div class='card' 'picture_frame' 'result' style = 'width: 18rem;'>")
    card.attr('id', id)

    var picture_frame = $("<div class = 'picture_frame'>")
    var picture = $("<img class= 'card-img-top'>")
    picture.attr("alt", "buildings in " + city_name)

    picture.attr('src', img_source)
    picture.attr('id', id)

    picture_frame.append(picture)
    card.append(picture_frame)

    var body = $("<div class='card-body'>")
    var title = $("<h5 class='card-title'>")
    title.append(city_name)

    var subtitle = $("<h6 class='card-subtitle mb-2 text-muted'>")
    subtitle.append(state_name)

    body.append(title, subtitle)
    card.append(body)
    card_container.append(card)
    $("#results").append(card_container)
}

$(document).on('click','.map', function(){
    city_id = this.id;
    alert('yaaa')
    route = "/view/" + city_id
    window.location.href = route
});




var delete_city = function(id){
    var id_to_delete = id         
    $.ajax({
        type: "POST",
        url: "delete_city",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(id_to_delete),
        success: function(result){
            alert("success!!!")
            cities = result["cities"]
            get_latest_entries(cities)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){
    get_latest_entries(cities)
})

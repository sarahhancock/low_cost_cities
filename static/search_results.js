var display_results = function(cities){
    nResults = 0
    $.each(cities, function(n, city_dict){
        addResult(city_dict)
        nResults++;
    })
    $("#nResults").append(nResults)
    var search = $("<div class = 'search'>")
    search.append('"', search_term, '"')
    $("#search_term").append(search)
    $(".card").click(function(){
        route = "/view/" + this.id
        window.location.href = route
    })
}

function highlightMatch(title,search_term) {
    var search_regexp = new RegExp(search_term, "gi");
    $(title).html($(title).html().replace(search_regexp, "<span class = 'highlight'>$&</span>"));
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

    picture.attr('src', img_source)
    picture.attr('id', id)

    picture_frame.append(picture)
    card.append(picture_frame)

    var body = $("<div class='card-body'>")
    var title = $("<h5 class='card-title'>")
    title.append(city_name)
    highlightMatch(title, search_term)

    var subtitle = $("<h6 class='card-subtitle mb-2 text-muted'>")
    subtitle.append(state_name)
    highlightMatch(subtitle, search_term)

    body.append(title, subtitle)
    card.append(body)
    card_container.append(card)
    $("#results").append(card_container)
}







$(document).ready(function(){
    display_results(results, search_term)
})

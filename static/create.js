function enter_data(city, state, photo, description, avg_home_price, features){
    var new_city = {
        "city": city,
        "state": state,
        "photo": photo,
        "map": "https://maps.google.com/maps?q=" + city + "%20" + state + "&t=&z=13&ie=UTF8&iwloc=&output=embed",
        "description": description,
        "avg_home_price": avg_home_price,
        "features": features
    }       
    $.ajax({
        type: "POST",
        url: "new_city",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(new_city),
        success: function(result){
            cities = result["cities"]
            id = result["id"] 
            var new_view = $("<div class = 'row new_view'>")
            var space = $("<div class = 'col-md-1'>")
            var view_btn = $("<button id = 'view_btn' class='btn btn-outline-info'>")
            view_btn.append("View City")
            new_view.append("New city successfully created!", space, view_btn)
            $("#created").append(new_view)
            $("#view_btn").click(function(){
                route = "/view/" + id
                window.location.href = route
            })
            $("#city-inp").val("")
            $("#state-inp").val("")
            $("#description-inp").val("")
            $("#avg_home_price-inp").val("")
            $("#feature1").val("")
            $("#feature2").val("")
            $("#feature3").val("")
            $("#photo-inp").val("")  
            $("#city-inp").focus()
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });    
}

function check_errors(city, state, description, photo, avg_home_price, f1, f2, f3){
    var flag = 0
    city = $.trim(city)
    state = $.trim(state)
    description = $.trim(description)
    photo = $.trim(photo)
    avg_home_price = $.trim(avg_home_price)
    f1 = $.trim(f1)
    f2 = $.trim(f2)
    f3 = $.trim(f3)

    //city input
    $("#city-error-msg").empty()
    if (city == ""){
        flag = 1
        $("#city-error-msg").append("Enter a city name.")
    }

    //state input
    $("#state-error-msg").empty()
    if (state == ""){
        flag = 1
        $("#state-error-msg").append("Enter a state name.")
    }

    //description input
    $("#description-error-msg").empty()
    if (description == ""){
        flag = 1
        $("#description-error-msg").append("Enter a description.")
    }

    //photo input
    $("#photo-error-msg").empty()
    if (photo == ""){
        flag = 1
        $("#photo-error-msg").append("Enter a photo URL.")
    }

    //avg home price input
    $("#avg_home_price-error-msg").empty()
    if (avg_home_price == ""){
        flag = 1
        $("#avg_home_price-error-msg").append("Enter an average home price.")
    } else if (!$.isNumeric(avg_home_price)){
        flag = 1
        $("#avg_home_price-error-msg").append("Average home price must be a numeric value.")
    }
    //features input
    $("#features-error-msg").empty()
    if (f1 == "" || f2 == "" || f3 == ""){
        flag = 1
        $("#features-error-msg").append("Enter 3 city features.")
    }
    return flag
}

$(document).ready(function(){
    $("#city-inp").focus()
    $("#submit").click(function(){
        $("#created").empty()
        var city = $("#city-inp").val()
        var state = $("#state-inp").val()
        var description = $("#description-inp").val()
        var avg_home_price = $("#avg_home_price-inp").val()
        var f1 = $("#feature1").val()
        var f2 = $("#feature2").val()
        var f3 = $("#feature3").val()
        var features = [
        {"name": f1, "mark_as_deleted": 0},
        {"name": f2, "mark_as_deleted": 0},
        {"name": f3, "mark_as_deleted": 0}]
        var photo = $("#photo-inp").val()
        if (check_errors(city, state, description, photo, avg_home_price, f1, f2, f3) == 0){
            enter_data(city, state, photo, description, avg_home_price, features) 
        } 
    })
})

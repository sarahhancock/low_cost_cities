var edit_city = function(id, new_description){
    data = {
        "new_description": new_description,
        "id_to_change": id
    }
    $.ajax({
        type: "POST",
        url: "/change_description",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
            route = "/view/" + id
            window.location.href = route
        },
        error: function(request, status, error){
            alert("not success")
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){
    $("#description").val(city["description"])
    $("#submit").click(function(){
        var new_description = $("#description").val()
        var id = city["id"]
        edit_city(id, new_description)
    });
    $("#discard").click(function(){
        route = "/view/" + city["id"]
        window.location.href = route
    });
})

var features_editable = 0

function add_feature(feature_n, feature){
    if (feature["mark_as_deleted"] == 0){
        var new_feature = $("<li class = 'row new-feature'>")
        var id = feature_n
        new_feature.attr("id", id)
        
        col1 = $("<div class = 'col-md-8'>")
        col1.append(feature["name"])
        $(col1).attr('id', id)
        
        var del_button = $("<button class='del_button btn btn-outline-danger'>")
        $(del_button).attr('id', id)
        $(del_button).text("X")

        col2 = $("<div class = 'col-md-1'>")
        col2.append(del_button)
        new_feature.append(col1, col2)
        $("#features").append(new_feature)
        
    } 
}

$(document).on('click','.del_button', function(){
    feature_id = this.id;
    var undo_button = $("<button class='undo_delete btn btn-outline-info'>")
    undo_button.text("Undo Delete")
    undo_button.attr("id", feature_id)
    var new_row = $("<li class = 'row'>")
    new_row.attr("id", feature_id)
    new_row.append(undo_button)
    $($(this).parent()).parent().replaceWith(new_row)
    delete_feature(city["id"], feature_id)
});

$(document).on('click','.undo_delete', function(){
    undo_delete(city['id'], this.id)
})

    


$(document).on('click','#edit-description', function(){
    makeDescriptionEditable()
});

$(document).on('click','#add-feature', function(){
    if (features_editable == 0){
       makeFeaturesEditable()
       features_editable = 1
    }

    
});


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

var delete_feature = function(city_id, feature_id){
    data = {
        "city_id": city_id,
        "feature_id": feature_id
    }
    $.ajax({
        type: "POST",
        url: "/delete_feature",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
            console.log("Success!")
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

var undo_delete = function(city_id, feature_id){
    data = {
        "city_id": city_id,
        "feature_id": feature_id
    }
    $.ajax({
        type: "POST",
        url: "/undo_delete",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data),
        success: function(result){
            route = "/view/" + city_id
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

var add_new_feature = function(id, new_feature){
    data = {
        "new_feature": new_feature,
        "id_to_change": id
    }
    $.ajax({
        type: "POST",
        url: "/add_feature",                
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

function addDescription(description_val){
    var header = $("<div class = 'features-header'> Description </div>") 
    var edit_button = $("<button href = '#'' type='button' class='btn btn-default'>")
    edit_button.append("<i id = 'edit-description' class='fas fa-edit edit'>")
    var descr = $("<div class = 'row' id = 'description'>")
    descr.append(description_val)
    $("#complete_description").append(header, edit_button, descr)
}

function makeDescriptionEditable(){
    var header = $("<div class = 'features-header'> Description </div>") 
    var editable_descr = $("<textarea id = 'description-editable'>")

    var submit = $("<button id = 'submit' class='btn btn-outline-info submit_button'>")
    submit.append("Submit")
    var discard = $("<button id = 'discard' class='btn btn-outline-info discard_button'>")
    discard.append("Discard Changes")
    var buttons = $("<div class = 'row'>")
    buttons.append(submit, discard)
    
    $("#complete_description").empty()
    $("#complete_description").append(header, $("<div class = 'row'>"), editable_descr, buttons)
    $("#description-editable").val(city["description"])
    $("#description-editable").focus()

    $("#submit").click(function(){
        var new_description = $("#description-editable").val()
        var id = city["id"]
        edit_city(id, new_description)
    });
    $("#discard").click(function(){
        route = "/view/" + city["id"]
        window.location.href = route
    });
}

function makeFeaturesEditable(){
    var space = $("<div class = 'row'>")
    $("#feature-sect").append(space)
    var newFeature = $("<li class='row new-feature'>")
    newFeature.append($("<textarea id = 'newFeature' class = 'col-md-9'>"))
    $("#feature-sect").append(newFeature, "<br>", "<br>")

    var submit = $("<button id = 'submit-f' class='btn btn-outline-info submit_button'>")
    submit.append("Add Feature")
    var discard = $("<button id = 'discard-f' class='btn btn-outline-info discard_button'>")
    discard.append("Discard Changes")
    var buttons = $("<div class = 'row'>")
    buttons.append(submit, discard)
    $("#feature-sect").append(buttons)
    $("#newFeature").focus()

    $("#submit-f").click(function(){
        var new_feature = $("#newFeature").val()
        var id = city["id"]
        features_editable = 0
        add_new_feature(id, new_feature)
    });
    $("#discard-f").click(function(){
        route = "/view/" + city["id"]
        features_editable = 0
        window.location.href = route
    });
}

$(document).ready(function(){
    $("#city").append(city["city"])
    $("#state").append(city["state"])
    var avg_home_price = city["avg_home_price"]
    $("#avg_home_price").append("$", avg_home_price.toLocaleString())
    addDescription(city["description"])
    $("#map").attr('src', city["map"])
    var features = city["features"]
    $.each(features, function(feature_n, feature){
        add_feature(feature_n, feature)
    })


})
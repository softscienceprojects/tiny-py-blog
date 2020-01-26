//do the window thing like at work

$(document).ready(function() {
    
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        console.log("form submitted")
    })
});
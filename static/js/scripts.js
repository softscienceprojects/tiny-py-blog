//do the window thing like at work

$(document).ready(function() {
    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        let form = $("#register-form").serialize();
        $.ajax({
            url: "/postregistration",
            type: "POST",
            data: form,
            success: function(response) {
                console.log(response)
            }
        });
    })
});
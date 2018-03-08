var offset = 0;
var totalSize = 0;
var logContainer = $('.js-log-container');

$('.js-get-log').on('click', function () {
    if (totalSize && totalSize <= offset) {
        logContainer.append('<p>END OF LOG</p>');
    } else {
        $.ajax({
            url: "/",
            method: "POST",
            data: {offset: offset}
        }).done(function (data) {
            if (data.ok) {
                offset = data.next_offset;
                totalSize = data.total_size;
                for (var i = 0; i < data.messages.length; i++) {
                    var message = JSON.parse(data.messages[i]).message;
                    message = '<p>' + message + '</p>';
                    logContainer.append(message);
                }
            } else {
                var reason = '<p>' + data.reason + '</p>';
                logContainer.append(reason);
            }
        });
    }

});
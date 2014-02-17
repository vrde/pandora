( function () {
    return;

    var holder = document.querySelector('.dnd');

    holder.ondragover = function () { this.classList.add('hover'); return false; };
    holder.ondragend = function () { this.classList.remove('hover'); return false; };

    holder.ondrop = function (e) {
        var file = e.dataTransfer.files[0];

        this.classList.remove('hover');
        e.preventDefault();
        console.log(file);

        return false;
    };

}) ();


$(function () {
    var uploader = new qq.FileUploader({
        action: POST_URL,
        element: $('#file-uploader')[0],
        //dropZoneElements: [ $('.dnd')[0] ],
        multiple: true,
        onComplete: function(id, fileName, responseJSON) {
            return;

            if(responseJSON.success) {
                alert("success!");
            } else {
                alert("upload failed!");
            }
        },
        onAllComplete: function(uploads) {
            window.location.reload();
            // uploads is an array of maps
            // the maps look like this: {file: FileObject, response: JSONServerResponse}
            // alert("All complete!");
        },
        params: {
            'csrf_token': CSRF_TOKEN,
            'csrf_name': 'csrfmiddlewaretoken',
            'csrf_xname': 'X-CSRFToken'
        },
    });
});


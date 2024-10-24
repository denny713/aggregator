function showNotice(type, title, message, callback) {
    Swal.fire({
        title: title,
        html: message,
        icon: type,
        showClass: {
            popup: 'animate__animated animate__zoomIn'
        },
        hideClass: {
            popup: 'animate__animated animate__zoomOut'
        }
    }).then(function () {
        callback && callback();
    });
}

function doUpload() {
    let fileInput = document.getElementById('csv');
    let file = fileInput.files[0];

    if (!file) {
        showNotice('error', "Error", "Tidak ada file yang diupload.", null);
        return;
    }

    let fileName = file.name;
    let fileExtension = fileName.split('.').pop().toLowerCase();

    if (fileExtension !== 'csv') {
        showNotice('error', "File Error", "File yang diupload harus berformat .csv.", null);
    } else {
        showNotice('success', "Upload Berhasil", "File berhasil diupload.", null);
    }
}
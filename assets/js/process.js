function doUpload() {
    let fileInput = document.getElementById('csv');
    let file = fileInput.files[0];

    if (!file) {
        showMsg('error', "Error", "Tidak ada file yang diupload.", null);
        return;
    }

    let fileName = file.name;
    let fileExtension = fileName.split('.').pop().toLowerCase();

    if (fileExtension !== 'csv') {
        showMsg('error', "File Error", "File yang diupload harus berformat .csv.", null);
        return;
    }

    readCsv()
        .then((data) => {
            let result = data[0][0].split(';');
            let elem = document.getElementById('process');
            appendOptions(elem, result, null);
            document.getElementById('process-csv').style.display = 'block';
        })
        .catch((error) => {
            showMsg('error', "Error", error, null);
        });
}

function extScrape(type) {
    alert(type);
}

function doProcess() {
    alert("Proses");
}

function doSearch() {
    alert("Search");
}
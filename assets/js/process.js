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

    readCsv().then((data) => {
        let result = data[0];
        let elem = document.getElementById('process');
        appendOptions(elem, result, null);
        document.getElementById('process-data').style.display = 'block';
    }).catch((error) => {
        showMsg('error', "Error", error, null);
    });
}

function externalScrape(type) {
    document.getElementById('csv-upload').style.display = 'none';
    document.getElementById('process-data').style.display = 'none';
    document.getElementById('search-keyword').style.display = 'block';
    alert(type);
}

function doProcessUpload() {
    let id = $('#process').val();
    let tbl1 = $('#table1').DataTable({
        "destroy": true,
        "scrollX": true,
        "responsive": false,
        "autoWidth": false,
        "paging": true,
        "searching": false
    });
    let tbl2 = $('#table2').DataTable({
        "destroy": true,
        "scrollX": true,
        "responsive": false,
        "autoWidth": false,
        "paging": true,
        "searching": false
    });

    tbl1.clear().draw();
    tbl2.clear().draw();
    readCsv().then((data) => {
        for (let x = 0; x < data.length; x++) {
            if (x > 0) {
                let response = getValueFromIndex(data[x], id);
                if (response == null) {
                    showMsg('error', "Error", "Tidak Ditemukan Data pada Index ke. " + id, null);
                    return;
                }

                tbl1.row.add([response]);
                tbl2.row.add([response]);
            }
        }

        tbl1.columns.adjust().draw();
        tbl2.columns.adjust().draw();
        document.getElementById('preprocess').style.display = 'block';
    }).catch((error) => {
        showMsg('error', "Error", error, null);
    });
}

function doSearch() {
    alert("Search");
}

function doDownload() {
    alert("Download");
}

function doReset() {
    alert("Reset");
}

function doPrepro() {
    alert("Preprocess");
}
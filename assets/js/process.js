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
        removeOptionsValue();
        let result = data[0];
        let elem = document.getElementById('process');
        appendOptions(elem, result, null);
        document.getElementById('process-data').style.display = 'block';
    }).catch((error) => {
        showMsg('error', "Error", error, null);
    });
}

function removeOptionsValue() {
    $("#process option").remove();
}

function externalScrape(type) {
    removeOptionsValue();
    let options = [];
    switch (type) {
        case "facebook":
        case "instagram":
        case "twitter":
        case "tiktok":
            options.push("url");
            break;
        case "playstore":
        case "appstore":
            options.push("App Name");
            break;
        case "wikipedia":
        case "ieee":
        case "acm":
            options.push("Title");
            options.push("Abstract");
            break;
        case "scholar":
            options.push("Author");
            break;
        case "bookonline":
            options.push("Title");
            break;
        case "youtube":
        case "stackoverflow":
        case "springer":
        case "sciencedirect":
            options.push("Keyword");
            break;
        case "tokopedia":
        case "shopee":
        case "bukalapak":
            options.push("Produk");
            options.push("Toko");
            break;
        case "detik":
            options.push("Title");
            options.push("Topic");
            break;
        default:
            options = [];
            break;
    }

    let elem = document.getElementById('process');
    appendOptions(elem, options, null);

    $("#process-type").val(type);
    $("#search").val("");
    document.getElementById('csv-upload').style.display = 'none';
    document.getElementById('process-data').style.display = 'block';
    document.getElementById('search-keyword').style.display = 'block';
    document.getElementById('preprocess').style.display = 'none';
    document.getElementById('btn-upload').style.display = 'none';
    document.getElementById('btn-scrape').style.display = 'block';
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

function doProcessScrape() {
    let processType = $("#process-type").val();
    let keywordType = $("#process option:selected").text();
    let keyword = $("#search").val();

    if (keyword === "" || keyword == null) {
        showMsg('warning', "Peringatan", "Harap isi keyword", null);
        return;
    }

    let request = {};
    request["module"] = processType;
    request["type"] = keywordType;
    request["search"] = keyword;

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

    let response = get("/api/scrape", "POST", request);
    for (let obj of response.data) {
        tbl1.row.add([obj]);
        tbl2.row.add([obj]);
    }

    tbl1.columns.adjust().draw();
    tbl2.columns.adjust().draw();
    document.getElementById('preprocess').style.display = 'block';
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
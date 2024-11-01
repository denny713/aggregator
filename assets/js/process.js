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

function changeSearchLabel(type) {
    let label = document.getElementById('lbl-search');
    switch (type) {
        case "facebook":
            label.innerHTML = "Keyword dari Facebook";
            break;
        case "instagram":
            label.innerHTML = "Keyword dari Instagram";
            break;
        case "twitter":
            label.innerHTML = "Keyword dari X / Twitter";
            break;
        case "tiktok":
            label.innerHTML = "Keyword dari TikTok";
            break;
        case "playstore":
            label.innerHTML = "Keyword dari Play Store";
            break;
        case "appstore":
            label.innerHTML = "Keyword dari App Store";
            break;
        case "wikipedia":
            label.innerHTML = "Keyword dari Wikipedia";
            break;
        case "ieee":
            label.innerHTML = "Keyword dari IEEE";
            break;
        case "acm":
            label.innerHTML = "Keyword dari ACM";
            break;
        case "springer":
            label.innerHTML = "Keyword dari Springer";
            break;
        case "sciencedirect":
            label.innerHTML = "Keyword dari Science Direct";
            break;
        case "bookonline":
            label.innerHTML = "Keyword dari Book Online (Goodreads)";
            break;
        case "scholar":
            label.innerHTML = "Keyword dari Google Scholar";
            break;
        case "youtube":
            label.innerHTML = "Keyword dari Youtube";
            break;
        case "stackoverflow":
            label.innerHTML = "Keyword dari Stack Overflow";
            break;
        case "tokopedia":
            label.innerHTML = "Keyword dari Tokopedia";
            break;
        case "shopee":
            label.innerHTML = "Keyword dari Shopee";
            break;
        case "bukalapak":
            label.innerHTML = "Keyword dari Bukalapak";
            break;
        case "detik":
            label.innerHTML = "Keyword dari Detik.com";
            break;
        default:
            label.innerHTML = "Keyword";
            break;
    }
}

function externalScrape(type) {
    removeOptionsValue();
    changeSearchLabel(type);
    let options = [];
    switch (type) {
        case "facebook":
        case "twitter":
        case "tiktok":
            options.push("URL");
            break;
        case "youtube":
        case "instagram":
            options.push("Keyword");
            break;
        case "playstore":
        case "appstore":
            options.push("App Name");
            break;
        case "wikipedia":
        case "ieee":
        case "acm":
        case "springer":
        case "sciencedirect":
        case "bookonline":
        case "scholar":
            options.push("Title");
            options.push("Abstract");
            break;
        case "tokopedia":
        case "shopee":
        case "bukalapak":
            options.push("Toko")
            options.push("Produk");
            break;
        case "detik":
            options.push("Title");
            options.push("Topic");
            break;
        case "stackoverflow":
            options.push("Topic");
            options.push("Question");
            options.push("Answer");
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
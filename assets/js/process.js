function doUpload() {
    let fileInput = document.getElementById('file-upload');
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
        case "playstore-ind":
            label.innerHTML = "Keyword dari Play Store Indonesian Version";
            break;
        case "appstore-ind":
            label.innerHTML = "Keyword dari App Store Indonesian Version";
            break;
        case "playstore-int":
            label.innerHTML = "Keyword dari Play Store International Version";
            break;
        case "appstore-int":
            label.innerHTML = "Keyword dari App Store International Version";
            break;
        case "wikipedia-eng":
            label.innerHTML = "Keyword dari Wikipedia English Version";
            break;
        case "wikipedia-ind":
            label.innerHTML = "Keyword dari Wikipedia Indonesian Version";
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
        case "wikipedia-ind":
        case "wikipedia-eng":
            options.push("Title");
            options.push("Content");
            break;
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
            options.push("Resume");
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
    $("#size").val("");
    document.getElementById('csv-upload').style.display = 'none';
    document.getElementById('process-data').style.display = 'block';
    document.getElementById('search-keyword').style.display = 'block';
    document.getElementById('preprocess').style.display = 'none';
    document.getElementById('btn-upload').style.display = 'none';
    document.getElementById('btn-scrape').style.display = 'block';
}

function doProcessUpload() {
    let id = $('#process').val();
    let dataList = [];

    showLoading();
    readCsv().then((data) => {
        for (let x = 0; x < data.length; x++) {
            if (x > 0) {
                let response = getValueFromIndex(data[x], id);
                if (response == null) {
                    showMsg('error', "Error", "Tidak Ditemukan Data pada Index ke. " + id, null);
                    return;
                }

                let resData = {};
                resData["user"] = "-";
                resData["timestamp"] = "-";
                resData["rating"] = "-";
                resData["content"] = response;
                dataList.push(resData);
            }
        }

        localStorage.setItem('scrape-data', JSON.stringify(dataList));
        $('#example').DataTable({
            "destroy": true,
            "serverSide": false,
            "processing": false,
            "responsive": true,
            "data": dataList,
            "columns": [
                {"data": "user"},
                {"data": "timestamp"},
                {"data": "rating"},
                {"data": "content"},
                {"data": "content"}
            ],
            "pageLength": 10,
            "paging": true,
            "searching": false,
            "ordering": true,
            "info": true,
            "autoWidth": false
        });

        document.getElementById('preprocess').style.display = 'block';
        hideLoading();
    }).catch((error) => {
        hideLoading();
        showMsg('error', "Error", error, null);
    });
}

function doProcessScrape() {
    localStorage.removeItem('scrape-data');

    let processType = $("#process-type").val();
    let keywordType = $("#process option:selected").text();
    let keyword = $("#search").val();
    let size = $("#size").val();
    if (size === "" || size == null) {
        size = "";
    }

    if (keyword === "" || keyword == null) {
        showMsg('warning', "Peringatan", "Harap isi keyword", null);
        return;
    }

    showLoading();
    $('#example').DataTable({
        "destroy": true,
        "serverSide": false,
        "processing": false,
        "responsive": true,
        "ajax": {
            "url": "/api/scrape",
            "type": "POST",
            "contentType": "application/json",
            "data": function (d) {
                return JSON.stringify({
                    "draw": d.draw,
                    "module": processType,
                    "type": keywordType,
                    "search": keyword,
                    "page": Math.ceil(d.start / d.length),
                    "size": size,
                    "sort": "ASC"
                });
            },
            "dataSrc": function (json) {
                localStorage.setItem("scrape-data", JSON.stringify(json.data));

                hideLoading();
                return json.data;
            }
        },
        "columns": [
            {"data": "user"},
            {"data": "timestamp"},
            {"data": "rating"},
            {"data": "content"},
            {"data": "content"}
        ],
        "pageLength": 10,
        "paging": true,
        "searching": false,
        "ordering": true,
        "info": true,
        "autoWidth": false
    });

    document.getElementById('preprocess').style.display = 'block';
}

function doDownload() {
    // get("/api/download", "POST", null);

    $.ajax({
        url: '/api/download',
        type: 'POST',
        xhrFields: {
            responseType: 'blob'
        },
        success: function (response) {
            let url = window.URL.createObjectURL(response);
            let a = document.createElement('a');
            a.href = url;
            a.download = 'data_series.csv';
            document.body.appendChild(a);
            a.click();
            a.remove();

            showMsg('success', "Sukses", "Download berhasil!");
        },
        error: function (jqXHR, textStatus, errorThrown) {
            showMsg('error', "Error", "Download gagal: " + textStatus);
        }
    });
}

function cancelProcessing() {
    localStorage.clear();
    window.location.reload();
    hideLoading();
}
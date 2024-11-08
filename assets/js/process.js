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
    removeCookie("scrape-data");
    removeCookie("process-data");

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
    let dataList = [];
    readCsv().then((data) => {
        for (let x = 0; x < data.length; x++) {
            if (x > 0) {
                let response = getValueFromIndex(data[x], id);
                if (response == null) {
                    showMsg('error', "Error", "Tidak Ditemukan Data pada Index ke. " + id, null);
                    return;
                }

                dataList.push(response);
                tbl1.row.add([response]);
                tbl2.row.add([response]);
            }
        }

        tbl1.columns.adjust().draw();
        tbl2.columns.adjust().draw();

        setCookie("scrape-data", dataList);
        setCookie("process-data", dataList);
        document.getElementById('preprocess').style.display = 'block';
    }).catch((error) => {
        showMsg('error', "Error", error, null);
    });
}

function doProcessScrape() {
    removeCookie("scrape-data");
    removeCookie("process-data");

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

    let request = {};
    request["module"] = processType;
    request["type"] = keywordType;
    request["search"] = keyword;
    request["size"] = size;

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

    setCookie("scrape-data", response.data);
    setCookie("process-data", response.data);
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

function doReset() {
    document.getElementById("remove_username").checked = false;
    document.getElementById("remove_rt").checked = false;
    document.getElementById("remove_hashtag").checked = false;
    document.getElementById("remove_url").checked = false;
    document.getElementById("remove_punctuation").checked = false;
    document.getElementById("remove_symbol").checked = false;
    document.getElementById("remove_number").checked = false;
    document.getElementById("remove_duplicate").checked = false;
    document.getElementById("replace_slang").checked = false;
    document.getElementById("replace_abbreviation").checked = false;
    document.getElementById("replace_elochar").checked = false;
    document.getElementById("lower_case").checked = false;
    document.getElementById("remove_stopword").checked = false;
    document.getElementById("stemming").checked = false;
    document.getElementById("join_case").checked = false;
    document.getElementById("tokenizing").checked = false;
}

function doPrepro() {
    removeCookie("process-data");
    let listProcess = [];

    if (document.getElementById("remove_username").checked === true) {
        listProcess.push(document.getElementById("remove_username").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_username").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("remove_rt").checked === true) {
        listProcess.push(document.getElementById("remove_rt").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_rt").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("remove_hashtag").checked === true) {
        listProcess.push(document.getElementById("remove_hashtag").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_hashtag").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("remove_url").checked === true) {
        listProcess.push(document.getElementById("remove_url").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_url").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("remove_punctuation").checked === true) {
        listProcess.push(document.getElementById("remove_punctuation").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_punctuation").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("remove_symbol").checked === true) {
        listProcess.push(document.getElementById("remove_symbol").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_symbol").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("remove_number").checked === true) {
        listProcess.push(document.getElementById("remove_number").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_number").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("remove_duplicate").checked === true) {
        listProcess.push(document.getElementById("remove_duplicate").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_duplicate").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("replace_slang").checked === true) {
        listProcess.push(document.getElementById("replace_slang").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("replace_slang").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("replace_abbreviation").checked === true) {
        listProcess.push(document.getElementById("replace_abbreviation").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("replace_abbreviation").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("replace_elochar").checked === true) {
        listProcess.push(document.getElementById("replace_elochar").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("replace_elochar").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("lower_case").checked === true) {
        listProcess.push(document.getElementById("lower_case").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("lower_case").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("remove_stopword").checked === true) {
        listProcess.push(document.getElementById("remove_stopword").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("remove_stopword").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("stemming").checked === true) {
        listProcess.push(document.getElementById("stemming").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("stemming").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("join_case").checked === true) {
        listProcess.push(document.getElementById("join_case").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("join_case").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    if (document.getElementById("tokenizing").checked === true) {
        listProcess.push(document.getElementById("tokenizing").value);
    } else {
        let index = listProcess.indexOf(document.getElementById("tokenizing").value);
        if (index !== -1) {
            listProcess.splice(index, 1);
        }
    }

    let req = {};
    req["process"] = listProcess;

    let response = get("/api/preprocessing", "POST", req);
    let tbl2 = $('#table2').DataTable({
        "destroy": true,
        "scrollX": true,
        "responsive": false,
        "autoWidth": false,
        "paging": true,
        "searching": false
    });

    tbl2.clear().draw();
    for (let obj of response.data) {
        tbl2.row.add([obj]);
    }

    setCookie("scrape-data", response.data);
    tbl2.columns.adjust().draw();
}
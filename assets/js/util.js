function showMsg(type, title, message, callback) {
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

function getValueFromIndex(data, index) {
    if (index > 0 && index <= data.length) {
        return data[index - 1];
    } else {
        return null;
    }
}

function appendOptions(select, data, param) {
    select.innerHTML = "";
    data.forEach((value, index) => {
        let option = document.createElement("option");
        option.value = index + 1;
        option.innerHTML = value;
        if (param && (param === value)) {
            option.setAttribute("selected", "selected");
        }
        select.appendChild(option);
    });
}

function readCsv() {
    return new Promise((resolve, reject) => {
        let fileInput = document.getElementById('file-upload');
        let file = fileInput.files[0];

        if (!file) {
            reject("Tidak ada file yang dipilih.");
            return;
        }

        let reader = new FileReader();

        reader.onload = function (event) {
            let csvData = event.target.result;
            resolve(processCsv(csvData, ";"));
        };

        reader.onerror = function (event) {
            reject("Error membaca file: " + event.target.error.message);
        };

        reader.readAsText(file);
    });
}

function readCsvFromFile(path, delimiter) {
    return fetch(path)
        .then(response => {
            if (!response.ok) {
                throw new Error("Gagal membaca file CSV.");
            }
            return response.text();
        })
        .then(csvData => processCsv(csvData, delimiter))
        .catch(error => {
            console.error("Terjadi kesalahan:", error);
            return [];
        });
}

function processCsv(csvData, delimiter) {
    let rows = csvData.split("\n");
    let result = [];

    for (const element of rows) {
        let row = element.split(delimiter);
        result.push(row);
    }

    return result;
}

function toggleSidebar() {
    let sidebar = document.getElementById('sidebar-container');
    let menuIcon = document.getElementById('menu-icon');

    if (sidebar.classList.contains('show')) {
        sidebar.classList.remove('show');
        sidebar.classList.add('d-none');
        menuIcon.classList.remove('fa-times');
        menuIcon.classList.add('fa-bars');
    } else {
        sidebar.classList.remove('d-none');
        sidebar.classList.add('show');
        menuIcon.classList.remove('fa-bars');
        menuIcon.classList.add('fa-times');
    }
}

function setCookie(name, value) {
    const date = new Date();
    date.setTime(date.getTime() + (24 * 60 * 60 * 1000));
    let expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + JSON.stringify(value) + ";" + expires + ";path=/";
}

function removeCookie(name) {
    document.cookie = name + '=;Max-Age=0;path=/';
}

function showLoading() {
    $("#loading").modal("show");
}

function hideLoading() {
    $("#loading").modal("hide");
}
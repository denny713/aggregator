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

function get(url, type, request) {
    let data = {};

    $.ajax({
        url: url,
        type: type,
        async: false,
        dataType: 'json',
        data: JSON.stringify(request),
        contentType: 'application/json; charset=utf-8',
        cache: false,
        timeout: 600000,
        beforeSend: function () {
            showLoading();
        }
    }).done(function (response) {
        hideLoading();
        data = response;
    }).fail(function (jqXHR, textStatus, errorThrown) {
        hideLoading();
        try {
            let response = JSON.parse(jqXHR.responseText);
            if (response.data && response.data.error) {
                let errorMessage = response.data.error;
                showNotice('error', "Error", errorMessage);
            } else {
                showNotice('error', "Error", textStatus + " : " + errorThrown);
            }
        } catch (e) {
            showNotice('error', "Error", textStatus + " : " + errorThrown);
        }
        data = null;
    });

    return data;
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
        let fileInput = document.getElementById('csv');
        let file = fileInput.files[0];

        if (!file) {
            reject("Tidak ada file yang dipilih.");
            return;
        }

        let reader = new FileReader();

        reader.onload = function (event) {
            let csvData = event.target.result;
            resolve(processCsv(csvData));
        };

        reader.onerror = function (event) {
            reject("Error membaca file: " + event.target.error.message);
        };

        reader.readAsText(file);
    });
}

function processCsv(csvData) {
    let rows = csvData.split("\n");
    let result = [];

    for (const element of rows) {
        let row = element.split(";");
        result.push(row);
    }

    return result;
}

function hideLoading() {
    $("#loading").modal("hide");
}

function showLoading() {
    $("#loading").modal("show");
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

function adjustSidebar() {
    let sidebarContainer = document.getElementById('sidebar-container');
    let hamburgerIcon = document.getElementById('hamburger-icon');
    let sidebarItem = document.getElementById("sidebar-item");
    let menuIcon = document.getElementById('menu-icon');
    menuIcon.classList.remove('fa-times');
    menuIcon.classList.add('fa-bars');

    if (window.innerWidth >= 1850) {
        sidebarContainer.classList.add('show');
        sidebarContainer.classList.remove('d-none');
        hamburgerIcon.style.display = 'none';
        sidebarItem.style.top = '75px';
    } else {
        sidebarContainer.classList.remove('show');
        sidebarContainer.classList.add('d-none');
        hamburgerIcon.style.display = 'block';
        sidebarItem.style.top = '0px';
    }
}
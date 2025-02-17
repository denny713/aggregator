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


}

function removeUserHandless(text) {
    return text.replace(/@\w+/g, '');
}

function removeRetweet(text) {
    return text.replace(/@\w+/g, "");
}

function removeHashtag(text) {
    return text.replace(/#\w+/g, "");
}

function removeUrl(text) {
    return text.replace(/https?:\/\/\S+/g, "");
}

function removePunctuation(text) {
    return text.replace(/[.,;:!?'"(){}\[\]\/\\`_]/g, "");
}

function removeSymbol(text) {
    return text.replace(/[^\w\s.,;:?!'"()\[\]/`_]/g, '');
}

function removeNumber(text) {
    return text.replace(/\d+/g, "");
}

function removeDuplicate(text) {

}

function replaceSlang(text) {

}

function replaceAbbreviation(text) {

}

function replaceEloChar(text) {

}

function lowerCase(text) {
    return text.toLowerCase();
}

function removeStopword(text) {

}

function stemming(text) {

}

function joinCase(text) {

}

function tokenizing(text) {
    return text.split(/\s+/);
}
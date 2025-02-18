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
    let listData = JSON.parse(localStorage.getItem("scrape-data"));
    const operations = [
        {id: "remove_username", func: removeUsername},
        {id: "remove_rt", func: removeRetweet},
        {id: "remove_hashtag", func: removeHashtag},
        {id: "remove_url", func: removeUrl},
        {id: "remove_punctuation", func: removePunctuation},
        {id: "remove_symbol", func: removeSymbol},
        {id: "remove_number", func: removeNumber},
        {id: "remove_duplicate", func: removeDuplicate},
        {id: "replace_slang", func: replaceSlang},
        {id: "replace_abbreviation", func: replaceAbbreviation},
        {id: "replace_elochar", func: replaceEloChar},
        {id: "lower_case", func: lowerCase},
        {id: "remove_stopword", func: removeStopword},
        {id: "stemming", func: stemming},
        {id: "join_case", func: joinCase},
        {id: "tokenizing", func: tokenizing}
    ];

    for (let data of listData) {
        let preview = data.preview;
        for (let operation of operations) {
            if (document.getElementById(operation.id).checked) {
                preview = operation.func(preview);
            }
        }

        data["preview"] = preview;
    }

    setDataToTable(listData);
}

function removeUsername(text) {
    return text.replace(/@\w+/g, '');
}

function removeRetweet(text) {
    return text.replace(/^RT\s+/, '');
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

function removeDuplicate(reqData) {
    return reqData.filter((value, index, self) =>
            index === self.findIndex((t) => (
                t.user === value.user &&
                t.timestamp === value.timestamp &&
                t.rating === value.rating &&
                t.content === value.content &&
                t.preview === value.preview
            ))
    );
}

function replaceSlang(text) {
    return readCsvFromFile('/assets/csv/slang_dataset.csv', ';')
        .then(slangDict => {
            let words = text.split(' ');
            let replacedWords = words.map(word => slangDict[word] || word);
            return replacedWords.join(' ');
        });
}

function replaceAbbreviation(text) {
    return readCsvFromFile('/assets/csv/abbre_dataset.csv', ' = ')
        .then(slangDict => {
            let words = text.split(' ');
            let replacedWords = words.map(word => slangDict[word] || word);
            return replacedWords.join(' ');
        });
}

function replaceEloChar(text) {
    return readCsvFromFile(csvPath, '\n')
        .then(csvData => {
            let elocharDict = processElocharCsv(csvData);
            let words = text.split(' ');
            let processedWords = [];

            words.forEach(word => {
                let lowerWord = word.toLowerCase();
                let found = false;

                for (let key in elocharDict) {
                    if (key && lowerWord.includes(key)) {
                        found = true;
                        break;
                    }
                }

                if (found) {
                    processedWords.push(word);
                } else {
                    let pattern = /(\w)\1+/g;
                    let replacedWord = word.replace(pattern, '$1');
                    processedWords.push(replacedWord);
                }
            });

            return processedWords.join(' ');
        });
}

function lowerCase(text) {
    return text.toLowerCase();
}

function removeStopword(text) {
    const stopWords = new Set([
        "dan", "atau", "adalah", "yang", "di", "ke", "dari", "untuk", "pada", "dengan",
        "ini", "itu", "sebuah", "sebagai", "jika", "saya", "kamu", "dia", "mereka",
        "kami", "kita", "itu", "sangat", "sudah", "belum", "akan", "tidak", "ya",
        "tidak", "apa", "apa", "yang", "itu", "semua", "bisa", "boleh", "harus",
        "seperti", "lebih", "dari", "sama", "saja", "satu", "dua", "tiga", "empat",
        "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh"
    ]);

    if (Array.isArray(text)) {
        return text.filter(word => !stopWords.has(word.toLowerCase()));
    } else {
        let words = text.split(' ');
        let filteredWords = words.filter(word => !stopWords.has(word.toLowerCase()));
        return filteredWords.join(' ');
    }
}

function stemming(text) {
    let stemmer = StemmerFactory.createStemmer();
    return stemmer.stem(text);
}

function joinCase(text) {
    if (Array.isArray(text)) {
        text = text.join('');
        text = [text];
    } else {
        text = text.replace(/ /g, '');
    }
    return text;
}

function tokenizing(text) {
    let doc = nlp(text);
    return doc.terms().out('array');
}

function processElocharCsv(csvData) {
    const elocharList = csvData.split('\n').map(line => line.trim()).filter(line => line);
    const elocharDict = {};

    elocharList.forEach(word => {
        elocharDict[word.toLowerCase()] = null;
    });

    return elocharDict;
}
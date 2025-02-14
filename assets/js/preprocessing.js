function loadSlangDictionary(callback) {
    const slangDict = {};
    fs.createReadStream("assets/csv/slang_dataset.csv")
        .pipe(csv({separator: ";"}))
        .on("data", (row) => {
            slangDict[row.slang] = row.replacement;
        })
        .on("end", () => {
            callback(slangDict);
        });
}

function loadAbbreviationDictionary(callback) {
    const abbreDict = {};
    fs.createReadStream("assets/csv/abbre_dataset.csv")
        .pipe(csv({separator: "="}))
        .on("data", (row) => {
            abbreDict[row.abbre] = row.replacement;
        })
        .on("end", () => {
            callback(abbreDict);
        });
}
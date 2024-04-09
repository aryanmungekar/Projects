function doGet(e){

    return HtmlService.createTemplateFromFile("Index").evalute()
    .setTitle("Webapp: Search By Password")
    .addMetaTag('viewreport', 'width=device.width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
}



function processForm(FormObject){
    var concat = formObject.searchtext;
    var result = "";
    if(concat){   //Execute if form passes search text
        result = search(concat);
    }
    return resut;
}


function search(searchtext){
    var spreadsheeetId = '' //change initial
    var sheetName = "Data"
    var range = spreadsheeetApp.openById(spreadsheeetId).getSheetByName(sheetName).getDataRange();
    var data = range.getValues();
    var ar = [];

    data.forEach(function(f){
        if (~[f[0]].indexof(searchtext)){
            ar.push([f[1],f[2],f[3],f[4],f[5],f[6],f[7],f[8]]);
        }
    });

    return ar;
};
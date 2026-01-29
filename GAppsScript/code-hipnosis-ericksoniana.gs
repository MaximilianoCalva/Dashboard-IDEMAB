/**
 * UNIVERSAL SHEET TO JSON API (IDEMAB HIPNOSIS ERICKSONIANA)
 * 
 * Returns data for ALL sheets in the format: 
 * { 
 *   "Aula TV M1": [ ... ],
 *   "Material M1": [ ... ]
 * }
 */
function doGet(e) {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheets = ss.getSheets();
    var result = {};

    sheets.forEach(function (sheet) {
        var sheetName = sheet.getName();
        var range = sheet.getDataRange();
        var values = range.getValues();
        
        // Need at least header + 1 row
        if (values.length < 2) return;
        
        var sheetData = [];
        
        // Start at row 1 (skipping header at 0)
        for (var i = 1; i < values.length; i++) {
            var row = values[i];
            
            // MAPEO SEGÚN COLUMNAS ESTÁNDAR IDEMAB
            // A=N°, B=Titulo, C=Descripción, D=Formato, E=Link, F=Status
            var numero = row[0];
            var titulo = row[1];
            var descripcion = row[2];
            var formato = row[3];
            var link = row[4];
            var status = row[5];
            
            // Validación básica: Titulo debe existir
            if (titulo && titulo.toString().trim() !== '') {
                sheetData.push({
                    numero: numero,
                    titulo: titulo.toString().trim(),
                    descripcion: descripcion ? descripcion.toString().trim() : "",
                    formato: formato ? formato.toString().trim() : "",
                    link: link ? link.toString().trim() : "",
                    status: status ? status.toString().trim() : "Activo"
                });
            }
        }
        
        // Only add sheet to result if it has data
        if (sheetData.length > 0) {
            result[sheetName] = sheetData;
        }
    });

    // Return simple JSON object (Dictionary)
    return ContentService.createTextOutput(JSON.stringify(result))
        .setMimeType(ContentService.MimeType.JSON);
}

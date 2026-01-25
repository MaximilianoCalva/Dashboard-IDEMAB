/**
 * ==========================================
 * SCRIPT UNIVERSAL PARA GOOGLE SHEETS TO JSON
 * ==========================================
 * 
 * INSTRUCCIONES:
 * 1. Ve a tu Google Sheet > Extensiones > Apps Script.
 * 2. Borra todo el código que haya y pega este código completo.
 * 3. Arriba a la derecha, clic en "Implementar" > "Nueva implementación".
 * 4. Tipo: "Aplicación web".
 * 5. Descripción: "API v1".
 * 6. Ejecutar como: "Yo" (Tu correo).
 * 7. Quién tiene acceso: "Cualquier usuario" (IMPORTANTE).
 * 8. Clic en "Implementar".
 * 9. Copia la "URL de la aplicación web" (termina en /exec).
 * 10. Pega esa URL en tu archivo HTML (snippet-mapa-contenidos.html).
 */

function doGet(e) {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheets = ss.getSheets();
    var result = {};

    // Iterar por cada pestaña del archivo
    sheets.forEach(function (sheet) {
        var sheetName = sheet.getName();

        // Ignorar pestañas ocultas o de sistema si quisieras (Opcional)
        // if (sheet.isSheetHidden()) return;

        var range = sheet.getDataRange();
        var values = range.getValues();

        // Si la pestaña está vacía, saltar
        if (values.length === 0) return;

        var headers = values[0]; // Primera fila son los encabezados
        var sheetData = [];

        // Iterar desde la fila 2 hasta el final
        for (var i = 1; i < values.length; i++) {
            var row = values[i];
            var rowObject = {};
            var hasData = false;

            for (var j = 0; j < headers.length; j++) {
                var key = headers[j].toString().trim();
                var value = row[j];

                // Solo agregar si hay header
                if (key) {
                    // Si es fecha, convertir a String legible
                    if (Object.prototype.toString.call(value) === '[object Date]') {
                        try {
                            value = Utilities.formatDate(value, ss.getSpreadsheetTimeZone(), "dd/MM/yyyy");
                        } catch (e) { }
                    }
                    rowObject[key] = value;

                    if (value && value.toString().trim() !== "") {
                        hasData = true;
                    }
                }
            }

            // Solo agregar filas que no estén completamente vacías
            if (hasData) {
                sheetData.push(rowObject);
            }
        }

        result[sheetName] = sheetData;
    });

    // Devolver JSON purificado
    return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        generated_at: new Date(),
        data: result
    })).setMimeType(ContentService.MimeType.JSON);
}

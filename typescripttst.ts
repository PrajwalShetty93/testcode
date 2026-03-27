function main(workbook: ExcelScript.Workbook) {
    let sheet = workbook.getActiveWorksheet();
    let usedRange = sheet.getUsedRange();
    let totalRowCount = usedRange.getRowCount();
    let processedRowCount = 0;
    let batchSize=500

    while(processedRowCount<rowCount)
    {
        let colCount = usedRange.getColumnCount();
    
        let headers = usedRange.getRow(0).getValues()[0] as string[];
        let allValues = usedRange.getValues() as string[][];

        let allValues =  usedRange.getCell(1, 0).getResizedRange(dataRows - 1, colCount - 1).getValues() as string[][];

        processedRowCount=processedRowCount+batchSize
    }




 
    // Remove columns: Member SKU ID and AD SKU ID
    const columnsToRemove = ["Member SKU ID", "AD SKU ID"];
    columnsToRemove.forEach(colName => {
        let colIdx = headers.indexOf(colName);
        if (colIdx !== -1) {
            headers.splice(colIdx, 1);
            for (let row = 0; row < rowCount; row++) {
                allValues[row].splice(colIdx, 1);
            }
            console.log(`Removed column: ${colName}`);
        } else {
            console.log(`Column not found: ${colName}`);
        }
    });
 
    // Add new columns at the beginning: Product Template, Product_Badge, Track_Inventory
    headers.unshift("Track_Inventory");
    headers.unshift("Product_Badge");
    headers.unshift("Product Template");
 
    for (let row = 0; row < rowCount; row++) {
        if (row === 0) {
            allValues[row].unshift("Track_Inventory");
            allValues[row].unshift("Product_Badge");
            allValues[row].unshift("Product Template");
        } else {
            allValues[row].unshift("");
            allValues[row].unshift("");
            allValues[row].unshift("Final Product Template");
        }
    }
    console.log("Added columns at beginning: Product Template, Product_Badge, Track_Inventory");
 
    // Method for Concatenating Package values columns with their UOM columns
    function concatColumns(mainColName: string, uomColName: string) {
        let mainIdx = headers.indexOf(mainColName);
        let uomIdx = headers.indexOf(uomColName);
        if (mainIdx === -1 || uomIdx === -1) {
            console.log(`Columns not found: ${mainColName} or ${uomColName}`);
            return;
        }
        for (let row = 1; row < rowCount; row++) {
            allValues[row][mainIdx] = `${allValues[row][mainIdx] || ""} ${allValues[row][uomIdx] || ""}`.trim();
        }
        for (let row = 0; row < rowCount; row++) {
            allValues[row].splice(uomIdx, 1);
        }
        headers.splice(uomIdx, 1);
    }
 
    // Duplicating Package_Weight into a new column Shipping_Weight and inserting it after Package_Weight_UOM
    let pkgWeightIdx = headers.indexOf("Package_Weight");
    let pkgWeightUomIdx = headers.indexOf("Package_Weight_UOM");
    if (pkgWeightIdx !== -1 && pkgWeightUomIdx !== -1) {
        headers.splice(pkgWeightUomIdx + 1, 0, "Shipping_Weight");
        for (let row = 1; row < rowCount; row++) {
            allValues[row].splice(pkgWeightUomIdx + 1, 0, allValues[row][pkgWeightIdx]?.toString().trim() || "");
        }
        allValues[0].splice(pkgWeightUomIdx + 1, 0, "Shipping_Weight");
        console.log("Shipping_Weight column created");
    } else {
        console.log("Package_Weight or Package_Weight_UOM not found");
    }
 
    // Concatenating all Package values with their UOMs
    const dimensionPairs = [
        ["Package_Weight", "Package_Weight_UOM"],
        ["Package_Width", "Package_Width_UOM"],
        ["Package_Height", "Package_Height_UOM"],
        ["Package_Length", "Package_Length_UOM"]
    ];
    for (let [mainCol, uomCol] of dimensionPairs) {
        concatColumns(mainCol, uomCol);
    }
    console.log("All Package values have been concatenated with their UOMs, and UOM columns have been removed.");
 
    // Updating Manufacturer_Item_Status: Active → False, Discontinued → True
    let statusColIdx = headers.indexOf("Manufacturer_Item_Status");
    if (statusColIdx !== -1) {
        for (let row = 1; row < rowCount; row++) {
            let cellVal = allValues[row][statusColIdx]?.toString().trim();
            if (cellVal === "Active") {
                allValues[row][statusColIdx] = "False";
            } else if (cellVal === "Discontinued") {
                allValues[row][statusColIdx] = "True";
            }
        }
        console.log("Manufacturer_Item_Status column transformed (Active to False, Discontinued to True)");
    } else {
        console.log("Manufacturer_Item_Status column not found");
    }
 
    sheet.getRangeByIndexes(0, 0, rowCount, allValues[0].length).setValues(allValues);
    console.log("Script completed successfully");
}
// Creating function for unique IDs for the grouped table
// var uniqueId = (function() {
//     var counter = 0;
//     return function() {
//         counter += 1;
//         return counter;
//     };   
// }());
$(document).ready(function(){
    // var groupingTable = null,
        // $rowSelect = $("#group-row"),
        // $colSelect = $("#group-col");
    // Getting json data and preparing it for table creation
    $.getJSON("/get_suggested_recipes/")
        .success(start)
        // Adding alert if server is not running
        .fail(function() {
            alert("Run your server silly.")
    });
    // Creating the report table and combo boxes
    function start(jsonData) {
        // Creating the table
        var $reportTableContainer = $("#table-container");
        var tableReadyData = prepare_table_data(jsonData);
        var $table = constructTable("   ", tableReadyData);
        $reportTableContainer.append($table);

        // $table.DataTable({
        //     "scrollY": "auto",
        //     "paging":   true,
        //     "searching": true,
        //     "ordering": true,
        //     "info":     true,
        //     "lengthMenu": [[10, 20, 30, 40, 50, -1], [10, 20, 30, 40, 50, "All"]]
        // });
        // console.log("ggwp")
    };


    function prepare_table_data(data) {
    table_data = [["Name", "Healthiness", "Prep-time", "Portions" ,"Image"]]
            $.each(data, function(index, value) {
                table_data_row = []
                 value.forEach(function(entry) {
                    table_data_row.push(entry)
                });
                 table_data.push(table_data_row)
            });
        return table_data
    };

    function constructTable(tableId, data) {
        // console.log("Im returned")
        var $tableElement = $("<table></table>"),
            $thead = $("<thead></thead>"),
            $theadRow = $("<tr></tr>"),
            $tbody = $("<tbody></tbody>");
            // tableId = "groupingTable" + uniqueId();

        $tableElement
            .attr("id", tableId)
            .attr("class", "table table-striped")

        $thead.append($theadRow);
        
        $tableElement.append($thead);
        $tableElement.append($tbody);
        // Creating headers
        headers = data[0]
        headers.forEach(function(header) {
            var $th = $("<th></th>");
            $th.text(header);
            $theadRow.append($th);

        });
        // Creating body
        body = data.slice(1, data.length)
        body.forEach(function(row) {
            $tr = $("<tr></tr>");
            $tbody.append($tr);
            row.forEach(function(item, index) {
                if(index === 4) {
                    $td = $("<td></td>");
                    $img = $("<img>", {src: item,
                                       width: 200});
                    $td.append($img);
                    $tr.append($td);    
                } else {
                    $td = $("<td></td>");
                    $td.text(item);
                    $tr.append($td);
                }
            });
        });
        return $tableElement;
    };
    //     // Creating combo boxes
    //     var $firstCombo = constructGroupingCombo("#group-col", tableReadyData[0]),
    //         $secondCombo = constructGroupingCombo("#group-row", tableReadyData[0])

    //     $firstCombo.on("change", function() {
    //         var rowValue = $secondCombo.val();
    //         var colValue = $firstCombo.val();
    //         triggerGroupingTableCreation(data, rowValue, colValue);
    //     });

    //     $secondCombo.on("change", function() {
    //         var rowValue = $secondCombo.val();
    //         var colValue = $firstCombo.val();
    //         triggerGroupingTableCreation(data, rowValue, colValue);
    //     });
    //     // Creating swap button for easier user experience with the table
    //     $("#swap").on("click", function() {
    //         var
    //             rowValue = $secondCombo.val(),
    //             colValue = $firstCombo.val(),
    //             swap = rowValue;

    //         rowValue = colValue;
    //         colValue = swap;

    //         $secondCombo.val(rowValue);
    //         $firstCombo.val(colValue);

    //         $secondCombo.trigger("change");
    //         $firstCombo.trigger("change");
    //     });
    // }
    // // Creating the grouped table when combo boxes are selected
    // function triggerGroupingTableCreation(data, rowValue, colValue) {
    //     if(rowValue == colValue) {
    //         alert("Choose different grouping options.");
    //         return
    //     }
    //     console.log(rowValue);
    //     console.log(colValue);
        
    //     var $groupingTableContainer = $("#grouped-container");
    //     var groupTableReadyData = createGroupingTableData(data, rowValue, colValue)
    //     var tableId = "grouping-table-" + uniqueId();

    //     var $table = constructTable(tableId, groupTableReadyData);

    //     $groupingTableContainer.html("");
    //     $groupingTableContainer.append($table);

    //     $table.DataTable({
    //         "paging":   true,
    //         "searching": false,
    //         "ordering": true,
    //         "info":     true,
    //     });
    // }   
    // // Creating the unique rows and columns for the grouped table
    // function getUniqueElementsForGroupingTable(data,row, col) {
    //     var uniqueRows = [];
    //     var uniqueCols = [];

    //     for (var i = 0; i < data.length; i++) {
    //         if (uniqueRows.indexOf(data[i][row]) === -1) {
    //             uniqueRows.push(data[i][row]);
    //         }
    //         if (uniqueCols.indexOf(data[i][col]) === -1) {
    //             uniqueCols.push(data[i][col]);
    //         }
    //     };
    //     uniqueRows.sort();
    //     uniqueCols.sort();

    //     return {
    //         "uniqueRows": uniqueRows,
    //         "uniqueCols": uniqueCols
    //     }
    // };
    // // Preparing the data for the grouped table
    // function createGroupingTableData(data, row, col) {
    //     // Getting the unique rows and columns
    //     var uniques = getUniqueElementsForGroupingTable(data, row, col);
    //     var secondTableData = {}
    //     // Counting the elements for the table
    //     for (var i = 0; i < uniques.uniqueCols.length; i++) {
    //         secondTableData[uniques.uniqueCols[i]] = {}
    //         for (var j = 0; j < uniques.uniqueRows.length; j++) {
    //             secondTableData[uniques.uniqueCols[i]][uniques.uniqueRows[j]] = 0;
    //         };
    //     };
    //     for (var n = 0; n < data.length; n++) {
    //         secondTableData[data[n][col]][data[n][row]] += 1;
    //     };
    //     // Preparing the data for the grouped table
    //     var groupingTableData = []
    //     groupingTableData.push([col + "/" + row].concat(uniques.uniqueRows));

    //     Object.keys(secondTableData).forEach(function(key) {
    //         values = Object.keys(secondTableData[key]).map(function(item) {
    //             return secondTableData[key][item];
    //         });

    //         groupingTableData.push([key].concat(values));
    //     });
    //     return groupingTableData
    // };
    // // Creating the combo bozes
    // function constructGroupingCombo(selector, comboItems) {
    //     var $combo = $(selector);

    //     comboItems.forEach(function(item) {
    //         var $option = $("<option></option>");
    //         $option.append(item);
    //         $combo.append($option);
    //     });
    //     return $combo;
    // }
    // Function for constructing either of the tables
    // // Preparing the data for the report table
    // function createFirstTableData(data) {
    //     firstTableData = [Object.keys(data[0])];
    //     data.forEach(function(item) {
    //         var firstTableRow = []
    //         Object.keys(item).forEach(function(key) {
    //             firstTableRow.push(item[key])
    //         });
    //         firstTableData.push(firstTableRow)
    //     });
    //     return firstTableData
    // };
});
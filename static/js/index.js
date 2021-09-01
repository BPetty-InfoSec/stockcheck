$(function() {
    console.log("Page ready");
    loadStocks();
    
    // Load JSON stocks file
    function loadStocks() {
        uriObj = $.getJSON("stocks.json", function(data) {
            populateTrackedStocks(data);
            $('.stockLink').click(function() {
                populateStockContent(data["Info"][this.text]);
            });
            $('.editstocksitem').click(function() {
                editStockList();
            });
            return data;
        });
    }

    // Populate Tracked Stocks list
    function populateTrackedStocks(data) {
        let checkNum = 0;
        for (let item in data["ToCheck"]) {
            $('.tracked_stocks').append($("<li class='stockitem'><a class='stockLink' href='javascript:void(0)'>" + item + "</li>"));
            if (checkNum == 0) {
                checkNum = 1;
                populateStockContent(data["Info"][item]);
            };
        }
        $('.tracked_stocks').append($("<li class='editstocksitem'><a class='editstocks' href='javascript: void (0)'>...Edit Stocks</a></li>"));
    }

    // Populate the details section for the selected stock
    // Initial pageload will load the first stock in the list
    function populateStockContent(stockObject) {

        // Format the header portion of the info section
        $('.subheader').text(stockObject["longName"] + " (" + stockObject["symbol"] + ")");
        $('.logo').attr('src',stockObject["logo_url"]);
        $('.stockWebsiteLink')
            .attr("href", stockObject["website"])
            .text(stockObject["website"]);
        
        // Add the long business description
        $('.stockDescription').text(stockObject["longBusinessSummary"]);
        
        // Fill out the Contact information for the business
        $('.addressName').text(stockObject["shortName"]);
        $('.addressStreet').text(stockObject["address1"]);
        $('.addressCityStateLine')
            .text(stockObject["city"] + ", " + stockObject["state"] + "  " + stockObject["zip"]);
        $('.addressCountry').text(stockObject["country"]);
        $('.stockPhone').text("Phone: " + stockObject["phone"]);

        // Information about the business finances
        $('.businessSector .infopart').text(stockObject["sector"]);
        $('.businessIndustry .infopart').text(stockObject["industry"]);
        $('.numEmployees .infopart')
            .text(Number(stockObject["fullTimeEmployees"]).toLocaleString("en-US"));
        $('.totalRevenue .infopart')
            .text(Number(stockObject["totalRevenue"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0}));
        $('.totalDebt .infopart')
            .text(Number(stockObject["totalDebt"])
                .toLocaleString('en-US', { style: 'currency', currency:'USD', minimumFractionDigits: 0}));
        $('.totalCash .infopart')
            .text(Number(stockObject["totalCash"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0}));
        $('.profitMargins .infopart')
            .text(parseFloat(stockObject["profitMargins"])
                .toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 3 }));
        $('.grossMargins .infopart')
            .text(parseFloat(stockObject["grossMargins"])
                .toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 3 }));
        $('.operatingMargins .infopart')
            .text(parseFloat(stockObject["operatingMargins"])
                .toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 3 }));
        $('.operatingCashflow .infopart')
            .text(Number(stockObject["operatingCashflow"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0 }));
        $('.revenueGrowth .infopart')
            .text(parseFloat(stockObject["revenueGrowth"])
                .toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 3 }));
        $('.debtToEquity .infopart')
            .text(parseFloat(stockObject["debtToEquity"])
                .toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 3 }));
        $('.lastFiscalYearEnd .infopart')
            .text(parseFloat(stockObject["lastFiscalYearEnd"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 0 }));

        // Information about Shares
        $('.52WeekChange .infopart')
            .text(parseFloat(stockObject["52WeekChange"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 8 }));
        $('.52WeekHigh .infopart')
            .text(parseFloat(stockObject["fiftyTwoWeekHigh"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 2 }));
        $('.52WeekLow .infopart')
            .text(parseFloat(stockObject["fiftyTwoWeekLow"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 2 }));
        $('.200DayAverage .infopart')
            .text(parseFloat(stockObject["twoHundredDayAverage"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 2 }));
        $('.averageVolume .infopart')
            .text(parseFloat(stockObject["averageVolume"]));
        $('.averageDailyVolume10Day .infopart')
            .text(parseFloat(stockObject["averageDailyVolume10Day"]));
        $('.dividendRate .infopart')
            .text(parseFloat(stockObject["dividendRate"])
                .toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 3 }));
        $('.dividendYield .infopart')
            .text(parseFloat(stockObject["dividendYield"])
                .toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 3 }));
        $('.5YearAvgDividendYield .infopart')
            .text(parseFloat(stockObject["fiveYearAvgDividendYield"])
                .toLocaleString('en-US', { style: 'percent', minimumFractionDigits: 3 }));
        $('.marketCap .infopart')
            .text(Number(stockObject["marketCap"])
                .toLocaleString('en-US'));
        $('.regularMarketPrice .infopart')
            .text(parseFloat(stockObject["regularMarketPrice"])
                .toLocaleString('en-US', { style: 'currency', currency: 'USD', minimumFractionDigits: 2 }));
    };

    // Change Tracked Stocks links to show Remove, and edit to Add.
    // Also add "Cancel Editing link"
    function editStockList() {
        let editElement = "<li class='editstocksitem'> <a class='editstocks' href='javascript: void (0)'>...Edit Stocks</a></li>";
        let addElement = "<li class='addstock'> <a class='editstocks' href='javascript: void (0)'>... + Add Stock</a></li>";
        $('.tracked_stocks li').each(function (index){
            console.log($(this).text());
            let replaceText = "( " + $(this).text() + " ) --Remove";
            if ($(this).attr('class') == 'editstocksitem') {
                $(this).replaceWith(addElement);
                $('.tracked_stocks').append($("<li class='canceledit'><a href='javascript:void (0)'>... Stop Editing</a></li>"));
            } else {
                $(this).replaceWith("<li class='stockitem'><a class='stockLink' href='javascript:void(0)'>" + replaceText + "</li>");
            }
        });
        $('.canceledit').click(function() {
            cancelEditingStockList();
        });
    };

    // Stop editing Stock List
    function cancelEditingStockList() {
        $('.tracked_stocks li').each(function(index) {
            $(this).remove();
        });
        loadStocks();
    }
});
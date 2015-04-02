
//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
$(function() {
    $(window).bind("load resize", function() {
        topOffset = 50;
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    var element = $('ul.nav a').filter(function() {
        return this.href == url || url.href.indexOf(this.href) == 0;
    }).addClass('active').parent().parent().addClass('in').parent();
    if (element.is('li')) {
        element.addClass('active');
    }

    // flot charts
    
    var priceContainer = $("#price-chart");
    var depthContainer = $("#depth-chart");
    var maximum = priceContainer.outerWidth() / 2 || 300;

    //var data = [];
    //function getRandomData() {
    //    if (data.length) {
    //        data = data.slice(1);
    //    }
    //    while (data.length < maximum) {
    //        var previous = data.length ? data[data.length - 1] : 50;
    //        var y = previous + Math.random() * 10 - 5;
    //        data.push(y < 0 ? 0 : y > 100 ? 100 : y);
    //    }
    //    // zip the generated y values with the x values
    //    var res = [];
    //    for (var i = 0; i < data.length; ++i) {
    //        res.push([i, data[i]])
    //    }
    //    return res;
    //}

    priceSeries = [{
        //data: getRandomData(),
        data: null,
        lines: {
            fill: true,
            fillColor: { colors: [{opacity: 0.1},{opacity: 0.5}]},
            show: true
        },
        label: 'Price'
    }];

    var plotPrice = $.plot(priceContainer, priceSeries, { 
                grid: {
                    borderWidth: 1,
                    minBorderMargin: 20,
                    labelMargin: 10,
                    margin: {
                        top: 8,
                        bottom: 20,
                        left: 20
                    },
                    markings: function(axes) {
                        var markings = [];
                        var xaxis = axes.xaxis;
                        for (var x = Math.floor(xaxis.min); x < xaxis.max; x += xaxis.tickSize * 2) {
                            markings.push({
                                xaxis: {
                                    from: x,
                                    to: x + xaxis.tickSize
                                },
                                color: "rgba(232, 232, 255, 0.01)"
                            });
                        }
                        return markings;
                    },
                    hoverable: true
                },
                tooltip: true,
                tooltipOpts: {
                    content: "Date: %x, USD: $%y"
                },
                legend: {
                    show: false
                },
                colors: [
                  //"#FF7070"
                  '#FF9939'
                ]
            });

    depthSeries = [{
        //data: getRandomData(),
        data: null,
        lines: {
            fill: true,
            fillColor: { colors: [{opacity: 0.1},{opacity: 0.5}]},
            show: true
        },
        label: 'Buy Depth'
    }, {
        data: null,
        lines: {
            fill: true,
            fillColor: { colors: [{opacity: 0.1},{opacity: 0.5}]},
            show: true
        },
        label: 'Sell Depth'

    }];

    var plotDepth = $.plot(depthContainer, depthSeries, { 
                grid: {
                    borderWidth: 1,
                    minBorderMargin: 20,
                    labelMargin: 10,
                    margin: {
                        top: 8,
                        bottom: 20,
                        left: 20
                    },
                    markings: function(axes) {
                        var markings = [];
                        var xaxis = axes.xaxis;
                        for (var x = Math.floor(xaxis.min); x < xaxis.max; x += xaxis.tickSize * 2) {
                            markings.push({
                                xaxis: {
                                    from: x,
                                    to: x + xaxis.tickSize
                                },
                                color: "rgba(232, 232, 255, 0.01)"
                            });
                        }
                        return markings;
                    },
                    hoverable: true
                },
                tooltip: true,
                tooltipOpts: {
                    content: "USD: $%x, BTC: %y"
                },
                legend: {
                    show: false
                },
                colors: [
                  "#84F766",
                  "#FF6939"
                ]
            });
    setInterval(function updateRandom() {
        //series[0].data = getRandomData();
        $.getJSON('/exchange/pricechart', function(data) {
            console.log('price chart data');
            console.log(data);
            priceSeries[0].data = data;
            plotPrice.setData(priceSeries);
            plotPrice.setupGrid();
            plotPrice.draw();
        });
        $.getJSON('/exchange/depthchart', function(data) {
            console.log('depth chart data');
            console.log(data);
            depthSeries[0].data = data[0];
            depthSeries[1].data = data[1];
            plotDepth.setData(depthSeries);
            plotDepth.setupGrid();
            plotDepth.draw();
        });
    }, 1000);
});

//var chart_data = [
//    [0, 0],
//    [0.2, 0.3],
//    [0.4, 0.8],
//    [1, 1]
//];

/* buying */

$('#btc-buy-amount').keyup(function (e) {
    var cost = calcBuyingCost($('#btc-buy-amount').val(), $('#btc-buy-price-amount').val());
    $('#btc-buy-cost').html(cost);
});

$('#btc-buy-price-amount').keyup(function (e) {
    var cost = calcBuyingCost($('#btc-buy-amount').val(), $('#btc-buy-price-amount').val());
    $('#btc-buy-cost').html(cost);
});

var calcBuyingCost = function (btc_amount, asking_price) {
    if(btc_amount != 0 && asking_price != 0 && !isNaN(btc_amount) && !isNaN(asking_price)) {
        var cost = btc_amount * asking_price;
        return cost.toFixed(2);
    }
    else {
        return 0;
    }
};

$('#buy-btn').click(function (e) {
    var btc_amount = $('#btc-buy-amount').val();
    var buying_price = $('#btc-buy-price-amount').val();

    if(btc_amount != 0 && buying_price != 0 && !isNaN(btc_amount) && !isNaN(buying_price)) {
        var buy_request = {
            //id: some session var?
            amount:btc_amount,
            price:buying_price
        }
        var url = "https://ourdomain/buy";
        $.post( url, JSON.stringify(buy_request), function (response) {
            // crate an open order
        })
    }

});

/* selling */

$('#btc-sell-amount').keyup(function (e) {
    var cost = calcSellingCredit($('#btc-sell-amount').val(), $('#btc-sell-price-amount').val());
    $('#btc-sell-credit').html(cost);
});

$('#btc-sell-price-amount').keyup(function (e) {
    var cost = calcSellingCredit($('#btc-sell-amount').val(), $('#btc-sell-price-amount').val());
    $('#btc-sell-credit').html(cost);
});

var calcSellingCredit = function (btc_amount, selling_price) {
    if(btc_amount != 0 && selling_price != 0 && !isNaN(btc_amount) && !isNaN(selling_price)) {
        var cost = btc_amount * selling_price;
        return cost.toFixed(2);
    }
    else {
        return 0;
    }
};

$('#sell-btn').click(function (e) {

});

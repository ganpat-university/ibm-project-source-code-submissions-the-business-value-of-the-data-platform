'use strict';
$(document).ready(function() {
    setTimeout(function() {
        barChart()
    }, 100);
});
var product_count = []
var product = []
for(var i in group_product_count['product'])
    product.push(group_product_count['product'][i]);
for(var i in group_product_count['total'])
    product_count.push(group_product_count['total'][i]);

function barChart() {
    // BOXPLOT start
    $(function() {
        var barChartOptions = {
            series: [{
            data: product_count
        }],
        chart: {
            type: 'bar',
            height: 400,
            toolbar:{
                show: false
            }
        },
        plotbarChartOptions: {
            bar: {
                borderRadius: 4,
                horizontal: true,
            }
        },
        dataLabels: {
            enabled: false
        },
        xaxis: {
            categories: product,
        }
        };
        new ApexCharts(document.querySelector("#bar-chart"), barChartOptions).render();
    });
}
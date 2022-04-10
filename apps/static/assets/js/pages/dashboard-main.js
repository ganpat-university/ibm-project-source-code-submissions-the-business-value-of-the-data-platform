'use strict';
$(document).ready(function() {
    setTimeout(function() {
        floatchart()
    }, 100);
});

function floatchart() {
    // [ customer-chart ] start
    $(function() {
        var options = {
            chart: {
                height: 150,
                type: 'donut',
            },
            dataLabels: {
                enabled: false
            },
            plotOptions: {
                pie: {
                    donut: {
                        size: '75%'
                    }
                }
            },
            labels: ['No', 'Yes'],
            series: [parseInt(customer_timely_responded_No), parseInt(customer_timely_responded_Yes)],
            legend: {
                show: false
            },
            tooltip: {
                theme: 'datk'
            },
            grid: {
                padding: {
                    top: 20,
                    right: 0,
                    bottom: 0,
                    left: 0
                },
            },
            colors: ["#4680ff", "#2ed8b6"],
            fill: {
                opacity: [1, 1]
            },
            stroke: {
                width: 0,
            }
        }
        var chart = new ApexCharts(document.querySelector("#customer-chart"), options);
        chart.render();
        var options1 = {
            chart: {
                height: 150,
                type: 'donut',
            },
            dataLabels: {
                enabled: false
            },
            plotOptions: {
                pie: {
                    donut: {
                        size: '75%'
                    }
                }
            },
            labels: ['No', 'Yes'],
            series: [parseInt(customer_disputed_count_No), parseInt(customer_disputed_count_Yes)],
            legend: {
                show: false
            },
            tooltip: {
                theme: 'dark'
            },
            grid: {
                padding: {
                    top: 20,
                    right: 0,
                    bottom: 0,
                    left: 0
                },
            },
            colors: ["#ff869a", "#2ed8b6"],
            fill: {
                opacity: [1, 1]
            },
            stroke: {
                width: 0,
            }
        }
        var chart = new ApexCharts(document.querySelector("#customer-chart1"), options1);
        chart.render();
    });
    // [ customer-chart ] end
    // [ unique-visitor-chart ] start
    var result = [];
    var max_complaint_count = 0
    for(var i in line_graph_month_d[0])
        result.push(line_graph_month_d[0][i]);
    var totalDates = result.length
    var series_data = []
    for(var i in line_graph_d['state'])
    {
        var temp_arr = Array(totalDates).fill(0);
        for(var j in line_graph_d['month'][i]){
            var current_complaint_count = line_graph_d['complaint_count'][i][j];
            var current_date_index = result.indexOf(line_graph_d['month'][i][j]);
            temp_arr[current_date_index] = current_complaint_count;
            if(max_complaint_count < current_complaint_count)
                max_complaint_count = current_complaint_count;
        }
        series_data.push({name:line_graph_d['state'][i],data:temp_arr})
    }
    $(function() {
        var options = {
            chart: {
                height: 400,
                type: 'line',
                toolbar: {
                    show: false,
                },
                toolbar: {
                    show: true,
                    offsetX: 0,
                    offsetY: 0,
                    tools: {
                      download: false,
                      selection: true,
                      zoom: true,
                      zoomin: true,
                      zoomout: true,
                      pan: false,
                      reset: true | '<img src="/static/icons/reset.png" width="20">',
                      customIcons: []
                    },
                    autoSelected: 'zoom' 
                  },
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                width: 2,
                curve: 'smooth'
            },
            series: series_data,
            legend: {
                position: 'top',
            },
            xaxis: {
                type: 'datetime',
                categories: result,
                axisBorder: {
                    show: false,
                },
                label: {
                    style: {
                        color: '#ccc'
                    }
                },
            },
            yaxis: {
                show: true,
                min: 0,
                max: max_complaint_count+5,
                labels: {
                    style: {
                        color: '#ccc'
                    }
                }
            },
            colors: ['#73b4ff', '#59e0c5'],
            fill: {
                type: 'gradient',
                gradient: {
                    shade: 'light',
                    gradientToColors: ['#4099ff', '#2ed8b6'],
                    shadeIntensity: 0.5,
                    type: 'horizontal',
                    opacityFrom: 1,
                    opacityTo: 1,
                    stops: [0, 100]
                },
            },
            markers: {
                size: 3,
                colors: ['#4099ff', '#2ed8b6'],
                opacity: 0.9,
                strokeWidth: 2,
                hover: {
                    size: 7,
                }
            },
            grid: {
                borderColor: '#cccccc3b',
            }
        }
        var element = document.querySelector("#unique-visitor-chart");
        element.innerHTML = '';
        var chart = new ApexCharts(element, options);
        chart.render();
    });
    // [ unique-visitor-chart ] end
}


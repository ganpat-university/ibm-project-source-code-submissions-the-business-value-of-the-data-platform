$('#complaint_state_select').on('change', function() {
    fetch('http://127.0.0.1:8000/get-state-data/'+this.value, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    }).then(
            res=>res.json()
    ).then(
        res => {
            console.log(res)
            complaint_location_chart(res['state'][0], res['complaint_count'][0], res['month'][0]);
        }
    );
});
function complaint_location_chart(state, complaint_count, months){
    var max_count = Math.max.apply(Math, complaint_count);
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
        series: [
            {
                name: state,
                data: complaint_count
            }
        ],
        legend: {
            position: 'top',
        },
        xaxis: {
            type: 'datetime',
            categories: months,
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
            max: max_count+5,
            labels: {
                style: {
                    color: '#ccc'
                }
            }
        },
        colors: ['#73b4ff'],
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'light',
                gradientToColors: ['#4099ff'],
                shadeIntensity: 0.5,
                type: 'horizontal',
                opacityFrom: 1,
                opacityTo: 1,
                stops: [0, 100]
            },
        },
        markers: {
            size: 3,
            colors: ['#4099ff'],
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
}
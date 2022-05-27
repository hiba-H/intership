




	var date = [];
    var project =[];
    var sups =[];

    const params = new URLSearchParams(window.location.search)
    for (const param of params) {

        console.log(sups)
        if (param[0] == 'date'){
            date.push(param[1])
        }
        if (param[0] == 'project'){
            for (i=0 ;i<=param[1] ; i++){
                project.push(i)
            }
            console.log(project)

        }
        if (param[0] == 'contact'){
            for (i=0 ;i<=param[1]; i++){
                sups.push(i)
            }
            console.log(sups.length)

            

        }
    
        console.log(project)   
    }
    if (sups.length < project.length){
        for (i = sups.length ; i<project.length;i++){
            sups.push(0);
        }
    }
else if (sups.length > project.length){
        for (i = sups.length ; i<=project.length;i++){
            project.push(0);
        }
    }
    console.log(sups)

// CHART: APEXCHART

console.log(date)
var options = {
    series: [{
        name: 'project name',
        data: project
    }, {
        name: 'supscribers',
        data: sups
    }],
    chart: {
        height: 350,
        type: 'area'
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth'
    },
    xaxis: {
        type: 'datetime',
        
        categories:date
    },
    tooltip: {
        x: {
            format: 'yyyy/MM/dd HH:mm:ss'
        },
    },
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();


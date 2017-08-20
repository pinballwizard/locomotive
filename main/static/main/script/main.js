$(document).ready(function () {
    var ctx = document.getElementById("myChart").getContext('2d');

    $("button").click(function(){
        $.post("/submit/",
            $("form").serialize(),
            function (data, status) {
                console.log("data: " + data + "\nStatus:" + status);
                data = JSON.parse(data);
                var years = data["years"];
                delete data["years"];
                var datasets = [];
                for (d in data) {
                    console.log(data[d]);
                    datasets.push({
                        label: d,
                        data: data[d],
                        backgroundColor: 'rgba(60, 141, 188, 0.2)',
                        borderColor: 'rgba(60, 141, 188,1)',
                        borderWidth: 1
                    })
                }
                console.log(datasets);
                myChart.data.labels = years;
                myChart.data.datasets = datasets;
                myChart.update();
            });
    });


    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: "",
            datasets: [{
                label: "",
                data: 0
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
});

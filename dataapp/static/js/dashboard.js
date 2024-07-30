// insights/static/js/dashboard.js
console.log('dashboard.js is loaded');
document.addEventListener('DOMContentLoaded', function() {
    console.log('dashboard.js is loaded and parsed');
    fetch('/api/data/')
        .then(response => response.json())
        .then(data => {
            console.log('data fetched fromapi:',data)
            populateFilters(data);
            drawChart(data);
            document.getElementById('submitButton').addEventListener('click', function() {
                event.preventDefault();
                console.log('submitted button clicked')
                const filteredData = filterData(data);
                console.log('filtered data',filterData)
                drawChart(filteredData);
            });
        });
    

    function populateFilters(data) {
        console.log('populating filters');
        const countryFilter = document.getElementById('countryFilter');
        const sectorFilter = document.getElementById('sectorFilter');
        const topicFilter = document.getElementById('topicFilter');
        const pestleFilter = document.getElementById('pestleFilter');

        const countries = [...new Set(data.map(item => item.country))];
        const regions = [...new Set(data.map(item => item.region))];
        const sectors = [...new Set(data.map(item => item.sector))];
        const topics = [...new Set(data.map(item => item.topic))];
        const pestles = [...new Set(data.map(item => item.pestle))];

        countries.forEach(country => {
            const option = document.createElement('option');
            option.value = country;
            option.text = country;
            countryFilter.appendChild(option);
        });





        regions.forEach(region => {
            const option = document.createElement('option');
            option.value = region;
            option.text = region;
            regionFilter.appendChild(option);
        });

        sectors.forEach(sector => {
            const option = document.createElement('option');
            option.value = sector;
            option.text = sector;
            sectorFilter.appendChild(option);
        });

        topics.forEach(topic => {
            const option = document.createElement('option');
            option.value = topic;
            option.text = topic;
            topicFilter.appendChild(option);
        });

        pestles.forEach(pest => {
            const option = document.createElement('option');
            option.value = pest;
            option.text = pest;
            pestleFilter.appendChild(option);
        });
    }


    function filterData(data) {
        const countryFilter = document.getElementById('countryFilter').value;
        const regionFilter = document.getElementById('regionFilter').value;
        const sectorFilter = document.getElementById('sectorFilter').value;
        const topicFilter = document.getElementById('topicFilter').value;
        const pestleFilter = document.getElementById('pestleFilter').value;

        console.log('filtering data with',{
            countryFilter,regionFilter,sectorFilter,topicFilter,pestleFilter
        });

        return data.filter(item => {
            return (countryFilter ==="" || countryFilter==='ALL'|| item.country === countryFilter)&&
                   (regionFilter === "" || regionFilter==='ALL' || item.region === regionFilter) &&
                   (sectorFilter === "" || sectorFilter==='ALL' || item.sector === sectorFilter) &&
                   (topicFilter === "" || topicFilter==='ALL' || item.topic === topicFilter) &&
                   (pestleFilter === "" || pestleFilter==='ALL' || item.pestle === pestleFilter);
        });
    }


    let chartInstance;

    function drawChart(data) {
        const ctx = document.getElementById('myChart').getContext('2d');
        console.log('drawing chart with data:',data)

        if (chartInstance){
            chartInstance.destroy();
        }
    
        chartInstance = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: data.map(item => item.region),
                datasets: [{
                    label: 'rel',
                    data: data.map(item => item.relevance),
                    backgroundColor: '#6B697B',
                    borderColor: '#9BD0F5',
                    borderWidth: 2
                },
                {
                    label: 'likelihood',
                    data: data.map(item => item.likelihood),
                    backgroundColor: '#f5bbf3',
                    borderColor: '#eda0b2',
                    borderWidth: 2
                },
                {
                    label: 'intensity',
                    data: data.map(item => item.intensity),
                    backgroundColor: '#09ed2c',
                    borderColor: '#09ed96',
                    borderWidth: 2
                },
                {label: 'endyear',
                    data: data.map(item => item.end_year),
                    backgroundColor: '#400752',
                    borderColor: '#b5b4bd',
                    borderWidth: 2
                }
                ]
                },
                
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: false
                    }
                }
            }
        });
    }
});

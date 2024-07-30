used pipenv shell for virtualenv 
for requirements see pipfile contains django,restframework,postgres-psycopg-binary
after installing dependencies and get into projectfolder run cmd->python manage.pyrunserver
for jsondata visit: http://127.0.0.1:8000/api/data/
for visualization dashboard visit: http://127.0.0.1:8000/api/index/  
select diffrent countries to see changes
 chartInstance = new Chart(ctx, {
            type: 'bar',------to see difffernt chart types :'bar','bubble','doughnut','pie',radar,line
            data: {
                labels: data.map(item => item.region),
                datasets: [{
                    label: 'rel',
                    data: data.map(item => item.relevance),
                    backgroundColor: '#6B697B',
                    borderColor: '#9BD0F5',
                    borderWidth: 2
                }
const visitors_element = document.getElementById('visitors').getContext('2d');
const ads_element = document.getElementById('ads').getContext('2d');

const visitors_char = new Chart(visitors_element, {
    type: 'line',
    data: {
        labels: ['01/2022', '02/2022', '03/2022', '04/2022', '05/2022', '06/2022'],
        datasets: [{
            label: 'visite mensili',
            data: [2200, 1190, 4029, 5768, 2239, 3098],
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const ads_char = new Chart(ads_element, {
    type: 'bar',
    data: {
        labels: ['01/2022', '02/2022', '03/2022', '04/2022', '05/2022', '06/2022'],
        datasets: [{
            label: 'guadagni ads',
            data: [2200, 1190, 4029, 5768, 2239, 3098],
            backgroundColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
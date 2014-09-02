$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2012 Q1',
            shows_local: 400,
            shows_fora: 33
        }, {
            period: '2012 Q2',
            shows_local: 380,
            shows_fora: 3
        }, {
            period: '2012 Q3',
            shows_local: 589,
            shows_fora: 2
        }, {
            period: '2012 Q4',
            shows_local: 200,
            shows_fora: 100
        }, {
            period: '2013 Q1',
            shows_local: 450,
            shows_fora: 46
        }, {
            period: '2013 Q2',
            shows_local: 109,
            shows_fora: 2
        }, {
            period: '2013 Q3',
            shows_local: 549,
            shows_fora: 62
        }, {
            period: '2013 Q4',
            shows_local: 682,
            shows_fora: 50
        }, {
            period: '2014 Q1',
            shows_local: 690,
            shows_fora: 67
        }, {
            period: '2014 Q2',
            shows_local: 789,
            shows_fora: 23
        }],
        xkey: 'period',
        ykeys: ['shows_local', 'shows_fora'],
        labels: ['Shows em São Luís', 'Shows em Outras Cidades'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    Morris.Donut({
        element: 'morris-donut-chart',
        data: [{
            label: "Download Sales",
            value: 12
        }, {
            label: "In-Store Sales",
            value: 30
        }, {
            label: "Mail-Order Sales",
            value: 20
        }],
        resize: true
    });

    Morris.Bar({
        element: 'morris-bar-chart',
        data: [{
            y: '2006',
            a: 100,
            b: 90
        }, {
            y: '2007',
            a: 75,
            b: 65
        }, {
            y: '2008',
            a: 50,
            b: 40
        }, {
            y: '2009',
            a: 75,
            b: 65
        }, {
            y: '2010',
            a: 50,
            b: 40
        }, {
            y: '2011',
            a: 75,
            b: 65
        }, {
            y: '2012',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true
    });

});

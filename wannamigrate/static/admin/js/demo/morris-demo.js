$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            period: '2012 Q1',
            shows_local: 400,
            shows_brasil: 33,
            shows_exterior: 0
        }, {
            period: '2012 Q2',
            shows_local: 380,
            shows_brasil: 3,
            shows_exterior: 0
        }, {
            period: '2012 Q3',
            shows_local: 589,
            shows_brasil: 2,
            shows_exterior: 0
        }, {
            period: '2012 Q4',
            shows_local: 200,
            shows_brasil: 100,
            shows_exterior: 1
        }, {
            period: '2013 Q1',
            shows_local: 450,
            shows_brasil: 46,
            shows_exterior: 1
        }, {
            period: '2013 Q2',
            shows_local: 109,
            shows_brasil: 2,
            shows_exterior: 0
        }, {
            period: '2013 Q3',
            shows_local: 549,
            shows_brasil: 62,
            shows_exterior: 0
        }, {
            period: '2013 Q4',
            shows_local: 682,
            shows_brasil: 50,
            shows_exterior: 1
        }, {
            period: '2014 Q1',
            shows_local: 690,
            shows_brasil: 67,
            shows_exterior: 0
        }, {
            period: '2014 Q2',
            shows_local: 789,
            shows_brasil: 23,
            shows_exterior: 0
        }],
        xkey: 'period',
        ykeys: ['shows_local', 'shows_brasil', 'shows_exterior'],
        labels: ['Shows em São Luís', 'Shows em Outras Cidades', 'Shows no Exterior'],
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
            y: '2012',
            a: 50,
            b: 40
        }, {
            y: '2013',
            a: 75,
            b: 65
        }, {
            y: '2014',
            a: 100,
            b: 90
        }],
        xkey: 'y',
        ykeys: ['a', 'b'],
        labels: ['Series A', 'Series B'],
        hideHover: 'auto',
        resize: true
    });

    Morris.Line({
        element: 'morris-line-chart',
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
            y: '2012',
            a: 50,
            b: 40
        }, {
            y: '2013',
            a: 75,
            b: 65
        }, {
            y: '2014',
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

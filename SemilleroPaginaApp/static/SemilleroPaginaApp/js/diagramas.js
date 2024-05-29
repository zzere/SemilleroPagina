
// Obtener el contexto del canvas
const ctx = document.getElementById('tabla').getContext('2d');

var labels  = typeof dynamicLabels !== 'undefined' ? dynamicLabels : [];
var data    = typeof dynamicData !== 'undefined' ? dynamicData : [];
var color   = typeof dynamicColor !== 'undefined' ? dynamicColor : [];
var label   = typeof dynamicLabel !== 'undefined' ? dynamicLabel : [];

// Datos para el gráfico de barras
var datos = {
    labels: labels,
    datasets: [{
        label: label,
        data: data, // Valores de las barras
        backgroundColor: color, // Color de fondo de las barras
        borderColor: 'rgba(54, 162, 235, 1)', // Color del borde de las barras
        borderWidth: 1
    }]
};


// Opciones del gráfico
var opciones = {
    scales: {
        y: {
            beginAtZero: true
        }
    },
    plugins: {
        // Plugin para dibujar la línea horizontal
        drawHorizontalLine: {
            yValue: 0,
            lineColor: 'red', // Color de la línea horizontal
            lineWidth: 2 // Grosor de la línea horizontal
        }
    }
};

// Crear el gráfico de barras
var miGrafico = new Chart(ctx, {
    type: 'bar',
    data: datos,
    options: opciones,
    plugins: [{
        // Implementación del plugin para dibujar la línea horizontal
        id: 'drawHorizontalLine',
        afterDraw: function (chart, args, options) {
            var yValue = options.yValue;
            var lineColor = options.lineColor;
            var lineWidth = options.lineWidth;

            var yAxis = chart.scales.y;
            var xPos = yAxis.getPixelForValue(yValue);

            // Dibujar la línea horizontal
            ctx.save();
            ctx.beginPath();
            ctx.strokeStyle = lineColor;
            ctx.lineWidth = lineWidth;
            ctx.moveTo(chart.chartArea.left, xPos);
            ctx.lineTo(chart.chartArea.right, xPos);
            ctx.stroke();
            ctx.restore();
        }
    }]
});

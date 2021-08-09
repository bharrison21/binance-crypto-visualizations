// //get all of the 
// window.onload = function (){
// 	var select = document.getElementById('symbol');
// 	// var array_symbols = "";
// 	for(var i = 0; i < select.options.length; i++){
// 	// 	console.log(select[i]);
// 		var ticker = select[i].value
// 	 }
	
// 	}
// window.onload = function (){
// 	var select = document.getElementById('symbol');
// 	var fin = select.value
// 	console.log(fin)
// }
var user = JSON.parse('{{ user | tojson | safe}}');
console.log(user) 


var chart = LightweightCharts.createChart(document.body, {
	width: 600,
  height: 300,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

var candleSeries = chart.addCandlestickSeries({
    upColor: '#6495ED',
    downColor: '#FF6347',
    borderVisible: false,
    wickVisible: true,
    borderColor: '#000000',
    wickColor: '#000000',
    borderUpColor: '#4682B4',
    borderDownColor: '#A52A2A',
    wickUpColor: '#4682B4',
    wickDownColor: '#A52A2A',
});

fetch('http://localhost:5000/settings')
.then((r)=>r.json())
.then((response)=>{
	console.log(response);
	candleSeries.setData(response);

})

var binanceSocket = new WebSocket ('wss://stream.binance.com:9443/ws/BTCUSDT@kline_15m');

binanceSocket.onmessage = function (event) {
	var message = JSON.parse(event.data);
	var candlestick = message.k;
	
	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close:candlestick.c
	})

}
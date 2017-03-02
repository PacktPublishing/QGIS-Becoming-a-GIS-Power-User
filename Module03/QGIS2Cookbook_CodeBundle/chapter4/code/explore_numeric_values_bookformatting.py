import processing 
from PyQt4.QtWebKit import QWebView

layer = iface.activeLayer()
values = []
features = processing.features(layer)
for f in features:
    values.append(f['elev_m'])

myWV = QWebView(None)
html='<html><head><script type="text/javascript"'
html+='src="https://www.google.com/jsapi"></script>'
html+='<script type="text/javascript">'
html+='google.load("visualization","1",{packages:["corechart"]});'
html+='google.setOnLoadCallback(drawChart);'
html+='function drawChart() { '
html+='var data = google.visualization.arrayToDataTable(['
html+='["%s"],' % (field_name)

for value in values:
    html+='[%f],' % (value)

html+=']);'
html+='var chart = new google.visualization.Histogram('
html+='                document.getElementById("chart_div"));'
html+='chart.draw(data, {title: "Histogram"});}</script></head>'
html+='<body><h1>Layer: %s</h1>' % (layer.name())
html+='<p>Values for %s range from: ' % (field_name)
html+='%d to %d</p>' % (min(values),max(values))
html+='<div id="chart_div"style="width:900px; height:500px;">'
html+='</div></body></html>'

myWV.setHtml(html)
myWV.show()
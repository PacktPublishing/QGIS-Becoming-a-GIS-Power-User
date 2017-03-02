import processing 
from PyQt4.QtWebKit import QWebView

layer = iface.activeLayer()
values = []
features = processing.features(layer)
for f in features:
    values.append( f['elev_m'] )

myWV = QWebView(None)
html="""<html><head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {  """
html+= "var data = google.visualization.arrayToDataTable([ [ '%s']," % (field_name)
for value in values:
    html+='[%f],' % (value)
html+= """  ]);
        var chart = new google.visualization.Histogram(document.getElementById('chart_div'));
        chart.draw(data, {title: 'Histogram'});
      }
    </script>
  </head>
  """
html+='<h1>Layer: %s</h1>' % (layer.name())
html+='<p>Values for %s range from: %d to %d</p>' % (field_name,min(values),max(values))
html+='<body><div id="chart_div" style="width: 900px; height: 500px;"></div></body>'
html+='</html>'

myWV.setHtml(html)
myWV.show()

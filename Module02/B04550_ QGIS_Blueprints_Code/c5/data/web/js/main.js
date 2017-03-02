var width = 960,
    height = 600;
	
//sets up the transformation from map coordinates to DOM coordinates
var projection = d3.geo.mercator()
	.center([-75.166667,40.03])
	.scale(60000);

//the shape generator
var path = d3.geo.path()
    .projection(projection);

var svg = d3.select("#map-container").append("svg")
    .attr("width", width)
    .attr("height", height);

var g = svg.append("g");

g.append( "rect" )
  .attr("width",width)
  .attr("height",height)
  .attr("fill","white")
  .attr("opacity",0)
  .on("mouseover",function(){
    hoverData = null;
    if ( probe ) probe.style("display","none");
  })

var map = g.append("g")
    .attr("id","map");

var probe,
    hoverData;

var dateScale, sliderScale, slider;

var format = d3.format(",");

  var months = ["Jan"],
      months_full = ["January"],
    orderedColumns = [],
    currentFrame = 0,
    interval,
    frameLength = 1000,
    isPlaying = false;

var sliderMargin = 65;

function circleSize(d){
  return Math.sqrt( .02 * Math.abs(d) );
};

//color scale
var color = d3.scale.linear()
	.domain([-.5, 0, 2.66])
    .range(["#FFEBEB", "#FFFFEB", "#E6FFFF"]);

//parse house_district.json TopoJSON, referece color scale and other styles
d3.json("/json/house_district.json", function(error, phila) {
  map.selectAll("path")
	  .data(topojson.feature(phila, phila.objects.house_district).features)
      .enter()
		  .append("path")
		  .attr("vector-effect","non-scaling-stroke")
		  .attr("class","land")
		  .style("fill", function(d) { return color(d.properties.d_avg_change); })
		  .attr("d", path);

//add a path element for district outlines
   map.append("path")
	   .datum(topojson.mesh(phila, phila.objects.house_district, function(a, b) { return a !== b; }))
       .attr("class", "state-boundary")
       .attr("vector-effect","non-scaling-stroke")
       .attr("d", path);

//probe is for popups
  probe = d3.select("#map-container").append("div")
    .attr("id","probe");

  d3.select("body")
    .append("div")
    .attr("id","loader")
    .style("top",d3.select("#play").node().offsetTop + "px")
    .style("height",d3.select("#date").node().offsetHeight + d3.select("#map-container").node().offsetHeight + "px");

//load and parse whites.csv
	d3.csv("csv/whites.csv",function(data){
    var first = data[0];
    // get columns
    for ( var mug in first ){
		if ( mug != "name" && mug != "lat" && mug != "lon" ){
        orderedColumns.push(mug);
      }
    }

    orderedColumns.sort( sortColumns );

    // draw city points 
    for ( var i in data ){
	  var projected = projection([ parseFloat(data[i].lon), parseFloat(data[i].lat) ])
      map.append("circle")
        .datum( data[i] )
        .attr("cx",projected[0])
        .attr("cy",projected[1])
        .attr("r",1)
        .attr("vector-effect","non-scaling-stroke")
        .on("mousemove",function(d){
          hoverData = d;
          setProbeContent(d);
          probe
            .style( {
              "display" : "block",
              "top" : (d3.event.pageY - 80) + "px",
              "left" : (d3.event.pageX + 10) + "px"
            })
        })
        .on("mouseout",function(){
          hoverData = null;
          probe.style("display","none");
        })
    }

    createLegend();

    dateScale = createDateScale(orderedColumns).range([0,3]);
    
    createSlider();

    d3.select("#play")
      .attr("title","Play animation")
      .on("click",function(){
        if ( !isPlaying ){
          isPlaying = true;
          d3.select(this).classed("pause",true).attr("title","Pause animation");
          animate();
        } else {
          isPlaying = false;
          d3.select(this).classed("pause",false).attr("title","Play animation");
          clearInterval( interval );
        }
      });

    drawMonth( orderedColumns[currentFrame] ); // initial map

    window.onresize = resize;
    resize();

    d3.select("#loader").remove();

  }) 

});
// d3.legend.js 
// (C) 2012 ziggy.jonsson.nyc@gmail.com
// MIT licence

(function() {
d3.legend = function(g) {
  g.each(function() {
    var g= d3.select(this),
        items = {},
        svg = d3.select(g.property("nearestViewportElement")),
        li = g.selectAll(".legend-items").data([true])

    li.enter().append("g").classed("legend-items",true)

    svg.selectAll("[data-legend]").each(function() {
        var self = d3.select(this)
        items[self.attr("data-legend")] = {
          pos : self.attr("data-legend-pos") || 1,
          color : self.attr("data-legend-color") != undefined ? self.attr("data-legend-color") : self.style("fill") != 'none' ? self.style("fill") : self.style("stroke") 
        }
      })

    items = d3.entries(items).sort(function(a,b) { return a.value.pos-b.value.pos})

    
    li.selectAll("text")
        .data(items,function(d) { return d.key})
        .call(function(d) { d.enter().append("text")})
        .call(function(d) { d.exit().remove()})
        .attr("y",function(d,i) { return i+"em"})
        .attr("x","1em")
        .text(function(d) { ;return d.key})
    
    li.selectAll("circle")
        .data(items,function(d) { return d.key})
        .call(function(d) { d.enter().append("circle")})
        .call(function(d) { d.exit().remove()})
        .attr("cy",function(d,i) { return i-0.25+"em"})
        .attr("cx",5)
        .attr("r","0.2em")
        .style("fill",function(d) { console.log(d.value.color);return d.value.color})  
    
  })
  return g
}
})()

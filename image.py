import golly as g
g.select(g.getrect())
startx = g.getselrect()[0]
starty = g.getselrect()[1]
endx = g.getselrect()[0]+g.getselrect()[2]
endy = g.getselrect()[1]+g.getselrect()[3]
with open("image.svg", "w") as svg:
    svg.write('<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" id="svg8" version="1.1" height="{}" width="{}">'.format(g.getselrect()[3]*2, g.getselrect()[2]*2))
    for y in range(starty, endy):
        for x in range(startx, endx):
            if g.getcell(x, y) != 0:
                svg.write('<rect style="fill:rgb({},{},{})" width="2" height="2" x="{}" y="{}"></rect>'.format(g.getcolors(g.getcell(x,y))[1],g.getcolors(g.getcell(x,y))[2],g.getcolors(g.getcell(x,y))[3],2*x,2*y))
    svg.write("</svg>")
g.setcolors([])
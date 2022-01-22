from django.shortcuts import render

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

def index(request):
#    Store components 
#    script, div = components(plot)

#    Feed them to the Django template.
#    return render(request, 'bokeh/index.html',
#            {'script' : script , 'div' : div} )
  
# Input Fields -> Parse Relevant Data -> Plot Relevant Plot

    plot = figure(plot_width=400, plot_height=400)
    plot.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
    script, div = components(plot)

    return render(request, 'bokeh/index.html', {'script': script, 'div': div})
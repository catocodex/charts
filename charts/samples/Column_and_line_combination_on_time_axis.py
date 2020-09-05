from django.shortcuts import render

# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
from charts.fusioncharts import FusionCharts
from charts.fusioncharts import FusionTable
from charts.fusioncharts import TimeSeries
import requests

# Loading Data and schema from a Static JSON String url
# The `chart` method is defined to load chart data from an JSON string.

def chart(request):

    data = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/data/column-line-combination-data.json').text
    schema = requests.get('https://s3.eu-central-1.amazonaws.com/fusion.store/ft/schema/column-line-combination-schema.json').text

    fusionTable = FusionTable(schema, data)
    timeSeries = TimeSeries(fusionTable)

    timeSeries.AddAttribute("caption", """{ 
                                        text: 'Web visits & downloads'
                                      }""")

    timeSeries.AddAttribute("subcaption", """{ 
                                    text: 'since 2015'
                                    }""")

    timeSeries.AddAttribute("yAxis", """[{
                                            plot: [{
                                                value: 'Downloads',
                                                type: 'column'
                                                }, {
                                                value: 'Web Visits',
                                                type: 'line'
                                                }]
                                        }]""")

    # Create an object for the chart using the FusionCharts class constructor
    fcChart = FusionCharts("timeseries", "ex1", 700, 450, "chart-1", "json", timeSeries)

     # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
    return  render(request, 'index.html', {'output' : fcChart.render(), 'chartTitle': "Column and line combination on time axis"})
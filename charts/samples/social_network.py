from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts

def chart(request):
   chartObj = FusionCharts( 'mscolumn2d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "App Publishing Trend",
    "subcaption": "2012-2016",
    "xaxisname": "Years",
    "yaxisname": "Total number of apps in store",
    "formatnumberscale": "1",
    "plottooltext": "<b>$dataValue</b> apps were available on <b>$seriesName</b> in $label",
    "theme": "fusion",
    "drawcrossline": "1"
  },
  "categories": [
    {
      "category": [
        {
          "label": "2012"
        },
        {
          "label": "2013"
        },
        {
          "label": "2014"
        },
        {
          "label": "2015"
        },
        {
          "label": "2016"
        }
      ]
    }
  ],
  "dataset": [
    {
      "seriesname": "iOS App Store",
      "data": [
        {
          "value": "125000"
        },
        {
          "value": "300000"
        },
        {
          "value": "480000"
        },
        {
          "value": "800000"
        },
        {
          "value": "1100000"
        }
      ]
    },
    {
      "seriesname": "Google Play Store",
      "data": [
        {
          "value": "70000"
        },
        {
          "value": "150000"
        },
        {
          "value": "350000"
        },
        {
          "value": "600000"
        },
        {
          "value": "1400000"
        }
      ]
    },
    {
      "seriesname": "Amazon AppStore",
      "data": [
        {
          "value": "10000"
        },
        {
          "value": "100000"
        },
        {
          "value": "300000"
        },
        {
          "value": "600000"
        },
        {
          "value": "900000"
        }
      ]
    }
  ]
}""")
   return render(request, 'index.html', {'output': chartObj.render()})
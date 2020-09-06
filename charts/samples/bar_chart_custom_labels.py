from django.shortcuts import render
from django.http import HttpResponse
from charts.fusioncharts import FusionCharts
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def chart(request):
   chartObj = FusionCharts( 'stackedbar2d', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Top Finishers",
    "subcaption": "2016-2017",
    "yaxisname": "Open Play Goals",
    "palettecolors": "#E64571, #88D786",
    "plotgradientcolor": " ",
    "theme": "fusion",
    "yaxismaxvalue": "30",
    "numdivlines": "2",
    "showlegend": "1",
    "interactivelegend": "0",
    "showvalues": "0",
    "showsum": "0"
  },
  "categories": [
    {
      "category": [
        {
          "label": "L.Suarez"
        },
        {
          "label": "L.Messi"
        },
        {
          "label": "G.Higuain"
        },
        {
          "label": "Z.Ibrahimovic"
        },
        {
          "label": "Diego Costa"
        },
        {
          "label": "H.Kane"
        },
        {
          "label": "D.Alli"
        },
        {
          "label": "A.Griezmann"
        },
        {
          "label": "Heung-Min Son"
        },
        {
          "label": "S.Mane"
        },
        {
          "label": "J.King"
        },
        {
          "label": "O.Giroud"
        },
        {
          "label": "R.Nainggolan"
        },
        {
          "label": "A.Robben"
        },
        {
          "label": "Pablo Sarabia"
        },
        {
          "label": "Isco"
        },
        {
          "label": "Rafinha"
        },
        {
          "label": "F.Bernardeschi"
        }
      ]
    }
  ],
  "dataset": [
    {
      "seriesname": "2016",
      "data": [
        {
          "value": "25"
        },
        {
          "value": "18"
        },
        {
          "value": "17"
        },
        {
          "value": "15"
        },
        {
          "value": "16"
        },
        {
          "value": "14"
        },
        {
          "value": "13"
        },
        {
          "value": "11"
        },
        {
          "value": "9"
        },
        {
          "value": "10"
        },
        {
          "value": "10"
        },
        {
          "value": "7"
        },
        {
          "value": "8"
        },
        {
          "value": "8"
        },
        {
          "value": "7"
        },
        {
          "value": "6"
        },
        {
          "value": "6"
        },
        {
          "value": "3"
        }
      ]
    },
    {
      "seriesname": "2017",
      "data": [
        {
          "value": "5"
        },
        {
          "value": "8"
        },
        {
          "value": "6"
        },
        {
          "value": "3"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        },
        {
          "value": "5"
        },
        {
          "value": "4"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        },
        {
          "value": "2"
        },
        {
          "value": "3"
        },
        {
          "value": "3"
        },
        {
          "value": "4"
        },
        {
          "value": "2"
        },
        {
          "value": "4"
        }
      ]
    }
  ],
  "annotations": {
    "groups": [
      {
        "id": "infobar",
        "items": [
          {
            "id": "1",
            "type": "line",
            "x": "$dataset.1.set.1.endx+10",
            "y": "$dataset.1.set.1.y",
            "tox": "$dataset.1.set.1.endx+50",
            "toy": "$dataset.1.set.1.y",
            "color": "#2F9AC4",
            "dashed": "0",
            "thickness": "1"
          },
          {
            "id": "2",
            "type": "line",
            "x": "$dataset.1.set.1.endx+50",
            "y": "$dataset.1.set.1.y",
            "tox": "$dataset.1.set.1.endx+50",
            "toy": "$dataset.0.set.1.y+50",
            "color": "#2F9AC4",
            "dashed": "0",
            "thickness": "1"
          },
          {
            "id": "3",
            "type": "line",
            "x": "$dataset.1.set.17.endx+5",
            "y": "$dataset.1.set.17.y",
            "tox": "$dataset.1.set.17.endx+200",
            "toy": "$dataset.0.set.17.y",
            "color": "#2F9AC4",
            "dashed": "0",
            "thickness": "1"
          },
          {
            "id": "4",
            "type": "line",
            "x": "$dataset.1.set.17.endx+200",
            "y": "$dataset.0.set.17.y",
            "tox": "$dataset.1.set.17.endx+200",
            "toy": "$dataset.0.set.17.y-40",
            "color": "#2F9AC4",
            "dashed": "0",
            "thickness": "1"
          },
          {
            "id": "shape",
            "type": "polygon",
            "startangle": "180",
            "sides": "3",
            "radius": "6",
            "color": "#2F9AC4",
            "x": "$dataset.1.set.17.endx+10",
            "y": "$dataset.1.set.17.y"
          },
          {
            "id": "shape",
            "type": "polygon",
            "startangle": "180",
            "sides": "3",
            "radius": "6",
            "color": "2F9AC4",
            "x": "$dataset.1.set.1.endx+10",
            "y": "$dataset.1.set.1.y"
          },
          {
            "id": "label1",
            "align": "RiGHT",
            "type": "text",
            "text": "Messi added{br}roughly 7 Goals from{br}his shot quality",
            "fillcolor": "#2F9AC4",
            "rotate": "90",
            "x": "$dataset.1.set.1.endx+65",
            "y": "$dataset.0.set.5.y"
          },
          {
            "id": "label2",
            "align": "CENTER",
            "type": "text",
            "text": "Bernardeschi{br}more than doubled{br}his chance quality{br}through shooting",
            "fillcolor": "#2F9AC4",
            "rotate": "90",
            "x": "$dataset.1.set.17.endx+200",
            "y": "$dataset.0.set.13.y"
          }
        ]
      }
    ]
  }
}""")
   return render(request, 'index.html', {'output': chartObj.render()})
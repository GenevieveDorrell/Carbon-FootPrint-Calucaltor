#Graphs the user's carbon against a baseline average
AVG_CARBON = 6370.09
DAILY_AVG = 17.45

import plotly.graph_objects as go
import plotly.io as pio
from datetime import datetime

def avg_carbon(usr_carbon, userID):
    pio.kaleido.scope.default_format = "png"
    dcarbon = []; dates = []
    for c in usr_carbon:
        dcarbon.append(c[0])
        date = datetime.strptime(c[1], '%Y-%m-%d')
        dates.append(date)
        
    acarbon = [DAILY_AVG] * len(dates)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=dcarbon, line=dict(color='royalblue', width=4)))
    fig.add_trace(go.Scatter(x=dates, y=acarbon, line=dict(color='firebrick', width=4, dash='dash')))

    fig.update_layout(
        {'plot_bgcolor':'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)'},
        title="Your carbon vs. the average college student in a dorm",
        xaxis = dict(
            tickmode='array',
            tickvals=dates)
    )
    fig.update_xaxes(title="Dates",tickformat = "%m/%d")
    fig.update_yaxes(title="lbs. CO2")
    path = "static/figures/"+ userID +"_avg_carbon.png" # added username to create folders for user for syconicity
    fig.write_image(path)
    return

def avg_carbon_str(usr_carbon):
    diff = round(AVG_CARBON - usr_carbon, 2)
    comp = " the average college student living in a dorm"
    if diff == 0:
        return "You use the same amount of carbon as" + comp
    elif diff < 0:
        return "You use " +str(abs(diff))+ " more lbs of CO2/yr. than" + comp
    else:
        return "You use " +str(abs(diff))+ " less lbs of CO2/yr. than" + comp

if __name__ == '__main__':
    # Unit test
    avg_carbon([[18.81, '2020-11-20'], [18.71, '2020-11-21']], "-1")
    print(avg_carbon_str(5000))
    print(avg_carbon_str(500))
    print(avg_carbon_str(5001))

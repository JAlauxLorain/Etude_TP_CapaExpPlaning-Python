#%%
InputFolder='Data/input/'
import numpy as np
import pandas as pd
import csv

import datetime
import copy

import plotly.graph_objects as go
Zones="FR"
year=2013

Selected_TECHNOLOGIES={'Thermal', 'OldNuke'} #you'll add 'HydroReservoir' after

#### reading CSV files
areaConsumption = pd.read_csv('CSV/input/areaConsumption'+str(year)+'_'+str(Zones)+'.csv',
                                sep=',',decimal='.',skiprows=0)
availabilityFactor = pd.read_csv('CSV/input/availabilityFactor'+str(year)+'_'+str(Zones)+'.csv',
                                sep=',',decimal='.',skiprows=0)
TechParameters = pd.read_csv('CSV/input/Gestion-Simple_TECHNOLOGIES.csv',sep=';',decimal=',',skiprows=0)

#### Selection of subset
availabilityFactor=availabilityFactor[ availabilityFactor.TECHNOLOGIES.isin(Selected_TECHNOLOGIES)]
TechParameters=TechParameters[TechParameters.TECHNOLOGIES.isin(Selected_TECHNOLOGIES)]


#graphe montrant le facteur de disponibilité du nucléaire en fonction de l'heure de l'année
tabl=availabilityFactor[availabilityFactor['TECHNOLOGIES']=='OldNuke']
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=list(tabl.TIMESTAMP), y=list(tabl.availabilityFactor)))
fig.update_layout(title_text="Facteur de dispo dans l'année",xaxis_title="heures de l'année")
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="en heures",
                     step="hour",
                     stepmode="backward")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="-"
    )
)
fig.show()

plotly.offline.plot(fig, filename='file.html')
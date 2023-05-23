#code Author Compiler Queen

import plotly.express as px 
	
import pandas as pd 
import plotly 
#opening the csv file or excel file 
df=pd.read_excel('DUMMY EXCEL.xlsx') #variable assignement based on columns in tables Slno=df['NUMBER'] 
City=df['City Name'] 
AQI=df['AQI Value'] 
Poll=df['Pollution Level'] 
print("original",df) 
rslt_df = df[df['Pollution Level']==' Moderate '] 
print("selected",rslt_df)

#histogram generation fig 1 
fig1=px.histogram(df, 
  
 y=City, 
 x=AQI, 
 color=Poll, 
 title='HISTOGRAM TO REPRESENT DATA OF CITIES AND THEIR  AQI', 
 color_discrete_sequence=["red", "green","blue", "goldenrod", "magenta"]  ) 
fig1.update_traces(visible=True,  
 textposition='inside', 
 selector=dict(type='densitymapbox') 
 ) 
fig1.update_layout( 
 title_font_size=40 
 )

#pie chart generation fig 2 
fig2=px.pie(df, 
 values=AQI, 
 names=Poll, 
 title='PIE CHART SHOWING RATING VS AQI VALUE '   
 ) 
fig2.update_traces( 
 textposition='inside', 
 textinfo='percent+label' 
 ) 
fig2.update_layout( 
 title_font_size=40 
 )

#Generation of Box plot fig 3 
fig3=px.box(rslt_df, 
 y=City, 
 x=Poll, 
  
 title='Box Plot REPRESENTING ALL CITIES WITH MODERATE AQI  LEVELS' 
 ) 
fig3.update_traces( 
 showlegend=True,  
 selector=dict(type='box') 
 ) 
fig3.update_layout( 
 title_font_size=37 
 )

#Generation of Scatter plot fig 4 
fig4= px.scatter(df, 
 x=City, y=Poll, 
 color_discrete_sequence=['red'], 
 title=' SCATTER PLOT REPRESENTING ALL CITIES WITH  RANGE OF POLL LEVELS' 
  
 ) 
  
with open('newgraph.html', 'a') as f: 
    f.write(fig1.to_html(full_html=False, include_plotlyjs='cdn'))  
    f.write(fig2.to_html(full_html=False, include_plotlyjs='cdn'))  
    f.write(fig3.to_html(full_html=False, include_plotlyjs='cdn'))  
    f.write(fig4.to_html(full_html=False, include_plotlyjs='cdn'))  

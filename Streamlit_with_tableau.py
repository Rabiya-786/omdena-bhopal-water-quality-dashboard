import streamlit as st
import streamlit.components.v1 as components 
import graphviz
import datetime
import pandas as pd
from PIL import Image

header = st.container()
with header : 

    #intials
    st.title("Omdena-VITBhopal Chapter")
    st.header("Monitoring of Water Quality in Bhopal through Satellite Imagery & GIS System")
    st.subheader("Water Quality Analysis of Lendiya Lake")


df = pd.read_csv(r"C:\Users\aniru\omdena-bhopal-water-quality-monitoring\Lendiya_Lake\All Paraneters.csv")

#workflow
st.subheader("WorkFlow")
src_workflow="https://whimsical.com/embed/9h4F2fEq2x3yiPp6Hb9o9V"
components.iframe(src_workflow, width=600, height=500, scrolling=False)

#dataframe

st.subheader("Click expander to observe Dataset")
with st.expander("Dataframe"):
    st.text("Here is the dataset that has been used in this Analysis : ")
    st.dataframe(df, height=500, width=1200)

#dateselction_parameter_view



#Visual Representation of Work Process for Temperature
st.subheader("Temperature Analysis of Lendiya-Lake")
st.text("This is representation of the Work-Flow for the Temperature Analysis")

graph = graphviz.Digraph()
graph.edge('data', 'Teamperature with outliers')
graph.edge('Teamperature with outliers', 'Temperature in degree celcius')
graph.edge('Temperature in degree celcius', 'Monsoon Analysis (Quater-wise)')
graph.edge('Temperature in degree celcius', ' Covid Analysis (Year-wise)')
st.graphviz_chart(graph)

#Integration of the Graph
st.subheader("Research Question: What is the variation for Temperature in Monsoon & Before/After Pandemic ?")
html_temp = """<div class='tableauPlaceholder' id='viz1679222151461' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Om&#47;OmdenaBhopal-LendiyaLake&#47;Temperature-Dash&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /><param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='OmdenaBhopal-LendiyaLake&#47;Temperature-Dash' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Om&#47;OmdenaBhopal-LendiyaLake&#47;Temperature-Dash&#47;1.png' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>         <script type='text/javascript'>                    var divElement = document.getElementById('viz1679222151461');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='1150px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp, width=1500, height=900)

st.subheader("Conclusion of the Temperature Parameter in Lendiya-Lake")
src_temp="https://whimsical.com/embed/LRzb5Pc3Xx4aZi9TatvDiQ"

components.iframe(src_temp, width=680, height=500, scrolling=False)

st.sidebar.selectbox("Graphs for Various Parameters",["Temperature", "Water Quality", "Dissolved Oxygen effect on Chlorophyll and Turbidity"])
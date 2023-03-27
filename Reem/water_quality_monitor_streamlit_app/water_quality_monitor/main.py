import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image
st.set_page_config(layout="wide")


@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    df1 = data.filter(
        [
            "Chlorophyll",
            "Dissolved Oxygen",
            "Dissolved Oxygen Matter",
            "Salinty",
            "Temperature",
            "Turbidity",
            "pH",
            "Suspended Matter",
        ]
    )
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Date"] = pd.to_datetime(data["Date"]).dt.date
    data["Year"] = pd.to_datetime(data["Date"]).dt.strftime("%Y")
    data["Month"] = pd.to_datetime(data["Date"]).dt.strftime("%m")
    data["Day"] = pd.to_datetime(data["Date"]).dt.strftime("%d")
    # data=data.set_index("Date")
    return data, df1


st.markdown(
    """
    <style>
@font-face {
font-family: 'Futura PT Light';
font-style: normal;
font-weight: normal;
src: local('Futura PT Light'), url('assets/fonts/FuturaCyrillicLight.woff') format('woff');
}
html, body, [class*="css"] {
font-family: 'Futura PT Light', sans-serif;
}
</style>
""",
    unsafe_allow_html=True,
)



st.title("Water Quality Monitoring")

header_project = st.container()
data_collection = st.container()
data_analysis = st.container()



data_df, df1 = load_data("C:\Users\aniru\omdena-bhopal-water-quality-monitoring\Reem\water_quality_monitor_streamlit_app\water_quality_monitor\merged_data.csv")

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "Project",
            "Data Collection",            
            "Interactive Data Analysis",
            "Data Analysis Findings",
        ],
        default_index=0,
    )


if selected == "Project":

    with header_project:
        st.title("Water Quality Monitoring in Lendyia Lake Bhopal")
        introduction_str=""" Water is a very crucial resource for all the living beings on Earth. Therefore, it is necessary to 
monitor water quality to ensure that it is safe for consumption and does not pose any harm to the 
environment. Water quality monitoring is done on the basis of various parameters. These 
parameters include Temperature, Turbidity, Chlorophyll-a (Chl-a), Blue-green algae 
Phycocyanin, Dissolved oxygen concentration, Specific conductivity, Fluorescent dissolved 
organic matter (FDOM) and Pollution sediments.  In the current world scenario there are many 
ways to monitor water quality. One of these ways is using Satellite Imagery and GIS techniques. 
Satellite imagery is a powerful tool for monitoring water quality as it provides a broad and 
detailed view of the region. It can capture data on water temperature, color, and clarity, which 
are essential indicators of water quality. Moreover, satellite imagery can provide data on the 
extent of contamination and the source of pollution. GIS techniques can be used to analyze and 
interpret the satellite data to identify areas of concern and develop appropriate strategies to 
address them. \n
 Bhopal region, located in the central part of India, is well known for its beautiful lakes. It is also 
called “The City of Lakes”.  However, due to rapid urbanization and industrialization, the water 
quality of the region is deteriorating at an alarming rate. The aftereffects of Bhopal Gas Tragedy 
still show significances in determining various water quality parameters. In this article we will 
see the measures taken by our Project in monitoring the water quality in Bhopal region using 
Satellite Imagery and GIS techniques. \n
In this article, we  will discuss the data visualization and analysis of Lendyia Lake. Lendyia 
Lake is a significant source of freshwater for the region, and its water quality is vital to maintain 
the ecological balance. In this analysis, we examine the various parameters of water quality in the lake
and identify the areas that require treatment.
"""
        st.text(introduction_str            
        )


if selected == "Data Collection":
    with data_collection:
        st.title("Data Collection")
        st.text(
            """ In the first week of the project, we conducted research on different types of APIs for 
collecting water quality data in Bhopal. After careful consideration, we chose the 
Google Earth Engine API for our data collection. \n
In the second week, we started collecting data using the Google Earth Engine API, 
using Sentinel 2A and Landsat 8 satellite imagery to collect data on various water 
quality parameters, including chlorophyll, turbidity, salinity, pH, dissolved oxygen, 
dissolved organic matter, and suspended matter."""
        )

if selected =='Data Analysis Findings':
	st.header("Water Quality Index and Parameters Identification")
	str_text_body = """ 
	There are several water quality parameters available, but the team has chosen the following 8 important 
parameters to monitor water quality.\n

1-pH:One of the most crucial indicators of water quality is pH. The pH scale determines how basic or acidic a 
solution is. \n
2- Salinity: The quantity of dissolved salts in water is known as salinity.
Water that is cloudy or hazy due to numerous tiny particles that are often unseen to the unaided eye is said to 
be turbid. Water quality is typically impacted by suspended sediments, such as clay, dirt, and silt particles, 
which frequently enter the water from disturbed locations.\n

3- Temperature: The aquatic system is significantly influenced by water temperature, which also affects the habitat's 
suitability for supporting aquatic life. Lower oxygen solubility in warmer water restricts the amount of oxygen
available.\n

4- Chlorophyll: A popular indicator of water quality and eutrophication level is chlorophyll-a.
The concentration of phytoplankton is determined by the amount of chlorophyll present in a water sample. 
Greater concentrations, which often occur when high algal production is sustained, indicate poorer water quality.\n


5- Suspended matter: Fine particles make up suspended matter, which is in suspension. Plankton, tiny pieces of plant matter,
and minerals are among those that naturally occur in river water, whilst others are a result of human activity
(organic and inorganic matter). Water can become more turbid due to suspended materials, harming the ecology 
of rivers and streams.\n

6- Dissolved oxygen (DO) is a gaseous form of molecular oxygen (O2) that comes from the environment. 
The concentrations of dissolved oxygen in water are influenced by salinity and temperature. 
Temperature and salinity have an opposite relationship with oxygen solubility in water;
as these two variables rise, so does DO.\n
7- The organic matter percentage in solution that passes through a 0.45 m filter is referred to as
"dissolved organic matter" (DOM). The mass of other elements, such as nitrogen, oxygen, and hydrogen,
that are present in organic material is also included in DOM. The total mass of the dissolved organic matter
is referred to here as DOM. \n

This figure shows paramters values for safe and danger zone. \n
"""
	st.text(str_text_body)
	image = Image.open('D:\\Omdena\\water_quality_monitor\\Parameter-Thresholds.png')
	st.image(image)

	st.header("Findings")
	st.subheader('Per-year Findins')
	str_findings= """
1- pH level had outlier in 2019, 2022. However it could be concluded that each year the distribution ranges changes
2- Turbidity had outliers values since 2019, however the disrtibution didn't change across the years
3- Temperautre had outliersin every-year. However we have no information in 2022.
 In covid year the disribution of temperatures varies. However before and  after 2020 the temperatures variation across years is not large
4- Salinty had large number of outliers in 2019. However distribution and ranges across year varies.
5- Disssolved oxygen matter is the most consisent features across years. There are small number of outliers
6- Dissolved oxygen had outliers since 2019. However the disrtibution across years are quit similar.
"""
	st.text(str_findings)
	st.subheader('Per-Month Findins')
	str_findings= """
1- Chrolophyll values across year pe-month ar not so good except for 2022 fisrt month has bad zone values. 
2- Dissloved oxygen for 20220 values where in bad zone and begging of2021. Hoever the rest are in good zone values
3- Dissolved oxygen matters for 2019,2018 the values where in bad zone ranges. However, 
for 2020,2021,2022 for first 2 months andlast 3 months the values where in good zone range however
from month 3-9 the values are too high
4- Salinty values are between 0-1 for most year hence, lies whithin bad zone values
5- Trubidity values are less than 0 for all months hence lies within good zone 
6- pH values are in good zone ranges for all years and months
"""
	st.text(str_findings)
	st.subheader('Overall Conclusion')
	str_findings="""
Our data collection efforts yielded a rich dataset of water quality parameters for Lendyia lake in the Bhopal region.
We found that chlorophyll levels varied widely showing high levels of chlorophyll, indicating high levels of algae and other aquatic plants. 
Turbidity levels were generally within the acceptable range.
pH levels were generally within the acceptable range.
Dissolved oxygen levels were generally within the acceptable range as well, however there were some outliers.
For the dissolved oxygen matters: Mmre than **50%** of the values lie in **need treatment zone**.
Overall, the data provides a comprehensive view of water quality in the Bhopal region and can be
used to inform future efforts to monitor and manage water resources in the area.
"""
	st.text(str_findings)
	st.subheader('Conclusion')
	str_conclusino="""
In conclusion, monitoring water quality using satellite imagery, GIS techniques, and 
machine learning is crucial to ensure safe water consumption and protect the 
environment. These technologies provide a broad and detailed view of the region, 
which is essential for developing appropriate strategies to address water quality 
issues. The project's findings and recommendations can inform stakeholders to 
implement effective and sustainable monitoring programs to ensure the long-term 
	"""
	st.text(str_conclusino)




if selected == "Interactive Data Analysis":
    st.header("Date Range")
    st.text("Please select start date and end date you want to visualize")

    d = st.date_input("Start Date", datetime.date(2018, 1, 1))

    e = st.date_input("End Date", datetime.date(2019, 1, 1))

    st.header("Data head analysis")
    st.text("Showing first few rows from the specified date range")

    date_interval_desired = data_df[(data_df["Date"] >= d) & (data_df["Date"] <= e)]
    st.write(date_interval_desired)
    df1_desired = date_interval_desired.filter(
        [
            "Chlorophyll",
            "Dissolved Oxygen",
            "Dissolved Oxygen Matter",
            "Salinty",
            "Temperature",
            "Turbidity",
            "pH",
            "Suspended Matter",
        ]
    )
    col_interested = [
        "Chlorophyll",
        "Dissolved Oxygen",
        "Dissolved Oxygen Matter",
        "Salinty",
        "Temperature",
        "Turbidity",
        "pH",
        "Suspended Matter",
    ]

    st.header("Yearwise data plotting for outliers")
    for i in col_interested:

        fig = px.box(date_interval_desired, x="Year", y=i)
        fig.update_traces(
            quartilemethod="exclusive"
        )  # or "inclusive", or "linear" by default
        st.plotly_chart(fig, use_container_width=True)

    st.header("Monthly Analysis")
    df2 = pd.DataFrame()
    for i in col_interested:
        r_mean_daily_max = date_interval_desired.groupby(
            ["Year", "Month", "Day"], as_index=False
        )[i].max()
        mda8 = r_mean_daily_max.groupby(["Year", "Month"], as_index=False)[i].median()
        fig, ax = plt.subplots(1, 2, figsize=(18, 4))
        sns.lineplot(data=df1_desired[i], ax=ax[0])
        sns.barplot(x="Month", y=i, data=mda8, hue="Year", ax=ax[1])
        df2[i] = r_mean_daily_max.groupby(["Year", "Month"], as_index=True)[i].median()
        plt.legend(bbox_to_anchor=(1.04, 0.5), loc="center left", borderaxespad=0)
        plt.title(i)
        plt.ylabel("count")
        st.pyplot(fig)
    st.header("Individual Feature Analysis")
    for i in col_interested:
        fig = px.scatter(date_interval_desired, y=i, color="Year")
        st.plotly_chart(fig, use_container_width=True)

    st.header("Distribution Plotting")
    st.subheader("Dissolved Oxygen Matter")
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(
        x="Dissolved Oxygen Matter",
        data=date_interval_desired[
            (date_interval_desired["Dissolved Oxygen Matter"] < 0.5)
        ],
        color="green",
        label="Dissolved Organic Matter < 0.5",
    )
    sns.histplot(
        x="Dissolved Oxygen Matter",
        data=date_interval_desired[
            (date_interval_desired["Dissolved Oxygen Matter"] >= 0.5)
            & (date_interval_desired["Dissolved Oxygen Matter"] <= 2)
        ],
        color="yellow",
        label="0.5 < Dissolved Organic Matter < 2",
    )
    sns.histplot(
        x="Dissolved Oxygen Matter",
        data=date_interval_desired[
            (date_interval_desired["Dissolved Oxygen Matter"] > 2)
        ],
        color="red",
        label="Dissolved Organic Matter >= 2",
    )
    ax.set_xlabel("Dissolved Organic Matter")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Temperature")
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(
        x="Temperature",
        data=date_interval_desired[
            (date_interval_desired["Temperature"] <= 35)
            & (date_interval_desired["Temperature"] >= 15)
        ],
        color="green",
        label="15 <= Temperature <= 35",
    )
    sns.histplot(
        x="Temperature",
        data=date_interval_desired[
            (
                (date_interval_desired["Temperature"] > 35)
                & (date_interval_desired["Temperature"] < 40)
            )
            | (
                (date_interval_desired["Temperature"] < 15)
                & (date_interval_desired["Temperature"] > 5)
            )
        ],
        color="yellow",
        label="5 < Temperature < 15 or 35 < Temperature < 40",
    )
    sns.histplot(
        x="Temperature",
        data=date_interval_desired[
            (date_interval_desired["Temperature"] >= 40)
            | (date_interval_desired["Temperature"] <= 5)
        ],
        color="red",
        label="Temperature >= 40 or Temperature <= 5",
    )
    ax.set_xlabel("Temperature")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Chlorophyll")
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(
        x="Chlorophyll",
        data=date_interval_desired[
            (date_interval_desired["Chlorophyll"] <= 0.1)
            & (date_interval_desired["Chlorophyll"] >= -0.1)
        ],
        color="green",
        label="Chlorophyll <= 0.1",
    )
    sns.histplot(
        x="Chlorophyll",
        data=date_interval_desired[
            (date_interval_desired["Chlorophyll"] > 0.1)
            & (date_interval_desired["Chlorophyll"] < 0.5)
        ],
        color="yellow",
        label="0.1 < Chlorophyll < 0.5",
    )
    sns.histplot(
        x="Chlorophyll",
        data=date_interval_desired[(date_interval_desired["Chlorophyll"] >= 0.5)],
        color="red",
        label="Chlorophyll >= 0.5",
        bins=np.arange(0.5, 1, 0.01),
    )
    ax.set_xlabel("Chlorophyll")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Turbidity")
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(
        x="Turbidity",
        data=date_interval_desired[
            (date_interval_desired["Turbidity"] <= 0)
            & (date_interval_desired["Turbidity"] >= -0.2)
        ],
        color="green",
        label="-0.2 <= Turbidity <= 0",
    )
    sns.histplot(
        x="Turbidity",
        data=date_interval_desired[
            (date_interval_desired["Turbidity"] > 0)
            & (date_interval_desired["Turbidity"] < 0.2)
        ],
        color="yellow",
        label="0 < Turbidity < 0.2",
        bins=np.arange(0, 0.2, 0.01),
    )
    ax.set_xlabel("Turbidity")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Salinty")
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(
        x="Salinty",
        data=date_interval_desired[
            (date_interval_desired["Salinty"] >= 0)
            & (date_interval_desired["Salinty"] <= 1)
        ],
        color="yellow",
        label="0 < Salinity < 0.2",
    )
    sns.histplot(
        x="Salinty",
        data=date_interval_desired[(date_interval_desired["Salinty"] < 0)],
        color="red",
        label="Salinity < 0",
        bins=np.arange(-1, 0, 0.01),
    )
    ax.set_xlabel("Salinity")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Dissolved Oxygen")
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(
        x="Dissolved Oxygen",
        data=date_interval_desired[(date_interval_desired["Dissolved Oxygen"] > 6.5)],
        color="green",
        label="Dissolved Oxygen >6.5",
    )
    sns.histplot(
        x="Dissolved Oxygen",
        data=date_interval_desired[
            (date_interval_desired["Dissolved Oxygen"] >= 4)
            & (date_interval_desired["Dissolved Oxygen"] <= 6.5)
        ],
        color="yellow",
        label="4 < Dissolved Oxygen < 6.5",
    )
    sns.histplot(
        x="Dissolved Oxygen",
        data=date_interval_desired[(date_interval_desired["Dissolved Oxygen"] < 4)],
        color="red",
        label="Dissolved Oxygen <4",
    )
    ax.set_xlabel("Dissolved Oxygen")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

    st.subheader("pH")
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(
        x="pH",
        data=date_interval_desired[
            (date_interval_desired["pH"] >= 6.5) & (date_interval_desired["pH"] <= 8.5)
        ],
        color="green",
        label="6.5 < pH < 8.5",
    )
    sns.histplot(
        x="pH",
        data=date_interval_desired[
            ((date_interval_desired["pH"] > 4) & (date_interval_desired["pH"] < 6.5))
            | ((date_interval_desired["pH"] < 11) & (date_interval_desired["pH"] > 8.5))
        ],
        color="yellow",
        label="4 < pH < 6.5 or 8.5 < pH < 11",
    )
    sns.histplot(
        x="pH",
        data=date_interval_desired[
            ((date_interval_desired["pH"] > 11) & (date_interval_desired["pH"] < 14))
            | ((date_interval_desired["pH"] < 4) & (date_interval_desired["pH"] > 1))
        ],
        color="red",
        label="11 < pH < 14 or 1 < pH < 4",
    )
    ax.set_xlabel("pH")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

    st.subheader("Suspended Matter")
    limit = 0.600
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.histplot(
        x="Suspended Matter",
        data=date_interval_desired[date_interval_desired["Suspended Matter"] <= limit],
        color="green",
        label=f"Suspended Matter <= {limit}",
    )
    sns.histplot(
        x="Suspended Matter",
        data=date_interval_desired[date_interval_desired["Suspended Matter"] > limit],
        color="yellow",
        label=f"Suspended Matter > {limit}",
        ax=ax,
    )
    ax.set_xlabel("Suspended Matter")
    ax.set_ylabel("Count")
    ax.legend()
    st.pyplot(fig)

    st.header("Correlations")
    fig, ax = plt.subplots()
    # plt.figure(figsize=(25, 6))
    sns.heatmap(
        date_interval_desired.corr(),
        annot=True,
        cmap=sns.diverging_palette(230, 20, as_cmap=True),
        vmax=0.3,
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
    )
    st.write(fig)

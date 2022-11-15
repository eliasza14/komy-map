import streamlit as st
import geopandas as gpd
import folium
from   streamlit_folium import st_folium
#import leafmap.kepler as leafmap
#import leafmap.colormaps as cm
import leafmap 
APP_TITLE= 'KOMMY MAP VISUALIZATION'
APP_SUB_TITLE='CMT PROOPTIKI 2022'



def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)

    #merge= geopandas.read_file('per_enotites.geojson')
    url='per_enotites.geojson'

    # m = leafmap.Map(center=[50, -110], zoom=2)
    # polygons = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_states.json'
    # m.add_geojson(url, layer_name="Countries")
    # m.add_colormap('Πληθυσμός',width=8.0,height=0.4,orientation='horizontal',vmin=0,vmax=4000,)
    # m.to_streamlit(width=400, height=800)
    
    # m = leafmap.Map()
    # m.add_basemap("OpenTopoMap")
    # m.add_colormap(
    # 'terrain',
    # label="Elevation",
    # width=0.4,
    # height=4,
    # orientation='vertical',
    # vmin=0,
    # vmax=4000,
    # )

    #cm.palettes.dem
    #cm.plot_colormap(colors=cm.palettes.dem, axis_off=True)
    #cm.palettes.ndvi
    #cm.plot_colormap(colors=cm.palettes.ndvi)
    #data = leafmap.examples.datasets.countries_geojson
    m = leafmap.Map()
    m.add_data(
    url, column='Πληθυσμός', scheme='Quantiles', cmap='Blues', legend_title='Population'
    )
    m.to_streamlit(width=400, height=800)

    # m.add_gdf(url, layer_name="Countries")
    # m.to_streamlit(width=400, height=800)

    # m = merge.explore(
    #     location=[40,23],
    #     zoom_start=6,
    #     tiles=None,
    #     column="Πληθυσμός",  # make choropleth based on "BoroName" column
    #     scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
    #     tooltip=columns_view,
    #     popup=columns_view,
    #     cmap="Greens",
    #     legend=True, # show legend
    #     k=10, # use 10 bins
    #     legend_kwds=dict(colorbar=False), # do not use colorbar
    #     name="periferiakes enotites", # name of the layer in the map
    #     show=False
    # )
    # m.to_streamlit(width=400, height=800)

    # merge2= geopandas.read_file('periferies.json')

    # columns_view=['Περιφερειακή Ενότητα','Πληθυσμός', 'ΚΟΜΥ']

    # columns_view2=['Περιφέρεια','Πληθυσμός', 'ΚΟΜΥ']
    # st.write('Breakpoint 1')
    # m = merge.explore(
    #  location=[40,23],
    #  zoom_start=6,
    #  tiles=None,
    #  column="Πληθυσμός",  # make choropleth based on "BoroName" column
    #  scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
    #  tooltip=columns_view,
    #  popup=columns_view,
    #  cmap="Greens",
    #  legend=True, # show legend
    #  k=10, # use 10 bins
    #  legend_kwds=dict(colorbar=False), # do not use colorbar
    # name="periferiakes enotites", # name of the layer in the map
    # show=False)


    # st.write('Breakpoint 2')

    # # merge2.explore(
    # #     m=m, # pass the map object
    # #     location=[40,23],
    # #     column="Πληθυσμός",  # make choropleth based on "BoroName" column
    # #     scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
    # #     tooltip=columns_view2,
    # #     popup=columns_view2,
    # #     legend=True,
    # #     cmap="Blues",
    # #     k=5, # use 10 bins
    # #     legend_kwds=dict(colorbar=False), # do not use colorbar
    # # #     legend_kwds = dict({"loc":"lower right"}),
    # # #      color="red", # use red color on all points
    # # #      marker_kwds=dict(radius=10, fill=True), # make marker radius 10px with fill
    # # #      tooltip="PER", # show "name" column in the tooltip
    # # #      tooltip_kwds=dict(labels=False), # do not show column label in the tooltip
    # #     name="periferies",
    # #     show=False# name of the layer in the map
    # # )

    # folium.TileLayer('Cartodb Positron', overlay=False, control=True).add_to(m)  # use folium to add alternative tiles
    # folium.LayerControl(collapsed=False).add_to(m)  # use folium to add layer control
    # m
    # #st.write('Breakpoint 3')
    # #st.write(m)   
    # st_folium(m)
if __name__ == "__main__":
    main()

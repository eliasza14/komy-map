import streamlit as st
import geopandas
import folium
from   streamlit_folium import st_folium

APP_TITLE= 'KOMMY MAP VISUALIZATION'
APP_SUB_TITLE='CMT PROOPTIKI 2022'



def main():
    st.set_page_config(APP_TITLE)
    st.title(APP_TITLE)

    merge= geopandas.read_file('per_enotites.geojson')



    # merge2= geopandas.read_file('periferies.json')

    columns_view=['Περιφερειακή Ενότητα','Πληθυσμός', 'ΚΟΜΥ']

    columns_view2=['Περιφέρεια','Πληθυσμός', 'ΚΟΜΥ']
    st.write('Breakpoint 1')
    m = merge.explore(
     location=[40,23],
     zoom_start=6,
     tiles=None,
     column="Πληθυσμός",  # make choropleth based on "BoroName" column
     scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
     tooltip=columns_view,
     popup=columns_view,
     cmap="Greens",
     legend=True, # show legend
     k=10, # use 10 bins
     legend_kwds=dict(colorbar=False), # do not use colorbar
    name="periferiakes enotites", # name of the layer in the map
    show=False)


    st.write('Breakpoint 2')

    # merge2.explore(
    #     m=m, # pass the map object
    #     location=[40,23],
    #     column="Πληθυσμός",  # make choropleth based on "BoroName" column
    #     scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
    #     tooltip=columns_view2,
    #     popup=columns_view2,
    #     legend=True,
    #     cmap="Blues",
    #     k=5, # use 10 bins
    #     legend_kwds=dict(colorbar=False), # do not use colorbar
    # #     legend_kwds = dict({"loc":"lower right"}),
    # #      color="red", # use red color on all points
    # #      marker_kwds=dict(radius=10, fill=True), # make marker radius 10px with fill
    # #      tooltip="PER", # show "name" column in the tooltip
    # #      tooltip_kwds=dict(labels=False), # do not show column label in the tooltip
    #     name="periferies",
    #     show=False# name of the layer in the map
    # )

    folium.TileLayer('Cartodb Positron', overlay=False, control=True).add_to(m)  # use folium to add alternative tiles
    folium.LayerControl(collapsed=False).add_to(m)  # use folium to add layer control
    m
    #st.write('Breakpoint 3')
    #st.write(m)   
    # st_folium(m)
    st.to_folium(m)
if __name__ == "__main__":
    main()





# import os
# import geopandas as gpd
# import streamlit as st


# def save_uploaded_file(file_content, file_name):
#     """
#     Save the uploaded file to a temporary directory
#     """
#     import tempfile
#     import os
#     import uuid

#     _, file_extension = os.path.splitext(file_name)
#     file_id = str(uuid.uuid4())
#     file_path = os.path.join(tempfile.gettempdir(), f"{file_id}{file_extension}")

#     with open(file_path, "wb") as file:
#         file.write(file_content.getbuffer())

#     return file_path


# def app():

#     st.title("Upload Vector Data")

#     row1_col1, row1_col2 = st.columns([2, 1])
#     width = 950
#     height = 600

#     with row1_col2:

#         backend = st.selectbox(
#             "Select a plotting backend", ["folium", "kepler.gl", "pydeck"], index=2
#         )

#         if backend == "folium":
#             import leafmap.foliumap as leafmap
#         elif backend == "kepler.gl":
#             import leafmap.kepler as leafmap
#         elif backend == "pydeck":
#             import leafmap.deck as leafmap

#         url = st.text_input(
#             "Enter a URL to a vector dataset",
#             "https://github.com/giswqs/streamlit-geospatial/raw/master/data/us_states.geojson",
#         )

#         data = st.file_uploader(
#             "Upload a vector dataset", type=["geojson", "kml", "zip", "tab"]
#         )

#         container = st.container()

#         if data or url:
#             if data:
#                 file_path = save_uploaded_file(data, data.name)
#                 layer_name = os.path.splitext(data.name)[0]
#             elif url:
#                 file_path = url
#                 layer_name = url.split("/")[-1].split(".")[0]

#             with row1_col1:
#                 if file_path.lower().endswith(".kml"):
#                     gpd.io.file.fiona.drvsupport.supported_drivers["KML"] = "rw"
#                     gdf = gpd.read_file(file_path, driver="KML")
#                 else:
#                     gdf = gpd.read_file(file_path)
#                 lon, lat = leafmap.gdf_centroid(gdf)
#                 if backend == "pydeck":

#                     column_names = gdf.columns.values.tolist()
#                     random_column = None
#                     with container:
#                         random_color = st.checkbox("Apply random colors", True)
#                         if random_color:
#                             random_column = st.selectbox(
#                                 "Select a column to apply random colors", column_names
#                             )

#                     m = leafmap.Map(center=(lat, lon))
#                     m.add_gdf(gdf, random_color_column=random_column)
#                     st.pydeck_chart(m)

#                 else:
#                     m = leafmap.Map(center=(lat, lon), draw_export=True)
#                     m.add_gdf(gdf, layer_name=layer_name)
#                     # m.add_vector(file_path, layer_name=layer_name)
#                     if backend == "folium":
#                         m.zoom_to_gdf(gdf)
#                     m.to_streamlit(width=width, height=height)

#         else:
#             with row1_col1:
#                 m = leafmap.Map()
#                 st.pydeck_chart(m)
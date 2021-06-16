import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from io import StringIO
st.set_page_config(page_title="CSV Plotter", page_icon="📈", layout='wide', initial_sidebar_state='auto')

# PLOTLY TOOLBAR/ BEHAVIOUR

config = dict({
    'scrollZoom': False,
    'displayModeBar': True,
    'editable': True,
    'modeBarButtonsToAdd':  ['drawline',
                            'drawopenpath',
                            'drawclosedpath',
                            'drawcircle',
                            'drawrect',
                            'eraseshape'
                            ],
    'toImageButtonOptions': {'format': 'svg',}
    
})


# SIDEBAR BEHAVIOUR

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 500px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Functions

#   GENERATE REQUEST ITEMS

def generate(df):

    plot_df = pd.DataFrame(Y_s)
    plot_df = plot_df[plot_df["Signal"]!='Not Selected']
    plot_df.reset_index(inplace=True)
    plot_sum = []
   
    if checkbox_plot == True:

        plot = go.Figure()

        for row in range(0,len(plot_df)):
        
            if plot_df["Name"][row] == str():
                Name = plot_df["Signal"][row]
            else:
                Name = plot_df["Name"][row]
            
            if plot_df["Type"][row] == 'lines':
                    plot.add_trace	(go.Scatter (  
                                        x       		= dataframe[symbol_0],
                                        y       		= dataframe[plot_df["Signal"][row]],
                                        name 			= Name,
                                        hovertemplate 	= '%{y:.2f} ',
                                        mode            = 'lines',
                                        line            = dict(color=plot_df["Color"][row], dash=plot_df["Style"][row], width = plot_df["Size"][row]),
                                        yaxis           = plot_df["Axis"][row]
                            )           )

            elif plot_df["Type"][row] == 'markers':
                    plot.add_trace	(go.Scatter (  
                                        x       		= dataframe[symbol_0],
                                        y       		= dataframe[plot_df["Signal"][row]],
                                        name 			= Name,
                                        hovertemplate 	= '%{y:.2f} ',
                                        mode            = 'markers',
                                        marker          = dict(color=plot_df["Color"][row], symbol=plot_df["Style"][row]),
                                        yaxis           = plot_df["Axis"][row]                              
                            )           )

            else:
                    plot.add_trace	(go.Scatter (  
                                        x       		= dataframe[symbol_0],
                                        y       		= dataframe[plot_df["Signal"][row]],
                                        name 			= Name,
                                        hovertemplate 	= '%{y:.2f} ',
                                        mode            = 'lines+markers',
                                        marker          = dict(color=plot_df["Color"][row]),
                                        line            = dict(color=plot_df["Color"][row]),
                                        yaxis           = plot_df["Axis"][row]
                            )           )
            
            max_signal = max(dataframe[plot_df["Signal"][row]])
            min_signal = min(dataframe[plot_df["Signal"][row]])
            mean_signal = np.mean(dataframe[plot_df["Signal"][row]])

            plot_sum.append([Name,plot_df["Signal"][row],max_signal,min_signal,mean_signal])

        plot.update_layout	(
                            title 		= plot_title,
                            xaxis_title = plot_xlabel,
                            yaxis	    = dict(title = plot_y1label),
                            yaxis2	    = dict( 
                                                title       = plot_y2label,
                                                overlaying  = 'y',
                                                side        = 'right'
                                                ),
                            hovermode	= "x",
                            autosize    = True,
                            height      = 720
                            )
                            
        st.plotly_chart(plot, use_container_width=True, config=config)
        plot_summary = pd.DataFrame(plot_sum)
        plot_summary.rename(columns = {0:'Name',1:'Signal',2:"Maximum",3:"Minimum",4:"Mean"}, inplace = True)
        st.table(plot_summary)

    if checkbox_table == True:
        st.subheader("Plotted Data")
        plotted_data = dataframe.loc[:,dataframe.columns.isin(plot_df["Signal"])]
        st.write(plotted_data)

    if checkbox_raw_table == True:
        st.subheader("Raw Data")
        st.write(dataframe)

#    DETERMINE TRACE CONFIGURATIONS

def plotsignals():
    trace_1 = dict([('Signal', symbol_1), ('Name', name_1), ('Axis', axis_1), ('Color', color_1), ('Type', type_1), ("Style", style_1),("Size", size_1) ])
    trace_2 = dict([('Signal', symbol_2), ('Name', name_2), ('Axis', axis_2), ('Color', color_2), ('Type', type_2), ("Style", style_2),("Size", size_2) ])
    trace_3 = dict([('Signal', symbol_3), ('Name', name_3), ('Axis', axis_3), ('Color', color_3), ('Type', type_3), ("Style", style_3),("Size", size_3) ])
    trace_4 = dict([('Signal', symbol_4), ('Name', name_4), ('Axis', axis_4), ('Color', color_4), ('Type', type_4), ("Style", style_4),("Size", size_4) ])
    trace_5 = dict([('Signal', symbol_5), ('Name', name_5), ('Axis', axis_5), ('Color', color_5), ('Type', type_5), ("Style", style_5),("Size", size_5) ])
    return(trace_1,trace_2, trace_3,trace_4,trace_5)

st.title('CSV Plotter')

left_column, right_column = st.beta_columns(2)

st.sidebar.markdown('''<small>v0.1</small>''', unsafe_allow_html=True)

with st.sidebar.beta_expander("📝 To Do"):
    st.write("- Dynamic generation of number of signals depending on amount of colomns in data file")
    st.write("- Plotted data table generation ✔️")
    st.write("- Multi Y axis ✔️")
    st.write("- Rename signal ✔️")
    st.write("- Add functions")
    st.write("- Allow deletion of annotation/shapes")
    st.write("- Export as HTML")
    st.write("- Add Line/maker styles ✔️")
    st.write("- Make .exe")

    
file_uploader = st.sidebar.file_uploader("")

if file_uploader is not None:
    # To read file as bytes:
    bytes_data = file_uploader.getvalue()   
    # To convert to a string based IO:
    stringio = StringIO(file_uploader.getvalue().decode("utf-8"))   
    # To read file as string:
    string_data = stringio.read()   
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(file_uploader)

    Index = np.arange(0, len(dataframe), 1)
    dataframe.insert(0, 'Index', Index)
    symbols = list(dataframe)
    symbols.insert(0, "Not Selected")

    with st.sidebar.beta_expander("X Axis"):
        name_0      = st.text_input("Rename Signal", "", key="name_0")
        symbol_0    = st.selectbox("Symbol", symbols, key="symbol_0")
        fuction_0   = st.multiselect('Functions', ['example:time2frequency'], key="function_0" )

    with st.sidebar.beta_expander("Signal 1"):
        name_1      = st.text_input("Rename Signal", "", key="name_1")
        symbol_1    = st.selectbox("Symbol", symbols, key="symbol_1")
        fuction_1   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_1" )
        
        col_axis, col_type, col_style = st.beta_columns(3)
        axis_1      = col_axis.radio('Axis', ['y1','y2'], key="axis_1")
        type_1      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_1" )
        if type_1 == 'lines':
            style_1    = col_style.selectbox("Style", ["solid", "dot", "dash", "longdash", "dashdot","longdashdot"], key="style_1")
        if type_1 == 'markers':
            style_1    = col_style.selectbox("Style", ["circle", "square", "diamond", "cross", "x","cross-thin","x-thin","triangle-up","triangle-down","triangle-left","triangle-right",'y-up','y-down'], key="style_1")
        
        col_color, col_size = st.beta_columns(2)
        color_1     = col_color.color_picker('Pick a color (Default: #636EFA)','#636EFA', key="color_1")
        size_1      = col_size.number_input("Size", min_value=0.0, max_value=10.0, value=1.0, step=0.5, key="size_1")
        
    with st.sidebar.beta_expander("Signal 2"):
        name_2      = st.text_input("Rename Signal", "", key="name_2")
        symbol_2    = st.selectbox("Symbol", symbols, key="symbol_2")
        fuction_2   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_2" )

        col_axis, col_type, col_style = st.beta_columns(3)
        axis_2      = col_axis.radio('Axis', ['y1','y2'], key="axis_2")
        type_2      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_2" )
        if type_2 == 'lines':
            style_2    = col_style.selectbox("Style", ["solid", "dot", "dash", "longdash", "dashdot","longdashdot"], key="style_2")
        if type_2 == 'markers':
            style_2    = col_style.selectbox("Style", ["circle", "square", "diamond", "cross", "x","cross-thin","x-thin","triangle-up","triangle-down","triangle-left","triangle-right",'y-up','y-down'], key="style_2")
        col_color, col_size = st.beta_columns(2)
        color_2     = col_color.color_picker('Pick a color (Default: #636EFA)','#636EFA', key="color_2")
        size_2      = col_size.number_input("Size", min_value=0.0, max_value=10.0, value=1.0, step=0.5, key="size_2")
        
    with st.sidebar.beta_expander("Signal 3"):
        name_3      = st.text_input("Rename Signal", "", key="name_3")
        symbol_3    = st.selectbox("Symbol", symbols, key="symbol_3")
        fuction_3   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_3" )

        col_axis, col_type, col_style = st.beta_columns(3)
        axis_3      = col_axis.radio('Axis', ['y1','y2'], key="axis_3")
        type_3      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_3" )
        if type_3 == 'lines':
            style_3    = col_style.selectbox("Style", ["solid", "dot", "dash", "longdash", "dashdot","longdashdot"], key="style_3")
        if type_3 == 'markers':
            style_3    = col_style.selectbox("Style", ["circle", "square", "diamond", "cross", "x","cross-thin","x-thin","triangle-up","triangle-down","triangle-left","triangle-right",'y-up','y-down'], key="style_3")
        col_color, col_size = st.beta_columns(2)
        color_3     = col_color.color_picker('Pick a color (Default: #636EFA)','#636EFA', key="color_3")
        size_3      = col_size.number_input("Size", min_value=0.0, max_value=10.0, value=1.0, step=0.5, key="size_3")

    with st.sidebar.beta_expander("Signal 4"):
        name_4      = st.text_input("Rename Signal", "", key="name_4")
        symbol_4    = st.selectbox("Symbol", symbols, key="symbol_4")
        fuction_4   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_4" )

        col_axis, col_type, col_style = st.beta_columns(3)
        axis_4      = col_axis.radio('Axis', ['y1','y2'], key="axis_4")
        type_4      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_4" )
        if type_4 == 'lines':
            style_4    = col_style.selectbox("Style", ["solid", "dot", "dash", "longdash", "dashdot","longdashdot"], key="style_4")
        if type_4 == 'markers':
            style_4    = col_style.selectbox("Style", ["circle", "square", "diamond", "cross", "x","cross-thin","x-thin","triangle-up","triangle-down","triangle-left","triangle-right",'y-up','y-down'], key="style_4")
        col_color, col_size = st.beta_columns(2)
        color_4     = col_color.color_picker('Pick a color (Default: #636EFA)','#636EFA', key="color_4")
        size_4      = col_size.number_input("Size", min_value=0.0, max_value=10.0, value=1.0, step=0.5, key="size_4")

    with st.sidebar.beta_expander("Signal 5"):
        name_5      = st.text_input("Rename Signal", "", key="name_5")
        symbol_5    = st.selectbox("Symbol", symbols, key="symbol_5")
        fuction_5   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_5" )

        col_axis, col_type, col_style = st.beta_columns(3)
        axis_5      = col_axis.radio('Axis', ['y1','y2'], key="axis_5")
        type_5      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_5" )
        if type_5 == 'lines':
            style_5    = col_style.selectbox("Style", ["solid", "dot", "dash", "longdash", "dashdot","longdashdot"], key="style_5")
        if type_5 == 'markers':
            style_5    = col_style.selectbox("Style", ["circle", "square", "diamond", "cross", "x","cross-thin","x-thin","triangle-up","triangle-down","triangle-left","triangle-right",'y-up','y-down'], key="style_5")
        col_color, col_size = st.beta_columns(2)
        color_5     = col_color.color_picker('Pick a color (Default: #636EFA)','#636EFA', key="color_5")
        size_5      = col_size.number_input("Size", min_value=0.0, max_value=10.0, value=1.0, step=0.5, key="size_5")

# Main Layout

# Plot labelling
col_title, col_xlabel, col_y1label, col_y2label = st.beta_columns(4)
plot_title      = col_title.text_input("Plot Title", "", key="plot_title")
plot_xlabel     = col_xlabel.text_input("X Label", "", key="plot_xlabel")
plot_y1label    = col_y1label.text_input("Y1 Label", "", key="plot_y1label")
plot_y2label    = col_y2label.text_input("Y2 Label", "", key="plot_y1label")


# Item Selection
checkbox_plot = st.checkbox('Plot',value = True)
checkbox_table = st.checkbox('Display selected data as table',value = True)
checkbox_raw_table = st.checkbox('Display all data as table')

# Generate

if st.button("Generate"):
    Y_s = plotsignals()
    generate(dataframe)

st.markdown("""---""")
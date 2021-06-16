from re import S
from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from io import StringIO
st.set_page_config(page_title="CSV Plotter", page_icon="📈", layout='wide', initial_sidebar_state='auto')
st.title('CSV Plotter V 0.1')

left_column, right_column = st.beta_columns(2)

# prehaps make a dict?
name_1 = "Name 1"
symbols = "No Data"
symbol_1 = "a"
plot_title = "title"
plot_xlabel = ""
plot_y1label = ""

#Plotly toolbar config
config = dict({
    'scrollZoom': True,
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
        fuction_0   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_0" )

    with st.sidebar.beta_expander("Signal 1"):
        name_1      = st.text_input("Rename Signal", "", key="name_1")
        symbol_1    = st.selectbox("Symbol", symbols, key="symbol_1")
        fuction_1   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_1" )
        col_axis, col_type, col_color = st.beta_columns(3)
        axis_1      = col_axis.radio('Axis', ['Y1','Y2'], key="axis_1")
        type_1      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_1" )
        color_1     = col_color.color_picker('Pick a color (Default: #636EFA)','#636EFA', key="color_1")

    with st.sidebar.beta_expander("Signal 2"):
        name_2      = st.text_input("Rename Signal", "", key="name_2")
        symbol_2    = st.selectbox("Symbol", symbols, key="symbol_2")
        fuction_2   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_2" )
        col_axis, col_type, col_color = st.beta_columns(3)
        axis_2      = col_axis.radio('Axis', ['Y1','Y2'], key="axis_2")
        type_2      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_2" )
        color_2     = col_color.color_picker('Pick a color (Default: #EF553B)','#EF553B', key="color_2")

    with st.sidebar.beta_expander("Signal 3"):
        name_3      = st.text_input("Rename Signal", "", key="name_3")
        symbol_3    = st.selectbox("Symbol", symbols, key="symbol_3")
        fuction_3   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_3" )
        col_axis, col_type, col_color = st.beta_columns(3)
        axis_3      = col_axis.radio('Axis', ['Y1','Y2'], key="axis_3")
        type_3      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_3" )
        color_3     = col_color.color_picker('Pick a color (Default: #00CC96)','#00CC96', key="color_3")

    with st.sidebar.beta_expander("Signal 4"):
        name_4      = st.text_input("Rename Signal", "", key="name_4")
        symbol_4    = st.selectbox("Symbol", symbols, key="symbol_4")
        fuction_4   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_4" )
        col_axis, col_type, col_color = st.beta_columns(3)
        axis_4      = col_axis.radio('Axis', ['Y1','Y2'], key="axis_4")
        type_4      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_4" )
        color_4     = col_color.color_picker('Pick a color (Default: #AB63FA)','#AB63FA', key="color_4")

    with st.sidebar.beta_expander("Signal 5"):
        name_5      = st.text_input("Rename Signal", "", key="name_5")
        symbol_5    = st.selectbox("Symbol", symbols, key="symbol_5")
        fuction_5   = st.multiselect('Functions', ['example:peak2rms','example:rms2peak','example:rollingaverage'], key="function_5" )
        col_axis, col_type, col_color = st.beta_columns(3)
        axis_5      = col_axis.radio('Axis', ['Y1','Y2'], key="axis_5")
        type_5      = col_type.radio('Type', ['lines','markers','lines+markers'], key="type_5" )
        color_5     = col_color.color_picker('Pick a color (Default: #FFA15A)','#FFA15A', key="color_5")

def generate(df):

    plot_df = pd.DataFrame(Y_s)
    plot_df = plot_df[plot_df["Signal"]!='Not Selected']
    plot_df.reset_index(inplace=True)
    plot_sum = []

    if checkbox_plot == True:
        # Plot
        plot = go.Figure()

        for row in range(0,len(plot_df)):  

            if plot_df["Name"][row] != plot_df["Signal"][row]:
                Name = plot_df["Signal"][row]
            else:
                Name = plot_df["Signal"][row]

            if plot_df["Type"][row] == 'lines':
                    plot.add_trace	(go.Scatter (  
                                        x       		= dataframe[symbol_0],
                                        y       		= dataframe[plot_df["Signal"][row]],
                                        name 			= Name,
                                        hovertemplate 	= '%{y:.2f} ',
                                        mode            = 'lines',
                                        line            =dict(color=plot_df["Color"][row])
                            )           )

            elif plot_df["Type"][row] == 'markers':
                    plot.add_trace	(go.Scatter (  
                                        x       		= dataframe[symbol_0],
                                        y       		= dataframe[plot_df["Signal"][row]],
                                        name 			= Name,
                                        hovertemplate 	= '%{y:.2f} ',
                                        mode            = 'markers',
                                        marker          = dict(color=plot_df["Color"][row])                              
                            )           )

            else:
                    plot.add_trace	(go.Scatter (  
                                        x       		= dataframe[symbol_0],
                                        y       		= dataframe[plot_df["Signal"][row]],
                                        name 			= Name,
                                        hovertemplate 	= '%{y:.2f} ',
                                        mode            = 'lines+markers',
                                        marker          = dict(color=plot_df["Color"][row]),
                                        line            = dict(color=plot_df["Color"][row])
                            )           )
            max_signal = max(dataframe[plot_df["Signal"][row]])
            min_signal = min(dataframe[plot_df["Signal"][row]])
            mean_signal = np.mean(dataframe[plot_df["Signal"][row]])

            plot_sum.append([Name,max_signal,min_signal,mean_signal])


        plot.update_layout	(
                            title 		= plot_title,
                            xaxis_title = plot_xlabel,
                            yaxis_title	= plot_y1label,
                            hovermode	= "x",
                            autosize    = True,
                            height      = 720
                            )

        st.plotly_chart(plot, use_container_width=True, config=config)

        plot_summary = pd.DataFrame(plot_sum)
        plot_summary.rename(columns = {0:'Signal',1:"Maximum",2:"Minimum",3:"Mean"}, inplace = True)
        st.table(plot_summary)

    if checkbox_table == True:
        st.subheader("Plotted Data")
        st.write(dataframe)



def plotsignals():
    trace_1 = dict([('Signal', symbol_1), ('Name', name_1), ('Axis', axis_1), ('Color', color_1), ('Type', type_1)])
    trace_2 = dict([('Signal', symbol_2), ('Name', name_2), ('Axis', axis_2), ('Color', color_2), ('Type', type_2)])
    trace_3 = dict([('Signal', symbol_3), ('Name', name_3), ('Axis', axis_3), ('Color', color_3), ('Type', type_3)])
    trace_4 = dict([('Signal', symbol_4), ('Name', name_4), ('Axis', axis_4), ('Color', color_4), ('Type', type_4)])
    trace_5 = dict([('Signal', symbol_5), ('Name', name_5), ('Axis', axis_5), ('Color', color_5), ('Type', type_5)])
    return(trace_1,trace_2, trace_3,trace_4,trace_5)



col_title, col_xlabel, col_ylabel = st.beta_columns(3)
plot_title      = col_title.text_input("Plot Title", "", key="plot_title")
plot_xlabel     = col_xlabel.text_input("X Label", "", key="plot_xlabel")
plot_y1label    = col_ylabel.text_input("Y1 Label", "", key="plot_y1label")

st.markdown("""---""")
checkbox_plot = st.checkbox('Generate Plot')
checkbox_table = st.checkbox('Display Data as Table')

if st.button("Generate"):
    Y_s = plotsignals()
    generate(dataframe)

st.markdown("""---""")
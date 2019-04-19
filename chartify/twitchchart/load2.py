import chartify
import pandas as pd

csvfile = '/home/kevin/py3invm/ChartifyK/Raise_TW_chartify/csv/raiseKK.csv'

chart = chartify.Chart(blank_labels = True, x_axis_type = 'categorical')
chart.plot.bar_stacked(data_frame = csvfile, categorical_columns = 'from', stack_column = 'age', numeric_column = 'tickets', normalize = True)
#normalize=True比例

chart.set_legend_location('outside_bottom')





chart.set_title('raise')
chart.set_subtitle('tickets & year')
chart.axes.set_xaxis_label('age')
chart.axes.set_yaxis_label('tickets')
chart.set_source_label('KK')






chart.show()
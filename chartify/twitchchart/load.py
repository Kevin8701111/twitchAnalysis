import chartify
import pandas as pd

csvfile = '/home/kevin/py3invm/ChartifyK/Raise_TW_chartify/csv/twitch0418.csv'

data = pd.read_csv(csvfile, sep = ',')
print(data.head(9))

# chart = chartify.Chart(x_axis_type = 'log')#1
# chart = chartify.Chart(x_axis_type = 'linear')#2
chart = chartify.Chart(blank_labels=True, x_axis_type='linear')

chart.set_title('Twitch')
chart.set_subtitle('Twitch & games')
chart.axes.set_xaxis_label('rank')
chart.axes.set_yaxis_label('views')
chart.set_source_label('KK')

# chart.axes.set_yaxis_range(0, 4500000)



chart.plot.scatter(data_frame=data, x_column='rownum', y_column='viewers', color_column='name')
# chart.plot.line(data_frame = data, x_column = 'age', y_column = 'tickets', color_column = 'from')#1
# chart.plot.area(data_frame = data, x_column = 'rownum', y_column = 'viewers', color_column = 'name')#2
#line , scatter , area , bar_stacked , heatmap , lollipop , 另外stacked = True可堆疊顯示(area)
#

chart.set_legend_location('outside_bottom')
#移動分類圖例至下方

chart.show()


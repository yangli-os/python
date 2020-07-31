# lua转c格式
主要是使用re库，对lua的代码进行批量处理转化成C格式的代码，练习re的使用，备注较少，读取和写入格式均为txt格式

# 根据文件名筛选文件
name_select.py
使用pytest-shutil库对符合条件的（某段数字范围）的文件复制到另外一个位置
rename.py
通过重命名路径名复制文件，不进行筛选

# save_dict_excel.py
保存一个dict格式的数据到excel，不保留keys

# groupbymm.py
通过groupby方式提取相应列，获取中值，均值等，代替for循环

# translate_pic.py
调用from aip import AipOcr接口识别图片中的文字信息

# draw_pic.py
通过读取excel的数据，批量自适应的画不等宽，但是同等大小的柱状图，并设置图片标签，原始数据还未上传#

# read_time.py
修改时间格式，进行时间提取

# interpret.py
通过scipy.interpolate使用拉格朗日差值对空值进行差值

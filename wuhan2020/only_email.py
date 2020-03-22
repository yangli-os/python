#整理邮箱程序
import pandas as pd
import numpy as np
sourse_path =r"C:\Users\liyang\Desktop\wuhan2020\certificate\志愿者邮箱汇总名单.xlsx"
slack_email = pd.read_json(r"C:\Users\liyang\Desktop\wuhan2020\certificate\users.json")
data_all = pd.read_excel(sourse_path,sheet_name = "信息组")
data_all = data_all[~(data_all.isnull())]
group_list = ["协调组","公众号机器人","宣传组","翻译组","渠道组","风控组","海外团队"]
slack_data = pd.read_excel(sourse_path,sheet_name = "技术组")
with pd.ExcelWriter(sourse_path) as writer:
    data_all.to_excel(writer,"信息组",index=False)
    for group in group_list:
        data = pd.read_excel(sourse_path,sheet_name = group)
        only_email = pd.DataFrame(columns=['姓名（或昵称）', '邮箱（和slack统一）'])
        for email in list(data.values):
            if email[-1] not in list(data_all["邮箱（和slack统一）"]):
                data_all.loc[len(data_all)] = email
                only_email.loc[len(data_all)] = email
                only_email.to_excel(writer,group,index=False)
    profile = slack_email["profile"]
    for pro in profile:
        try:
            if pro["email"] not in list(data_all["邮箱（和slack统一）"]):
                slack_data.loc[len(slack_data)] = ["",pro["email"]]
        except:
            continue
    slack_data.to_excel(writer,"技术组",index=False)

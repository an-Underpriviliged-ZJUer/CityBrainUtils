import pandas as pd
import numpy as np
import random


def get_data(dpAddress, sql):
	url = "http://www.citybrain.org/api/getData"
	data = {"dpAddress": dpAddress, "payload": "{\"selectSql\":\"" + sql + "\"}"}
	resp = requests.post(url=url, headers={"content-type": "application/json"}, json=data)
	result = resp.json()
	data=result["data"]
	
	datalist = data[2:-3].split('=[')
	header_name = datalist[1].split("]")
	header_name_2 = header_name[0].split(',')
	print(header_name_2)
	P = datalist[-1].split(",")
	value_list = []
	for i in range(len(P)):
	    value_list.append(P[i].split(';'))
	
	df4 = pd.DataFrame(data=value_list, columns=header_name_2)
	return df4
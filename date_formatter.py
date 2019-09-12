# Date formatter assuming all dates should be in %d-%m-%y or %d %m %y


def format_date(date_string):
	from datetime import datetime
	possible_sep = [".", "/"]
	for sep in possible_sep:
		if sep in date_string:
			date_string = date_string.replace(sep, "-")
	month_json = {
			'january' 	: '01', 'february' 	: '02', 'march' 	: '03',
			'april' 	: '04', 'may'		: '05', 'june' 		: '06',
			'july'		: '07', 'august'	: '08', 'september'	: '09',
			'october'	: '10', 'november' 	:'11', 'december':'12',
			'jan' : '01','feb' : '02', 'mar' : '03', 'apr' : '04', 'may' : '05',
			'jun' : '06', 'jul' : '07', 'aug' : '08', 'sep' : '09', 'oct' : '10',
			'nov' : '11', 'dec' : '12'
			}
	temp_list = date_string.split(' ')
	if len(temp_list) > 1:
		for i in range(len(temp_list)):
			if temp_list[i].lower() in month_json.keys():
				temp_list[i] = month_json[temp_list[i].lower()]
		date_string = "-".join(temp_list)
	date_obj = datetime.strptime(date_string, '%d-%m-%Y').date()
	print(date_obj)

format_date("24.09.2019")





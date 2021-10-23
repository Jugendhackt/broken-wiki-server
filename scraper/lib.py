def edit_count(history):
    return_dict = {}
    for change in history:
        if change.user in return_dict.keys():
            return_dict[change.user] += 1
        else:
            return_dict.update({change.user: 1})
    return return_dict

def edit_time(history):
    return_dict = {}
    for change in history:
        if change.time.strftime("%d-%m-%Y") in return_dict.keys():
            return_dict[change.time.strftime("%d-%m-%Y")] += 1
        else:
            return_dict.update({change.time.strftime("%d-%m-%Y"): 1})
    return return_dict


import wikipedia_histories

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
        if change.time.strftime("%Y-%m-%d") in return_dict.keys():
            return_dict[change.time.strftime("%Y-%m-%d")] += 1
        else:
            return_dict.update({change.time.strftime("%Y-%m-%d"): 1})
    return return_dict

def edit_major_count(history):
    return_dict = {}
    for change in history:
        # Checks if the change is minor (true) or major (false)
        if not change.get_kind:
            if change.user in return_dict.keys():
                return_dict[change.user] += 1
            else:
                return_dict.update({change.user: 1})
    return return_dict

def edit_minor_count(history):
    return_dict = {}
    for change in history:
        # Checks if the change is minor (true) or major (false)
        if change.get_kind:
            if change.user in return_dict.keys():
                return_dict[change.user] += 1
            else:
                return_dict.update({change.user: 1})
    return return_dict

if __name__ == "__main__":
    search = "AlmaLinux"
    results = wikipedia_histories.get_history(search)
    returned = edit_count(results)
    print(returned) 

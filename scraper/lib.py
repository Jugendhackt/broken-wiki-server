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
        if change.time.strftime("%d-%m-%Y") in return_dict.keys():
            return_dict[change.time.strftime("%d-%m-%Y")] += 1
        else:
            return_dict.update({change.time.strftime("%d-%m-%Y"): 1})
    return return_dict

if __name__ == "__main__":
    search = "AlmaLinux"
    results = wikipedia_histories.get_history(search)
    returned = edit_count(results)
    print(returned) 
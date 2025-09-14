def count_words(text):
    return len(text.split())

def count_caract(text):
    count_results = {} 
    for caract in text.lower():
        count_results[caract]=count_results.get(caract,0)+1
    return count_results

def sort_caract_count(caract_count):
    list_dict=[]
    for caract,count in caract_count.items():
        list_dict.append({"char": caract, "num": count})
    list_dict.sort(key=lambda item:item["num"],reverse=True)
    return list_dict 


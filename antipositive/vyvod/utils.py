def round_array(arr):
    return [round(x, 3) for x in arr]

def convert_array(array):
    converted_array = []
    for item in array:
        converted_item = str(item).replace(".", "")
        converted_item = float(converted_item[:-1])
        converted_array.append(converted_item)
    return converted_array

def convert_array2(array):
    converted_array = []
    for item in array:
        converted_item = float(str(item))
        converted_array.append(converted_item)
    return converted_array


img = 0
char_color_set = [' ', '.', ',', ':', '=', '+', 'b', '#', 'Ж']

symb_width = 8
symb_height = 12

def symb_size(x):
    global symb_width
    global symb_height
    size = [[8, 12], [4, 6], [2, 3]]
    symb_width, symb_height = size[x-1]

def change_color_set(flag):
    global char_color_set
    if(flag):
        char_color_set = [' ', '.', ',', ':', '=', '+', 'b', '#', 'Ж']
    else:
        char_color_set = ['Ж', '#', 'b', '+', '=', ':', ',', '.', ' ']

def color_of_area(char_area_position):
    width, heigh = symb_width, symb_height
    pos_x, pos_y = char_area_position
    full_r, full_g, full_b = 0, 0, 0
    for y in range(heigh):
        for x in range(width):
            getcolor = img.getpixel((pos_x + x, pos_y + y))
            full_r = full_r + getcolor[0]
            full_g = full_g + getcolor[1]
            full_b = full_b + getcolor[2]
    color = full_r + full_g + full_b
    color = color/(width*heigh*3)
    return color

def choose_symbol(color):
    min, result = 255, 0
    length_of_list = len(char_color_set)
    for index in range(length_of_list):
        diff = abs(color - index*32)
        if(diff < min):
            min = diff
            result = index
    return char_color_set[result]

def convert_image_to_text():
    converted_text = ""
    width, heigh = img.size
    for y in range(0, heigh, symb_height):
        if(y + symb_height >= heigh):
            break
        for x in range(0, width, symb_width):
            if(x + symb_width >= width):
                break
            position = (x, y)
            symb = choose_symbol(color_of_area(position))
            converted_text += symb
        converted_text += '\n'
    return converted_text
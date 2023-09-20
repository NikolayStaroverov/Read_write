cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    line=f.readline().strip()
    while line !="":
        list_of_ingredients=[]
        list_ingredient_name = []
        list_quantity = []
        list_measure = []
        dish_name = line
        dish_qty=int(f.readline().strip())
        for i in range(dish_qty):
            list_1=list(f.readline().strip().split('|'))
            ingredient_name=list_1[0]
            quantity=list_1[1]
            measure=list_1[2]
            list_of_ingredients.append(({'ingredient_name': ingredient_name, "quantity": quantity, 'measure': measure}))
        empty_line=f.readline()
        line=f.readline().strip()
        cook_book[dish_name]=list_of_ingredients
print(cook_book)

def get_shop_list_by_dishes(dishes,person_count):
    total_ingredients= {}
    dishes_qty=int(len(dishes))
    for i in range(dishes_qty):
        dish=dishes[i]
        get_list_of_ingredients=[]
        get_list_of_ingredients = list(cook_book.get(dish))
        qty_if_ingredient=len(get_list_of_ingredients)
        for m in range(qty_if_ingredient):
            one_ingredient_dict={}
            one_ingredient=get_list_of_ingredients[m]
            ingredient_name=one_ingredient['ingredient_name']
            one_ingredient_dict['measure']=one_ingredient['measure']
            one_ingredient_dict['quantity'] = int(one_ingredient['quantity'])*person_count
            total_ingredients[ingredient_name]=one_ingredient_dict
    print(total_ingredients)
print(get_shop_list_by_dishes (['Омлет','Запеченный картофель'],2))



Final_File={}
file_names=['1.txt','2.txt','3.txt']
num_of_files=int(len(file_names))
text_dict={}
length_and_text_dict={}
file_name_and_length={}
for i in range(num_of_files):
    with open(file_names[i], encoding='utf-8') as file:
        text=file.readlines()
        number_of_lines=len(text)
        text_dict [file_names[i]] = [number_of_lines,text]
        file_name_and_length[number_of_lines]=file_names[i]
        length_and_text_dict [number_of_lines]= text

file_names_sorted=[]
file_name_and_len_sorted=sorted(file_name_and_length.items())
for i in range(num_of_files):
    file_names_sorted.append(file_name_and_len_sorted[i][1])

def write_to_file (f):
    with open('final.txt', 'a',encoding='utf-8') as final_file:
        final_file.write(f+'\n')
        final_file.write(str(text_dict[f][0])+'\n')
        for LINE in text_dict[f][1]:
            final_file.write(LINE)
        final_file.write('\n')
        final_file.write('\n')
    return

for i in range(num_of_files):
    write_to_file(file_names_sorted[i])

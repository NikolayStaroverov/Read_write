import collections

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
    dishes_dict={}
    dishes_dict=collections.Counter(dishes)
    for i in range(len(dishes_dict)):
        unique_dish=list(dishes_dict.keys())[i]
        get_list_of_ingredients=[]
        get_list_of_ingredients = list(cook_book.get(unique_dish))
        qty_of_ingredient=len(get_list_of_ingredients)
        for m in range(qty_of_ingredient):
            one_ingredient_dict={}
            one_ingredient=get_list_of_ingredients[m]
            ingredient_name=one_ingredient['ingredient_name']
            one_ingredient_dict['measure']=one_ingredient['measure']
            one_ingredient_dict['quantity'] = int(one_ingredient['quantity'])*person_count*dishes_dict[unique_dish]
            total_ingredients[ingredient_name]=one_ingredient_dict
    return total_ingredients

print(get_shop_list_by_dishes (['Омлет','Омлет'],2))



def read_and_sort_files (f1,f2,f3):
    file_names = [f1, f2, f3]
    num_of_files=int(len(file_names))
    file_name_and_length={}
    for i in range(num_of_files):
        with open(file_names[i], encoding='utf-8') as file:
            text=file.readlines()
            number_of_lines=len(text)
            file_name_and_length[number_of_lines]=file_names[i]
    file_name_and_len_sorted=sorted(file_name_and_length.items())
    global file_names_sorted
    file_names_sorted=[]
    for i in range(num_of_files):
        file_names_sorted.append(file_name_and_len_sorted[i][1])
    return file_names_sorted

read_and_sort_files('1.txt','2.txt','3.txt')

def write_to_file (f):
    with open(f, encoding='utf-8') as file:
        text=file.readlines()
    with open('final.txt', 'a',encoding='utf-8') as final_file:
        final_file.write(f+'\n')
        final_file.write(str(len(text))+'\n')
        for LINE in text:
            final_file.write(LINE)
        final_file.write('\n')
        final_file.write('\n')

for i in range(3):
    write_to_file(file_names_sorted[i])

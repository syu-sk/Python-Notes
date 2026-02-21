import json
#Real-World application of json data

with open('donuts.json') as f:
    data = json.load(f)
    with open('donut_menu.txt', 'w') as f:
        f.write('Donut Menu: \n')
        for donut in data:
            f.write(f'''
    -----------------------------
    id {donut['id']}: {donut['name']}
    -----------------------------
    Batters:
    {[item['type'] for item in donut['batters']['batter']]}
    
    Toppings:
    {[item['type'] for item in donut['topping']]}
    -----------------------------
                ''')

#automatic formatting of json data into a human readable menu
#it is possible to quote the 'key of the key' in a dictionary, if another dictionary is nested in it
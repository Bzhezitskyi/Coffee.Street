menu = {
    'американо': 25,
    'латте': 30,
    'капучино': 30,
    'флет уайт': 45,
    'фраппе': 35
}

def order():
    total_cost = 0
    order_list = {}
    
    while True:
        item = input("Введіть назву товару (або 'готово', щоб завершити замовлення): ").lower()
        
        if item == 'готово':
            break
        
        if item not in menu:
            price = float(input("Введіть ціну за одиницю товару: "))
            menu[item] = price
        else:
            price = menu[item]
        
        quantity = int(input("Введіть кількість товару: "))
        cost = price * quantity
        order_list[item] = {'кількість': quantity, 'вартість': cost}
        total_cost += cost
    
    print("\nЗамовлення:")
    for item, details in order_list.items():
        print(f"{item}: {details['кількість']} шт. - {details['вартість']} грн")
    print(f"Загальна вартість: {total_cost} грн")

order()

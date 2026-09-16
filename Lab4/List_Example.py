shopping_list = []
shopping_list.append("Milk")
shopping_list.append("Eggs")
shopping_list.append("Bread")
shopping_list.append("Butter")
shopping_list.append("Cheese")
shopping_list.append(42)
print("Shopping List:", shopping_list)

shopping_list.remove("Cheese")
print("Updated Shopping List:", shopping_list)

shopping_list.pop()
print("Shopping List after popping last item:", shopping_list)
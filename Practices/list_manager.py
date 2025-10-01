# MR 2nd Shopping List Manager

#Put your shopping list variable here
shopping_list= []
while True:
    action = input("\nWhat would you like to do to your shopping list?\nAdd\nRemove\nView\nExit\n").strip().lower()
    print(action)
    
    if action =="Remove" and not shopping_list:
        print("Your shopping list is empty, cannot remove from your list.\n")
    elif action == "add":
        added_item = input("What would you like to add to your shopping list?\n").strip().capitalize()
        shopping_list.append(added_item)
    elif action =="remove":
        removed_item = input("What would you like to remove from your shopping list?\n").strip().capitalize()
        shopping_list.remove(removed_item)
    elif action == "view":
        print("This is your shopping list.\n")
        for x in shopping_list:
            print(x)
    elif action == "exit":
        break
    else:
        print("Please try again.")
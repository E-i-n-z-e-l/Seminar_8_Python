import functions

while True:
	print('1. Нажмите 1 чтобы посмотреть весь справочник \n2. Нажмите 2 чтобы добавить контакт в справочник \n3. Нажмите 3 чтобы найти контакт в справочнике \n4. Нажмите 4, что изменить контакт в справочнике \n5. Нажмите 5 чтобы удалить контакт из справочника ')
	mode = int(input())
	if mode == 1:
		functions.show_data()
	elif mode == 2:
		functions.add_data()
	elif mode == 3:
		functions.find_data()
	elif mode == 4:
		functions.change_data()
	elif mode == 5:
		functions.delete_data()
	else:
		break;



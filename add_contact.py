import User_interface as user

user.get_info()

num = int(input('Если хотите увидеть отображение книги по строкам, нажмите 1, столбцами - 2: '))
if num == 1:
    with open("Phonebook.txt", "r+") as file:
        for idx, line in enumerate(file.readlines(), start=1):
            print(idx, line.strip())










def writing_csv(family, name, phone_number, description):
    with open('Phonebook.xsl', 'a', encoding = 'utf-8') as file:
        file.write(f' family: {family}, \n name: {name}, \n phone_number: {phone_number}, \n description: {description}\n')


def writing_txt(family, name, phone_number, description):
    with open('Phonebook.txt', 'a') as file:
        file.write(f' {family} {name}  {phone_number} {description};\n')




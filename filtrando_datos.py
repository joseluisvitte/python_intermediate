DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #Listas de desarrolladores, adultos y adultos mayores
    all_python_devs = [worker["name"] for worker in DATA if worker ["language"] == "python"] 
    adults = list(filter(lambda worker: worker["age"] >= 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    #extrayendo datos de una lista de diccionarios y añadiendo un nuevo diccionario
    #devolverá un diccionario con el campo old con opciones True o False según sea el caso
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) 
    
    
    #reto (high order functions): Crear listas de desarrolladores python y trabajadores de platzi usando la combinación de filter y map
    python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    python_devs = list(map(lambda worker: worker["name"], python_devs))

    #reto (list comprehensions): adults con list comprehensions
    adultos = [worker["name"] for worker in DATA if worker["age"] >= 18]

    for worker in adultos:
        print(worker)



if __name__ == '__main__':
    run()
DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
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
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Ciancoders',
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
        'position': 'internship',
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
  
  # Comprehensions solutions
  # 1. obtener todos los desarrolladores de python
    
  python_filter = list (filter(lambda x: x['language'] == 'python', DATA))
  print (python_filter)
  
  
  # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
  
  python_age_filter = list (filter(lambda x: x['language'] == 'python' and x['age'] > 20, DATA))
  print(python_age_filter)
  
  
  # 3. obtener todos los trabajadores de ciancoders 
  
  ciancoders = list (filter(lambda x: x['organization'] == 'Ciancoders', DATA))
  print(ciancoders)
  
  
  # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
  
  ciancoders_age = list (filter(lambda x: x['organization'] == 'Ciancoders' and x['age'] > 30, DATA))
  print(ciancoders_age)
  
  
  # 5. obtener todos los trabajadores de mayores de 18 años
  
  age_18 = list (filter(lambda x: x['age'] > 18, DATA))
  print(age_18)
  
  
  # 6. obtener todos los trabajadores de mayores a 70 años
  age_70 = list (filter(lambda x: x['age'] > 70, DATA))
  print(age_70)
  # pass

if __name__ == '__main__':
    run()
    
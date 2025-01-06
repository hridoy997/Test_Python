"""
Write a function that takes the list of the names of the Presidents of a country as a parameter and prints the following things:

* What number is the current President?
* Name of the first President.
* Name of the second to the last President.
* Name of the middle President.
"""

presidents_of_bangladesh = [
    'Sheikh Mujibur Rahman',
    'Syed Nazrul Islam', 
    'Abu Sayeed Chowdhury',
    'Mohammad Mohammadullah',
    'Sheikh Mujibur Rahman',
    'Khondaker Mostaq Ahmad',
    'Abu Sadat Mohammad Sayem',
    'Ziaur Rahman',
    'Abdus Sattar',
    'Ahsanuddin Chowdhury',
    'Hussain Muhammad Ershad',
    'Shahabuddin Ahmed',
    'Abdur Rahman Biswas',
    'Shahabuddin Ahmed',
    'Badruddoza Chowdhury',
    'Muhammad Jamiruddin Sircar',
    'Iajuddin Ahmed',
    'Zillur Rahman',
    'Abdul Hamid'
]

def about_presidents(presidents):
    print(f'The current President is {len(presidents)}th President.')
    print(f'The first President was "{presidents[0]}".')
    print(f'The second to the last President was "{presidents[-2]}".')
    mid_index = len(presidents) // 2
    print(f'The middle President is "{presidents[len(mid_index)]}".')

about_presidents(presidents_of_bangladesh)
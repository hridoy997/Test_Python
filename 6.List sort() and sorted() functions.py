# Sort and sorted the list

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

# sorted the list
# The sorted() method sorts the list temporarily.
sorted_presidents = sorted(presidents_of_bangladesh)
print(sorted_presidents)
print(presidents_of_bangladesh)

# sort the list
# The sort() method sorts the list permanently.
presidents_of_bangladesh.sort()
print(presidents_of_bangladesh)
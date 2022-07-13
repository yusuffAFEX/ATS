from re import U
from this import s


dummy_data = [

    {'firstname': 'Yusuff',
    'lastname': 'Oyedele',
    'date of birth': '11-11-1999',
    'attendance': 11,
    'height': '1.7m',
    'weight': '50kg',
    'age': '22' },
    
    {'firstname': 'Awwal',
    'lastname': 'Adeleke',
    'date of birth': '01-10-1976',
    'attendance': 10,
    'height': '1.5m',
    'weight': '60kg',
    'age': '43'},

    {'firstname': 'Abraham',
    'lastname': 'Adekunle',
    'date of birth': '21-11-1996',
    'attendance': 9,
    'height': '1.8m',
    'weight': '65kg',
    'age': '25'},

    {'firstname': 'Abdulwali',
    'lastname': 'Tajudeen',
    'date of birth': '15-1-1990',
    'attendance': 8,
    'height': '1.4m',
    'weight': '40kg',
    'age': '29'},

    {'firstname': 'Adebusola',
    'lastname': 'Adeyeye',
    'date of birth': '12-11-1996',
    'attendance': 9,
    'height': '1.6m',
    'weight': '55kg',
    'age': '25'},

    {'firstname': 'Basheer',
    'lastname': 'Balogun',
    'date of birth': '11-11-1980',
    'attendance': 7,
    'height': '1.7m',
    'weight': '50kg',
    'age': '40'},

    {'firstname': 'Abdullahi',
    'lastname': 'Salaam',
    'date of birth': '2-7-1994',
    'attendance': 11,
    'height': '1.55m',
    'weight': '53kg',
    'age': '27'},

    {'firstname': 'Faith',
    'lastname': 'Adeosun',
    'date of birth': '11-2-1995',
    'attendance': 5,
    'height': '1.51m',
    'weight': '49kg',
    'age': '26'},

    {'firstname': 'ahmad',
    'lastname': 'sharafudeen',
    'date of birth': '11-10-1993',
    'attendance': 10,
    'height': '1.5m',
    'weight': '50kg',
    'age': '28'},

    {'firstname': 'Lukman',
    'lastname': 'Abisoye',
    'date of birth': '11-11-1998',
    'attendance': 11,
    'height': '1.65m',
    'weight': '56kg',
    'age': '24'},

    {'firstname': 'Toluwanimi',
    'lastname': 'Ogunbiyi',
    'date of birth': '7-11-1960',
    'attendance': 11,
    'height': '1.73m',
    'weight': '50kg',
    'age': '57'},


]



# def attendance_increment(firstname: str):
#     for i in dummy_data:
#         if i['firstname']==firstname:
#             i['attendance'] += 1
#         print(i)

# print(attendance_increment('Ahmad'))


# def update_profile(firstname, new_firstname, new_lastname):
#     for i in dummy_data:
#         if i['firstname']==firstname:
#             i['firstname'] = new_firstname
#             i['lastname'] = new_lastname
#         print(i)

# print(update_profile('Ahmad', 'Adeniyi', 'Sharaf'))


def full_names():
    all_names = []
    for i in dummy_data:
        all_names.append(i['firstname']+' '+i['lastname'])
        # all_names.append(i['lastname'])
    return all_names


print(full_names())







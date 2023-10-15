contacts = {
    'number': 4,
    'students':
        [
            {'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
            {'name': 'Harry potter', 'email': 'harry_potter@example.com'},
            {'name': 'bob german', 'email': 'bob@example.com'},
            {'name': 'ron miller', 'email': 'ron@example.com'}
        ]

}

print('Student Emails: ')
for student in contacts['students']:
    print(student['email'])

    
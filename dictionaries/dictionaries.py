course = {'teacher':'ash', 'title':'intor', 'level':'begg'}

print(course['teacher'])
print(course.keys())
print(course.values())
print(sorted(course.keys()))

course['teacher'] = 'Teasurer'
print(course)

# del(course['title'])

for key, value in course.items():
    print(key, value)


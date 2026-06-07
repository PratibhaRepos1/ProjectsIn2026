# CORE STRING OPERATIONS: INDEXING, SLICING, CONCATENATING

message = 'GenAI is amazing!'

print(message[0])
print(message[5])

print('Version: ' + str(4.0))

separator = '🤖'

print(separator * 5)

tech = 'Machine Learning'
#String[start:stop]
print(tech[0:7])

print(tech[:7])
print(tech[8:])

# my_string = 'GenAI'
# my_string[0] = 'x'

# print(my_string)

a, b = '1', '2'
print(a + b * 3)

print('Python 3!!!'[:7:2])

mac = 'b4:6d:83:77:85:f3'
print(mac[-1] + mac[:2])

# COMMON STRING METHOD

model_ouput = 'ai IS the future of everything!'
print(model_ouput.upper())
print(model_ouput.lower())

response = ' 🤖 Hello, human! 🤖 '
print(response.strip())
print(response.strip(' 🤖 '))

new_text = 'ML is a critical component of modern AI. ML techniques are advancing rapidly.'
updated_text = new_text.replace('ML', 'Machine Learning')
print(updated_text)
print(updated_text.count('Machine Learning'))
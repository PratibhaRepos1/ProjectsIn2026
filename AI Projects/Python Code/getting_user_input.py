# GETTING USER INPUT

# command = input('Ask your AI assistant a question: ')
# print('Your question was: ', command)

# training_hours = input('Enter hours spent training the model: ')
# print('Data type of training_hours:', type(training_hours))

iterations = input('Enter the number of model iterations: ')
iterations = int(iterations)

datasets = input('Enter the number of datasets: ')
datasets = int(datasets)

total = iterations * datasets

print('Total processing unit: ', total)



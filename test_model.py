import pickle

pipe = pickle.load(open('pipe.pkl', 'rb'))

print(pipe.predict([[1, 'female', 25, 0, 0, 500, 'S']]))
print(pipe.predict([[3, 'male', 40, 0, 0, 10, 'S']]))
print(pipe.predict([[1, 'female', 5, 1, 2, 100, 'C']]))
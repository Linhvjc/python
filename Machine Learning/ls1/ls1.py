
from sklearn import tree

# Step 1: collect data
# Step 2: handle data
# Step 3: Training model
# Step 4: Predict result
# Step 5: Evaluate the effective of the model

my_tree = tree.DecisionTreeClassifier()

feature = [[1,3,3,7],
            [5,2,4,6],
            [1,2,4,6],
            [5,4,4,3],
            [1,4,4,7],
            [3,2,3,7],
            [3,3,3,6],
            [5,2,2,7]]
label = [0,1,1,0,0,0,0,1]

model = my_tree.fit(feature, label)

result = model.predict([[1,4,3,6]])
import numpy as np

# Assuming you have already defined y_test and y_predict arrays

# Combining actual and predicted values side by side
result = np.column_stack((y_test, y_predict))

# Printing the Results
print("Actual Values | Predicted Values")
print("------------------------")
for actual, predicted in result:
    print(f"{actual:12.2f} | {predicted:14.2f}")

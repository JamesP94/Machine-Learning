# Regression Tree
![Regression Tree](assets\regression_tree.png)
peruse01 <= 6.5 terminal node says that if you have a new data instance with a peruse01 value of 6.5 or less, the regression tree suggests that the expected outcome is very close to 6.92, with a small range of variation around this prediction due to the low squared error

peruse03 <= 5.5 terminal node says that if you have a new data instance with a peruse03 value of 5.5 or less, the regression tree suggests that the expected outcome is very close to 6.56, with a small range of variation around this prediction due to the low squared error

pereou02 <= 6.5 terminal node says that if you have a new data instance with a pereou02 value of 6.5 or less, the regression tree suggests that the expected outcome is very close to 6, with a small range of variation around this prediction due to the low squared error.


# Classification Tree
![Classification Tree](assets\classification_tree.png)
This tree seems overfit, many of the nodes in the survivor side of the tree hold a very low percentage (some none) of the actual data in them.

![Pruned Classification Tree](assets\pruned_classification_tree.png)
After pruning the tree, the survivor side of the tree is more evenly distributed among the nodes and quite honestly, it just makes more intuitive sense when interpreting it than the classification tree that isn't pruned.
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/696BHbim)
# Classification ICE
To submit, please perform the following:
1. Save a script file for Python with the following name: `ice_lastname_firstname.py` where lastname is your last name and firstname is your first name.
1. Save your plots to the directory `assets`.
1. Link the images of your plots from `assets` to `submission.md` where appropriate.
1. Answer questions in `submission.md`.
1. Push your assignment to GitHub.

## Regression trees
For this portion of the exercise, use the [reduction_data_new.txt](/data/reduction_data_new.txt) file. Create a regression tree using `intent01` as the target variable. Perform the following tasks:
* For this tree, you can use 3 to 5 predictor variables. Create a plot for your tree. (3 pts.)
* Assess the output of your tree and choose three terminal nodes to explain what they mean; i.e. interpret the results of those nodes.  (2 pts.)

The dataset is a survey assessing the potential adoption of a new operating system within an organization. Each variable in the dataset is a statement assessed on a scale ranging from "Strongly Disagree" to "Strongly Agree." Thus, each employee selected a value for each statement. The following are the statements (with the variable name) the employees assessed:
* `peruse01`: Using the operating system would enable me to accomplish tasks more quickly. 
* `peruse02`: Using the operating system would improve my performance. 
* `peruse03`: Using the operating system would increase my productivity. 
* `peruse04`: Using the operating system would enhance my effectiveness. 
* `peruse05`: Using the operating system would make it easier to do my job. 
* `peruse06`: I would find the operating system useful in my job.
* `pereou01`: Learning to operate the operating system would be easy for me.
* `pereou02`: I would find it easy to get the operating system to do what I want it to do. 
* `pereou03`: My interaction with the operating system would be clear and understandable.
* `pereou04`: I would find the operating system to be flexible to interact with. 
* `pereou05`: It would be easy for me to become skillful at using the operating system. 
* `pereou06`: I would find the operating system easy to use. 

## Classification trees
Use the [titanic_data.txt](/data/titanic_data.txt) file for the classification tree. Use the variable `Survived` as the target variable for the tree. Perform the following tasks:
* Provide the plot for the tree and have a minimum of 5 levels (2 pts.)
  * Interpret the tree (1 pt.)
* Prune the tree and restrict it to just 3 levels (2 pts.)
  * Does a pruned tree perform better? Justify.
## K-Nearest Neighbors

In this assignment we explore the KNN algorithm on data from the Dram Shop. This repo contains two files for you to apply KNN to. The file `knn-training-data.txt` holds a specific subset of Dram customer data. The data has the following fields: 

* `customer_id`: a unique ID for the customer
* `most_popular_category`: the most popular category for the customer
* `relationship_days`: the number of days between the first and last transaction for the customer.
* `total_spend`: the lifetime total spend by the customer
* `beverage_categories`: the number of distinct beverage categories the customer has purchased from.
* `segment`: a four-level categorical variable that segments the customers.

Using the course materials and class discussion, determine a distance metric between customers. Use this metric to implement a k-nearest neighbor algorithm. You don't need to do any systematic testing of `k`, but I'd recommend picking something larger than 10 since we have four categories. 

The file `knn-testing-data.txt` holds data with the segments removed. Use your algorithm to apply segments to this data. I've included the file `testing-true-values.txt` so that you can measure your accuracy. Don't be despondent if your accuracy is low on this assignment. 

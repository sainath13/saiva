[[Database]]
# Difference Between Views and Materialized Views in PL/SQL  |  GeeksforGeeks
Last Updated : 05 Nov, 2024

In PL/SQL views play an important role in data accessibility, data manipulation, and query optimization. ****Views**** help restrict the user's data, which is not supposed to be accessed by a particular user. Views are instrumental in securing data by restricting the visibility of specific fields or rows based on user permissions.

The two main types of views in Oracle PL/SQL are standard ****Views**** and ****Materialized Views****. Each type has unique properties, functions, and use cases, making it essential to understand when to apply one over the other.

In this article, we'll examine the differences between Views and Materialized Views, including their properties, syntax, and practical implementations.

What Are Views and Materialized Views in PL/SQL?
------------------------------------------------

Views and Materialized Views help to form a layer of abstraction over the database table which restricts user's accessibility and manipulation of data. The major difference between Views and Materialized Views is that Views are ****dynamic**** (show the latest data) and materialized views are ****static**** (show data from last refresh). Let's look into the concept of Views and Materialized views.

### 1\. Views

Views are the virtual table of the dataset which are created by executing ****SELECT**** query in ****SQL****. It acts as an actual relation. Views do not get stored in physical memory instead it returns original and updated data from the table every time it is accessed. The important thing to know about views is that if we make any changes in the original table, it will also get reflected in the views table. We can generate virtual tables or views as per our data requirements.

****Syntax:****

```
CREATE VIEW view_name AS
SELECT column1, column2,...
FROM table_name
WHERE condition;
```


### 2\. Materialized View

****Materialized views**** also act as a virtual table but in this, the result of the query is stored in physical memory and the stored result of the query reduces the need for repeated computations and helps to enhance the query performance. They can also be considered as a physical copy of the original database which helps in the warehousing of data. Unlike Views, they are not updated every time they are accessed. If we want to update Materialized View then we need to do it manually with the help of some trigger.

****Syntax:****

```
CREATE MATERIALIZED VIEW materialized_view_name
AS
SELECT column1, column2, ...
FROM table_name
[WHERE condition]
[GROUP BY columns]
[ORDER BY columns]
```


Examples
--------

### Example 1: Creating a View

To create a view in SQL, first, let's take a database table named ****"employees"****. This table shows the employee data such as their ID, name, department, and salary. We want to create a view that displays only the employee ID, name, and department of the employees where the department is ****"IT"****.

![Employees-database-table](https://media.geeksforgeeks.org/wp-content/uploads/20240301120348/Employees-database-table.png)

Employees database table

Now, to create a ****view**** we will execute the below query:

```
CREATE VIEW employee_view AS
SELECT emp_id, emp_name, emp_salary
FROM employees
WHERE department = 'IT';
```


We have successfully created a view named ****employee\_view**** that displays the employee ID, name, and department for all employees. To show the view in a database table we will use below mentioned query:

```
SELECT * FROM employee_view;
```


****Output:****

![Output-of-querying-the-'employee_view'](https://media.geeksforgeeks.org/wp-content/uploads/20240301120142/Output-of-querying-the-'employee_view'.png)

Output of querying the 'employee\_view'

### Example 2: Creating Materialized View

To create a Materialized View, first, we'll take a database table named ****"sales"**** which has sales data such as product ID and quantity sold. Then we will create a materialized view named ****sales\_mv**** that contains the product ID and total sales for each product.

![Sales Database Table](https://media.geeksforgeeks.org/wp-content/uploads/20240301120226/Sales-Database-Table.png)

Sales Database Table

  
Now, to create a ****materialized view**** we will execute the below query:

```
CREATE MATERIALIZED VIEW sales_mv AS
SELECT product_id, SUM(quantity_sold) AS total_sales
FROM sales
GROUP BY product_id;
```


To show the result of querying materialized view:

```
SELECT * FROM sales_mv;
```


****Output:****

![Output-of-querying-the-sales_mv](https://media.geeksforgeeks.org/wp-content/uploads/20240301120300/Output-of-querying-the-sales_mv.png)

Output of querying the sales\_mv

Key Differences between Views and Materialized Views
----------------------------------------------------

* Properties: Data Storage
  * Views: It does not store data in physical memory.
  * Marginalized View: It stores data physically and helps to reduce repeated computations.
* Properties: Data Freshness
  * Views: It always returns the updated and original data from the base table.
  * Marginalized View: It does not reflect the updated data and needs to be refreshed.
* Properties: Query Performance
  * Views: It is dynamic which results in slow query performance.
  * Marginalized View: It is static and provides fast query performance as it stores data in physical memory.
* Properties: Storage Overhead
  * Views: Minimum because it only stores query definition.
  * Marginalized View: Additional storage overhead because it stores data physically.
* Properties: Usage
  * Views: It is suitable for real-time and frequent data access.
  * Marginalized View: It is suitable for less frequent changing data.
* Properties: Maintenance
  * Views: It does not need any manual maintenance for updates in data.
  * Marginalized View: It does require manual refreshing for data updates.


When to Use Views vs. Materialized Views
----------------------------------------
Choosing between Views and Materialized Views depends on your use case:

*   ****Use Views**** when you need real-time access to updated data, such as in transactional systems or real-time dashboards.
*   ****Use Materialized Views**** when you prioritize performance over freshness, especially in data warehousing scenarios or for complex aggregations.

Conclusion
----------
Views and Materialized Views both are important tools in data abstraction and data manipulation. Views are dynamic which means they always return the updated and original data whereas Materialized Views are static which only provide the last refreshed data. Both are used for data abstraction as per the situation of the user due to their different functionalities. By understanding the difference between these two we can effectively use them for data abstraction in ****PL/SQL****.



# Differences Between Views and Materialized Views in SQL | GeeksforGeeks
Last Updated : 02 Dec, 2024

When working with databases, ****views**** and ****materialized views**** are important tools for ****managing data**** effectively. Both have their ****unique characteristics****, ****advantages**** and use cases. Understanding the differences can help us choose the best option for our ****requirements****.

In this article, we will cover ****detailed explanations****, ****practical examples****, ****clear outputs and key differences between view and materialized view**** for ****better understanding****.

Key Differences Between Views and Materialized Views
----------------------------------------------------

Following are the differences between the view and table:

| Feature              | View                                                                 | Materialized View                                                            |
| -------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Definition**       | A virtual table created from a query; doesn't store data physically. | Stores the results of a query physically for faster retrieval.               |
| **Data Storage**     | Only the query is stored; result set is generated dynamically.       | Query results are stored physically, using additional storage.               |
| **Performance**      | Slower for complex queries; results computed on access.              | Faster as results are precomputed and stored.                                |
| **Update Behavior**  | Automatically reflects changes in base tables.                       | Needs manual or automatic refresh to stay updated.                           |
| **Storage Cost**     | No additional storage cost.                                          | Requires extra storage for saved query results.                              |
| **Maintenance Cost** | No maintenance cost; always reflects current data.                   | Requires maintenance to refresh data periodically.                           |
| **SQL Standards**    | Fully standardized and widely supported.                             | Not fully standardized; varies across database systems.                      |
| **Use Cases**        | Best for infrequent access needing up-to-date values.                | Ideal for frequent access and performance-critical scenarios like analytics. |


What is a View in SQL?
----------------------

A [View](https://www.geeksforgeeks.org/sql-views/) is a ****virtual relation**** that acts as an ****actual relation****. It is not a part of ****logical relational model**** of the database system. It is a ****virtual table**** created by a [SQL query](https://www.geeksforgeeks.org/sql-concepts-and-queries/). It dynamically fetches data from the underlying tables whenever accessed, without storing the ****data physically**** in the ****database****.

### ****Characteristics of Views****

*   ****Dynamic Execution:**** Data is generated each time the view is accessed.
*   ****No Physical Storage:**** Views only store the query definition.
*   ****No Storage or Update Cost:**** Since no data is stored, no additional costs are involved.
*   ****Use Cases:**** Useful for simplifying complex queries, enhancing data security, and creating a logical layer for specific users.

****Syntax****

```
CREATE VIEW view_name AS  
SELECT column1, column2, ...  
FROM table_name  
WHERE condition;
```


****What is a Materialized View in SQL?****
-------------------------------------------

A ****materialized view**** stores the ****result of a query**** physically in the database. It can be refreshed manually or automatically to ****reflect updates**** in the underlying tables. The process of keeping the [materialized views](https://www.geeksforgeeks.org/materialization-view-in-dbms/) updated is known as ****view maintenance****. Database system uses one of the three ways to keep the materialized view updated:

*   Update the materialized view as soon as the relation on which it is defined is updated.
*   Update the materialized view every time the view is accessed.
*   Update the materialized view periodically.

### ****Characteristics of Materialized Views****

*   ****Physical Storage:**** Stores query results for faster data retrieval.
*   ****Refresh Options:**** Can be refreshed immediately, on-demand, or periodically.
*   ****Performance Benefits:**** Improves query performance for frequently accessed or large datasets.
*   ****Storage and Update Costs:**** Requires additional space and incurs overhead for maintaining data consistency.

****Syntax****

```
CREATE MATERIALIZED VIEW materialized_view_name  
BUILD [IMMEDIATE | DEFERRED]  
REFRESH [FAST | COMPLETE | FORCE]  
ON [COMMIT | DEMAND]  
AS  
SELECT column1, column2, ...  
FROM table_name  
WHERE condition;
```


Conclusion
----------

Both ****views**** and ****materialized views**** are powerful tools in ****SQL**** for ****managing**** and ****optimizing**** data. While views are ****ideal**** for ****creating dynamic****, ****virtual tables**** for occasional use, ****materialized views**** are better suited for scenarios requiring frequent access to precomputed results. By understanding their differences and use cases, we can improve our [database design](https://www.geeksforgeeks.org/database-design-in-dbms/) and performance.
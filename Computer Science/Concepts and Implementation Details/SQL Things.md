OLTP ===> OnLine Transaction Processing 
			Small queries, Quick response times
			 Small Responses as well
OLAP ===> OnLine Analytics Processing
			 Big aggregations, big responses, big Response times as well

Clustered VS non Clustered.
Clustered ==> store data physically close and together!
	Quick to access. 
	 Only one such index can be there

Non clustered 
	Multiple such indices can be there
	 Logical order for data. Physical order remains unchanged
	 Consists of a sorted list of values, along with pointers back to the physical rows in the data table
	 Each non-clustered index contains the indexed column data, along with a pointer (row locator) to the actual data row.
	 
![[sql_join.jpg]]



- A **correlated** subquery cannot be considered as an independent query, but it can refer to the column in a table listed in the FROM of the main query.
- A **non-correlated** subquery can be considered as an independent query and the output of the subquery is substituted in the main query.

### What are Constraints in SQL?

Constraints are used to specify the rules concerning data in the table. It can be applied for single or multiple fields in an SQL table during the creation of the table or after creating using the ALTER TABLE command. The constraints are:

- **NOT NULL** - Restricts NULL value from being inserted into a column.
- **CHECK** - Verifies that all values in a field satisfy a condition.
- **DEFAULT** - Automatically assigns a default value if no value has been specified for the field.
- **UNIQUE** - Ensures unique values to be inserted into the field.
- **INDEX** - Indexes a field providing faster retrieval of records.
- **PRIMARY KEY** - Uniquely identifies each record in a table.
- **FOREIGN KEY** - Ensures referential integrity for a record in another table.


Normalization represents the way of organizing structured data in the database efficiently.

Denormalization is the inverse process of normalization, where the normalized schema is converted into a schema that has redundant information. The performance is improved by using redundancy and keeping the redundant data consistent. The reason for performing denormalization is the overheads produced in the query processor by an over-normalized structure.



Normalization:

First Normal Form :
A relation is in first normal form if every attribute in that relation is a **single-valued attribute**. 
Books issued : Until the Day I Die (Emily Carpenter), Inception (Christopher Nolan)
to
Books issued :
Until the Day I Die (Emily Carpenter)
Inception (Christopher Nolan)

![[Pasted image 20250610133859.png]]


Second Normal Form
A relation is in second normal form if it satisfies the conditions for the first normal form and does not contain any partial dependency. A relation in 2NF has **no partial dependency**, i.e., it has no non-prime attribute that depends on any proper subset of any candidate key of the table. Often, specifying a single column Primary Key is the solution to the problem.

![[Pasted image 20250610133928.png]]


Third Normal Form : 
A relation is said to be in the third normal form, if it satisfies the conditions for the second normal form and there is **no transitive dependency** between the non-prime attributes, i.e., all non-prime attributes are determined only by the candidate keys of the relation and not by any other non-prime attribute.


Truncate - : Truncate data, keep table schema
Delete - : delete certain rows
Drop - : drop everything , schema too

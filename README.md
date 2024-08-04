
In this project, we'll take on the role of an analyst for a chain of retail stores. The chief financial officer has tasked us with creating a study that explores the chain's sales performance over the past few years across all categories.

We'll start by exploring the available data, then we'll perform a series of analyses to look at sales, profitability, and other metrics by segment and over time. At the end of the project, we'll have a complete report in the form of an Excel workbook.

As with most analytics projects, not all the data you'll need to complete the project is available in a single dataset. The superstore.xlsx workbook contains three worksheets: orders, people, and returns. It consists of records on sales, products, and so forth of a fictitious retail company. There are three tables available in the workbook:

orders table:
- row_id: unique row identifier
- order_id: unique order identifier
- order_date: date the order was placed
- ship_date: date the order was shipped
- ship_mode: how the order was shipped
- customer_id: unique customer identifier
- customer_name: customer name
- segment: segment of product
- country: country of customer
- city: city of customer
- state: state of customer
- postal_code: postal code of customer
- region: Superstore region represented
- product_id: unique product identifier
- category: category of product
- sub_category: subcategory of product
- product_name: name of product
- sales: total sales of that product in the order
- quantity: total units sold of that product in the order
- discount: percent discount applied for that product in the order
- profit: total profit for that product in the order

people table:
- region: name of region
- person: name of region's supervisor

returns table:
- order_id: unique order identifier
- returned: TRUE indicates the order was returned
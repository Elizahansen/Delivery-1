CREATE VIEW EmployeeSales AS
    SELECT 
        employee.employee_id,
        SUM(orders.unitprice * orders.quantity) AS sold
    FROM
        employee
            LEFT JOIN
        orders ON employee.employee_id = orders.employee_id
    GROUP BY employee.employee_id;

create VIEW CustomerOrders AS
    SELECT 
        customers.customer_id, first_name, last_name,
        SUM(orders.unitprice * orders.quantity) AS customerorder
    FROM
        customers
            LEFT JOIN
        orders ON customers.customer_id = orders.customer_id
    GROUP BY customers.customer_id, first_name, last_name
    order by customerorder desc;

Create VIEW CategorySales as
    SELECT 
        products.productname,
        SUM(orders.product_id * orders.quantity) AS quantity_sold,
        products.type1 AS producttype
    FROM
        products
            INNER JOIN
        orders ON products.product_id = orders.product_id
    GROUP BY products.product_id, producttype
    ORDER BY quantity_sold DESC;
    
CREATE VIEW Top5products AS
    SELECT 
        quantity_sold, product_id
    FROM
        categorysales
    ORDER BY quantity_sold DESC
    LIMIT 5;

CREATE VIEW Top5customers AS
    SELECT 
        customerorder, customer_id
    FROM
        customerorders
    ORDER BY customerorder DESC
    LIMIT 5;
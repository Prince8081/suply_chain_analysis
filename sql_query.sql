create database supply_chain_analysis;
use supply_chain_analysis;

select count(*) from delivery_person ;
select count(*) from location ;
select count(*) from orders;

----- Total Orders Placed -----

SELECT 
    COUNT(*) AS total_orders
FROM
    orders;


     -- Orders by City --

SELECT 
    city , COUNT(id) AS total_orders
FROM
    orders
GROUP BY city
ORDER BY total_orders desc;


-- Rename column -- 

ALTER TABLE orders 
CHANGE `time_taken(min)` time_taken_min BIGINT;


-- Average Delivery Time by City --

SELECT 
    city, ROUND(AVG(time_taken_min), 2) AS avg_delivery_time
FROM
    orders
GROUP BY city
ORDER BY avg_delivery_time DESC;


-- Average Delivery Time by Weather --

SELECT 
    weatherconditions,
    ROUND(AVG(time_taken_min), 2) AS avg_delivery_time
FROM
    orders
GROUP BY weatherconditions
ORDER BY avg_delivery_time DESC; 


-- Impact of Traffic on Delivery Time --

SELECT 
    road_traffic_density,
    ROUND(AVG(time_taken_min), 2) AS avg_delivery_time
FROM
    orders
GROUP BY 1
ORDER BY 2 DESC;


-- Festival Impact on Delivery Time --

SELECT 
    festival, ROUND(AVG(time_taken_min), 2) AS avg_delivery_time
FROM
    orders
GROUP BY 1
ORDER BY 2 DESC;


-- Top 5 Fastest Delivery Persons -- 

SELECT 
    delivery_person_id,
    ROUND(AVG(time_taken_min), 2) AS avg_delivery_time
FROM
    delivery_person
        JOIN
    orders ON delivery_person.id = orders.id
GROUP BY 1
ORDER BY 2 asc limit 5 ;


-- Average Delivery Person Age & Rating by City --

SELECT 
    city,
    ROUND(AVG(delivery_person_age), 1) AS avg_age,
    ROUND(AVG(delivery_person_ratings),2) AS avg_rating
FROM
    delivery_person
        JOIN
    orders ON delivery_person.id = orders.id
GROUP BY 1;


 -- Orders per Type of Order --
 
SELECT 
    type_of_order, COUNT(id) AS orders
FROM
    orders
GROUP BY 1;



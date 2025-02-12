
  
    

  create  table "galp_project"."public"."yearly_average__dbt_tmp"
  
  
    as
  
  (
    WITH yearly_data AS (
    SELECT 
        DATE_PART('year', date) AS year,
        AVG(open) AS avg_open,
        AVG(high) AS avg_high,
        AVG(low) AS avg_low,
        AVG(close) AS avg_close,
        AVG(adjusted_close) AS avg_adjusted_close,
        AVG(volume) AS avg_volume,
        AVG(dividend_amount) AS avg_dividend
    FROM public.monthly_adjusted_data
    GROUP BY year
    ORDER BY year
)
SELECT * FROM yearly_data
  );
  
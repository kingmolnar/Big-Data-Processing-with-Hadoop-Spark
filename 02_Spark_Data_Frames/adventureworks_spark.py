if not 'sqlCtx' in vars():
   sqlCtx = SQLContext(sc)

Employees_df = sqlCtx.read.format('com.databricks.spark.csv')\
    .options(header=True, inferschema=True)\
    .load('/user/pmolnar/data/AdventureWorks/Employees.csv.gz')

Territory_df = sqlCtx.read.format('com.databricks.spark.csv')\
    .options(header=True, inferschema=True)\
    .load('/user/pmolnar/data/AdventureWorks/SalesTerritory.csv.gz')

Orders_df = sqlCtx.read.format('com.databricks.spark.csv')\
    .options(header=True, inferschema=True)\
    .load('/user/pmolnar/data/AdventureWorks/ItemsOrdered.csv.gz')

Customers_df = sqlCtx.read.format('com.databricks.spark.csv')\
    .options(header=True, inferschema=True)\
    .load('/user/pmolnar/data/AdventureWorks/Customer.csv.gz')


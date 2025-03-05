# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "164abf49-996f-4f15-9a22-60c20c06843e",
# META       "default_lakehouse_name": "NYCLakehouse",
# META       "default_lakehouse_workspace_id": "731d745e-c3f7-4b62-b85f-66635649366e",
# META       "known_lakehouses": [
# META         {
# META           "id": "164abf49-996f-4f15-9a22-60c20c06843e"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM NYCLakehouse.Bronze LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

IDS706_DataEngineering_BarbaraFlores_Miniproject11
# 📂 Data Pipeline with Databricks

The primary purpose of this project is to design and develop an efficient data pipeline using Databricks. This pipeline should integrate data sources and destinations, emphasizing the designer's ability to perform extraction, transformation, and loading (ETL) tasks effectively. The focus is on ensuring the efficiency and scalability of the pipeline, along with the proper configuration of data sources and destinations.

## 📌 References

This project is guided by the official [Databricks Data Pipeline documentation](https://docs.databricks.com/en/getting-started/data-pipeline-get-started.html). Please refer to this documentation for detailed information and best practices.

## 🎵 Dataset

In this project, we will use a dataset suggested as an example in the Databricks documentation. This dataset is a subset of the Million Song Dataset, containing features and metadata for contemporary music tracks. You can access this dataset in the [sample datasets](https://docs.databricks.com/en/dbfs/databricks-datasets.html#databricks-datasets-databricks-datasets) included in the Databricks workspace.

## 🛠️ Project Workflow Steps
The steps carried out to execute this project are:

### Step 1: Create a cluster

For the data processing and analysis conducted in this example, a cluster was established to provide the essential computing resources for command execution. This cluster creation is fundamental for efficiently running Databricks commands, ensuring seamless operations throughout the data pipeline.

![00](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/00.png)

### Step 2: Explore the source data
To learn how to use the Databricks interface to explore raw source data, commands from Databricks Utilities and PySpark were executed in a notebook. The goal was to examine both the source data and associated artifacts.

Data exploration took place in the notebook [Explore songs data.py](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/blob/main/Explore%20songs%20data.py).

![01](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/01.png)

### Step 3: Ingest Raw Data
In this step, the raw data is loaded into a table to make it accessible for subsequent processing. However, during our data exploration, we noticed that the header is not stored with the data. Therefore, it becomes necessary to explicitly define the schema, as demonstrated in the following example.

![02](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/02.png)

### Step 4: Prepare the raw data

![03](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/03.png)

### Step 5: Query the transformed data

![04](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/04.png)


![05](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/05.png)

### Step 6: Create a Databricks job to run the pipeline
![06](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/06.png)

![07](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/07.png)

### Step 7: Schedule the data pipeline job

![08](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Miniproject11/main/images/08.png)



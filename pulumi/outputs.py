import pulumi
from pulumi_azure_native import streamanalytics

def create_table_storage_output():
    return streamanalytics.StreamOutput(
        "myOutput",
        resource_group_name="your_resource_group_name",
        streaming_job_name="your_streaming_job_name",
        serialization=streamanalytics.JsonOutputSerializationArgs(type="LineSeparated"),
        datasource=streamanalytics.AzureTableStorageStreamOutputDataSourceArgs(
            account_name="your_table_storage_account_name",
            table_name="your_table_name",
            account_key="your_account_key",
        ),
    )
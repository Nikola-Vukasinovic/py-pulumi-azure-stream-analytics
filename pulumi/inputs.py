import pulumi
from pulumi_azure_native import streamanalytics

def create_iot_hub_input():
    return streamanalytics.StreamInput(
        "myInput",
        resource_group_name="your_resource_group_name",
        streaming_job_name="your_streaming_job_name",
        serialization=streamanalytics.JsonInputSerializationArgs(type="LineSeparated"),
        datasource=streamanalytics.IoTHubStreamInputDataSourceArgs(
            iot_hub_name="your_iot_hub_name",
            shared_access_policy_name="your_shared_access_policy_name",
            shared_access_policy_key="your_shared_access_policy_key",
        ),
    )
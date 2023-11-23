"""An Azure RM Python Pulumi program - Create Stream Analytics Service in Azure"""

import pulumi
from pulumi.stream_analytics import StreamingJob
from pulumi.inputs import create_iot_hub_input
from pulumi.outputs import create_table_storage_output
from pulumi_azure_native import resources, streamanalytics

simple_query = False

if (not simple_query):
    location = "West Europe"

    query = """
        SELECT 
            id,
            sl_id,
            m_id,
            ts,
            d,
            [key],
            mdbs_a,
            data
        INTO output
        FROM iothub
    """
    # Create an Azure Stream Analytics Job
    stream_analytics_job = streamanalytics.StreamingJob(
        resource_name = "pqaStreamTest",
        output_error_policy = "Drop",
        location = location,
        resource_group_name= "test_group",
        sku = streamanalytics.SkuArgs(
            name="Standard",
            ),
        transformation = streamanalytics.TransformationArgs(
            name = "test",
            query = query,
            streaming_units = 1,
            )
        )

    pulumi.export("stream_analytics_job_name", stream_analytics_job.name)

else:
    from pulumi.inputs import create_iot_hub_input
    from pulumi.outputs import create_table_storage_output
    
    # Select the appropriate query file
    query_file = "./pulumi/queries/query.sql"
    with open(query_file, "r") as file:
        query = file.read()

    # Create Azure Stream Analytics Input (Azure IoT Hub)
    stream_analytics_input = create_iot_hub_input()

    # Create Azure Stream Analytics Output (Azure Table Storage)
    stream_analytics_output = create_table_storage_output()

    # Create an Azure Stream Analytics Job
    stream_analytics_job = StreamingJob(
        "myStreamAnalyticsJob",
        resource_group_name="your_resource_group_name",
        location="your_location",
        sku={"name": "Standard"},
        transformation={
            "name": "test",
            "query": query,
            "streaming_units": 1,
        },
        inputs=[{"inputName": "myInput", "input": stream_analytics_input}],
        outputs=[{"outputName": "myOutput", "output": stream_analytics_output}],
    )

    pulumi.export("stream_analytics_job_name", stream_analytics_job.name)
    

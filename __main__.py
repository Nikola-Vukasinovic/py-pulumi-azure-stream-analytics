"""An Azure RM Python Pulumi program - Create Stream Analytics Service in Azure"""

import pulumi
from pulumi_azure_native import resources, streamanalytics

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

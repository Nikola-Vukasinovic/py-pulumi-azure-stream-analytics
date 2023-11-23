import pulumi
from pulumi_azure_native import streamanalytics
from pulumi.stream_analytics import StreamingJob


class StreamingJob(pulumi.ComponentResource):
    def __init__(self, resource_name, query, inputs, outputs, **kwargs):
        super().__init__("custom:pulumi:StreamingJob", resource_name, {}, **kwargs)

        self.stream_analytics_job = streamanalytics.StreamingJob(
            resource_name,
            output_error_policy="Drop",
            location=kwargs.get("location", "West Europe"),
            resource_group_name=kwargs.get("resource_group_name", "test_group"),
            sku=streamanalytics.SkuArgs(name="Standard"),
            transformation=streamanalytics.TransformationArgs(
                name=kwargs.get("transformation_name", "test"),
                query=query,
                streaming_units=kwargs.get("streaming_units", 1),
            ),
            inputs=inputs,
            outputs=outputs,
            opts=pulumi.ResourceOptions(parent=self),
        )

        self.register_outputs({"stream_analytics_job_name": self.stream_analytics_job.name})
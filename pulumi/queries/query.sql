/*Message Type 1*/
SELECT IoTHub.ConnectionDeviceId
    , EventProcessedUtcTime
    , Entity
    , [Values].[key]
    , [Values].value
    , [Values].ts

INTO 
    [booldata]
FROM 
    [input] TIMESTAMP BY [Values].ts
WHERE MsgType=1 /*AND LAG([Values].[ts]) OVER (PARTITION BY Entity, [Values].[key] LIMIT DURATION(hour, 7)) != [Values].[ts]*/
/*Message Type 2*/
/* Disable due to maximum number of recievers limitation
SELECT IoTHub.ConnectionDeviceId
    , EventProcessedUtcTime
    , Entity
    , [Values].[key]
    , [Values].value
    , [Values].ts

INTO 
    [bigintdata]
FROM 
    [input] TIMESTAMP BY [Values].ts
WHERE MsgType=2 /*AND LAG([Values].[ts]) OVER (PARTITION BY Entity, [Values].[key] LIMIT DURATION(hour, 7)) != [Values].[ts]*/

*/
/*Message Type 3*/
SELECT IoTHub.ConnectionDeviceId
    , EventProcessedUtcTime
    , Entity
    , [Values].[key]
    , [Values].value
    , [Values].ts

INTO 
    [floatdata]
FROM 
    [input] TIMESTAMP BY [Values].ts
WHERE MsgType=3 /*AND LAG([Values].[ts]) OVER (PARTITION BY Entity, [Values].[key] LIMIT DURATION(hour, 7)) != [Values].[ts]*/

/*Test Duration*/
SELECT IoTHub.ConnectionDeviceId
    , EventProcessedUtcTime
    , Entity
    , [Values].[key]
    , DATEDIFF(
		second,
		LAST([Values].[ts]) OVER (PARTITION BY Entity, [Values].[key] LIMIT DURATION(hour, 24) WHEN [Values].[value]=1),
		[Values].ts) as duration,
    [Values].ts


INTO [durationdata]
   
FROM [input] TIMESTAMP BY [Values].ts
WHERE MsgType=1 /*AND [Values].value=0 AND LAG([Values].[ts]) OVER (PARTITION BY Entity, [Values].[key] LIMIT DURATION(hour, 7)) != [Values].[ts]*/

/*
Store float values into AZ Table Storage - Gen2 Data Lake
*/

SELECT TRIM(Entity) AS PartitionKey
    ,CONCAT_WS('|',[Values].[key],GetMetadataPropertyValue(Input, 'EventId'),[Values].ts) AS RowKey
    ,GetMetadataPropertyValue(Input, 'EventId') AS EventId
    ,[Values].[key] 
    ,[Values].value 
    ,[Values].ts 
INTO [datalaketablestorage]
FROM [Input] TIMESTAMP BY [Values].ts
WHERE MsgType=3

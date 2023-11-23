Create & deploy azure stream analytics resource with Py & Pulumi

# Deploy Azure Stream Analytics

This is example of helper code stack for fast deployment of Stream Analytics service in Azure. Biggest advantage of using Pulumi is ease of use and rich API when working with Azure services.

## Prerequisites

Working with Python version 3.7 or later.

Pulumi >=3.0.0, <=4.0.0.

pulumi-azure-native >=2.0.0, <=3.0.0.

## Installation of Pulumi

Install Pulumi

```
pip install pulumi
```

New azure-python project

```
pulumi new azure-python
```

Last step just spin it up with

```
pulumi up
```

When done with the resource it can be deleted with

```
pulumi destroy
```

## Multiple stacks

Pulumi supports multiple stacks (dev, stage, prod etc.)

You can see stacks with

```
pulumi stack ls
```

For more information plese see [stacks](https://www.pulumi.com/docs/concepts/stack/)

## Pulumi Authentication

In order to enable Pulumi to interact with you're Azure subscription there are multiple options to register you're py-pulumi app with Azure.

For fast setup you can use **Azure CLI** but preffered way is to use authentication with **Service Principal.**

### **Azure CLI**

How to install Azure CLI please follow [link](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

On you're terminal just use

```
az login
```

When logged in you need to configure pulumi to use azure cli with:

```
pulumi config set cloud:useAzureCli true
```

### Service Principal

There are multiple resources on this topic so you can follow this to find out more about Service Principal authentication of the apps [link](https://learn.microsoft.com/en-us/cli/azure/azure-cli-sp-tutorial-1?tabs=bash)

Create new application

1. In the left navigation pane, click on "Azure Active Directory."
2. Under "App registrations," click on "New registration."
3. Provide a name for your application, select the appropriate account type, and enter a redirect URI if required. Click "Register."
4. Note down the "Application (client) ID" and "Directory (tenant) ID" from the overview page. These will be needed for configuring Pulumi.

Add client secret


1. In the left navigation pane, click on "Certificates & Secrets."
2. Under "Client secrets," click on "New client secret." Enter a description, choose an expiry period, and click "Add."
3. Note down the value of the client secret immediately. This will be needed for configuring Pulumi.

Adjust permissions


1. In the left navigation pane, click on "API permissions."
2. Ensure that your application has the necessary permissions to manage Azure resources. If needed, click on "Add a permission" and grant the required permissions.

### Configure Pulumi with Azure Credentials

```
pulumi config set azure:clientId <Application (client) ID>
pulumi config set azure:clientSecret <Client Secret>
pulumi config set azure:tenantId <Directory (tenant) ID>
pulumi config set azure:subscriptionId <Your Azure Subscription ID>
```

On the end of the configuration confirm settings with

```
pulumi up
```

## **Pulumi Secrets**

Another great aspect of Pulumi is built-in secret manger. You can store and retrieve secrets with:

```
pulumi config set myApiKey <your-secret-api-key>
```

In you're program to retrieve the secret you can do:

```python
import pulumi

config = pulumi.Config()

# Access the secret
api_key = config.require_secret("myApiKey")

# Use the secret in your infrastructure definition
# (Replace this with the actual resource where the secret is needed)
my_resource = SomeResource(name="example", api_key=api_key)
```

## Stream Analytics Query

Being declared as subset of T-SQL syntax it really looks and feels familiar and apart from stream settings like handling late arrival events, dropping conditions etc. this is the foundation of the service.

Feel free to see detailed documentation on [link](https://learn.microsoft.com/en-us/stream-analytics-query/stream-analytics-query-language-reference).

## Stream Analytics Inputs & Outputs

One of the appealing side when starting an IoT adventure is mature enviroment of inputs and ouputs on Azure that can be easily connected with stream analytics. Do pretty complex things in the stream and sink it somewhere.

**Inputs**

Example and throught the repo's you will find inputs addressing Azure IoT Hub since this is my main source of information in my projects but it can be easily ported to Event Hubs and even more interesting integration is use of topics with blob storage and Data Lake storage but this won't be addressed here.

For the inputs more information can be found [here](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-define-inputs).

**Outputs**

For detailed overview of vaiable outputs please see [outputs](https://learn.microsoft.com/en-us/azure/stream-analytics/stream-analytics-define-outputs).

When working with IoT projects it has been accepted at least from my side three very attractive outputs in regular use case like SQL Database and Table storage.

Selection of output reflects project needs for additional processing of gathered data. Ofcourse this falls in the realm of service architecture where usually there is a split in hot and cold path. Cold path being the cheaper one and larger one (like blob storage and table storage) and more "interactive" and expensive one like SQL DB. Apart from these two I have tested and used PoweBI as direct output in creating IoT dashboard of incoming data in one of the data paths.

### Simple query insert * into sink

In the main branch is the most simplified version that relies on "manul" creation of the inputs & outputs. This is how I've used it since on many occasions needed custom configration of the inputs and ouputs can be more easily done when testing "by hand" then for code. 

Query can be submitted as string or read from .sql file. The latter is preferred way since it gives you ability to track changes and be flexible about it.

Query selects columns from my input data coming from IoT Hub, the data is from simple Modubs device that is sending electrical energy measurements. Output was configured as Table storage to test te ingestion.

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

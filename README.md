This project serves to demonstrate an ImportError thrown in the uamqp module when it runs in Azure Functions.

To run:
 - Create a new Azure DevOps project, and import this repo
 - Create an Azure Function with a Python 3.9 runtime, and Linux operating system
 - Create an App Registration to be used by the deployment pipeline, and update azure-pipelines.yaml with the ID
 - Run the pipeline

Invocation traces for the function should show failure, with the cause being an ImportError in the uamqp module.

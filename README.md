<span style=" font-family: 'Consolas';font-size:14px">

# **Flask Web POC Application Deployment with AKS using Terraform CICD**

## **Application Overview**

- The Flask application consists of a simple **"Hello world POC"** page that demonstrates proper communication with a PostgreSQL database hosted on Azure.<br></br>

- The repository contains the code and configuration files for deploying a Flask web application with Kubernetes on Azure.<br></br>
- The deployment process includes Helm charts for application deployment and Terraform for provisioning Kubernetes infrastructure.

## **Folder Structure of Application**

POC_Application_Repo/
│
├── application/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── helm-chart/
│   ├── Chart.yaml
│   ├── templates/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── _helpers.tpl
│   ├── values.yaml
│   └── templates.yaml
│
└── terraform/
    ├── main.tf
    ├── variables.tf
    └── .github/
        └── workflows/
            └── ci-cd.yaml

## **Application Structure**

- **app.py:** Python script defining the Flask web application and its routes.<br></br>

- **requirements.txt:** List of Python dependencies for the Flask application.<br></br>

- **Helm Chart:**<br></br>
  
  - The Helm chart (flask-app) defines the Kubernetes resources required for deploying the Flask application.<br></br>
  
- **Chart Structure:**<br></br>

    - **Chart.yaml:** Metadata about the Helm chart.<br></br>
  
    - **values.yaml:** Default configuration values for the Helm chart.<br></br>
  
    - **deployment.yaml:** Kubernetes Deployment resource for deploying the Flask application.<br></br>
  
    - **service.yaml:** Kubernetes Service resource for exposing the Flask application.<br></br>
  
    - **secret.yaml:** Kubernetes Secret resource for storing database credentials.<br></br>
    
- **Terraform:**<br></br>

  - The Terraform configuration provisions the Kubernetes cluster on Azure.<br></br>
  
- **Terraform Files**:<br></br>

    - **main.tf:** Defines the Azure resources, including the Kubernetes cluster.<br></br>
  
    - **variables.tf:** Declares input variables for Terraform configuration.<br></br>

    - **outputs.tf:** Declares output variables for Terraform configuration.<br></br>
  
- **CI/CD Pipeline:**<br></br>

    - The CI/CD pipeline automates the deployment process using GitHub Actions.<br></br>
  
## **Pipeline Steps**

  - **Build Docker Image:** Builds and pushes the Docker image to Azure Container Registry.<br></br>

  - **Deploy with Helm:** Deploys the Flask application using Helm.<br></br>

  - **Provision Infrastructure:** Provisions Kubernetes infrastructure using Terraform.<br></br>

## **Prerequisites**

- Before deploying the application, ensure the following prerequisites are met:<br></br>
  
- **Azure Account:** You need an active Azure account to provision resources.<br></br>

  - **Azure Resource Group:** Create an Azure resource group where the Kubernetes cluster will be deployed. You can use the Azure CLI or the Azure portal to create the resource group.<br></br>

  - **Azure Container Registry (ACR):** Set up an Azure Container Registry to store Docker images. This registry will be used to store the Docker images of your application.<br></br>
  
  - **PostgreSQL Database:** Provision a PostgreSQL database instance. You can use Azure Database for PostgreSQL or any other compatible database service. Make sure to note down the connection details, including the host, port, database name, username, and password.<br></br>

## **Setup Instructions**

- Follow these steps to deploy the application:<br></br>

    - **Configure Azure Credentials:** Set up Azure credentials with appropriate permissions. This can be done using Azure CLI or by creating a service principal.<br></br>

    - **Create Kubernetes Cluster:** Use Terraform to create an AKS (Azure Kubernetes Service) cluster. Update the **main.tf file** with your Azure credentials and desired configurations.<br></br>

    - **Deploy Helm Chart:** Use Helm to deploy the application to the Kubernetes cluster. Update the Helm chart values file (**values.yaml**) with the necessary configurations, including database connection details.<br></br>

    - **Run CI/CD Pipeline:** Push your changes to the main branch to trigger the Terraform CI/CD pipeline. This pipeline will apply the Terraform configurations to provision the AKS cluster.<br></br>

    - **Access the Application:** Once deployed, access the application using the external IP provided by the Azure Load Balancer. You should see the **"Hello world POC"** page indicating **successful communication with the database**.<br></br>

## **Notes**

- Ensure that all sensitive information, such as database credentials, are stored securely and not exposed in version-controlled files.<br></br>

- Regularly review and update your Terraform configurations to match any changes in your infrastructure requirements.
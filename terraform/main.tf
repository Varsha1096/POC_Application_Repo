provider "azurerm" {
  features {}
}

# Define variables
variable "resource_group_name" {
  description = "The name of the resource group in which to create the AKS cluster."
  type        = string
  default     = "pocapplicationresource"
}

variable "location" {
  description = "The Azure region where the resources will be deployed."
  type        = string
  default     = "East US"
}

# Create AKS cluster
resource "azurerm_kubernetes_cluster" "aks" {
  name                = "pocapplicationdeploy"  # Updated cluster name
  location            = var.location
  resource_group_name = var.resource_group_name
  dns_prefix          = "pocapplicationcluster"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_DS2_v2"
  }

  identity {
    type = "SystemAssigned"
  }
}

# Output AKS cluster name
output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.aks.name  # Update output to use the resource attribute
}
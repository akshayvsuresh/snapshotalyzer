variable "project_id" {
  type        = string
  description = "The ID of the project where this VPC will be created"
  default     = ""
}

variable "prefix" {
  type        = string
  description = "The ID of the project where this VPC will be created"
  default     = ""
}


variable "iap_firewall_name" {
  type        = string
  description = "IAPFirewall name "
  default     = ""
}

variable "nat_ip" {
  type        = string
  description = "Nat IP "
  default     = ""
}

variable "vpc_name" {
  type        = string
  description = "The name of the network being created"
  default     = ""
}
variable "network_name" {
  type        = string
  description = "The name of the network being created"
  default     = ""
}
variable "environment" {
  type        = string
  description = "The name of the environment"
  default     = ""
}
variable "region" {
  type        = string
  description = "The name of the region"
  default     = ""
}
variable "vpc_routing_mode" {
  type        = string
  description = "The network routing mode (default 'GLOBAL')"
  default     = ""
}
variable "external_subnet" {
  type        = string
  description = "The external subnet name"
  default     = ""
}
variable "internal_subnet" {
  type        = string
  description = "The internal subnet name"
  default     = ""
}
variable "external_subnet_cidr" {
  type        = string
  description = "The external subnet cidr range"
  default     = ""
}
variable "internal_subnet_cidr" {
  type        = string
  description = "The internal subnet cidr range"
}
variable "pod_ip_cidr_range" {
  type        = string
  description = "The pod ip cidr range"
}
variable "service_ip_cidr_range" {
  type        = string
  description = "kubernetes service cidr range"
}
variable "master_ipv4_cidr_block" {
  type        = string
  description = "The IP range in CIDR notation to use for the hosted master network"
}
variable "nat_name" {
  type        = string
  description = "The name of cloud nat"
  default     = ""
}
variable "router_name" {
  type        = string
  description = "The name of cloud router "
  default     = ""
}
variable "cluster_name" {
  type        = string
  description = "The name of GKE cluster"
  default     = ""
}
variable "zones" {
  type        = list(string)
  description = "The zones to host the cluster in (optional if regional cluster / required if zonal)"
  default     = []
}
variable "default_max_pods_per_node" {
  description = "The maximum number of pods to schedule per node"
  default     = 110
}
variable "node_type" {
  type        = string
  description = "Node instance type"
  default     = ""
}
variable "node_locations" {
  type        = string
  description = "Node locations"
  default     = ""
}
variable "node_min_count" {
  description = "The minimum count of nodes"
  default     = ""
}
variable "node_max_count" {
  description = "The maximum count of nodes"
  default     = ""
}

variable "num_management_instances" {
  description = "Number of bastion instances"
}
variable "bastion_instance_name" {
  type        = string
  description = "Name of bastion instances"
  default     = ""
}
variable "bastion_template_name" {
  type        = string
  description = "bastion template name"
  default     = ""
}
variable "istio_enabled" {
  type        = string
  description = "istio enabled or not"
  default     = ""
}
variable "sa_gke" {
  type        = string
  description = "service account for gke"
  default     = ""
}
variable "sa_bastion" {
  type        = string
  description = "service account for bastion"
  default     = ""
}

variable "zone" {
  type    = string
  default = ""
}

variable "tier" {
  description = "The tier of the redis instance."
  type        = string
}



variable "mem_size" {
  description = "The memory size of the redis instance."

}

variable "redis_version" {
  description = "The version of redis."
  type        = string

}

variable "location_id" {
  description = "The location ID of Redis."
  type        = string

}


variable "redis_display_name" {
  description = "The display name of redis."
  type        = string

}


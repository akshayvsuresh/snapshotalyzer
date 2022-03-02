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

module "vpc" {
  source = "../../../shared-modules/terraform-google-network"

  project_id   = var.project_id
  network_name = "${var.prefix}-vpc"
  routing_mode = var.vpc_routing_mode

  subnets = [
    {
      subnet_name      = "${var.prefix}-public-subnet"
      subnet_ip        = "${var.external_subnet_cidr}"
      subnet_region    = var.region
      subnet_flow_logs = "true"
    },
    {
      subnet_name           = "${var.prefix}-private-subnet"
      subnet_ip             = "${var.internal_subnet_cidr}"
      subnet_region         = var.region
      subnet_private_access = "true"
      subnet_flow_logs      = "true"
    },
  ]

  secondary_ranges = {
    "${var.prefix}-private-subnet" = [
      {
        range_name    = "${var.prefix}-private-subnet-pod"
        ip_cidr_range = "${var.pod_ip_cidr_range}"
      },
      {
        range_name    = "${var.prefix}-private-subnet-service"
        ip_cidr_range = "${var.service_ip_cidr_range}"
      },
    ]
  }
}

provider "google" {
}
resource "google_storage_bucket" "bucket" {
  name     = "${var.google_storage_bucket}"
  location = "${var.region}"
  project = var.project_id
}

resource "google_storage_bucket_object" "archive" {
  name   = "${var.google_storage_bucket_object}"
  bucket = google_storage_bucket.bucket.name
  source = "/Users/benfrancis/terraform-build/cloud-function/index.zip"
  
}


  resource "google_cloudfunctions_function" "function" {
  name        = "${var.name}-function"
  region      = "${var.region}"
  description = "cloud function by terraform "
  runtime     = "python38"
  project = var.project_id

  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  trigger_http          = true
  entry_point           = "${var.function_entry_point}"
  labels = {
      my-labels = "${var.labels}"
  }
  
}


# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name
  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "churn_data" {
  bucket = "customer-churn-bucket"
  acl    = "private"
}

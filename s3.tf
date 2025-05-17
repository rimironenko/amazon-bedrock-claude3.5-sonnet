#################################################
# S3 bucket for the Bedrock Knowledge Base source
#################################################

module "vector_store_input_bucket" {
  source  = "terraform-aws-modules/s3-bucket/aws"
  version = "4.2.2"

  bucket        = "bedrock-rag-vector-store-${random_pet.this.id}"
  force_destroy = true

  tags = var.aws_resource_tags

}

resource "aws_s3_object" "object" {
  bucket     = module.vector_store_input_bucket.s3_bucket_id
  key        = "postgresql-16-A4.pdf"
  source     = "documents/postgresql-16-A4.pdf"
  etag       = filemd5("documents/postgresql-16-A4.pdf")
  depends_on = [module.vector_store_input_bucket]
}
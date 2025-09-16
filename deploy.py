import boto3
import sagemaker
from sagemaker.model import Model

# Replace with your details
role = "<YOUR-IAM-ROLE-ARN>"
ecr_image = "<YOUR-ECR-IMAGE-URI>"

# Create model object
model = Model(image_uri=ecr_image, role=role)

# Deploy model as endpoint
predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.t2.micro"  # free-tier
)

# Test API call
runtime = boto3.client("sagemaker-runtime")
response = runtime.invoke_endpoint(
    EndpointName=predictor.endpoint_name,
    ContentType="application/json",
    Body='{"word": "speling"}'
)
print(response["Body"].read().decode())

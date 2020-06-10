STACK_NAME=recicly

stack:
	@sam build \
		--template cloudformation/template.yaml

	@sam package \
		--s3-bucket recicly-artifacts-bucket \
		--s3-prefix sam/$(STACK_NAME) \
		--template-file .aws-sam/build/template.yaml \
		--output-template-file cloudformation/packaged.yaml

	@sam deploy \
		--capabilities=CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset \
		--stack-name=$(STACK_NAME) \
		--template-file=cloudformation/packaged.yaml

	@rm -f cloudformation/packaged.yaml


resources:
	@aws cloudformation describe-stack-resources \
		--stack-name=$(STACK_NAME) \
		--query='StackResources[].{LogicalResourceId: LogicalResourceId, PhysicalResourceId: PhysicalResourceId, ResourceStatus: ResourceStatus}' \
		--output=table

status:
	@aws cloudformation describe-stacks \
		--stack-name=$(STACK_NAME) \
		--query='Stacks[].Outputs[].{OutputKey: OutputKey, Description: Description, OutputValue: OutputValue}' \
		--output=table

events:
	@aws cloudformation describe-stack-events \
		--stack-name=$(STACK_NAME) \
		--query='StackEvents[].{LogicalResourceId: LogicalResourceId, ResourceType: ResourceType, ResourceStatus: ResourceStatus}' \
		--output=table

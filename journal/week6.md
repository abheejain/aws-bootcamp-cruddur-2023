# Week 6 — Deploying Containers


**Preparation**:
- Make sure we can connect to the RDS using PROD_CONNECTION_URL adding the `test` script
- revert back to `CONNECTION_URL` 

- Task Flask Script
- Update `app.py` for `health-check`
- Flask Folder - script

- Running script 
```
<urlopen error [Errno 111] Connection refused>
```

- Create Cloudwatch Group using AWS CLI, name `cruddur`
```
aws logs create-log-group --log-group-name cruddur
aws logs put-retention-policy --log-group-name cruddur --retention-in-days 1
```
## Varification image




## Provision ECS Cluster
- Create ECS Cluster using AWS CLI
```
aws ecs create-cluster \
 --cluster-name cruddur \
 --service-connect-defaults namespace=cruddur
```
## Verification 
Log
```
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:ap-southeast-1:530454120249:cluster/cruddur",
        "clusterName": "cruddur",
        "status": "PROVISIONING",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "statistics": [],
        "tags": [],
:...skipping...
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:ap-southeast-1:530454120249:cluster/cruddur",
        "clusterName": "cruddur",
        "status": "PROVISIONING",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "statistics": [],
        "tags": [],
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ],
        "capacityProviders": [],
        "defaultCapacityProviderStrategy": [],
        "attachments": [
            {
                "id": "a6e63d39-86c7-4544-8064-347f69574fbf",
:...skipping...
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:ap-southeast-1:530454120249:cluster/cruddur",
        "clusterName": "cruddur",
        "status": "PROVISIONING",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "statistics": [],
        "tags": [],
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ],
        "capacityProviders": [],
        "defaultCapacityProviderStrategy": [],
        "attachments": [
            {
                "id": "a6e63d39-86c7-4544-8064-347f69574fbf",
                "type": "sc",
:...skipping...
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:ap-southeast-1:530454120249:cluster/cruddur",
        "clusterName": "cruddur",
        "status": "PROVISIONING",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "statistics": [],
        "tags": [],
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ],
        "capacityProviders": [],
        "defaultCapacityProviderStrategy": [],
        "attachments": [
            {
                "id": "a6e63d39-86c7-4544-8064-347f69574fbf",
                "type": "sc",
                "status": "ATTACHING",
                "details": []
:...skipping...
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:ap-southeast-1:530454120249:cluster/cruddur",
        "clusterName": "cruddur",
        "status": "PROVISIONING",
        "registeredContainerInstancesCount": 0,
        "runningTasksCount": 0,
        "pendingTasksCount": 0,
        "activeServicesCount": 0,
        "statistics": [],
        "tags": [],
        "settings": [
            {
                "name": "containerInsights",
                "value": "disabled"
            }
        ],
        "capacityProviders": [],
        "defaultCapacityProviderStrategy": [],
        "attachments": [
            {
                "id": "a6e63d39-86c7-4544-8064-347f69574fbf",
                "type": "sc",
                "status": "ATTACHING",
                "details": []
            }
        ],
        "attachmentsStatus": "UPDATE_IN_PROGRESS",
        "serviceConnectDefaults": {
            "namespace": "arn:aws:servicediscovery:ap-southeast-1:530454120249:namespace/ns-qwsmtxxaqbdmr2mk"
        }
    }
}
```
AWS ECS create namespace1

AWS ECS create namespace2



Prepare ECR
- Need respos
1. Base image - Python
2. Frontend - Flask
3. Backend - React JS

	
```
aws ecr create-repository \
 --repository-name cruddur-python \
 --image-tag-mutability MUTABLE

aws ecr create-repository \
 --repository-name backend-flask \
 --image-tag-mutability MUTABLE

aws ecr create-repository \
 --repository-name frontend-react-js \
 --image-tag-mutability MUTABLE
```

Note: Select the repo in the ECR, and press on the button called `View push commands`. 

## Verificaton image
week6-aws-ecr-repositories-created.png



## Running for Python image and making sure it works with backend and db

Use the push commands
- Make sure to Export and remember some AWS env vars in the gitpod workspace:
```
export AWS_ACCOUNT_ID=XXXXX
gp env AWS_ACCOUNT_ID=XXXXX

export ECR_PYTHON_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/cruddur-python"
gp env ECR_PYTHON_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/cruddur-python"

export ECR_FRONTEND_REACT_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/frontend-react-js"
gp env ECR_FRONTEND_REACT_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/frontend-react-js"

export ECR_BACKEND_FLASK_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/backend-flask"
gp env ECR_BACKEND_FLASK_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/backend-flask"
```


1. need to login and for that we need to use some `env` variables 
```sh
aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"
```
```
aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"```
```
- Gives
```
WARNING! Your password will be stored unencrypted in /home/gitpod/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```


cruddur-python	
530454120249.dkr.ecr.ap-southeast-1.amazonaws.com/cruddur-python

2. Set URL
```sh
export ECR_PYTHON_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/cruddur-python"
echo $ECR_PYTHON_URL
```


## Verification Image
ECR-URI
```
cruddur-python	
530454120249.dkr.ecr.ap-southeast-1.amazonaws.com/cruddur-python
```


3. Pull Image
```
docker pull python:3.10-slim-buster

```
4. Tag Image 
```
docker tag python:3.10-slim-buster $ECR_PYTHON_URL:3.10-slim-buster
```
5. Push Image
```
docker push $ECR_PYTHON_URL:3.10-slim-buster
```

## Verification Image
image-inside-ECR-repositories

week6-aws-ecr-repositories-python-slimbuster.png


- Once done, we need to update the FlaskApp to use this
update the `backend-flask/Dockerfile` to update the `FROM` 


- get Repository URL [`530454120249.dkr.ecr.ap-southeast-1.amazonaws.com/cruddur-python`] and replace


```
FROM accountID.dkr.ecr.ap-southeast-a......./cruddur-python:3.10-slim-buster
```
- Make sure the `Context` is correct, which prompt to use to run the `docker  commands` 
- so, do `docker login`with same command above 
```sh
aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"
```

and get success, and use that command prompt for further docker operations


- do `docker- compose up` with only `backend` and `db`
```
docker compose up backend-flask db
```
gave 
```
-err - `FATAL: databse `cruddur` does not exist`
```
We will ignore for now but go to URL of backend-flask (port 4567), and add `/api/health-check`

- it should return 

```
{
	"success": true
}
```


week6-aws-ecr-health-check-success.png



Ready to push
`backend-flask - docker file
ENV FLASK_ENVIRONEMNT` 
change to 
`ENV FLASK_DEBUG=1`

- Ref: Web server for Python - `gunicorn` 
https://guniicorn.org


Next, we need to Create ECR repo and push image for backend-flask	
- Make sure you are in backend-flask directory
- Repeat 1, 2, 3(Build Image), 4 and 5 for `backend-flask`

- Go to ECS and try to launch it 

Note: 
Task - as soon as it finishes, it will kill itself
Services: keep running always

- Create Service via `CLI`
- We will come back again here after finishing the `pre-requisite` 


- Deploy Backend Flask app as a service to Fargate
	
We will start with Backend first to make sure it all works

- aws/task-definitions/
	- backend-flask.json

Needs following to be created

1- TaskRole - Permissions that the container will have what its running
2- Environment variables [Cognito-pool-id and Region]
3- Secrets to stored in the `AWS Parameter Store`

---
 
1- ExecutionRole - Role need to execute the Container
	https://github.com/beiciliang/aws-bootcamp-cruddur-2023/commit/740f126d260e543a52261b053ff72d7990cbeab6

- create the ExecutionRole and attach policies at `aws-bootcamp-cruddur-2023/aws/policies/` as -
- service-execution-policy.json 
- service-assume-role-execution-policy.json
- cruddur-message-stream-policy.json (already there)

```
aws iam create-role \
  --role-name CruddurServiceExecutionRole \
  --assume-role-policy-document file://aws/policies/service-assume-role-execution-policy.json

aws iam put-role-policy \
  --policy-name CruddurServiceExecutionPolicy \
  --role-name CruddurServiceExecutionRole \
  --policy-document file://aws/policies/service-execution-policy.json

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchFullAccess \
  --role-name CruddurServiceExecutionRole

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy \
  --role-name CruddurServiceExecutionRole
```


Note: `arn:aws:iam::530454120249:role/CruddurServiceExecutionRole`


2 - Then create the TaskRole CruddurTaskRole and attach policies:
```
aws iam create-role \
    --role-name CruddurTaskRole \
    --assume-role-policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[\"sts:AssumeRole\"],
    \"Effect\":\"Allow\",
    \"Principal\":{
      \"Service\":[\"ecs-tasks.amazonaws.com\"]
    }
  }]
}"

aws iam put-role-policy \
  --policy-name SSMAccessPolicy \
  --role-name CruddurTaskRole \
  --policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[
      \"ssmmessages:CreateControlChannel\",
      \"ssmmessages:CreateDataChannel\",
      \"ssmmessages:OpenControlChannel\",
      \"ssmmessages:OpenDataChannel\"
    ],
    \"Effect\":\"Allow\",
    \"Resource\":\"*\"
  }]
}"

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchFullAccess \
  --role-name CruddurTaskRole

aws iam attach-role-policy \
  --policy-arn arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess \
  --role-name CruddurTaskRole
```


3- secrets to store in the `AWS Parameter Store`

Passing sensitive data to AWS for running backend-flask later:

```
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/AWS_ACCESS_KEY_ID" --value $AWS_ACCESS_KEY_ID
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/AWS_SECRET_ACCESS_KEY" --value $AWS_SECRET_ACCESS_KEY
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/CONNECTION_URL" --value $PROD_CONNECTION_URL
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/ROLLBAR_ACCESS_TOKEN" --value $ROLLBAR_ACCESS_TOKEN
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/OTEL_EXPORTER_OTLP_HEADERS" --value "x-honeycomb-team=$HONEYCOMB_API_KEY"
```

week6-aws-ssm-createed-parameters.png


***
***

Create ECR repo and push image for fronted-react-js
- Repeat 1, 2, 3, 4 and 5 for `backend-react-js`
	
Deploy Frontend React JS app as a service to Fargate

****
****


- Here Creating Registering the Task Definitions

-- backend using 
```
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json
```
Will give successful message as 

```
{
    "taskDefinition": {
        "taskDefinitionArn": "arn:aws:ecs:ap-southeast-1:530454120249:task-definition/backend-flask:1",
        "containerDefinitions": [
            {
                "name": "xray",
                "image": "public.ecr.aws/xray/aws-xray-daemon",
                "cpu": 0,
                "portMappings": [
                    {
                        "containerPort": 2000,
                        "hostPort": 2000,
                        "protocol": "udp",
                        "name": "xray"
                    }
                ],
                "essential": true,
                "environment": [],
                "mountPoints": [],
                "volumesFrom": [],
                "user": "1337"
            },
            {
                "name": "backend-flask",
                "image": "530454120249.dkr.ecr.ap-southeast-1.amazonaws.com/backend-flask",
                "cpu": 0,
                "portMappings": [
                    {
                        "containerPort": 4567,
                        "hostPort": 4567,
                        "protocol": "tcp",
                        "name": "backend-flask",
                        "appProtocol": "http"
                    }
                ],
                "essential": true,
                "environment": [
                    {
                        "name": "OTEL_SERVICE_NAME",
                        "value": "backend-flask"
                    },
                    {
                        "name": "AWS_DEFAULT_REGION",
                        "value": "ap-southeast-1"
                    },
                    {
                        "name": "BACKEND_URL",
                        "value": "*"
                    },
                    {
                        "name": "AWS_COGNITO_USER_POOL_ID",
                        "value": "ap-southeast-1_jiRQOZ7SS"
                    },
                    {
                        "name": "AWS_COGNITO_USER_POOL_CLIENT_ID",
                        "value": "7p3n1sa7ea43n6q205g82fnu9"
                    },
                    {
                        "name": "OTEL_EXPORTER_OTLP_ENDPOINT",
                        "value": "https://api.honeycomb.io"
                    },
                    {
                        "name": "FRONTEND_URL",
                        "value": "*"
                    }
                ],
                "mountPoints": [],
                "volumesFrom": [],
                "secrets": [
                    {
                        "name": "AWS_ACCESS_KEY_ID",
                        "valueFrom": "arn:aws:ssm:ap-southeast-1:530454120249:parameter/cruddur/backend-flask/AWS_ACCESS_KEY_ID"
                    },
                    {
                        "name": "AWS_SECRET_ACCESS_KEY",
                        "valueFrom": "arn:aws:ssm:ap-southeast-1:530454120249:parameter/cruddur/backend-flask/AWS_SECRET_ACCESS_KEY"
                    },
                    {
                        "name": "CONNECTION_URL",
                        "valueFrom": "arn:aws:ssm:ap-southeast-1:530454120249:parameter/cruddur/backend-flask/CONNECTION_URL"
                    },
                    {
                        "name": "ROLLBAR_ACCESS_TOKEN",
                        "valueFrom": "arn:aws:ssm:ap-southeast-1:530454120249:parameter/cruddur/backend-flask/ROLLBAR_ACCESS_TOKEN"
                    },
                    {
                        "name": "OTEL_EXPORTER_OTLP_HEADERS",
                        "valueFrom": "arn:aws:ssm:ap-southeast-1:530454120249:parameter/cruddur/backend-flask/OTEL_EXPORTER_OTLP_HEADERS"
                    }
                ],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-group": "cruddur",
                        "awslogs-region": "ap-southeast-1",
                        "awslogs-stream-prefix": "backend-flask"
                    }
                },
                "healthCheck": {
                    "command": [
                        "CMD-SHELL",
                        "python /backend-flask/bin/health-check"
                    ],
                    "interval": 30,
                    "timeout": 5,
                    "retries": 3,
                    "startPeriod": 60
                }
            }
        ],
        "family": "backend-flask",
        "taskRoleArn": "arn:aws:iam::530454120249:role/CruddurTaskRole",
        "executionRoleArn": "arn:aws:iam::530454120249:role/CruddurServiceExecutionRole",
        "networkMode": "awsvpc",
        "revision": 1,
        "volumes": [],
        "status": "ACTIVE",
        "requiresAttributes": [
            {
                "name": "com.amazonaws.ecs.capability.logging-driver.awslogs"
            },
            {
                "name": "ecs.capability.execution-role-awslogs"
            },
            {
                "name": "com.amazonaws.ecs.capability.ecr-auth"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.19"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.17"
            },
            {
                "name": "com.amazonaws.ecs.capability.task-iam-role"
            },
            {
                "name": "ecs.capability.container-health-check"
            },
            {
                "name": "ecs.capability.execution-role-ecr-pull"
            },
            {
                "name": "ecs.capability.secrets.ssm.environment-variables"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.18"
            },
            {
                "name": "ecs.capability.task-eni"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.29"
            }
        ],
        "placementConstraints": [],
        "compatibilities": [
            "EC2",
            "FARGATE"
        ],
        "requiresCompatibilities": [
            "FARGATE"
        ],
        "cpu": "256",
        "memory": "512",
        "registeredAt": "2023-04-13T12:31:12.518000+00:00",
        "registeredBy": "arn:aws:iam::530454120249:user/equinox9"
    }
}
```

-- and frontend using 
```
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/frontend-react-js.json
```
Will give successful message as 

```
{
    "taskDefinition": {
        "taskDefinitionArn": "arn:aws:ecs:ap-southeast-1:530454120249:task-definition/frontend-react-js:1",
        "containerDefinitions": [
            {
                "name": "xray",
                "image": "public.ecr.aws/xray/aws-xray-daemon",
                "cpu": 0,
                "portMappings": [
                    {
                        "containerPort": 2000,
                        "hostPort": 2000,
                        "protocol": "udp",
                        "name": "xray"
                    }
                ],
                "essential": true,
                "environment": [],
                "mountPoints": [],
                "volumesFrom": [],
                "user": "1337"
            },
            {
                "name": "frontend-react-js",
                "image": "530454120249.dkr.ecr.ap-southeast-1.amazonaws.com/frontend-react-js",
                "cpu": 0,
                "portMappings": [
                    {
                        "containerPort": 3000,
                        "hostPort": 3000,
                        "protocol": "tcp",
                        "name": "frontend-react-js",
                        "appProtocol": "http"
                    }
                ],
                "essential": true,
                "environment": [],
                "mountPoints": [],
                "volumesFrom": [],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-group": "cruddur",
                        "awslogs-region": "ap-southeast-1",
                        "awslogs-stream-prefix": "frontend-react-js"
                    }
                },
                "healthCheck": {
                    "command": [
                        "CMD-SHELL",
                        "curl -f http://localhost:3000 || exit 1"
                    ],
                    "interval": 30,
                    "timeout": 5,
                    "retries": 3
                }
            }
        ],
        "family": "frontend-react-js",
        "taskRoleArn": "arn:aws:iam::530454120249:role/CruddurTaskRole",
        "executionRoleArn": "arn:aws:iam::530454120249:role/CruddurServiceExecutionRole",
        "networkMode": "awsvpc",
        "revision": 1,
        "volumes": [],
        "status": "ACTIVE",
        "requiresAttributes": [
            {
                "name": "com.amazonaws.ecs.capability.logging-driver.awslogs"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.24"
            },
            {
                "name": "ecs.capability.execution-role-awslogs"
            },
            {
                "name": "com.amazonaws.ecs.capability.ecr-auth"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.19"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.17"
            },
            {
                "name": "com.amazonaws.ecs.capability.task-iam-role"
            },
            {
                "name": "ecs.capability.container-health-check"
            },
            {
                "name": "ecs.capability.execution-role-ecr-pull"
            },
            {
                "name": "com.amazonaws.ecs.capability.docker-remote-api.1.18"
            },
            {
                "name": "ecs.capability.task-eni"
            }
        ],
        "placementConstraints": [],
        "compatibilities": [
            "EC2",
            "FARGATE"
        ],
        "requiresCompatibilities": [
            "FARGATE"
        ],
        "cpu": "256",
        "memory": "512",
        "registeredAt": "2023-04-13T12:33:51.928000+00:00",
        "registeredBy": "arn:aws:iam::530454120249:user/equinox9"
    }
}

```

## Verification Image
week6-aws-ecs-task-definitions-fr-bk-end.png


- Now to launch the Containers

Get DEFAULT_VPC_ID and DEFAULT_SUBNET_IDS

```
export DEFAULT_VPC_ID=$(aws ec2 describe-vpcs \
--filters "Name=isDefault, Values=true" \
--query "Vpcs[0].VpcId" \
--output text)
echo $DEFAULT_VPC_ID
```

Gives `vpc-0ff6dae504ed3bab0`

and

```
export DEFAULT_SUBNET_IDS=$(aws ec2 describe-subnets  \
 --filters Name=vpc-id,Values=$DEFAULT_VPC_ID \
 --query 'Subnets[*].SubnetId' \
 --output json | jq -r 'join(",")')
echo $DEFAULT_SUBNET_IDS
```

Gives 
```
subnet-0f312708d4a604aef,subnet-000578155d60cd14c,subnet-09eb17c5d3a26b561
```
Note:
subnet-0f312708d4a604aef
subnet-000578155d60cd14c
subnet-09eb17c5d3a26b561


- Create Security Group

```
export CRUD_SERVICE_SG=$(aws ec2 create-security-group \
  --group-name "crud-srv-sg" \
  --description "Security group for Cruddur services on ECS" \
  --vpc-id $DEFAULT_VPC_ID \
  --query "GroupId" --output text)
echo $CRUD_SERVICE_SG
```
Gives 
```
sg-0499b02238724729b
```

- Authorise `ports`
```
aws ec2 authorize-security-group-ingress \
  --group-id $CRUD_SERVICE_SG \
  --protocol tcp \
  --port 4567 \
  --cidr 0.0.0.0/0
{
    "Return": true,
    "SecurityGroupRules": [
        {
            "SecurityGroupRuleId": "sgr-09fffcf592793f28c",
            "GroupId": "sg-0499b02238724729b",
            "GroupOwnerId": "530454120249",
            "IsEgress": false,
            "FromPort": 4567,
            "ToPort": 4567,
            "CidrIpv4": "0.0.0.0/0"
        }
    ]
}
```

```
aws ec2 authorize-security-group-ingress \
  --group-id $CRUD_SERVICE_SG \
  --protocol tcp \
  --port 3000 \
  --cidr 0.0.0.0/0
{
    "Return": true,
    "SecurityGroupRules": [
        {
            "SecurityGroupRuleId": "sgr-09d621c7e66ea487a",
            "GroupId": "sg-0499b02238724729b",
            "GroupOwnerId": "530454120249",
            "IsEgress": false,
            "IpProtocol": "tcp",
            "FromPort": 3000,
            "ToPort": 3000,
            "CidrIpv4": "0.0.0.0/0"
        }
   
```


```
aws ec2 authorize-security-group-ingress \
  --group-id $DB_SG_ID \
  --protocol tcp \
  --port 5432 \
  --source-group $CRUD_SERVICE_SG
{
    "Return": true,
    "SecurityGroupRules": [
        {
            "SecurityGroupRuleId": "sgr-094b53a43090d5cd0",
            "GroupId": "sg-009cb92245c927eb4",
            "GroupOwnerId": "530454120249",
            "IsEgress": false,
            "IpProtocol": "tcp",
            "FromPort": 5432,
            "ToPort": 5432,
            "ReferencedGroupInfo": {
                "GroupId": "sg-0499b02238724729b",
                "UserId": "530454120249"
            }
        }
    ]
}
```

---
---

Added `fargate` to `connect to service` for Troubleshooting
---

`./bin/ecs/connect-to-service <service ID> backend-flask`


## Application Load Balancer for Frontend

- Provision and configure Application Load Balancer along with target groups
	
ALB - 

New SG

Basic configurations: name cruddur-alb, Internet-facing, IPv4 address type;
Network mapping: default VPC, select first three availability zones;
Security groups: create a new security group named cruddur-alb-sg, set inbound rules of HTTP and HTTPS from anywhere, and Custom TCP of 4567 and 3000 from anywhere (set description as TMP1 and TMP2);

Note: `sg-079d711a94c8c7921`

- Configure


week6-aws-cruddur-alb-sg.png

week6-aws-alb-crud-srv-sg

- Target Group
week6-aws-cruddur-backend-flask-tg

Next page, `Register targets` keep as default, press `Create target group`
- Created `arn:aws:elasticloadbalancing:ap-southeast-1:530454120249:targetgroup/cruddur-backend-flask-tg/1b124527a9b268b3`

- Use this in the creation of  ALB creation above `cruddur-alb`

- Add another Target group listening on `port 3000` name `cruddur-frontend-react-js`
 
week6-aws-cruddur-alb-cration.png

---

- Now, use Target arn to put in to `json` files:

#1 `aws/json/service-backend-flask.json`
```
- cruddur-backend-flask-tg - 

targetGroupArn: arn:aws:elasticloadbalancing:ap-southeast-1:530454120249:targetgroup/cruddur-backend-flask-tg/1b124527a9b268b3

LoadBalancerArn: arn:aws:elasticloadbalancing:ap-southeast-1:530454120249:loadbalancer/app/cruddur-alb/d9ebc12f8dfbe573
continerName: "backend-flask"
containerPort: 4567
```


-Optional - 
- Attributes enable to save in S3  - paid service 
- create `S3` bucket for `Cruddur ALb Access Logs` 

## Verification 
week6-backend-target- group-healthy.png


--- 
Backend -DONE
---

- Now we will CONTINUE the Frontend, where we have already 
- Create Repo - Done
- Set URL - Done
- Build Image
- Tag Image
- Push Image

- Create 
- `frontend-react-js.json` in  `aws/task-definition`

Next #2 is Optional and we want to have `multi-build- stage` for `Docker-file` 
SO we do not add `loadBalancer` block in the `aws/json/service-frontend-react-js.json`

#2  `aws/json/service-frontend-react-js.json`
- cruddur-frontend-react-js
- `arn:aws:elasticloadbalancing:ap-southeast-1:530454120249:targetgroup/cruddur-frontend-react-js/52282d896b504c0d`


- Create `Dockerfile.prod` in the `frontend-react-js`
```
# Base Image ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM node:16.18 AS build

ARG REACT_APP_BACKEND_URL
ARG REACT_APP_AWS_PROJECT_REGION
ARG REACT_APP_AWS_COGNITO_REGION
ARG REACT_APP_AWS_USER_POOLS_ID
ARG REACT_APP_CLIENT_ID

ENV REACT_APP_BACKEND_URL=$REACT_APP_BACKEND_URL
ENV REACT_APP_AWS_PROJECT_REGION=$REACT_APP_AWS_PROJECT_REGION
ENV REACT_APP_AWS_COGNITO_REGION=$REACT_APP_AWS_COGNITO_REGION
ENV REACT_APP_AWS_USER_POOLS_ID=$REACT_APP_AWS_USER_POOLS_ID
ENV REACT_APP_CLIENT_ID=$REACT_APP_CLIENT_ID

COPY . ./frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
RUN npm run build

# New Base Image ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM nginx:1.23.3-alpine

# --from build is coming from the Base Image
COPY --from=build /frontend-react-js/build /usr/share/nginx/html
COPY --from=build /frontend-react-js/nginx.conf /etc/nginx/nginx.conf

EXPOSE 3000
```

Because the `build` folder will be created once the Dockerfile.prod runs with NodeJS 
- .gitignore, add `frontend-react-js/build/*`

- Create `nginx.conf` 
```
# Set the worker processes
worker_processes 1;
# Set the events module
events {
  worker_connections 1024;
}
# Set the http module
http {
  # Set the MIME types
  include /etc/nginx/mime.types;
  default_type application/octet-stream;
  # Set the log format
  log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';
  # Set the access log
  access_log  /var/log/nginx/access.log main;
  # Set the error log
  error_log /var/log/nginx/error.log;
  # Set the server section
  server {
    # Set the listen port
    listen 80;
    listen 3000;

    # Set the root directory for the app
    root /usr/share/nginx/html;
    # Set the default file to serve
    index index.html;
    # Set the error page
    error_page  404 /404.html;
    location = /404.html {
      internal;
    }
    # Set the error page for 500 errors
    error_page  500 502 503 504  /50x.html;
    location = /50x.html {
      internal;
    }
  }
}
```

- Now we will try run the `build` commands 
- Switch to `frontend-react-js` directory
- `npm run build`
- ignore any `warnings` in yellow color 


-note: 
- Make sure `setCognitoErrors` changed to `setErrors` in files - 
https://github.com/abheejain/aws-bootcamp-cruddur-2023/blob/main/frontend-react-js/src/pages/
- `RecoverPage.js`
- `ConfirmationPage.js`


- Frontend `Build Image` (get `cognito` and `client_ID` from `docker-compose` file) set as
```
      AWS_COGNITO_USER_POOL_ID: "ap-southeast-1_jiRQOZ7SS"
      AWS_COGNITO_USER_POOL_CLIENT_ID: "7p3n1sa7ea43n6q205g82fnu9"
```



- Make sure we have the 
1. `task-definition` for `frontend`
2. `aws/json/service-frontend-react-js.json` 
	- Update the VALUES to your account 
	- Add `loadBalancer` block with correct vaues from above #2
		- targetGroupARN: arn:aws:elasticloadbalancing:ap-southeast-1:530454120249:targetgroup/cruddur-frontend-react-js/52282d896b504c0d
		- containerName: frontend-react-js
		- containerPort: 3000




- Next 
in the `build Image` section above we used `--build-arg REACT_APP_BACKEND_URL="https://4567-$GITPOD_WORKSPACE_ID.$GITPOD_WORKSPACE_CLUSTER_HOST" \`
but that needs to be the URL of Load Balancer , so collect the LoadBalancer `DNS Name` -  `A Record` 
`cruddur-alb-1528392881.ap-southeast-1.elb.amazonaws.com`

Then Rebuild it correct way 
```
docker build \
--build-arg REACT_APP_BACKEND_URL="http://cruddur-alb-1528392881.ap-southeast-1.elb.amazonaws.com:4567" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID="ap-southeast-1_jiRQOZ7SS" \
--build-arg REACT_APP_CLIENT_ID="7p3n1sa7ea43n6q205g82fnu9" \
-t frontend-react-js \
-f Dockerfile.prod \
.
```
## Verification image
week6-frontend-build-npm.png

Make sure you are logged in to the ECR by checking in correct context
```
aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com"
```


- Tag Image
```
docker tag frontend-react-js:latest $ECR_FRONTEND_REACT_URL:latest
```

- Push Image
```
docker push $ECR_FRONTEND_REACT_URL:latest
```


#Verification Image
week6-frontend-iamge-push-Login-first.png


If you want to run and test it
```
docker run --rm -p 3000:3000 -it frontend-react-js 
```

Check with F12, chec red error for `4567`
- means correctly working even though we did not get connection between freontend and backend

## Verification Image
C:\Users\Rainbow Laptop\Pictures\AWS Bootcamp\week6-frontend-test-after-push.png





Make sure you are on the correct directory of `aws-bootcamp-cruddur-2023` 

Register Task Definition 
```
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/frontend-react-js.json
```


Create Service Frontend 
```
aws ecs create-service --cli-input-json file://aws/json/service-frontend-react-js.json
```

- Check
Go to ECS Services 
or

Target Group - Frontend
- `Target `Tab 
still kept initalizing 

so we need to `shell` into it to see what is wrong 


week6-frontend-service-healthy.png

week6-frontend-target- group-healthy.png

---


## Manage your domain useing Route53 via hosted zone
Note: Domain used is `lifecoaches.club`

Register Task Defintion
```
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json
```
Create Service Backend
```
aws ecs create-service --cli-input-json file://aws/json/service-backend-flask.json
```

## Verification 
week6-backend-service-healthy.png


http://cruddur-alb-1528392881.ap-southeast-1.elb.amazonaws.com:3000/

## Verification image
week6-frontend-service-using-elb.png

	
### Create Hosted Zone

- Setup the NS Records
- check and confirm
```
PS C:\WINDOWS\system32> nslookup -type=ns lifecoaches.club
Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
lifecoaches.club        nameserver = ns-1287.awsdns-32.org
lifecoaches.club        nameserver = ns-831.awsdns-39.net
lifecoaches.club        nameserver = ns-46.awsdns-05.com
lifecoaches.club        nameserver = ns-1609.awsdns-09.co.uk

ns-1287.awsdns-32.org   internet address = 205.251.197.7
ns-1609.awsdns-09.co.uk internet address = 205.251.198.73
ns-46.awsdns-05.com     internet address = 205.251.192.46
ns-831.awsdns-39.net    internet address = 205.251.195.63
ns-1287.awsdns-32.org   AAAA IPv6 address = 2600:9000:5305:700::1
ns-1609.awsdns-09.co.uk AAAA IPv6 address = 2600:9000:5306:4900::1
ns-46.awsdns-05.com     AAAA IPv6 address = 2600:9000:5300:2e00::1
ns-831.awsdns-39.net    AAAA IPv6 address = 2600:9000:5303:3f00::1
```

- Create an SSL cerificate via ACM

- Update the ALB with new Liserners 

## Verificatino Image
week6-domain-setup-added-listerners-to-alb.png

- Remove `HTTP-3000` and `HTTP-4567`

## Verification 

- Add Rule to `443` as `Host isapi.lifecoaches.club` to `Forward to
cruddur-backend-flask-tg: 1 (100%)`

- Create 2 records in Route53 
- Setup a record set for naked domain to point to frontend-react-js and
- Setup a record set for api subdomain to point to the backend-flask, - `api.domainname`
as
```
A Record 
Alias 
- Region 
`dualstack.cruddur-alb-15283928...`
``
- This will crate A Records for `lifecoaches.club` and `api/lifecoaches.club/api/health-check`


## Verification

week6-domain-setup-backend-done.png
week6-domain-setup-frontend-done.png

---
---

# Week-7 Combined here as to continue from Week-6
---

## Configure CORS to only permit traffic from our domain	
- Get the endpoints working 

- update `task-definitions/backend-flask.json` file with correct `frontend` and `backend` URLs
```
{"name": "FRONTEND_URL", "value": "https://lifecoaches.club"},
{"name": "BACKEND_URL", "value": "https://api.lifecoaches.club"},
```



- Register the Task Definition for `backend`

```
aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json

```
no need to push image for `backend` but for `frontend`

- and for `frontend`, we need to update the `build script` 
- make sure `logged in to ECR`

- Set URL for Frontend
```
export ECR_FRONTEND_REACT_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/frontend-react-js"
echo $ECR_FRONTEND_REACT_URL
```
gives `530454120249.dkr.ecr.ap-southeast-1.amazonaws.com/frontend-react-js`

- go in to `frontend` dir

```
docker build \
--build-arg REACT_APP_BACKEND_URL="https://api.lifecoaches.club" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID="ca-central-1_CQ4wDfnwc" \
--build-arg REACT_APP_CLIENT_ID="5b6ro31g97urk767adrbrdj1g5" \
-t frontend-react-js \
-f Dockerfile.prod \
.

```

- Tag Image
```
docker tag frontend-react-js:latest $ECR_FRONTEND_REACT_URL:latest
```
- Push Image
```
docker push $ECR_FRONTEND_REACT_URL:latest
```

---

## Secure Flask by not running in debug mode	

- From the `cruddur-alb-sg` security group, remove the `4567` and `3000`
And
- `443` and `80`, set `Source` to `My IP`

- Remove `degugger  FASK` code from `Dockerfile`
- Next, check on the `Dockerfile.prod` in `backend`, set ` --no-debugger` 

- create `ecr/login` , `chmod` 

- from the `backed` folder, run 
```
docker build -f Dockerfile.prod -t backend-flask-prod .
```
- Before going to test it, make sure the local Pordgres Server is running 


Create ./bin/docker/backend-flask-prod


#! /usr/bin/bash
```
docker run -rm \
-p 4567:4567 \
-e AWS_ENDPOINT_URL="http://dynamodb-local:8000" \
-e CONNECTION_URL="postgresql://postgres:password@db:5432/cruddur" \
-e FRONTEND_URL="https://3000-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}" \
-e BACKEND_URL="https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}" \
-e OTEL_SERVICE_NAME='backend-flask' \
-e OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io" \
-e OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=${HONEYCOMB_API_KEY}" \
-e AWS_XRAY_URL="*4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}*" \
-e AWS_XRAY_DAEMON_ADDRESS="xray-daemon:2000" \
-e AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}" \
-e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
-e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
-e ROLLBAR_ACCESS_TOKEN="${ROLLBAR_ACCESS_TOKEN}" \
-e AWS_COGNITO_USER_POOL_ID="${AWS_COGNITO_USER_POOL_ID}" \
-e AWS_COGNITO_USER_POOL_CLIENT_ID="5b6ro31g97urk767adrbrdj1g5" \   
-it backend-flask-prod
```

- It may give an error 
`pool-1: Connection is bad: Name or service not known` 
because the Docker is not running 


Just run only `db` and `dynamodb-local` containers 

- But still it was failing to `run` 

- Went to `app.py` 

THis is to test only to `generate a bug`, added 
```
hello = nune
hello()
```
in the `def health_check():` block

- Run Docker composer 

- Check 4567 cntainer in browser with `api/health-check` to see if it throws an error
- It should 

and 

- now `change` to set `--no-debug`
- docker compose up again to check 
- Check 4567 cntainer in browser with `api/health-check` to see if it throws an error `Internal Server Error`

- Success 

---

Arranging the script files

- Create Folder structure to arrange the `docker comands` 
- Docker
	- run
		- backend-flask-prod
			```
			#! usr/bin/bash
	
			docker build -f Dockerfile.prod -t backend-flask-prod .
			```
		- frontend-react-js
			```
			#! usr/bin/bash
	
			docker build \
			--build-arg REACT_APP_BACKEND_URL="https://api.lifecoaches.club" \
			--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
			--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
			--build-arg REACT_APP_AWS_USER_POOLS_ID="ap-southeast-1_jiRQOZ7SS" \
			--build-arg REACT_APP_CLIENT_ID="7p3n1sa7ea43n6q205g82fnu9" \
			-t frontend-react-js \
			-f Dockerfile.prod \
			.
			```
					

	- build

	
## Fix Messaging In Production


## Implement Refresh Token for Amazon Cognito	Refactor bin directory to be top level	


// "python /backend-flask/bin/flask/health-check"
          
./bin/db/setup 
./bin/db/schema-load 
./bin/db/seed 
 ./bin/ddb/schema-load
./bin/ddb/seed 


INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Andrew Bayko', 'bayko@exampro.co', 'bayko' ,'MOCK');

## Here we will fix the `Token Expiry` issue as well 
Thank you to the user `poxrud` 
Note as - 
Cognito by itself will automatically store the access token in local storage. It is unnecessary to store it again.
Here is a simpler getAccessToken function.

```
const getAccessToken = async () => {
  try {
    const session = await Auth.currentSession();
    return session.getAccessToken().getJwtToken();
  } catch (err) {
    console.log(err);
  }
};
```

Then whenever you need the access token you can just get it from Cognito:
```
const access_token = await getAccessToken();
const res = await fetch(backend_url, {
  headers: {
    Authorization: `Bearer ${access_token}`,
  },
  method: "GET",
});
```
---
## Configure task defintions to contain x-ray and turn on Container Insights	
### Tasks to be done under this sectin of Week-7 Part are
- Change Docker Compose to explicitly use a user-defined network	
- Create Dockerfile specfically for production use case	
- Using ruby generate out env dot files for docker using erb templates

Using Andrew's favourite part to tdo with `Ruby Language` With erb FOLDER
`.env` naming convention to be noted 

Note: Make sure the values passed in `double quotations` 
But in the `.rb` files do not need quotations

After making the changes and adding the erb files along with using the .env var files, `docker-compose up` to make sure it all works `LOCALLY`

Update aws/task-definiitions/backend-flask.json has `health-check` path
Need to be fixed by moving the `health-check` file to `backend-flask/bin/health-check`

After that we refresh the code in prod 

Backend
- build
- push
- register (as we have new values in Task Definition) (IAM PassRle issue, `Cruddur_TaskRole`- maybe SCP - because keys are committed to the repo 

- Need to protect keys - do not commit your AWS secret 

- Again push
- deploy
(Issue in `health check`)

- Shows X-Ray Running, backend -Healthy
- X-ray helath check need to see if it is defined

- Register and deploy again still Xray shows `unknown`

- Update the aws/task-definition - frontend-flask-js

- Frontend
-- register and deploy

Last COMMIT UPdate task def not to have netstat

- Backend 
-- register and deploy

- Frontend 
register and deploy

- Turn on Container Insights by going to `ECS Cluster` and  press `update`, Monitoring Tab - enable `Use Container Insights` - press `Update` 

- Turned on now

This can be checked in CoudWatch - Container Insights

=====
Week 6 - 7 Finished 
=====
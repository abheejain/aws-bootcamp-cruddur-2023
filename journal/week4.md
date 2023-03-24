# Week 4 — Postgres and RDS

## Create RDS Postgres Instance 

Proof of the RDS Postgres Instance Creation 

## Verificaton Image

![RDS Creation](assets/week-4/week4-rds-created-stopped.png)

</hr>

## Bash scripting for common database actions
- Created various `bash scripts` to make it wasy to interact with the local and the Prod daabases
## Verificaton Image

![DB Bash Cript](assets/week-4/week4-common-db-bash-commands.png)

</hr>

## Install Postgres Driver in Backend Application
## Verificaton Image

![PG Driver in Backend1](assets/week-4/week4-Postgres-Driver-in-Backend-1.png)

![PG Driver in Backend2](assets/week-4/week4-Postgres-Driver-in-Backend-2.png)

</hr>


## Connect Gitpod to RDS Instance
## Verificaton Image

![DB Connect to GitPod](assets/week-4/week4-postgres-Connect-RDS-with-Gitpod-final.png)

![DB Connect Lambda 200](assets/week-4/week4-schema-loaded-on-prod-before-labmda-200.png)

</hr>


## Create Congito Trigger to insert user into database
## Verificaton Image

</hr>
### Notes: 
`Configuration` -  `Permissions`
The provided execution role does not have permissions to call CreateNetworkInterface on EC2

So need to Add Policy in addition to the existing `Configuration` - `Permissions` - Role - `roles/cruddur-post-confirmation-role-a2i0hdsu`

Created new Policy and attached 
Ref: https://stackoverflow.com/questions/41177965/aws-lambdathe-provided-execution-role-does-not-have-permissions-to-call-describ

Managed Policy Created: `AWS-Lambda-VPC-Access-Execution-Role`
</hr>

![User Created](assets/week-4/week4-post-cofirmation-lambda-User-Created.png)


![User Created CLI](assets/week-4/week4-post-cofirmation-lambda-User-Created-x-on.png)


</hr>


## Create new activities with a database insert
## Verificaton Image

![Created Activities](assets/week-4/week4-activities-created.png)


![Created Activities User](assets/week-4/week4-activities-created-user.png)
</hr>



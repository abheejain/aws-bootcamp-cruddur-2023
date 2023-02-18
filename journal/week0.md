# Week 0 — Billing and Architecture

## REQUIRED WORK

### Pre-requisites for this week

Getting all the information and th base to be crated from the reference videos from ExamPro Playlist on YouTube, which includes Videos
- Chirag's Week 0 - Spend Considerations
- Ashish's Week 0 - Security Considerations

## The Homework Tasks for Week0

### Recreate Conceptual Diagram in Lucid Charts or on a Napkin

## Verificaton Image

![Cruddur ConceptualDiagram Napkin](assets/week-0/Cruddur-ConceptualDiagram-Napkin.png)


Link to the Lucidchart file: [Conceptual-Diagram-Napkin](https://lucid.app/lucidchart/bb00a564-d795-4a8a-9853-fa7bc77510f4/edit?viewport_loc=-359%2C-51%2C2128%2C1009%2C0_0&invitationId=inv_fc7fbf1d-ee1e-4549-ba40-b1759ee9ff01)

![Cruddur ConceptualDiagram](assets/week-0/Cruddur-Conceptual-Diagram.png)

### Recreate Logical Architectual Diagram in Lucid Charts
## Verificaton Image
![Cruddur Logical Diagram](assets/week-0/Cruddur-Logical-Diagram.png)

Link to the Lucidchart file: [Logical-Diagram](https://lucid.app/lucidchart/d275d5fb-6f7d-4bea-bb2d-4e7d7c330e0d/edit?viewport_loc=-1701%2C-286%2C2160%2C1024%2C0_0&invitationId=inv_ca9fd736-ffe9-4d02-bd36-21fbc06d7503)

<hr>

AWS CLI is most ofter and widely used for working with AWS commands using a command prompt. We will start with installing the AWS CLI

### AWS CLI- Install

- We are going to install the AWS CLI when our Gitpod enviroment lanuches.
- We are are going to set AWS CLI to use partial autoprompt mode to make it easier to debug CLI commands.
- The bash commands we are using are the same as the [AWS CLI Install Instructions]https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html


Update our `.gitpod.yml` to include the following task.

```sh
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```

We'll also run these commands indivually to perform the install manually

### Create a new User and Generate AWS Credentials

- Go to (IAM Users Console](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users) andrew create a new user
- `Enable console access` for the user
- Create a new `Admin` Group and apply `AdministratorAccess`
- Create the user and go find and click into the user
- Click on `Security Credentials` and `Create Access Key`
- Choose AWS CLI Access
- Download the CSV with the credentials

### Set Env Vars

We will set these credentials for the current bash terminal
```
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION=us-east-1
```

We'll tell Gitpod to remember these credentials if we relaunch our workspaces
```
gp env AWS_ACCESS_KEY_ID=""
gp env AWS_SECRET_ACCESS_KEY=""
gp env AWS_DEFAULT_REGION=us-east-1
```

### Check that the AWS CLI is working and you are the expected user

```sh
aws sts get-caller-identity
```

Received the output as: (I am showing sampple Account number here ofr security reasons)
```json
{
    "UserId": "AIDAXXAMHQ443QG2N3EEA",
    "Account": "5304541202499",
    "Arn": "arn:aws:iam::5304541202499:user/equinox9"
}
```
<hr>
  
## Verificaton Image
  
![AWS STS Caller Identity](assets/week-0/aws-sts-caller-identity.png)

<hr>
## Enable Billing 

We need to turn on Billing Alerts to recieve alerts...


- In your Root Account go to the [Billing Page](https://console.aws.amazon.com/billing/)
- Under `Billing Preferences` Choose `Receive Billing Alerts`
- Save Preferences


## Creating a Billing Alarm

### Create SNS Topic

- We need an SNS topic before we create an alarm.
- The SNS topic is what will delivery us an alert when we get overbilled
- [aws sns create-topic](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html)

We'll create a SNS Topic
```sh
aws sns create-topic --name billing-alarm
```
which will return a TopicARN

We'll create a subscription supply the TopicARN and our Email
```sh
aws sns subscribe \
    --topic-arn TopicARN \
    --protocol email \
    --notification-endpoint your@email.com
```

Check your email and confirm the subscription

## Verificaton Image
![SNS Confirmation](assets/week-0/AWS-SNS-Subscription-Confirmed.png)



#### Create Alarm

- [aws cloudwatch put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html)
- [Create an Alarm via AWS CLI](https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-estimatedcharges-alarm/)
- We need to update the configuration json script with the TopicARN we generated earlier
- We are just a json file because --metrics is is required for expressions and so its easier to us a JSON file.

```sh
aws cloudwatch put-metric-alarm --cli-input-json file://aws/json/alarm_config.json
```
## Verificaton Image
![Alarm Confirmation](assets/week-0/aws-alarm-set-confirm.png)

<hr> 

## Create an AWS Budget

[aws budgets create-budget](https://docs.aws.amazon.com/cli/latest/reference/budgets/create-budget.html)

Get your AWS Account ID
```sh
aws sts get-caller-identity --query Account --output text
```

- Supply your AWS Account ID
- Update the json files
- This is another case with AWS CLI its just much easier to json files due to lots of nested json

```sh
aws budgets create-budget \
    --account-id AccountID \
    --budget file://aws/json/budget.json \
    --notifications-with-subscribers file://aws/json/budget-notifications-with-subscribers.json
```
## Verificaton Image

![Budget Confirmation](assets/week-0/aws-budget-set-confirm.png)


<hr>
## HOMEWORK CHALLENGES

To be added soon
<hr>
## ADDITIONAL HOMEWORK CHALLENGES

To be added soon

<hr>

# Week 5 — DynamoDB and Serverless Caching
</hr> 

## Tasks to be done are: 

- Data Modelling
- Backend Preparation
- DynamoDB Utility Scripts
- Implement Conversations with DynamoDB Local
- Implement DynamoDB Stream with AWS Lambda

</hr>

## Data Modelling


## Backend Preparation

Setting up AWS Boto3 for Dynamodb local setup
Ref: https://boto3.amazonaws.com/v1/documentation/


Creatng New Item in DynamoDB
Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html

AWS CLI - DynamDB List Tables
https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html
https://docs.aws.amazon.com/cli/latest/reference/dynamodb/list-tables.html



delete-table
https://docs.aws.amazon.com/cli/latest/reference/dynamodb/delete-table.html


/hr> 

## DynamoDB Utility Scripts

```

gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ chmod u+x bin/ddb/list-tables 
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/list-tables 
---------------------
|    ListTables     |
+-------------------+
|  cruddur-message  |
+-------------------+
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/list-tables 
---------------------
|    ListTables     |
+-------------------+
|  cruddur-message  |
+-------------------+
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ chmod u+x bin/ddb/drop 
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/drop 
No TABLE_NAME argument supplied eg ./bin/ddb/drop cruddur-messages prod 
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/drop cruddur-messages
deleting table: cruddur-messages

An error occurred (ResourceNotFoundException) when calling the DeleteTable operation: Cannot do operations on a non-existent table
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/drop cruddur-message
deleting table: cruddur-message
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "pk",
                "AttributeType": "S"
            },
            {
                "AttributeName": "sk",
                "AttributeType": "S"
            }
        ],
        "TableName": "cruddur-message",
        "KeySchema": [
            {
                "AttributeName": "pk",
                "KeyType": "HASH"
            },
            {
:...skipping...
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "pk",
                "AttributeType": "S"
            },
            {
                "AttributeName": "sk",
                "AttributeType": "S"
            }
        ],
        "TableName": "cruddur-message",
        "KeySchema": [
            {
                "AttributeName": "pk",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "sk",
                "KeyType": "RANGE"
:...skipping...
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "pk",
                "AttributeType": "S"
            },
            {
                "AttributeName": "sk",
                "AttributeType": "S"
            }
        ],
        "TableName": "cruddur-message",
        "KeySchema": [
            {
                "AttributeName": "pk",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "sk",
                "KeyType": "RANGE"
            }
:...skipping...
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "pk",
                "AttributeType": "S"
            },
            {
                "AttributeName": "sk",
                "AttributeType": "S"
            }
        ],
        "TableName": "cruddur-message",
        "KeySchema": [
            {
                "AttributeName": "pk",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "sk",
                "KeyType": "RANGE"
            }
        ],
:...skipping...
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "pk",
                "AttributeType": "S"
            },
            {
                "AttributeName": "sk",
                "AttributeType": "S"
            }
        ],
        "TableName": "cruddur-message",
        "KeySchema": [
            {
                "AttributeName": "pk",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "sk",
                "KeyType": "RANGE"
            }
        ],
        "TableStatus": "ACTIVE",
:...skipping...
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "pk",
                "AttributeType": "S"
            },
            {
                "AttributeName": "sk",
                "AttributeType": "S"
            }
        ],
        "TableName": "cruddur-message",
        "KeySchema": [
            {
                "AttributeName": "pk",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "sk",
                "KeyType": "RANGE"
            }
        ],
        "TableStatus": "ACTIVE",
        "CreationDateTime": "2023-03-28T10:40:48.738000+00:00",
:...skipping...
{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "pk",
                "AttributeType": "S"
            },
            {
                "AttributeName": "sk",
                "AttributeType": "S"
            }
        ],
        "TableName": "cruddur-message",
        "KeySchema": [
            {
                "AttributeName": "pk",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "sk",
                "KeyType": "RANGE"
            }
        ],
        "TableStatus": "ACTIVE",
        "CreationDateTime": "2023-03-28T10:40:48.738000+00:00",
        "ProvisionedThroughput": {
            "LastIncreaseDateTime": "1970-01-01T00:00:00+00:00",
            "LastDecreaseDateTime": "1970-01-01T00:00:00+00:00",
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:ddblocal:000000000000:table/cruddur-message"
    }
}
```



Seeding data in DDB
REF to the Dat Modeling 

pk				sk (created_at or last_reply_at)
MSG#{message_group_uuid}		MSG#{created_at}
GRP#{my_user_uuid}		GRP#{last_reply_at}
GRP#{my_user_uuid}		GRP#{last_reply_at}



1:07:13 
Created with 
seed

I got error

gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/seed
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/359.
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/359.
from: can't read /var/mail/datetime
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/359.
import-im6.q16: unable to open X server `' @ error/import.c/ImportImageCommand/359.
./bin/ddb/seed: line 7: syntax error near unexpected token `('
./bin/ddb/seed: line 7: `current_path = os.path.dirname(os.path.abspath(__file__))'

Fixed with correcting the path '..'

Now can `seed` the data and `scan` as well 
```
./bin/ddb/seed

./bin/ddb/scan

```

Next to Fix for the Read and Write for DynamDB

```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ chmod u+x bin/ddb/patterns/get-conversation
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ chmod u+x bin/ddb/patterns/list-conversations 
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/d
db/  ddb/ 
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/d
db/  ddb/ 
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/patterns/get-conversation 
{
  "ConsumedCapacity": {
    "CapacityUnits": 1.0,
    "TableName": "cruddur-messages"
  },
  "Count": 20,
  "Items": [
    {
      "message": {
        "S": "Definitely. I think his character is a great example of the show's ability to balance humor and heart, and to create memorable and beloved characters that fans will cherish for years to come."
      },
      "message_uuid": {
        "S": "b2d16770-1f19-45c6-9ce9-650e299ba081"
      },
      "pk": {
        "S": "MSG#5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
      },
      "sk": {
        "S": "2023-03-28T21:02:11.141577+00:00"
      },
      "user_display_name": {
        "S": "Andrew Bayko"
      },
      "user_handle": {
        "S": "bayko"
      },
      "user_uuid": {
        "S": "ddc941dd-ce74-4732-8f01-73fe3bcb28b8"
      }
    },
    {
      "message": {
        "S": "And Zathras was just one example of that. He was a small but important part of the show's legacy, and he's still remembered fondly by fans today."
      },
      "message_uuid": {
        "S": "25c29899-ec10-42a0-a693-1ba2b331afa1"
      },
      "pk": {
        "S": "MSG#5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
      },
      "sk": {
        "S": "2023-03-28T21:01:11.141577+00:00"
      },
      "user_display_name": {
        "S": "Andrew Brown"
      },
      "user_handle": {
        "S": "andrewbrown"
      },
      "user_uuid": {
        "S": "9ad98342-8f75-4b56-a514-1c8f48e800d1"
      }
    },
    {
      "message": {
        "S": "Yes, that's a good point. Babylon 5 was really great at creating a diverse and interesting cast of characters, with each one feeling like a fully-realized and distinct individual."
      },
      "message_uuid": {
        "S": "beaf3446-a07e-4952-9fb6-7902fee61a98"
      },
      "pk": {
        "S": "MSG#5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
      },
      "sk": {
        "S": "2023-03-28T21:00:11.141577+00:00"
      },
      "user_display_name": {
        "S": "Andrew Bayko"
      },
      "user_handle": {
        "S": "bayko"
      },
      "user_uuid": {
        "S": "ddc941dd-ce74-4732-8f01-73fe3bcb28b8"
      }
    },
   
   .
   .
   I CUT IT SHORT TO REDUCE THE LENGTH OF JOURNAL
   .
   .
   
    {
      "message": {
        "S": "One thing that really stands out about Babylon 5 is the quality of the special effects. What did you think about the show's use of CGI and other visual effects?"
      },
      "message_uuid": {
        "S": "748d5f46-d53e-4280-a3a9-15c4eeb1ed5e"
      },
      "pk": {
        "S": "MSG#5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
      },
      "sk": {
        "S": "2023-03-28T20:43:11.141577+00:00"
      },
      "user_display_name": {
        "S": "Andrew Brown"
      },
      "user_handle": {
        "S": "andrewbrown"
      },
      "user_uuid": {
        "S": "9ad98342-8f75-4b56-a514-1c8f48e800d1"
      }
    }
  ],
  "LastEvaluatedKey": {
    "pk": {
      "S": "MSG#5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
    },
    "sk": {
      "S": "2023-03-28T20:43:11.141577+00:00"
    }
  },
  "ResponseMetadata": {
    "HTTPHeaders": {
      "content-type": "application/x-amz-json-1.0",
      "date": "Tue, 28 Mar 2023 19:33:55 GMT",
      "server": "Jetty(9.4.48.v20220622)",
      "transfer-encoding": "chunked",
      "x-amz-crc32": "2203357864",
      "x-amzn-requestid": "77b94513-37ae-4734-bb39-8492569c4352"
    },
    "HTTPStatusCode": 200,
    "RequestId": "77b94513-37ae-4734-bb39-8492569c4352",
    "RetryAttempts": 0
  },
  "ScannedCount": 20
}
{
  "CapacityUnits": 1.0,
  "TableName": "cruddur-messages"
}
andrewbrown 2023-03-28 08:43 PM   One thing that really stands out about B...
bayko       2023-03-28 08:44 PM   I thought the special effects in Babylon...
andrewbrown 2023-03-28 08:45 PM   Yes, I was really blown away by the leve...
bayko       2023-03-28 08:46 PM   And I also appreciated the way the show ...
andrewbrown 2023-03-28 08:47 PM   Absolutely. The show had a great balance...
bayko       2023-03-28 08:48 PM   And it's also worth noting the way the s...
andrewbrown 2023-03-28 08:49 PM   Yes, I agree. And it's impressive how th...
bayko       2023-03-28 08:50 PM   Definitely. And it's one of the reasons ...
andrewbrown 2023-03-28 08:51 PM   Agreed. And it's also worth noting the w...
bayko       2023-03-28 08:52 PM   Yes, it definitely had a big impact on t...
andrewbrown 2023-03-28 08:53 PM   Another character I wanted to discuss is...
bayko       2023-03-28 08:54 PM   Zathras was a really unique and memorabl...
andrewbrown 2023-03-28 08:55 PM   Yes, I thought he was a great addition t...
bayko       2023-03-28 08:56 PM   And I appreciated the way the show used ...
andrewbrown 2023-03-28 08:57 PM   Definitely. It was a great way to integr...
bayko       2023-03-28 08:58 PM   Yeah, that was a clever storytelling dev...
andrewbrown 2023-03-28 08:59 PM   I also thought that Zathras was a great ...
bayko       2023-03-28 09:00 PM   Yes, that's a good point. Babylon 5 was ...
andrewbrown 2023-03-28 09:01 PM   And Zathras was just one example of that...
bayko       2023-03-28 09:02 PM   Definitely. I think his character is a g...
```



Note: 'KeyConditionExpression': 'pk = :pk AND begins_with(sk,:year)',
  #although the document says BEGINS_WITH we need to use small case `begins_with`


## list-conversations

```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/patterns/list-conversations 
Traceback (most recent call last):
  File "./bin/ddb/patterns/list-conversations", line 37, in <module>
    my_user_uuid = get_my_user_uuid()
  File "./bin/ddb/patterns/list-conversations", line 32, in get_my_user_uuid
    uuid = db.query_value(sql,{
AttributeError: 'Db' object has no attribute 'query_value'
```

Fixed by updating db.py with `def query_value(self,sql,params={}):` and adding `params`

```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/patterns/list-conversations 
 SQL STATEMENT-[value]------

    SELECT 
      users.uuid
    FROM users
    WHERE
      users.handle =%(handle)s
   {'handle': 'andrewbrown'}
my-uuid: 9ad98342-8f75-4b56-a514-1c8f48e800d1
{
  "ConsumedCapacity": {
    "CapacityUnits": 0.5,
    "TableName": "cruddur-messages"
  },
  "Count": 1,
  "Items": [
    {
      "message": {
        "S": "this is a filler message from Abheeshek"
      },
      "message_group_uuid": {
        "S": "5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
      },
      "pk": {
        "S": "GRP#9ad98342-8f75-4b56-a514-1c8f48e800d1"
      },
      "sk": {
        "S": "2023-03-28T19:19:11.141577+00:00"
      },
      "user_display_name": {
        "S": "Andrew Bayko"
      },
      "user_handle": {
        "S": "bayko"
      },
      "user_uuid": {
        "S": "ddc941dd-ce74-4732-8f01-73fe3bcb28b8"
      }
    }
  ],
  "ResponseMetadata": {
    "HTTPHeaders": {
      "content-length": "462",
      "content-type": "application/x-amz-json-1.0",
      "date": "Tue, 28 Mar 2023 19:53:55 GMT",
      "server": "Jetty(9.4.48.v20220622)",
      "x-amz-crc32": "3241719255",
      "x-amzn-requestid": "bf8ac080-07a4-480a-903e-11629e84b1dc"
    },
    "HTTPStatusCode": 200,
    "RequestId": "bf8ac080-07a4-480a-903e-11629e84b1dc",
    "RetryAttempts": 0
  },
  "ScannedCount": 1
}
```
</hr> 

### Finished Utility scripts working with DynamoDB 
</hr>


## Implement DynamoDB into Frontend and Backend application

Ref: [week-5-again-again]

List Cognito Users
AWS CLI 
```
aws cognito-idp - list-users --user-pool-id=ap-southeast-1_jiRQXXXXXXX
```
week5-cognito-list-users.png 


Will ist users, but we want to fetch using SDK

Before implementing the Cognito `list-users`
we need to `export` the Cognito pool ID

```
export AWS_COGNITO_USER_POOL_ID="ap-southeast-1_jiRQOZ7SS"

gp env AWS_COGNITO_USER_POOL_ID="ap-southeast-1_jiRQOZ7SS"

```
Update in Docker-compose file 

Boto3 - List Users

```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ chmod u+x bin/cognito/list-users 
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/cognito/list-users 
[
  {
    "Attributes": [
      {
        "Name": "sub",
        "Value": "d45e40df-5c28-4570-a857-2c4350c4bff9"
      },
      {
        "Name": "preferred_username",
        "Value": "equinox9.in"
      }
    ],
    "Enabled": true,
    "UserCreateDate": "2023-03-23 11:19:15.738000+00:00",
    "UserLastModifiedDate": "2023-03-23 20:45:23.635000+00:00",
    "UserStatus": "CONFIRMED",
    "Username": "d45e40df-5c28-4570-a857-2c4350c4bff9"
  }
]
{
  "equinox9.in": "d45e40df-5c28-4570-a857-2c4350c4bff9"
}
```

### Update Cognito User Ids

```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ chmod u+x bin/db/update_cognito_user_ids 
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/db/update_cognito_user_ids 
== db-update-cognito-user-ids
---- equinox9.in d45e40df-5c28-4570-a857-2c4350c4bff9
 SQL STATEMENT-[commit with returning]------

    UPDATE public.users
    SET cognito_user_id = %(sub)s
    WHERE
      users.handle = %(handle)s;
   {}
```

{} is empty, because we did not pass the `params` in db.py at

```
self.print_sql('commit with returning',sql,params)
```

```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/db/update_cognito_user_ids 
== db-update-cognito-user-ids
---- equinox9.in d45e40df-5c28-4570-a857-2c4350c4bff9
 SQL STATEMENT-[commit with returning]------

    UPDATE public.users
    SET cognito_user_id = %(sub)s
    WHERE
      users.handle = %(handle)s;
   {'handle': 'equinox9.in', 'sub': 'd45e40df-5c28-4570-a857-2c4350c4bff9'}
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ 
```


- Issue of Messages not showing after all setup 

- To resolve that, according to the Discord community help, I needed to change the `my_handle`

- so Changed  my_handle in ddb/seed 


- Another issue was regarding the  
```
ERROR:  database "your_db" is being accessed by other users
DETAIL:  There is 1 other session using the database.
```

- Resolution again from the Discord help, the following approach solved it for me:

```
REVOKE CONNECT ON DATABASE <mydbname> FROM public;
ALTER DATABASE <mydbname> allow_connections = off;
SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '<mydbname>';
DROP DATABASE <mydbname>;
```

## Message Group UUID Acheived 

https://3000-abheejain-awsbootcampcr-5vhi0gh6ozh.ws-us93.gitpod.io/messages/5ae290ed-55d1-47a0-bc6d-fe2bc2700399


- Now need to implement the code on server-side
- Now can see the messages sent 


## Create a New Conversation 
# Londo Mollari :) 

```
cruddur=# INSERT INTO public.users (display_name, email, handle, cognito_user_id)
cruddur-# VALUES ('Londo Mollari', 'lmollari@centari.co', 'londo' ,'MOCK');
INSERT 0 1

```

```
https://3000-abheejain-awsbootcampcr-5vhi0gh6ozh.ws-us93.gitpod.io/messages/new/londo
```

Redirected to 
```
https://3000-abheejain-awsbootcampcr-5vhi0gh6ozh.ws-us93.gitpod.io/messages/29eaa2a5-e6e8-4124-a08f-a58a332c46ba
```

</ hr>


## Implement DynamoDB Stream with AWS Lambda

## IMP IMP Need to make sure postgres database exists first
Ref: Thread : `DynamoDB Stream implementation error`
https://discord.com/channels/1055552619441049660/1090636148570849380/1090936493759012905


So runnng will `./bin/db/setup`will do


```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/db/setup
==== db-setup
== db-drop
NOTICE:  database "cruddur" does not exist, skipping
DROP DATABASE
== db-create
CREATE DATABASE
== db-schema-load
/workspace/aws-bootcamp-cruddur-2023/backend-flask/db/schema.sql
CREATE EXTENSION
NOTICE:  table "users" does not exist, skipping
DROP TABLE
NOTICE:  table "activities" does not exist, skipping
DROP TABLE
CREATE TABLE
CREATE TABLE
== db-seed
/workspace/aws-bootcamp-cruddur-2023/backend-flask/db/seed.sql
INSERT 0 3
INSERT 0 1
== db-update-cognito-user-ids
---- equinox9.in d45e40df-5c28-4570-a857-2c4350c4bff9
 SQL STATEMENT-[commit with returning]------

    UPDATE public.users
    SET cognito_user_id = %(sub)s
    WHERE
      users.handle = %(handle)s;
   {'handle': 'equinox9.in', 'sub': 'd45e40df-5c28-4570-a857-2c4350c4bff9'}
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ 
```


## We do need to do schema-load against the RDS database so we have the database structure.


```
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ ./bin/ddb/schema-load prod
{'TableDescription': {'AttributeDefinitions': [{'AttributeName': 'message_group_uuid', 'AttributeType': 'S'}, {'AttributeName': 'pk', 'AttributeType': 'S'}, {'AttributeName': 'sk', 'AttributeType': 'S'}], 'TableName': 'cruddur-messages', 'KeySchema': [{'AttributeName': 'pk', 'KeyType': 'HASH'}, {'AttributeName': 'sk', 'KeyType': 'RANGE'}], 'TableStatus': 'CREATING', 'CreationDateTime': datetime.datetime(2023, 4, 1, 15, 55, 23, 389000, tzinfo=tzlocal()), 'ProvisionedThroughput': {'NumberOfDecreasesToday': 0, 'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}, 'TableSizeBytes': 0, 'ItemCount': 0, 'TableArn': 'arn:aws:dynamodb:ap-southeast-1:530454120249:table/cruddur-messages', 'TableId': '2fcf335b-fd38-4df4-ac6a-f52f4861c157', 'GlobalSecondaryIndexes': [{'IndexName': 'message-group-sk-index', 'KeySchema': [{'AttributeName': 'message_group_uuid', 'KeyType': 'HASH'}, {'AttributeName': 'sk', 'KeyType': 'RANGE'}], 'Projection': {'ProjectionType': 'ALL'}, 'IndexStatus': 'CREATING', 'ProvisionedThroughput': {'NumberOfDecreasesToday': 0, 'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}, 'IndexSizeBytes': 0, 'ItemCount': 0, 'IndexArn': 'arn:aws:dynamodb:ap-southeast-1:530454120249:table/cruddur-messages/index/message-group-sk-index'}], 'DeletionProtectionEnabled': False}, 'ResponseMetadata': {'RequestId': 'H9OFQP4LVAQUS8NOOT7PJH9RI7VV4KQNSO5AEMVJF66Q9ASUAAJG', 'HTTPStatusCode': 200, 'HTTPHeaders': {'server': 'Server', 'date': 'Sat, 01 Apr 2023 15:55:23 GMT', 'content-type': 'application/x-amz-json-1.0', 'content-length': '1155', 'connection': 'keep-alive', 'x-amzn-requestid': 'H9OFQP4LVAQUS8NOOT7PJH9RI7VV4KQNSO5AEMVJF66Q9ASUAAJG', 'x-amz-crc32': '3430233949'}, 'RetryAttempts': 0}}
gitpod /workspace/aws-bootcamp-cruddur-2023/backend-flask (main) $ 
```
- Remove the `#AWS_ENDPOINT_URL: "http://dynamodb-local:8000"` so that we can re-run the `docker-compose` using the `PROD` values

- Running the new frontend, `Messages` tab will show `EMPTY` but we need to set the url 
`https://3000-abheejain-awsbootcampcr-og9ik1hw5op.ws-us93.gitpod.io/messages/new/bayko`

wich once confirmed the user in the system, will `redirect` to the correct `Group UUID` 
`https://3000-abheejain-awsbootcampcr-og9ik1hw5op.ws-us93.gitpod.io/messages/a4b2807c-8ebd-426c-a1f5-6f9229cf9d9f`

FINISHED 


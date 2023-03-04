# Week 2 — Distributed Tracing


## Instrument our backend flask application to use Open Telemetry (OTEL) with Honeycomb.io as the provider
- Instrumented - Backend 
 
Connecting to the Honeycomb was just fixed by `exporting` the `key`

Proof of the Instrumentation with Honeycomb 
## Verificaton Image

![Instrumntation](assets/week-2/week2-honeycomb-start-receiving.png)


Adding span for the Mock-data in Honeycomb for the Home Page activites 
## Verificaton Image

![home-activities-mock-data](assets/week-2/week2-honeycomb-mock-span.png)


<hr>

## Run queries to explore traces within Honeycomb.io

Running various querries was done using the reference from https://docs.honeycomb.io/getting-data-in/opentelemetry/python/ to `acquiring the Tracer` and for `Query to trace` 

Various Queries run and results received for `app.data` and `app_results_length` 
## Verificaton Image
### ISOFormat Query
![Query](assets/week-2/week2-honeycomb-mock-span-isoformat-querry-results.png)


### Adding Span for Result Length 
![Query ](assets/week-2/week2-honeycomb-mock-span-results-length-max.png)


### Query for the P90ms on 
![Query ](assets/week-2/week2-honeycomb-querry-P90ms.png)

<hr>

## Instrument AWS X-Ray into backend flask application

- Setup X-Ray Traces 
After receiving JSON log 
https://ap-southeast-1.console.aws.amazon.com/cloudwatch/home?region=ap-southeast-1#xray:settings/groups

## Verificaton Image
![Setup X-Ray-Traces ](assets/week-2/week2-aws-xray-added-xray-traces.png)


- Added Sampling Rules using `AWS CLI`
    We used CLI, compared to the AWS Console because, the interface keep changing, but we know the values to set using CLI is easy.

## Verificaton Image
![Setup Sampling Rules using CLI ](assets/week-2/week2-aws-xray-added-sampleing-rule.png)

<hr>


## X-Ray Instrumented

## Verificaton Image
![AWS X-Ry INstrumented ](assets/week-2/week2-aws-xray-added-xray-instrumented.png)

<hr>

## Add X-Ray sub-segment

Ref: https://github.com/aws/aws-xray-sdk-python
Tried to workput with the `UserActivities` service, but received `500` error`. I would skip now and keep it for my extended homework 

<hr>

## Cloudwatch Instrumented
## Verificaton Image
![AWS Cloudwatch Log ](assets/week-2/week2-aws-cloudwatch-log1.png)

### Home Activities Cloudwatch Logs

## Verificaton Image
![AWS Cloudwatch Home Activities ](assets/week-2/week2-aws-cloudwatch-log-home-activities.png)

<hr>


## Integrate Rollbar for Error Logging

## Verificaton Image
![Roll Integration ](assets/week-2/week2-rollbar-setup.png)

New UI More events
## Verificaton Image
![Rollbar Integration2 ](assets/week-2/week2-rollbar-integration-new-ui.png)


<hr>

## Trigger an error an observe an error with Rollbar
## Verificaton Image
![Rollbar Integration ](assets/week-2/week2-rollbar-trigger-error.png)
 
Error Details
## Verificaton Image
![Rollbar Integration ](assets/week-2/week2-rollbar-trigger-error-details.png)

<hr>

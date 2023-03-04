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
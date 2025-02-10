# openmetadata-dremio-connector
Custom OpenMetadata connector to connect data from Dremio to OpenMetadata. 

This connector uses the [sqlalchemy-dremio](https://github.com/narendrans/sqlalchemy_dremio) package to establish a connection to Dremio over the arrow flight API. 

![Static Badge](https://img.shields.io/badge/Metadata-43a047?style=flat)
![Static Badge](https://img.shields.io/badge/Query_Usage-ff7c50?style=flat)
![Static Badge](https://img.shields.io/badge/Data_Profiler-ff7c50?style=flat)
![Static Badge](https://img.shields.io/badge/Data_Quality-ff7c50?style=flat)
![Static Badge](https://img.shields.io/badge/Lineage-ff7c50?style=flat)
![Static Badge](https://img.shields.io/badge/Column_level_Lineage-ff7c50?style=flat)
![Static Badge](https://img.shields.io/badge/dbt-ff7c50?style=flat)
![Static Badge](https://img.shields.io/badge/Owners-ff7c50?style=flat)
![Static Badge](https://img.shields.io/badge/Tags-ff7c50?style=flat)
![Static Badge](https://img.shields.io/badge/Stored_Procedures-ff7c50?style=flat)


## Installation

Refer to the official OpenMetadata documentation for installing custom database connectors: https://docs.open-metadata.org/latest/connectors/custom-connectors

## Configuration

This Connector is currently implemented as `CustomDatabase` connector and therefore the only way to configure any connection parameters is using the `connectionOptions`.

```yaml
config:
    type: CustomDatabase
    sourcePythonClass: metadata.ingestion.source.database.dremio.metadata.DremioSource
    connectionOptions:
        hostPort: <host>:<arrowFlightPort>
        username: <username>
        password: <password>
        # optional
        UseEncryption: False
        disableCertificateVerification: True
```

## Local Dev Stack

Requirements:
- Access to a Dremio instance

Steps:

1. Setup python venv and install dependencies with `pip install -e .`
2. Start openmetadata local stack
    ```bash
    make local-openmetadata-stack 
    ```
3. Create `workflow.dremio.yaml` as a copy from `workflow.dremio.template.yaml`
4. Configure `workflow.dremio.yaml`. Mainly editing connection credentials to Dremio and the jwtToken for OpenMetadata (e.g. from the ingestion bot)
5. Run / Debug ingestion
    ```bash
    metadata ingest -c ./workflow.dremio.yaml
    ```
    Or use the provided Run configuration for IntelliJ


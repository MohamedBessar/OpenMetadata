
from metadata.ingestion.source.database.dremio.metadata import DremioSource
from metadata.utils.service_spec.default import DefaultDatabaseSpec

ServiceSpec = DefaultDatabaseSpec(
    metadata_source_class=DremioSource,
    lineage_source_class="not.implemented",
    usage_source_class="not.implemented",
)

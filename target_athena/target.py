"""Athena target class."""

from singer_sdk.target_base import Target
from singer_sdk import typing as th

from target_athena.sinks import (
    AthenaSink,
)


class TargetAthena(Target):
    """Sample target for Athena."""

    name = "target-athena"
    config_jsonschema = th.PropertiesList(
        th.Property("s3_bucket", th.StringType, required=True),
        th.Property("athena_database", th.StringType, required=True),
        th.Property("aws_access_key_id", th.StringType),
        th.Property("aws_secret_access_key", th.StringType),
        th.Property("aws_session_token", th.StringType),
        th.Property("aws_profile", th.StringType),
        th.Property("delimiter", th.StringType, default=","),
        th.Property("quotechar", th.StringType, default='"'),
        th.Property("add_metadata_columns", th.BooleanType, default=False),
    ).to_dict()
    default_sink_class = AthenaSink
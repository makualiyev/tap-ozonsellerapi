"""OzonSellerAPI tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_ozonsellerapi import streams


class TapOzonSellerAPI(Tap):
    """OzonSellerAPI tap class."""

    name = "tap-ozonsellerapi"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        
        th.Property(
            "offer_id",
            th.StringType,
            description="The offer id to get product infos for v2 product info stream"
        ),
        th.Property(
            "offer_ids",
            th.StringType,
            description="The list with offer ids to get product infos for v2 product info stream"
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.OzonSellerAPIStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            # streams.v2CategoryTreeStream(self),
            # streams.v2ProductInfoStream(self, key_=self.config_jsonschema.get('offer_id')),
            streams.v2ProductInfoListStream(self, key_=self.config.get('offer_ids').split(',')),
        ]


if __name__ == "__main__":
    TapOzonSellerAPI.cli()

"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_tap_test_class

from tap_ozonsellerapi.tap import TapOzonSellerAPI


SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    # TODO: Initialize minimal tap config
}


# Run standard built-in tap tests from the SDK:
TestTapOzonSellerAPI = get_tap_test_class(
    tap_class=TapOzonSellerAPI,
    config=SAMPLE_CONFIG
)


# TODO: Create additional tests as appropriate for your tap.

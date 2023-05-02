"""Stream type classes for tap-ozonsellerapi."""

from __future__ import annotations

from typing import Any
from pathlib import Path

import requests
from singer_sdk import typing as th  # JSON Schema typing helpers
from singer_sdk.pagination import BaseAPIPaginator

from tap_ozonsellerapi.client import OzonSellerAPIStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class v2CategoryTreeStream(OzonSellerAPIStream):
    """Define custom stream."""

    name = "v2_category_tree"
    path = "/v2/category/tree"
    primary_keys = ["category_id"]
    records_jsonpath = "$.result[*]"

    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "v2_category_tree.json"

    def build_prepared_request(
            self, *args: Any, **kwargs: Any
    ) -> requests.PreparedRequest:
        prepared_request = super().build_prepared_request(*args, **kwargs)
        prepared_request.method = 'POST'
        return prepared_request

    def prepare_request_payload(
            self,
            context: dict | None,
            next_page_token
    ) -> dict | None:
        return {
            # 'category_id': 17031399
        }
    

class v2ProductListStream(OzonSellerAPIStream):
    """Define custom stream."""

    name = "v2_product_list"
    path = "/v2/product/list"
    primary_keys = ["product_id"]
    records_jsonpath = "$.result.items[*]"
    next_page_token_jsonpath = "$.result.last_id"
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    schema_filepath = SCHEMAS_DIR / "v2_product_list.json"
    

    def build_prepared_request(
            self, *args: Any, **kwargs: Any
    ) -> requests.PreparedRequest:
        
        prepared_request = super().build_prepared_request(*args, **kwargs)
        prepared_request.method = 'POST'
        return prepared_request
    
    def get_new_paginator(self) -> BaseAPIPaginator:
        return super().get_new_paginator()

    def prepare_request_payload(
            self,
            context: dict | None,
            next_page_token
    ) -> dict | None:
        return {
            # 'category_id': 17027492
        }
    

class v2ProductInfoStream(OzonSellerAPIStream):
    """Define custom stream."""

    def __init__(self, *args, key_: str) -> None:
        super().__init__(*args)
        self.key_ = key_
    
    name = "v2_product_info"
    path = "/v2/product/info"
    primary_keys = ["id"]
    records_jsonpath = "$.result"

    replication_key = None
    schema_filepath = SCHEMAS_DIR / "v2_product_info.json"

    def build_prepared_request(
            self, *args: Any, **kwargs: Any
    ) -> requests.PreparedRequest:
        
        prepared_request = super().build_prepared_request(*args, **kwargs)
        prepared_request.method = 'POST'
        return prepared_request
    
    def get_new_paginator(self) -> BaseAPIPaginator:
        return super().get_new_paginator()

    def prepare_request_payload(
            self,
            context: dict | None,
            next_page_token
    ) -> dict | None:
        return {
            'offer_id': self.key_
        }


class v2ProductInfoListStream(OzonSellerAPIStream):
    """Define custom stream."""

    def __init__(self, *args, key_: str) -> None:
        super().__init__(*args)
        self.key_ = key_
    
    name = "v2_product_info_list"
    path = "/v2/product/info/list"
    primary_keys = ["id"]
    records_jsonpath = "$.result.items[*]"

    replication_key = None
    schema_filepath = SCHEMAS_DIR / "v2_product_info.json"

    def build_prepared_request(
            self, *args: Any, **kwargs: Any
    ) -> requests.PreparedRequest:
        
        prepared_request = super().build_prepared_request(*args, **kwargs)
        prepared_request.method = 'POST'
        return prepared_request
    
    def get_new_paginator(self) -> BaseAPIPaginator:
        return super().get_new_paginator()

    def prepare_request_payload(
            self,
            context: dict | None,
            next_page_token
    ) -> dict | None:
        return {
            'offer_id': self.key_
        }
    
# Copyright 2025-present DatusAI, Inc.
# Licensed under the Apache License, Version 2.0.
# See http://www.apache.org/licenses/LICENSE-2.0 for details.

from datus.cli.main import ArgumentParser


def test_db_type_choices_are_user_facing_strings():
    parser = ArgumentParser().parser

    args = parser.parse_args(["--db_type", "duckdb"])

    assert args.db_type == "duckdb"
    assert "DBType.DUCKDB" not in parser.format_help()
    assert "{sqlite,snowflake,duckdb}" in parser.format_help()

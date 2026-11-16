# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:53:14 2026

@author: Admin
"""

import sys
from pathlib import Path

# Make sure Python can find the hr_pipeline folder
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Force Python to re-read our files from disk on every run
for name in list(sys.modules):
    if name.startswith("hr_pipeline"):
        del sys.modules[name]

from hr_pipeline.database import HRDatabase
from hr_pipeline.queries import BASIC_QUERIES, AGGREGATE_QUERIES


def run_queries(db, queries):
    """Run every query in the dictionary and print its result."""
    for title, sql in queries.items():
        print(f"\n=== {title} ===")
        print(db.query(sql).to_string(index=False))


def main():
    db = HRDatabase()
    db.connect()
    try:
        print("########## BASIC QUERIES ##########")
        run_queries(db, BASIC_QUERIES)

        print("\n########## AGGREGATE QUERIES ##########")
        run_queries(db, AGGREGATE_QUERIES)
    finally:
        db.close()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)

for gg in User.__table__.columns:
    print("{}: {}".format(gg, gg.type))

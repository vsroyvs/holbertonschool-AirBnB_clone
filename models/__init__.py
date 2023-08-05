#!/usr/bash/python3
"""
For import modules, packages
convert to paquets directories
also like a db engine
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

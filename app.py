import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# DB URI import for local workspace
from os import path
if path.exists("env.py"):
    import env

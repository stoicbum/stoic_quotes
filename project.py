from flask import Flask, render_template, request, redirect,url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Stoics, Quote, User

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Stoic Quotes"

#connect to Database and create database session
engine = create_engine('sqlite:///stoic.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

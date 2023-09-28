from flask import Blueprint
from ..controllers.user_controller import UserController

bp_servers= Blueprint("servers",__name__)
bp_servers.route("/", methods=["GET"])(UserController.get)
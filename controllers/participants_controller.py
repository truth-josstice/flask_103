from flask import Blueprint, jsonify, request, abort
from main import db
from models.participants import Participant
from schemas.participants_schema import participant_schema, participants_schema

participants = Blueprint('participants', __name__, url_prefix="/participants")

# Get route
@participants.route('/')
def get_participants():
    stmt = db.select(Participant)
    participants_list = db.session.scalars(stmt)
    result = participants_schema.dump(participants_list)
    return jsonify(result)

# Post route
@participants.route('/', methods=["POST"])
def create_participant():
    participant_fields = request.get_json()
    new_participant = Participant(
        address=participant_fields.get("address"),
        name=participant_fields.get("name"),
        phone=participant_fields.get("phone")
    )
    db.session.add(new_participant)
    db.session.commit()
    return jsonify(participant_schema.dump(new_participant))

# Delete route
@participants.route('/<int:id>/', methods=["DELETE"])
def delete_participant(id):
    stmt = db.select(Participant).where(Participant.id == id)
    participant = db.session.scalar(stmt)
    #error:
    if not participant:
        return abort (400, description="Participant doesn't exist")
    db.session.delete(participant)
    db.session.commit()
    return jsonify(participant_schema.dump(participant))


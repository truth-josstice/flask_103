from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.participants import Participant

class ParticipantSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Participant
        ordered = True
        include_fk = True
        load_instance = True

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)
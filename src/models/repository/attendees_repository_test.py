import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason = "Não necessita")
def test_insert_attendee():
    attendee_info = {
        "uuid": "meu-uuid-teste",
        "name": "meu-nome",
        "email": "meu-email3",
        "event_id": "uuid-test"
    }

    attendee = AttendeesRepository()
    response = attendee.insert_attendee(attendee_info)
    
    print(response)

def test_get_attendee_badge_by_id():
    attendee_id = "meu-uuid-teste"

    attendee = AttendeesRepository()
    response = attendee.get_attendee_badge_by_id(attendee_id)

    print(response)




    



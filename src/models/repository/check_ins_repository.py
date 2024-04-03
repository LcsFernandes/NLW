from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError

class CheckInRepository:
    def insert_check_in(self, attendee_id):
        with db_connection_handler as db:
            try:
                check_in = (
                    CheckIns(attendeeId = attendee_id)
                )
                db.session.add(check_in)
                db.session.commit()

                return attendee_id
            

            except IntegrityError:
                raise Exception("Check-in já cadastrado!")
            
            except Exception as exception:
                db.session.rollback()
                raise exception
from django.utils.crypto import get_random_string
from django.db import transaction
from evaluations.models import Evaluation, Key


class KeyRepository:
    MAX_ATTEMPTS = 3

    @transaction.atomic
    def create_keys(self, section):
        sid = transaction.savepoint()
        evaluation = Evaluation.objects.filter(semester=section.semester.id).filter(status=Evaluation.STATUSES[0][0])
        if evaluation:
            attempts = 0
            created = 0
            while created <= section.enrolled:
                try:
                    if created < section.enrolled:
                        Key.objects.create(
                            value=get_random_string(length=Key.KEY_LENGTH),
                            evaluation=evaluation[0],
                            section=section
                        )
                    else:
                        Key.objects.create(
                            value=get_random_string(length=Key.HELPER_KEY_LENGTH),
                            evaluation=evaluation[0],
                            section=section,
                            helper=True
                        )
                    created += 1
                except Exception:
                    if attempts >= self.MAX_ATTEMPTS:
                        transaction.savepoint_rollback(sid)
                        return False
                    attempts += 1
            transaction.savepoint_commit(sid)
            return True

    def delete_keys(self, section):
        evaluation = Evaluation.objects.filter(semester=section.semester.id).filter(status=Evaluation.STATUSES[0][0])
        if evaluation:
            try:
                Key.objects.filter(section=section.id, evaluation=evaluation[0]).delete()
            except Exception:
                return False
            else:
                return True

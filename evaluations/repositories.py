from django.utils.crypto import get_random_string
from evaluations.models import Evaluation, Key


class KeyRepository:
    def create_keys(self, section):
        evaluation = Evaluation.objects.filter(semester=section.semester.id).filter(status=Evaluation.STATUSES[0][0])
        if evaluation:
            created_keys = 0
            attempts = 0
            while created_keys < section.enrolled and attempts < 5:
                # Key.objects.create(value=get_random_string(length=5), evaluation=evaluation[0], section=section)
                # created_keys += 1
                # attempts += 1
                try:
                    Key.objects.create(value=get_random_string(length=5), evaluation=evaluation[0], section=section)
                except Exception:
                    pass
                    print('Flop!')
                    attempts += 1
                # I'll need to do more here.
                else:
                    created_keys += 1

            # Creating helper key
            attempts = 0
            while created_keys <= section.enrolled and attempts < 5:
                try:
                    Key.objects.create(value=get_random_string(length=6), evaluation=evaluation[0], section=section,
                                       helper=True)
                except Exception:
                    pass
                    print('Flop!')
                    attempts += 1
                # Come and console the system
                else:
                    created_keys += 1

    def delete_keys(self, section):
        evaluation = Evaluation.objects.filter(semester=section.semester.id).filter(status=Evaluation.STATUSES[0][0])
        if evaluation:
            try:
                Key.objects.filter(section=section.id, evaluation=evaluation[0]).delete()
            except Exception:
                pass
                print('Flop!')

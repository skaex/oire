from evaluations.repositories import KeyRepository


class SectionRepository:
    def __init__(self):
        self.key_repository = KeyRepository()

    def open_section(self, section):
        if section.status == section.STATUSES[1][0]:
            if self.key_repository.create_keys(section):
                section.status = section.STATUSES[0][0]
                section.save()
                return True
            else:
                return False

    def close_section(self, section):
        if section.status == section.STATUSES[0][0]:
            if self.key_repository.delete_keys(section):
                section.status = section.STATUSES[1][0]
                section.save()
                return True
            else:
                return False
        elif section.status == section.STATUSES[2][0]:
            if self.key_repository.delete_keys(section):
                section.status = section.STATUSES[3][0]
                section.save()
                return True
            else:
                return False
        else:
            section.status = section.status
            section.save()

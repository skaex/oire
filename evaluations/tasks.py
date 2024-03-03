from oire.celery import app
from sections.repositories import SectionRepository
from evaluations.models import Evaluation

@app.task
def open_all_sections(evaluation_id):
    evaluation = Evaluation.objects.get(id=evaluation_id)
    sections = evaluation.semester.section_set.all()
    section_repository = SectionRepository()
    for section in sections:
        section_repository.open_section(section)

@app.task
def close_all_sections(evaluation_id):
    evaluation = Evaluation.objects.get(id=evaluation_id)
    sections = evaluation.semester.section_set.all()
    section_repository = SectionRepository()
    for section in sections:
        section_repository.close_section(section)

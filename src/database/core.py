from taskiq import Context

from .models import Person


async def get_persons(context: Context) -> list:
    # querying the model and guetting results
    query = context.state.session.query(Person)
    return query.all()


async def add_person(context: Context) -> None:
    newPerson = Person(name="Henry")
    context.state.session.add_all([newPerson])
    context.state.session.commit()

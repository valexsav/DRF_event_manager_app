import factory.fuzzy
from factory import Faker
from .models import Event


class EventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Event

    title = Faker('text', max_nb_chars=20)
    description = Faker('text', max_nb_chars=100)
    date = Faker('date')
    time = Faker('time')
    total_tickets = factory.fuzzy.FuzzyInteger(800, 1000)
    available_tickets = factory.fuzzy.FuzzyInteger(200, 800)
    location = Faker('address', locale='pl_PL')
    category = Faker('text', max_nb_chars=20)
    organizer = factory.SubFactory('user.factories.OrganizerFactory')

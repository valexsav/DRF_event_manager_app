from .models import User
import factory.fuzzy


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')
    username = factory.Faker('user_name')


class GuestFactory(UserFactory):
    role = User.GUEST


class ParticipantFactory(UserFactory):
    role = User.PARTICIPANT


class OrganizerFactory(UserFactory):
    role = User.ORGANIZER

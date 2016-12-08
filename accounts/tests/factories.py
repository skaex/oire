import factory
from ..models import TESTING_PASSWORD, User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))
    username = factory.Sequence(lambda n: 'user-{0}'.format(n))
    password = factory.PostGenerationMethodCall('set_password', TESTING_PASSWORD)
    is_superuser = True

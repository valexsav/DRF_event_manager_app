from xcevent.test import TestCase

from user.factories import (
    OrganizerFactory,
    ParticipantFactory,
    UserFactory,
)


class EventViewSetTestCase(TestCase):

    def test_only_authenticated_users_can_see_events(self):

        for user in [
            OrganizerFactory(),
            ParticipantFactory(),
            UserFactory()
        ]:
            with self.subTest(user=user):
                self.set_user(user)
                response = self.client.get('/event/')
                self.assertEqual(response.status_code, 200)

        self.set_user(None)
        resp = self.client.get('/authors/')
        self.assertEqual(resp.status_code, 401)

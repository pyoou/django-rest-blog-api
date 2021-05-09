from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserAccount(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'user@test.com', 'username', 'firstname', 'lastname', 'password',
        )
        self.assertEqual(super_user.email, 'user@test.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertEqual(super_user.last_name, 'lastname')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'username')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                'user@test.com', 'username', 'firstname', 'lastname', 'password', is_staff=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                'user@test.com', 'username', 'firstname', 'lastname', 'password', is_superuser=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                '', 'username', 'firstname', 'lastname', 'password',
            )

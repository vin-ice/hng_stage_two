from unittest import TestCase
from models.user import User
import models


class TestUser(TestCase):
    def test_user_create(self):
        """user creation"""
        user_1 = User("Jane Doe", "No bio")
        self.assertIsInstance(user_1, User)
        assert hasattr(user_1, "name")
        assert hasattr(user_1, "value")
        assert hasattr(user_1, "user_id")

        args = {"name": "John Doe", "value": "No data yet!"}
        user_2 = User(**args)
        self.assertIsInstance(user_2, User)
        assert hasattr(user_2, "name")
        assert hasattr(user_2, "value")
        assert hasattr(user_2, "user_id")

        user_3 = User(name=user_1.name, value=user_2.value, user_id=user_1.user_id)
        self.assertIsInstance(user_3, User)
        self.assertEqual(user_3.name, user_1.name)
        self.assertEqual(user_3.value, user_2.value)
        self.assertEqual(user_3.user_id, user_1.user_id)

    def test_user_save(self):
        """tests save functionality"""
        user = User("John Doe", "Missing Info")
        self.assertIsInstance(user, User)
        user.save()
        self.assertIsNotNone(models.store.get("users", user.user_id))

    def test_user_get(self):
        user_1 = User(name="Kenny", value="The Gambler")
        user_2 = User(name="Jane Doe", value="Missing")

        user_1.save()
        saved_user_1 = models.store.get("users", user_id=user_1.user_id)
        self.assertIsNotNone(saved_user_1)
        assert hasattr(user_1, "name")
        assert hasattr(user_1, "value")
        assert hasattr(user_1, "user_id")
        self.assertIsNone(models.store.get("users", user_2.user_id))

    def test_from_store(self):
        """tests user's model static method: from_store"""
        user_1 = User(name="Cena", value="Can't see me!")
        user_2 = User(name="god", value="omnipotent")
        user_2.save()
        self.assertIsNone(User.from_store(user_id=user_1.user_id))
        record = User.from_store(user_id=user_2.user_id)
        self.assertIsInstance(record, User)
        assert hasattr(user_2, "name")
        assert hasattr(user_2, "value")
        assert hasattr(user_2, "user_id")
        self.assertEqual(record.user_id, user_2.user_id)
        self.assertEqual(record.name, user_2.name)
        self.assertEqual(record.value, user_2.value)

    def test_update_user(self):
        """"""
        u = User("Jane Doe", "No bio")
        u.save()
        instance = User.from_store(u.user_id)
        self.assertIsNotNone(instance)
        instance.name = "John Doe"
        instance.update()
        instance_2 = User.from_store(instance.user_id)
        self.assertIsNotNone(instance_2)
        self.assertEqual(instance_2.name, "John Doe")
        self.assertEqual(instance_2.user_id, u.user_id)
        self.assertEqual(instance_2.value, u.value)

    def test_delete_user_(self):
        """delete user data"""
        user = User(name="New", value="User")
        user.save()
        user.delete()
        self.assertIsNone(models.store.get('users', user.user_id))

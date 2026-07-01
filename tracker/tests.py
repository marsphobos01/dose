from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Med


class MedTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")

    def make_med(self, **overrides):
        defaults = {
            "user": self.user,
            "name": "Vitamin D",
            "dosage": 1000,
            "unit": "IU",
            "daily_amount": 2,
            "total_amount": 10,
            "expiration_date": timezone.localdate() + timezone.timedelta(days=30),
        }
        defaults.update(overrides)
        return Med.objects.create(**defaults)

    def test_mark_taken_subtracts_daily_amount_from_total(self):
        med = self.make_med()

        med.mark_taken()

        med.refresh_from_db()
        self.assertEqual(med.total_amount, 8)
        self.assertTrue(med.has_taken_today)

    def test_mark_taken_only_subtracts_once_per_day(self):
        med = self.make_med()

        med.mark_taken()
        med.mark_taken()

        med.refresh_from_db()
        self.assertEqual(med.total_amount, 8)

    def test_mark_taken_does_not_make_total_negative(self):
        med = self.make_med(daily_amount=2, total_amount=1)

        med.mark_taken()

        med.refresh_from_db()
        self.assertEqual(med.total_amount, 0)

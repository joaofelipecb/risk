from django.test import TestCase
from .models import AccountReceivable

class ProbabilityTest(TestCase):
    def test_sum(self):
        a1 = AccountReceivable(value=1000,probability=0.80)
        a2 = AccountReceivable(value=1200,probability=0.65)
        p = ProbabilityMulticiplicity([a1,a2])
        p.calculate()
        self.AssertIs(p.get_values(),[0,1000,1200,2200])
        

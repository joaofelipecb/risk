from django.test import TestCase
from .models import AccountReceivable
import riskApp.p26struct.ProbabilityMultiplicity

class ProbabilityTest(TestCase):
    def test_sum(self):
        a1 = AccountReceivable(value=1000,probability=0.80)
        a2 = AccountReceivable(value=1200,probability=0.65)
        p = riskApp.p26struct.ProbabilityMultiplicity.ProbabilityMultiplicity([a1,a2])
        p.calculate()
        values = list(map(lambda x: x.value, p.combinations))
        self.assertEquals(values,[0,1000,1200,2200])
        

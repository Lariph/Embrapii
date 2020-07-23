from django.db import models

TEST_TYPES = [
    ('RT', 'RT-PCR'),
    ('S', 'Sorologia'),
    ('AG', 'Teste Rápido - Antígenos'),
    ('AC', 'Teste Rápido - Anticorpos'),
]

TEST_RESULTS = [
    ('P', 'Positivo'),
    ('N', 'Negativo'),
]

class Pacient(models.Model):
    name            = models.TextField(max_length=100)
    birth           = models.DateField(auto_now=False, auto_now_add=False)
    test_type       = models.CharField(max_length=2, choices=TEST_TYPES)
    test_result     = models.CharField(max_length=1, choices=TEST_RESULTS)

    def __str__(self):
        return self.name
    




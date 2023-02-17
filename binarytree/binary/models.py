from django.db import models

class BinaryTree(models.Model):
    name = models.CharField(max_length=100)
    node_id = models.IntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.node_id})'

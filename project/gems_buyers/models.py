from django.db import models



class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    spent_money = models.IntegerField(default=0)
    gems = models.ManyToManyField("Gem", through="Customers_Gems", default='allGems')

    def __str__(self):
        return f"{self.username} - {self.spent_money}"

    def allGems(self):
        return self.gems.all()

class Deal(models.Model):
    customer = models.CharField(max_length=50)
    item = models.CharField(max_length=60)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField(unique=True)

    def __str__(self):
        return f"{self.customer} - {self.item}: {self.total}"


class Gem(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Customers_Gems(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    gem = models.ForeignKey("Gem", on_delete=models.CASCADE)

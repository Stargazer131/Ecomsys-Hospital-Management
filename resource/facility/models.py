from django.db import models
from inventory.models import Resource


class Building(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    floor = models.IntegerField()

    def __str__(self):
        return f"Room {self.room_number} in {self.building.name} on floor {self.floor}"


class Bed(models.Model):
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bed_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Bed {self.bed_number} in {self.room}"


class Furniture(models.Model):
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} in {self.room}"


class MedicalEquipment(models.Model):
    resource = models.OneToOneField(Resource, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50, unique=True)
    usage = models.TextField()

    def __str__(self):
        return f"{self.name} (SN: {self.serial_number}) in {self.room}"

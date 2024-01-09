#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app, db
from models import Owner, Pet

fake = Faker()

with app.app_context():
    # Clear existing data
    Pet.query.delete()
    Owner.query.delete()

    # Seed Owners
    owners = [Owner(name=fake.name()) for _ in range(50)]
    db.session.add_all(owners)

    # Seed Pets
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
    pets = [Pet(name=fake.first_name(), species=rc(species), owner=rc(owners)) for _ in range(100)]
    db.session.add_all(pets)

    # Commit changes
    db.session.commit()


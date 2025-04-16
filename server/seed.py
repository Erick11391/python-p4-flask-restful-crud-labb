#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():
    # Clear existing data using ORM
    Plant.query.delete()
    db.session.commit()  # Commit the deletion first
    
    # Add new plants
    plants = [
        Plant(
            name="Aloe",
            image="/images/aloe.jpg",
            price=11.50,
            is_in_stock=True,
        ),
        Plant(
            name="ZZ Plant",
            image="/images/zz-plant.jpg",
            price=25.98,
            is_in_stock=False,
        )
    ]
    
    db.session.add_all(plants)
    db.session.commit()
    print("🌱 Successfully seeded plants!")
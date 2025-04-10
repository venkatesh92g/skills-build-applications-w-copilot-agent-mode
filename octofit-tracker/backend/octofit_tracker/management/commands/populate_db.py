from django.core.management.base import BaseCommand
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the MongoDB database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)  # Update with your MongoDB host and port if different
        db = client['octofit_db']  # Update with your MongoDB database name

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": 'thundergod', "email": 'thundergod@mhigh.edu', "password": 'thundergodpassword'},
            {"_id": ObjectId(), "username": 'metalgeek', "email": 'metalgeek@mhigh.edu', "password": 'metalgeekpassword'},
            {"_id": ObjectId(), "username": 'zerocool', "email": 'zerocool@mhigh.edu', "password": 'zerocoolpassword'},
            {"_id": ObjectId(), "username": 'crashoverride', "email": 'crashoverride@hmhigh.edu', "password": 'crashoverridepassword'},
            {"_id": ObjectId(), "username": 'sleeptoken', "email": 'sleeptoken@mhigh.edu', "password": 'sleeptokenpassword'},
        ]
        db.users.insert_many(users)

        # Create teams
        team = {"_id": ObjectId(), "name": 'Blue Team', "members": [user["_id"] for user in users]}
        db.teams.insert_one(team)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": 'Cycling', "duration": timedelta(hours=1).total_seconds()},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": 'Crossfit', "duration": timedelta(hours=2).total_seconds()},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": 'Running', "duration": timedelta(hours=1, minutes=30).total_seconds()},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": 'Strength', "duration": timedelta(minutes=30).total_seconds()},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": 'Swimming', "duration": timedelta(hours=1, minutes=15).total_seconds()},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard_entries)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": 'Cycling Training', "description": 'Training for a road cycling event'},
            {"_id": ObjectId(), "name": 'Crossfit', "description": 'Training for a crossfit competition'},
            {"_id": ObjectId(), "name": 'Running Training', "description": 'Training for a marathon'},
            {"_id": ObjectId(), "name": 'Strength Training', "description": 'Training for strength'},
            {"_id": ObjectId(), "name": 'Swimming Training', "description": 'Training for a swimming competition'},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the MongoDB database with test data.'))
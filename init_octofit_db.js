// Connect to the octofit_db database
use octofit_db;

// Create the users collection and ensure a unique index on the email field
db.users.createIndex({ "email": 1 }, { unique: true });

// Create the teams collection
db.createCollection("teams");

// Create the activity collection
db.createCollection("activity");

// Create the leaderboard collection
db.createCollection("leaderboard");

// Create the workouts collection
db.createCollection("workouts");

// List all collections in the octofit_db database
print("Collections in octofit_db:");
printjson(db.getCollectionNames());

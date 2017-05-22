# django-ember-admin-template
A project template to generate pre-configured Django projects to function as APIs and Admin panel for Ember (or other javascript powered) applications.

##Technologies

Currently, the project template leverages:

- Django Whitenoise for static file serving (We are only serving the assets for the admin, so makes everything easier)
- Amazon AWS S3 for media storage
- PostgreSQL as a db backend
- Django Suit for making the admin page super cool.
- Django Filer for file uploads
- drf-schema-adapter to generate Ember models (can be used for other JS frameworks as well).

The app assumes that is gets mounted on a */backend* subpath. Let's say you have your public (static) site serving from http(s)://example.com.
This app should get mounted on the */backend* subpath, so you get the following links:

- http(s)://example.com/backend/admin/ , For admin panel access
- http(s)://example.com/backend/api/ , For serving your api to your app

##Configuration

The project expets a number of environment variables to be set in order to function. A list follows:

- *SERVER_TYPE*, value should be 'PROD' in production
- *DB_NAME*, name of the database
- *DB_USERNAME*, username of user with access to the db
- *DB_PASSWORD*, db user password
- *AWS_ACCESS_KEY_ID*,
- *AWS_SECRET_ACCESS_KEY*,
- *AWS_STORAGE_BUCKET_NAME*, bucket name on AWS S3 for media uploads
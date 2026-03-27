How to run the template project?

```
python manage.py migrate
python manage.py runserver
```

This app features image and text upload in the form of knowledge cards, allowing the user to store images and their relevant information. For ease of browsing, the system supports image search to more easily find uploaded knowledge cards. Images are stored in S3 buckets, text descriptions and image metadata is stored in a SQLite database.



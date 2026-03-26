How to run the template project?

```
python manage.py migrate
python manage.py runserver
```

Student code implementations on code-example

I modified the initial example code by implementing a histogram similarity formula based on cosine similarity for image comparison and to determine similarity percentages. I also modified the card image database to hold a field for the histogram signature, and to compute a histogram signature on image upload. 

I also implemented functionality for the image search. When initiated, the image search will compare histogram signatures between the inputted image and the image storage. It then returns a sorted list of cards which determine the order and amount of images that will appear when image search is completed.

I deployed this website on an EC2 instance and implemented S3 bucket storage for images uploaded.

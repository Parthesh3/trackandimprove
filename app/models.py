from django.db import models

# Create your models here.
class technology(models.Model):
    frontorbackchoice = [("frontend","Frontend"),("backend","Backend")]
    
    techname = models.CharField(max_length=200)
    techtype = models.CharField(max_length=200)
    f_or_b = models.CharField(max_length=200,choices=frontorbackchoice,null=True,blank=True)

    def __str__(self) -> str:
        return self.techname

class topics(models.Model):
    technology = models.ForeignKey(technology, on_delete=models.CASCADE)
    topics_name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f'{self.topics_name}'    

class subtopics(models.Model):
    topics_name= models.ForeignKey(topics,on_delete=models.CASCADE)
    subtopics_name = models.CharField(max_length=500)
    solutions = models.TextField()

    def __str__(self) -> str:
        return f'{self.topics_name} || {self.subtopics_name}'
    
class reusablecode(models.Model):
    technology = models.ForeignKey(technology,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    code = models.TextField()
    descriptions = models.TextField()

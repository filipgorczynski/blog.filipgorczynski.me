Title: Robot Framework - sprawdzenie, czy element zawiera kilka łańcuchów znaków
Date: 2019-06-12 09:21
Author: filipgorczynski
Category: Programowanie
Slug: robot-framework-sprawdzenie-czy-element-zawiera-kilka-lancuchow-znakow
Status: draft

```

Another option - write xpath that has three strings.  
i.e.  
```//element\[contains(text(),"stringA") and contains(text(),"stringB") and contains(text(),"stringC")\]```  
And use  
```Wait until page contains element```

```

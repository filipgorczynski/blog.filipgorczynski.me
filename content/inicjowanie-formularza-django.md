Title: Inicjowanie formularza Django
Date: 2017-10-08 07:51
Author: filipgorczynski
Category: Dobre praktyki, Programowanie, Rozwiązania
Tags: Django forms, initialize form
Slug: inicjowanie-formularza-django
Status: draft

[![Django Logo](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png?w=150){.alignleft .size-thumbnail .wp-image-1153 width="150" height="52"}](https://filipgorczynski.files.wordpress.com/2015/10/django-logo-positive.png)

 

 

Dodatkowe problemy, np. wyświetlanie komunikatów z błędami.

\[code language="python"\]  
\<pre\>def new\_topic(request, pk):  
board = get\_object\_or\_404(Board, pk=pk)  
user = User.objects.first() \# TODO: get the currently logged in user  
form = NewTopicForm(request.POST or \[\])  
if request.method == 'POST':  
if form.is\_valid():  
\# return naive\_approach(board, request)  
topic = form.save(commit=False) \# save() eturns an instance of the Model saved into the database  
topic.board = board  
topic.starter = user  
topic.save()  
Post.objects.create(  
message=form.cleaned\_data.get('message', ''),  
topic=topic,  
created\_by=user,  
)  
return redirect('board\_topics', pk=board.pk)

return render(  
request,  
'boards/new\_topic.html',  
{  
'board': board,  
'form': form,  
}  
)  
\[/code\]

\[code language="python"\]  
\<pre\>def new\_topic(request, pk):  
board = get\_object\_or\_404(Board, pk=pk)  
user = User.objects.first() \# TODO: get the currently logged in user  
form = NewTopicForm(request.POST or None)  
if request.method == 'POST':  
if form.is\_valid():  
\# return naive\_approach(board, request)  
topic = form.save(commit=False) \# save() eturns an instance of the Model saved into the database  
topic.board = board  
topic.starter = user  
topic.save()  
Post.objects.create(  
message=form.cleaned\_data.get('message', ''),  
topic=topic,  
created\_by=user,  
)  
return redirect('board\_topics', pk=board.pk)

return render(  
request,  
'boards/new\_topic.html',  
{  
'board': board,  
'form': form,  
}  
)  
\[/code\]

\[code language="python"\]\</pre\>  
\<pre\>def new\_topic(request, pk):  
board = get\_object\_or\_404(Board, pk=pk)  
user = User.objects.first() \# TODO: get the currently logged in user  
form = NewTopicForm(request.POST or \[\])  
if request.method == 'POST':  
if form.is\_valid():  
\# return naive\_approach(board, request)  
topic = form.save(commit=False) \# save() eturns an instance of the Model saved into the database  
topic.board = board  
topic.starter = user  
topic.save()  
Post.objects.create(  
message=form.cleaned\_data.get('message', ''),  
topic=topic,  
created\_by=user,  
)  
return redirect('board\_topics', pk=board.pk)

return render(  
request,  
'boards/new\_topic.html',  
{  
'board': board,  
'form': form,  
}  
)\</pre\>  
\[/code\]

\[code language="python"\]  
\<pre\>def test\_new\_topic\_invalid\_post\_data(self):  
url = reverse('new\_topic', kwargs={'pk': 1})  
response = self.client.post(url, {})  
form = response.context.get('form')  
self.assertEquals(response.status\_code, 200)  
self.assertTrue(form.errors)\</pre\>  
\[/code\]

# ExerciseTracker
<p>This is an application that tracks exercises, weights and calories. I post it, especially for the students in my IT 112 class to show 
extra techniques and tools that are not explicitly covered in class: these include:</p>
<ul>
<li>Using aggregate functions with data</li>
<li>writing classes in the model file that are not models but are used to manipulate model data</li>
<li>limiting the number of records to display</li>
<li>sorting or ordering the records displayed</li>
<li>Passing multiple values in the view context</li>
<li>Using if statements and other python structures in templates</li>
</ul>
<p>The first commit included all the models, views, and templates. I hope to add more comments and to expand the tests to show a complete set of 
unit tests.</p>
<p>The next commit added some tests. More to come.</p>
<p>The third commit added the wsgi file though I am not doing anything with it currently. It is important if one were to attach the django project to Apache and actually serve it to the world</p>
<p>Added a view and links to the table on the index page that shows the number of records in each database table. The links go to the appropriate page to provide details on each of the data sets. </p>
<p>Misc commit on 4-9-2022 uploaded a few changes to the html files, particularly stepstomiles.html where it added an if else structure.</p>
<p>In the journal commit I added an exercise journal with a form for entry and page for viewing.</p>
<p>For the expanded journals commit I limited the get journal entries to 5 entries but add a link to see all journal entries. All journal entries provides a table of all the journal entries by data and with title. Clicking on the title will return that complete journal entry. Additional note: I uploaded the pictures I am using but they are full sized. They really should be resized. If my site were actually online the pictures would take up unnecessary ram and resources. I may resize them in the near future.</p>
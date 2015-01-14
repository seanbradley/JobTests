I chose as the first task was to convert the CSV file into something that
could be leveraged either as the data file, or as a fixture for Postgres.
In keeping with my pre-existing AMI image, I chose the latter.

Django will not accept a CSV file for a fixture, and its fixtures require
primary keys...(which although can be set to null in order to load the
data, the CSV file had no PK field.)  So, first I had to add a PK field,
and rather than set the PK to null, I incremented it programmatically for
each line.  I then used the csvkit library to convert the CSV file to
JSON...and loaded it into Postgres as a fixture.

I then immediately generated a simple functional view with a filter for
returning matching VSNs to a results page...  Some basic validators test
if the submitted VSN exists, and/or if it is comprised of six letters
followed by six numbers.

Given the constraints of the assignment, I know, of course, I need a more
sophisticated implementation...

I didn't want to go with a full-blown solution like Haystack or Solr...
and, moreover, most plug-and-play third-party packages are meant more
for text search...like sifting through titles and content in blog posts.

I intuit there may be an intelligent way to do this without anything so
heavy-duty as Haystack...

    {vsn_input_by_user: number_of_alphanumeric chars_not_matching_vsns_in_database}

    test the above against each element in this array...

    [{vsn_in_database: number_of_astericks}, {anoher_vsn_in_database: number_of_astericks} ...]

    more_astericks = lower_weighted_matching_score

    return vsn_with_highest_weighted_matching_score


I also looked at, but did not yet implement, any of the following...

#DJANGO SIMPLE SEARCH
http://gregbrown.co.nz/code/django-simple-search/

Requires fulltext_indexes in Postgres...

http://wiki.postgresql.org/wiki/Full_Text_Indexing_with_PostgreSQL
http://www.postgresql.org/docs/9.1/static/textsearch-intro.html

Fast queries, but a bit more of a pain to implement.  I wanted to keep
things in the application layer.

I'm also of the mindset that class based views in Django make more sense
if you're subclassing other views. I did spend a good deal of time
hacking at several solutions involving class-based views.  I settled on
functional views.

http://stackoverflow.com/questions/13416502/django-search-form-in-class-based-listview

Along the lines of the above, I also looked at...


#QUERIES WITH KEYWORD ARGS
http://www.nomadjourney.com/2009/04/dynamic-django-queries-with-kwargs/

http://stackoverflow.com/questions/3246443/django-simple-search-form

http://stackoverflow.com/questions/2584502/simple-search-in-django

http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap

See http://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get


#DJANGO Q OBJECTS
After scouring docs on best practices with regard to leveraging Q objects,
I found this short but relatively old blog post by Daniel Lindsey of Toastdriven
(aka Haystack author)...

http://toastdriven.com/blog/2008/nov/09/quick-dirty-search-django/

...the gist of it is that it overrides the model manager, and implements
a Q object there, rather than in the view.


#REGEX BASED SOLUTIONS
I considered the following...

Split input string into two strings--an 'alpha_input_string' and a 'num_input_string'.

Compile a regex for each where...

p = re.compile( '(A|B|C..X|Y|Z)')

...AND later...

p = re.compile( '(0|1|2..7|8|9)')

...THEN...

p.subn = ('*', alpha_input_string)

...AND later...

p.subn = ('*', num_input_string)

The idea was, prior to searching, to return an array of strings--permutations
of each database record--to match against the string input by the user via
the app's form.  Each member of the array would be one permutation of
an existing database record (would've used itertools for that)...each permutation
in the array replacing the database record's wildcard characters with
possible / potential alphanumeric characters from the user's input (would've
used translate for that)...and then, once the array is constructed,
match the user input against the array's resultant members.  A separate
function would return a count of the total number of characters replaced
in matching permutations.

I guess I would have used translate to sub out alphanumeric characters of
returned database records, and then match and weight these records against
the user input. Obviously, it's an inarticulate and horrifically inefficient
idea with a lot of computational overhead...
http://www.tutorialspoint.com/python/string_translate.htm
http://docs.python.org/3/howto/regex.html#search-and-replace

I also considered using a regex to find the largest substring of VSNs in
the database that matched the input string...
http://docs.python.org/3/howto/regex.html#match-versus-search

Or, to flip the whole thing on its head: I'd have generated permutations
for the string input by the user--where each permutation substitutes every
increasing alphanumeric characters of the input string with astericks.
Then, I'd count astericks in each substring, sum the counts, compare matches,
and display the search match with the the least number of astericks.
http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python


#LEXERS / AHO-CORASICK
I also explored lexers, and other more advanced and/or algorithmic
solutions...to allow matching alphanumeric characters against the wildcard
characters in the database, including...

...the esmre library and the Aho-Corasick algorithm --  "a very fast algorithm
to match an input string against a set of patterns (actually keywords), that
are preprocessed and organized in a trie, to speedup matching".  Requires
knowledge of a trie as a data structure, as well as pre-processing the VSNs
as a trie.  Didn't have time to do this or to dig into it with greater
detail...and wasn't certain if it was an appropriate solution.

http://code.google.com/p/esmre/

http://stackoverflow.com/questions/7049894/how-to-efficiently-match-an-input-string-against-several-regular-expressions-at

http://papercruncher.com/2012/02/26/string-searching-using-aho-corasick/

Alternatively, use Car.objects.all() to return all car objects.  Split the
VSN fields off of the result use the VSNs to create a set of patterns to
be used by the Aho-Corasick algorithm.  Match the user's input string
against this table of patterns.


OTHER SOLUTIONS BEYOND ME TO IMPLEMENT QUICKLY
http://stackoverflow.com/questions/192957/efficiently-querying-one-string-against-multiple-regexes

Operate directly on the car_data.csv with shlex...
http://docs.python.org/2/library/shlex.html
http://pymotw.com/2/shlex/

http://www.gooli.org/blog/a-simple-lexer-in-python/

Use the Python wrapper for Google's RE2 (See https://pypi.python.org/pypi/re2/)
http://t3094.codeinpro.us/q/51501bcbe8432c04260fe629
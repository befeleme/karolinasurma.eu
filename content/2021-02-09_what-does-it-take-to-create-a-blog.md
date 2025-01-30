Title: What does it take to create a blog
Date: 2021-02-09 21:11
Category: Currents
Tags: pelican, coding, EN
Slug: what-does-it-take-to-create-a-blog


## Why blogging?

- My old domain was unused for the last few years. I had little idea what to put there though.
- Having a **showcase** of the things I do which may be interesting for the other people. 
- I **like writing** and miss it since I switched to tech. 
- There are all those tips from seniors to juniors about **writing down the lists of what you've learnt**. 
This makes sense as juniors tend to underestimate their progress in time.
So I treat this as an opportunity to have some edulog, maybe helpful for others, maybe just for me.
- And, of course, I just wanted to **build something with my own hands**! Well, not from scratch in this case.


## To blog or HOW to blog - that is the question

As a teenager I just created an account on Blogger and successfully blogged for another 10 years or longer. 
Blogger belongs to Google now and will probably end in a few years.

And being a wannabe coder, well, you just kind of **have to** create your own solution, isn't it right?
I've been using Python for pretty much everything in the last three years. 
Those, however, were just **scripts**. 
You run them with `python file.py` and never actually get to build a whole solution.
I felt like I lack the experience in **gluing things together**. 
It seemed like a natural solution to build upon my Python knowledge.

### Django? Yes, but.

How about Django? Django sounds cool! 
And I've been to a [Django Girls workshop](https://tutorial.djangogirls.org/en/), so this couldn't be that complicated, could it? 
I've spent a great time playing with a web application in Django. I really have! 
The app is connected to a *Postgres database*, uses those cool *Jinja templates*, I even used *Bootstrap* to make the site responsive, wrote a nice *admin interface* and made it possible to use *Markdown* in the blog posts. 

Then I realized I need *categories* and plenty of other changes that will require more time spent digging in application models and Jinja.
I started reading about deployment and went through what [Heroku](https://www.heroku.com/) has to offer.

I learned about the `DJANGO_SECRET_KEY` when I published the code of my app on GitHub and immediately got a warning e-mail that I've compromised something important.

The time has passed and I wasn't any closer to having the actual website out there. 
In fact it felt like learning programming: **with each step I was even further from my goal as I realized how much more I need to learn to make it happen**.


### Static and simple

I went to look for something more down-to-earth. 
I remembered [our project's blog](https://roboprojekt.pyladies.cz/) which was on the other side of the complexity spectrum: there were Markdown blog posts and deployment on commit on GitHub. 
No databases, minimum code, static site - suddenly this sounded so beautifully simple!
Why to overcomplicate things?
I took a long look at that other blog and realized it was built on the extension to [Pelican](https://blog.getpelican.com/) engine, which is written in Python. 
I looked also at Jekyll and later Hugo, but decided to stick to what seemed like a nice case of *gluing* task I intended to perform.

## Pelican

First things first: I went through all the [Pelican themes](http://www.pelicanthemes.com/). I was looking for something minimalistic yet pretty with a support of categories and optionally tags. 
That was surprisingly tough task.
One of the last on the list was [MinimalXY](https://github.com/petrnohejl/MinimalXY) by Petr Nohejl (funnily enough, a developer from Brno) which I felt in love with as soon as I saw it. 

So I was decided and could frantically start with edits:

- deleting plenty of code I didn't want. That was a nice exercise in reading someone else's code. 
- removing Google Analytics related code for now as I'm not sure I want to track anything here.
- installing the Open Sans font locally rather than fetching it from Google Fonts. 


## Out there
I was never inclined to frontend and have limited knowledge about its technologies. 
The edits I've made were nice small tasks forcing me to look for explanations around the Internet. 
It makes me still a bit uneasy that I don't understand everything in the project.

Inspired by Honza Javorek's [weeknotes script](https://github.com/honzajavorek/honzajavorek.cz/blob/master/weeknotes.py) I made a template generator to make it easier to add new posts. Thanks!
Many other inspirations came from the open source projects on GitHub. 
I took a look at deployment routines, went through some people's configurations and repository structures. 

And all of this crash course took place in around a week.
This time I feel like a winner :).

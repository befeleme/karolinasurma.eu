Title: The debug tale
Date: 2021-08-15 17:38
Category: Python
Tags: EN, coding
Slug: the-debug-tale

## Debugging

The word anyone attempting programming knows from the almost beginning.
You know, the moment you learn: if it doesn't work, look at the traceback, then add 153 `print` statements, then try to understand where the heck you forgot the missing parenthesis.

When some clever programmers told me to start using debugger, I gave it a try. 
But even after attending some workshops and reading tutorials, I wasn't sure why I'd ever want to use it.
After all, I could just run the application and see where it crashes.

## The right tool for the task. Which task?

Today I think it's a matter of presenting the use cases.
The typical story would be: *I write the application and it behaves strangely. So I run a debugger and...*.

My guess is that this is where the beginner stops. 
When all you've ever written are one-file scripts or very small programs, it sounds as if it's an overkill. Print & tracebacks will do. 

BTW, I recently found some clever senior programmers who admitted they use `print` too! No reason to be ashamed!

Let me present the other use cases that a junior may be more likely to meet.

*I have this script/tool that should do X. When I run it, it doesn't do X, instead it produces Y. I want to understand why.*

or: 

*I want to contribute to a big project that I found on GitHub which has got plenty of tasks labeled "Good first issue". There is a bug - when you do A, the B's output is corrupted. I want to understand the relationship between A and B.*
 
or - my _eureka_ case:

*I use the project that bundles a lot of libraries within. I want to use it with the libraries from the system instead. I want to test that it still works as expected.*

The common features of those use cases are:

- I'm not the author of the original code.
- I have to read a lot of code lines in order to start working on a task.
- The applications I want to understand don't have the conventional problems - they don't crash, no traceback is involved.
- The more complicated program, the more context there is to keep through many function calls.
- Constant adding and removing 153 `print` statements would be pain in the... fingers.

## Humans - not the right tool for the task

As a human without modern tools, you'd have to find that line and start displaying stuff: print variable's contents, check the function's call, find the function's definition, print some variables there, see there is another function's call making some transformation with your initial variable, so check its definition and -- why not -- add more prints there.

You could go the other way around and start with some import buried deep down in the module, and gradually find your way up to the user interface.

**Humans are capable of (if really motivated to...), but in fact don't excel in keeping the context through many files and levels of hierarchy.**
A computer is much better suited for the task. 

Depending on what tool you use, setting up a debugger can be as easy as setting a single breakpoint on the line that you're interested in. 
Now you have the tools to step into the functions and dig as deep as you need to.
You can see the contents of the variables or arguments that were passed on the go.
You can see the boolean evaluation of the statements and play interactively with the program's current state.

## Into the details

I came across this talk by Nina Zakharenko which I recommend if you want to get a sense of how a debugger can be useful for you: [Goodbye Print, Hello Debugger!](https://www.youtube.com/watch?v=5AYIe-3cD-s)

Let me include also the article about the various debugging techniques (not focused entirely on debuggers) which may be interesting in those traditional use cases, when it's your own application you deal with. [Ultimate Guide to Python Debugging](https://towardsdatascience.com/ultimate-guide-to-python-debugging-854dea731e1b) by Martin Heinz provides the means to having a clarity of how your program actually works. 

## Post scriptum

Finding a way to include the debugger into your workflow is not a trivial quest.
If you feel you haven't really found the convincing use case yet, there is nothing wrong to it.

In my original case, I realized it'd be great to use the debugger just as I headed to the **last** item on my library's list.
I would have saved many hours if I used it right from the start.
The taste of learning is sometimes bitter.

Since the _eureka_ moment I started using the debugger baked in my IDE more often. 
It is especially helpful when a script written by someone else doesn't produce the output I've expected. 
Ironically enough, the tool designed to find the flaws in the code seems to be as good in debugging humans.

> Oh, and by the way... If someone tells you that writing a readable code is important, just believe them.
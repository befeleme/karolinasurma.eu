Title: PEP 639 adventures
Date: 2025-07-28 18:00
Category: Python
Tags: EN
Slug: pep-639-adventures

With almost a year passing after the [PEP 639](https://peps.python.org/pep-0639/) was accepted, I was pondering whether it makes sense to note down some thoughts on the process.

But, since I want to keep a record (if only for my memory), let's dive straight in.

## PEP 639

In Fedora, we wanted this PEP. It standardized the licensing of distribution artifacts in terms of the license expressions (using [SPDX identifiers](https://spdx.dev/)),
and in terms of including license files in the distributions.
That would allow us to programmatically detect and mark license files.
In the meantime (it was the end of 2023), Fedora started migration from its bespoke licensing format to SPDX,
which opened the way to leverage the newly defined license expressions too.

Anything that touches **legalese in software development** is a tough sell.
There were two long PEP threads and two previous authors.
The PEP has been significantly reworked multiple times.
**My predecessors have done amazing job with all the research and specification definition**.
I thank them for their effort from the bottom of my heart.

As Fedorans, we were following the discussions around PEP, and when it looked like it could be rejected, I stepped up and decided to help bring it through the finish line.
I inherited the longest PEP in history written in the span of almost 4 years.

## The learnings

I had no previous knowledge of the PEP processes.
I knew I'd learn on the go. I did: there was facilitating the discussion, reacting to feedback, redrafting (in `rst`, which I also learned on the job).
Understanding multiple use cases.
Understanding what is and what isn't a specification.
Multiple changes to [packaging.python.org](https://packaging.python.org/en/latest/) (probably still not complete).
Post-acceptance discussions.
Waiting for build backends to implement and bring real feedback from the users.
Realizing mistakes and oversights.
A lot of community support and always a civil discussion, even in the moments of disagreement.

I didn't have a deadline in a traditional sense, but there was a sense of urgency: everyone, including the PEP delegate, was tired with the drag and it was quite clear that either we make it happen or it'll be dropped.
While gaining velocity through a project that was spanning months, I discovered a self-hack that helped me immensely: **I signed up to give two talks about the topic**, one on [Python Pizza](https://www.youtube.com/live/KdFXjYURlws?feature=shared&t=6520) in Prague (February 2024) and another at [EuroPython](https://www.youtube.com/watch?v=8PuhFlojJ2s) (July 2024).
They acted as soft deadlines: for the first one I researched the topic of licensing in Python ecosystem (while doing PEP edits in the background), for the second I brought the whole proposal publicly.
I can totally recommend this approach if you want to have one more motivator on a project.
I've been very fortunate to have the time allocated for this adventure by my employer.

## What next?

PEP 639 has been first, but certainly not the last licensing PEP in the Python packaging.
There have been use cases left over on purpose, with the aim to specify them in the future. The adoption in simple use cases - which are the overwhelming majority of Python projects (when the license of all distribution artifacts is the same) should be without issues.
What's being discussed now, is how to express the per-distribution license expression in those rare cases when they're different.
I keep my fingers crossed for the future PEPs authors!

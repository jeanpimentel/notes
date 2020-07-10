# How to Review Pull Requests


- [Automate](#automate)
- [Reviewing code is work](#reviewing-code-is-work)
- [Latency is Key](#latency-is-key)
- [Be Empathetic](#be-empathetic)
- [Code reviews for new joiners](#code-reviews-for-new-joiners)
- [Tone of the Review](#tone-of-the-review)
- [Use Emojis 😎](#use-emojis-)
- [Make Yourself More Familiar with the Code](#make-yourself-more-familiar-with-the-code)
- [Always Provide Suggestions for Code Improvements](#always-provide-suggestions-for-code-improvements)
- [Talking to Each Other](#talking-to-each-other)
- [Leave at Least One Positive Remark](#leave-at-least-one-positive-remark)
- [Code reviews are a tradeoff](#code-reviews-are-a-tradeoff)
- [Nitpick](#nitpick)
- [Use checklists](#use-checklists)


Approach code reviews with two key goals in mind: __allow for learning and growth__ of all parties and __ship healthy code__.


Reviewing someone else's code is not just a technical task, it's also a human one. That gives most of its delicateness.


A code review is not about going line by line and looking for fault in each line. A code review is about looking at the code as a whole to see how it fits into the larger system, is not just about being right or wrong. It is about understanding the author's approach and the implications of the code, transferring knowledge, and being collaborative. That isn't to say nit comments are never warranted, but they should not be the focus of the code review.


__No comment should be personal. No comment should be made about the author or the reviewer. A review must always be about the code!__


## Automate

If a computer can decide and enforce a rule, let the computer do it. Arguing spaces vs. tabs is not a productive use of human time. Languages and modern tooling pipelines have no shortage of ways to enforce rules (linting) and repeatedly apply them. Find your language's linter and plug it into your build pipeline.


## Reviewing code is work

It's value add to the company, so you should treat it as such and really own it. It's okay to spend many hours on reviewing code, and it's okay to call it out as what you're working on. Rushed code reviews will only come back to bite you in the future.


## Latency is Key

Turning around a Code Review quickly is incredibly important. Long Code Review latency can kill productivity and morale. Hearing about a PR you assigned for review 3 days ago is jarring. _Oh, yeah. What was I doing here?_ The back-and-forth is built-in context switching. Get your team caring about code review latency and get better as a team.


## Be Empathetic

As a reviewer, it's essential to provide feedback politely. Remember that you are reviewing your teammates' code who you like to talk to and go for team outings, lunches etc. Feelings can get hurt easily! So, be empathetic during your reviews.


Understand that someone put time into the code you're about to review. They want it to be great. Your coworkers behave with the best of intentions, and no one wants to ship crappy code.


## Code reviews for new joiners

Use the same quality bar and approach for everyone, regardless of their job title, level or when they joined the company. But pay additional attention to making the first few reviews for new joiners a great experience. Reviewers are empathetic that the recent joiner might not be aware of all the coding guidelines and might be unfamiliar with parts of the code. These reviews put additional effort into explaining alternative approaches, pointing to guides. They are also very positive in tone, celebrating the first few changes to the codebase that the author is suggesting.


## Tone of the Review

Did you know that in written communication, neutral content looks more negative than it actually is? The tone of code reviews can greatly influence morale within teams. Reviews with a harsh tone contribute to a feeling of a hostile environment with their microaggressions. Opinionated language can turn people defensive, sparking heated discussions. At the same time, professional and positive tone can contribute to a more inclusive environment. People in these environments are open to constructive feedback and code reviews trigger healthy and lively discussions. Also, avoid selective ownership of the code (that is, don't use "mine," "not mine," "yours"…) and don't be sarcastic, even if you are buddies as other reviewers/readers might find some comments inappropriate.


## Use Emojis 😎

Emojis are one of the best tools for improving your online communication. Using them automatically adds a friendly tone to your messages. You can use them when you start feeling that the conversation is getting too serious. But if that's not your style then don't force it, keep it real.


## Make Yourself More Familiar with the Code

Always get in the habit of teaching, it doesn't matter if you consider yourself a junior or a senior developer. Instead of telling them what the problem is, ask them questions, make them think and use a friendly tone. Here are a few examples:

- Do you think maybe we could assign this to a variable and re-use it on line 9?
- Could we possibly use this helpful utility that already does that for us which our dear teammate Sarah built?
- Can we move this code in its own function so we can write more tests?
- What do you think about trying this option?
- I'm not sure if I understand the whole picture, could you explain what this function is doing? 
    - This might make them think the function name could be renamed. After they explain what it does, then follow it up with a suggestion such as: _"I get it now, sorry! I'm not sure but do you think we could rename this function to option1, option2 or something along those lines, what are your thoughts"?_
    
Always ask them their thoughts, remember you are a reviewer, and they wrote the code so it's possible they have more context than you do.


Just imagine if your co-worker said something along the lines of, _"Don't do this, just rename the function"._ That phrasing is much harsher and less friendly than the example above. It sounds like you're giving them a command rather than taking into account their input.


## Always Provide Suggestions for Code Improvements

Rather than just telling them, _"this code could be improved"_. Provide them with specific suggestions/examples on how it could be improved further, such as:


> This code works perfectly but, after I started reading, I thought of another idea that I wanted to run it by you. I'm not sure, but what about:
> 
> sample code #1,
> 
> sample code #2
> 
> What are your thoughts?


Communicate which ideas you feel strongly about and which you don't. If you just express your preference, say that it's only your preference. If you suggest something, share proofs for why it's better (like articles, studies, books, and so on).


## Talking to Each Other

Reviewers should proactively reach out to the person making the change after they do a first pass on the code and have _lots of comments and questions_. These people have learned that they save a lot of time, misunderstandings and hard feelings this way, over going back-and-forth on the new revisions. The fact that there are many comments on the code indicates that there is likely some misunderstanding on either side.


These kinds of misunderstandings are easier identified and resolved by talking things through. When you meet face to face, you automatically develop more empathy and understand their point of view even further and alternatively, they understand yours. When you come to a conclusion, post a comment on the PR summarizing your discussion so other readers following along are aware of it and your future self will thank you for it.


## Leave at Least One Positive Remark

Code Reviews by their nature are negative affairs. _Tell me what's wrong with this code before I send it into the ether._ They are raw affairs. Someone spent time on this and there is the expectation that you will point out how it could be better.


For this reason, always leave at least one positive remark. Make it meaningful and personal. If someone has finally gotten the hang of something they've been struggling with, call it out. It can be as simple as a 👍 or a "_Love this._"


Leaving a few positive bits on each code review are subtle reminders that we're in this together. We all benefit if we create better code.


## Code reviews are a tradeoff

Because a piece of code has room for improvement, it doesn't always mean it needs to be improved. Code reviews are a tradeoff between quality and velocity and depending on the scope and stage of the project it might make sense to let a few things behind.

Don't increase the scope of the pull request. If you think of new things that need to be done, create a new pull request/task for that matter.


## Nitpick

While reviewing code, you may find something that is a nitpick i.e. it may not necessarily block the approval of the PR but is something to consider. Nitpicks are not important but technically correct. They can be related to grammar corrections, unintentional new lines, aesthetics, minor code refactor and more.


Too many nitpicks are a smell of lack of tooling or a lack of standards. Reviewers who come across these frequently will look at solving this problem outside the code review process. For example, most of the common nitpick comments can be solved via automated linting. Those that cannot, can usually be resolved by the team agreeing to certain standards, following them - perhaps even automating them, eventually.


## Use checklists

Omissions in particular are the hardest defects to find because it's difficult to review something that isn't there. Checklists are the most effective way to eliminate frequently made errors and to combat the challenges of omission finding. Code review checklists also provide team members with clear expectations for each type of review and can be helpful to track for reporting and process improvement purposes.


## Sources:

- [https://smartbear.com/learn/code-review/guide-to-code-review-process/]()
- [https://books.thoughtbot.com/assets/maintaining-open-source-projects.pdf]()
- [https://opensource.guide/best-practices/]()
- [https://rangle.io/blog/the-art-of-humanizing-pull-requests-prs/]()
- [https://dev.to/samjarman/giving-and-receiving-great-code-reviews]()
- [https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/]()
- [https://blog.pragmaticengineer.com/good-code-reviews-better-code-reviews/]()
- [https://www.freecodecamp.org/news/create-a-sane-office-environment-with-these-effective-code-review-guidelines-1d99ae2bdd47/]()
- [https://kellysutton.com/2018/10/08/8-tips-for-great-code-reviews.html]()
- [https://www.freecodecamp.org/news/a-zen-manifesto-for-effective-code-reviews-e30b5c95204a/]()
- [https://blog.plaid.com/building-an-inclusive-code-review-culture/]()
- [https://medium.com/unpacking-trunk-club/designing-awesome-code-reviews-5a0d9cd867e3]()

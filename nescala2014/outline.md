# Academese to English: Scala's Type System, Dependent Types and What It Means To You

**Abstract**
Lots of people talk about doing magic with Scala’s type system: “dependent
types”, “type-level computation", "typeclasses". What are dependent types
really? And what does Scala have to do with them? This talk will turn the
academese into English, starting with a whirlwind tour of Scala’s type system
and all the things that make people call it “powerful”. We’ll delve into what
dependent types are across different PLs like Coq & Idris, comparing
throughout with Scala. We’ll see how cool libraries like shapeless and spiral
fit into the picture. Finally, we’ll cover how dependent types are useful!

## Proposed Agenda

1. Whirlwind tour of Scala's type system
2. Type-level computation, type classes, dependent types – what are they?
3. Dependent types, history, and what they are in other languages
4. Dependent types in Scala, where shapeless and spire come in, what to expect from dotty?
5. Dependent types can be useful

Not sure if this is the best progression. I'd like to cover some other stuff,
like the sort of things covered in Ken's "Sexy Types in Action" paper.

Also wanted to talk about the powers and limitations of things like
existential types and higher-kinds.

Stuff that was promised in abstract:

- Scala's type system, and all of the things that make it powerful. 
- Coq and Idris, dependent types in those langauges
- Dependent types in Scala
- What type-level programming means

Simon Peyton Jones on Sexy Types (POPL talk 2003)

- Well typed programs don’t go wrong!
- Less mundanely (but more allusively) sexy types let you think higher thoughts and still stay [almost] sane:

    – deeply higher-order functions
    – functors
    – folds and unfolds
    – monads and monad transformers
    – arrows (now finding application in real-time reactive programming)
    – short-cut deforestation
    – bootstrapped data structures

Dependently typed programming languages: 

- Epigram
- Idris
- Coq

Indexed datatypes aren't really dependent types.

The motivation is to express application-specific properties that the typechecker can check.

Connection to domain-specific languages. You have an embedded DSL and you want
to have custom typechecking for the constructs in this language.

Type-level programming related to implicits. Adriaan's OOPSLA paper talks
about type-level programming.

Type-level computation: what is it?
You compute a new type at compile-time given other types.
(Slide with people talking on twitter about type-level computation)

**Can't forget to do...**<br/>
Help Martin make points about dotty simplifications – the why's<br/>
The practical troubles with some of these features

**Possible intro...?**
Think about all the cool stuff you can do without type systems. Recursion,
etc. Let's do all of that _with_ the type system. What does this even mean?
Why is it useful?

## Dependent Types

Scala has only path-dependent types. That's all. 

A dependent method type is the type of method which includes the entire
signature of the method. If there is a path-dependent type occurring in the
method type in a way where that path-dependent type refers to a parameter of
the method, then the method has a dependent method type.

    def m(x: C)(y: x.D): ...

Dependent method types. What are dependent method types useful for?

**Dependent method types** 

A method has a result type that refers to the method's parameters then the
method has dependent method type.

    def m(x: T): x.C

Where do indexed datatypes fit in? We can have these in Scala. Shapeless has
them. (I think?)

What are all of the ways that types can be "dependent" in other languages?


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


## Introduction

[Page limit: 14 pages including references.]
Serialization or pickling, i.e., persisting runtime objects by
converting them into a binary or text representation is ubiquitous in
distributed programming.

There has never been a Scala-specific solution to serialization which
can support certain aspects of Scala's type system, nor which can
generate serialization-related boilerplate at compile-time. Even the
fastest Java serialization frameworks must generate all
pickler-related code at runtime, which in preliminary benchmarks
amounts to a factor 10 slow-down over a naive but fully-static pickler
combinator-based approach.

The goal of this project is a new framework for pickling (or
serialization). The idea is to automatically generate pickler
combinators at compile-time.

The main contribution would be to extend existing approaches to
pickler combinators with support for object-oriented mechanisms, such
as subclassing.

#### Guiding Principles

Scala Pickling should be:

- more typesafe than Java serialization.
- faster than Java serialization.
- more extensible than Java serialization.
- but should not be more complicated to think about than Java serialization.

### Related Work

Figure **[ABOVE]** compares the main pickling/serialization
frameworks with respect to type-safety, object-orientation, type
extensibility, and format extensibility.

### Contributions

- A new pickling framework for object-oriented languages that (a)
  is fast through compile-time generated picklers, (b) enables
  retrofitting pickling support to existing types retroactively, (c)
  supports pluggable pickling formats, and (d) does not require
  changes to the underlying VM.

  The framework is thus extensible in several dimensions: first,
  pickling can be enabled for classes that have not been prepared
  beforehand (through extending a specific interface, for
  example). Second, new pickling formats (JSON, XML, Protobuf, etc.)
  can be added and selected modularly.

- Our approch extends pickler combinators (a well-established
  approach in the functional programming
  community~\cite{Kennedy,Elsman}) to support core concepts of
  object-oriented programming, namely open class hierarchies and
  ad-hoc polymorphism (runtime dispatch).

- To the best of our knowledge we are the first to extend pickler
  combinators with pluggable pickling formats.

- We present a complete implementation of our approach in
  Scala. (http://github.com/heathermiller/scala-pickling/) We have
  evaluated our framework by comparing its performance with the native
  serialization support of the Java Virtual Machine, as well as the
  Kryo serialization framework~\cite{Kryo} for Java. In the context of
  a suite of microbenchmarks, our framework outperforms Java
  serialization by a factor of X, and Kryo by a factor of Y. We have
  also integrated our pickling framework in Spark~\cite{Zaharia2010}
  and Akka~\cite{Akka}, and found that on representative applications
  our pickling framework improves performance by $X \%$ (Spark) and $Y
  \%$ (Akka) on average without requiring changes in user code.

Other points to include:

- has the benefits of pickler combinators, composable and user-definable
- run-time fallback in the case that a compile-time pickler can't be generated, so everything can always be pickled


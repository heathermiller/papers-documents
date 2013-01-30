---
layout: page
title: Scala Pickling <i>[Design Document]</i>
---

{{ site.author.twitter }}

<!-- Serialization, or _pickling_ in Scala has always depended Java-based
frameworks or libraries-- most famously, the JVM's built-in runtime
serialization. Most of these frameworks automatically take care of serialization for the
programmer, but do so at runtime, incurring a considerable runtime performance hit.

Pickler combinators have been long been thought of as the most robust approach
to serialization in functional languages. Pickler combinators compose
elegantly, but are considered a major source of boilerplate to manually write. -->

There has never been a Scala-specific solution to serialization which can
supports certain aspects of Scala's type system, nor which can generate
serialization-related boilerplate at compile-time. Even the fastest Java
serialization frameworks must generate all pickler-related code at runtime,
which in preliminary benchmarks

**Guiding principles:**

- Should be more typesafe than Java serialization.
- Should be faster than Java serialization.
- Should be more extensible than Java serialization.
- Should not be more complicated to think about than Java serialization.

**Short-term goal:** submission to OOPSLA 2013.

**Medium-term goal:** SIP and inclusion in Scala 2.11.

## Design

We're building a framework for pickling (or serialization). The idea is to
automatically generate picklers. The main contribution would be to extend
existing approaches to pickler combinators with support for OO mechanisms,
such as subclassing. An ideal plan for the design is below. The hope is that
we can work together on the code generation parts of this.

A crucial part of the entire effort is the generation of the pickling code at
compile time. For example, one would expect to be able to call `pickle` on an
arbitrary object, via an implicit conversion or an implicit class. For
example,

    implicit class PickleOps[T](x: T) {
      def pickle(implicit pickler: Pickler[T]): Pickle[T] = ...
    }

Note that the implicit `pickler` argument should be generated automatically.
There are some difficulties. For example, if `T` is a class `C` with private
fields, then the `Pickler[C]` would need to have access to those fields.

One approach would be to generate this `Pickler[C]` in `C`'s companion object.
However, when compiling class `C` it cannot, in general, be known whether
instances of this class are going to be pickled in other parts of the program
(those other parts could be separately compiled). There is a case, though,
where we have more information. For example, when class `C` is compiled in a
compilation unit which also contains code which requires an implicit value of
type `Pickler[C]`, then we know instances of class `C` are potentially
pickled. In that case, we could generate the pickler in `C`'s companion
object.

If we cannot add the pickler to the companion object of a class, because we
don't know whether instances of that class are ever pickled, we need to fall
back to a dynamically-generated pickler. Apart from a difference in accessing
private fields, the code for a fall-back pickler should be the same as for a
regular pickler, except that the generation of the fall back is executed at
runtime.

    implicit val pickler: Pickler[C] = new Pickler[C] {
      def pickle(o: C): Pickle[C] = {
        // obtain types of fields
        // obtain superclass (if any)
        // ...
      }
    }

Another issue is constructor parameters. To get access to those for pickling,
we could generate synthetic private fields inside the class, which could then
be accessed inside the companion object.

    class Person(name: String, age: Int) {
      var grades = List[String]()
      // synthetic:
      private def ctorArgs: Array[Any]
    }

    object Person {
      implicit val pickler: Pickler[Person] = {
        // look up/generate picklers for types of fields: String, Int, List, ...
      }
    }

One tricky bit is to be able to add members both to the class and its
companion object. To be idealistic, let's assume we can do this for now.

The `Pickler[T]` trait contains a method `unpickle` which takes a pickled
representation of type `T` (could be an `Array[Byte]`) and returns a `T`. The
unpickling code comprises:

  1. code to create a new instance of type `T`
  2. code to re-initialize `T`'s fields

How to generate _unpickling code_ for a `Pickler[C]` where `C` is a class with
a superclass different from `AnyRef`? Example:

    class C extends D {
      var x: Int = _
    }
    class D {
      var s: String = _
    }

Idea: 1. create new instance `c` of class `C`. Re-initialize `c`'s fields
using `reinit` methods (`fieldVals` is an `Array[Any]` with the unpickled
field values):

    val c = new C
    picklerC.reinit(c, fieldVals)

The `reinit` method of `Pickler[C]` uses `reinit` of the looked-up
`Pickler[D]`:

    def reinit(c: C, fieldVals: Array[Any]) {
      c.x = fieldVals.head.asInstanceOf[Int]
      picklerD.reinit(c, fieldVals.tail)
    }



## Class without constructor parameters or private fields

Q: where to put the implicit picklers in that case?





How to support separate compilation? Let's assume class `Person` has been
compiled. Then, we compile code which demands a `Pickler[Person]`. We somehow
need to generate accessors for `Person`s constructor parameters retro-actively
in class `Person`.

(One approach could be to use a Java agent that rewrite the bytecode of class
`Person` when `Person` is loaded.)


    person.pickle(<implicit pickler>)


Table of picklers.


generate extra stuff for types `T` where in some part of the program we need
an implicit of type `Pickler[T]`?





class C {
  private val privfld: String = ...
  val pubfld: Int = ...
}

object C {
  implicit val pickler: Pickler[C] = ...
}


class C extends D {

}


class C(x: Int) {
  private val ctor_x: Int = x
}

object C {

}


o: T
o.pickle


                                                             ---
layout: page
title: Pickler Framework Design and Implementation Notes <i>[February 5th, 2013]</i>
---


## Pickler generation at compile-time

Our goal is to generate both the `IR` and the `Pickler` at compile-time,
during macro expansion.

Then we can have rules for when an IR can be generated from a type.

1. Build the IR at compile time.
2. Generate template Expr, the code that we want to execute at runtime.
(Essentially the runtime version of newObject and newField methods in
PickleFormat). Genraete this from comile-time IR.

Advantage of IR is that there's no additional stuff like methods, type
members, etc. All modifiers of methods. All of the stuff that I can find in
the symbol table, i.e., it doesn't matter for serialization.

Another advantage is that it can be close to a possible formalization in the
paper. "From a program, we can assume that we can extract this IR". All rules
would be based on the IR.

## Changes that need to be made...

Modify the IR to remove the values. Then we can create the IR at compile-time.
And then we can use the runtime instance of the PickleFormat that we have at
compile time to produce an Expr given that IR. We call the write method at
compile time.

## Deciding when to generate a pickler

Given an object with a number of fields, we could first try to search for an
implicit `Pickler` of the correct field type. (This could be, for example, a
`Pickler[Int]`). _We search for this with macro expansion disabled._

    // to pickle a field (i.e. to generate the pickler), we need:
    // 1. PickleFormat
    // 2. Type

Now, it's possible that there's no implicit found.
If there's no implicit found, we call genPickler ourselves. We call it directly.
We need to be able to call this genPicklerImpl method...

## Status/Plan

Next steps:

1. Change the IR to remove the values. That is, don't store values at all.
Keep only their types and the names of the fields. Wherever there's a value,
remove it. IR should be at compile-time only, so no need to ever have a value
in it.

2. Expand on the code which inspects the fields (in `pickle` macro). After
`fields` method in `package.scala`, we can create an instance of the IR by
passing in the information we obtained from the fields. And the type of the
object. Now we can simply create instances of ObjectIR and FieldIRs for each
field. Each field, when we create a FieldIR, it has to create ObjectIRs for
the fields. Make sure nesting is happening if a FieldIR has some type that
should be an ObjectIR.

3. After we built the IR, we can use it to generate the template Expr. We can
pass the IR to the PickleFormat, and it generates an expression so that when
we run the Expr at runtime, passing in the runtime values for the fields etc,
so we fill in the values of the already-generated pickle template.


Flat: fast
Nested: human-readable


    Pickle template: (this is created at compile-time using the IR by the PickleFormat)
    {
        "tpe": "Person",
        "name": "___",
        "age": "___"
    }

    Completed pickle (this is created at runtime using the pickle template and the runtime values):
    {
        "tpe": "Person",
        "name": "Bob",
        "age": "56"
    }

    Scala Binary Format:
    [Type | Value(s)]


    case class Profession(name: String, since: Int)

    class Person {
      val name: String
      val age: Int
      val prof: Profession
    }

    [Person | "Bob", 56, [Profession | "Cabinetmaker", 1999]]

    {
        "tpe": "Person",
        "name": "Bob",
        "age": "56",
        "prof": {
            "name": "Cabinetmaker",
            "since": 1999
        }
    }


## Builder Pattern for Pickler Templates

Idea is that we call a method that returns a builder. We ask the pickle format
for a builder that we can use to build this template.

We pass it a macro context, and that... After done inserting, we call `result`
on builder and we should have the finished pickler template.


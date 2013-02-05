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

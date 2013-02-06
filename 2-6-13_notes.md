---
layout: page
title: Pickler Framework Design and Implementation Notes <i>[February 6th, 2013]</i>
---

## Making PickleFormat do all the work of generatig the pickle at compile time

Given that we want to have the following methods:

    def genObjectTemplate
    def genFieldTemplate

Both of these messages serve to, given the intermediate representation, produce a _template_ that should be used at runtime.

#### Problems

Can't call methods on `PickleFormat` at compile-time. This is because we mix
the things that are computed at compile-time with the things that we generate
to be run at runtime.

So, back to the drawing board! Need a different approach.
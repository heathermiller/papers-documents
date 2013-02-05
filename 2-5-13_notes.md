---
layout: page
title: Pickler Framework Design and Implementation Notes <i>[February 5th, 2013]</i>
---

## Deciding when to generate a pickler

Given an object with a number of fields, we could first try to search for an
implicit `Pickler` of the correct field type. (This could be, for example, a
`Pickler[Int]`). _We search for this with macro expansion disabled._



## Pickler generation at compile-time

Our goal is to generate both the `IR` and the `Pickler` at compile-time,
during macro expansion.

    // to pickle a field (i.e. to generate the pickler), we need:
    // 1. PickleFormat
    // 2. Type

Now, it's possible that there's no implicit found.
If there's no implicit found, we call genPickler ourselves. We call it directly.
We need to be able to call this genPicklerImpl method...
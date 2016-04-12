// The references are persisted at machine 1 but the actual data,
// the silos are hosted at machine 2.
val persons: SiloRef[List[Person]] = ... 
val isGrown: Spore[Person, Boolean] = spore { ps => ps.filter(p => p.age >= 18) }
val adults: SiloRef[List[Person]] = persons.map(isGrownUp)

// The references are persisted at machine 1
// but the actual data is distributed:
//   adults   @m1 --> Silo[List[Person]]            @m2
//   vehicles @m1 --> Silo[List[Vehicle]]           @m3
//   owners   @m1 --> Silo[List[(Person,Verhicle)]] @m3
// In order to create `owners`, we combine data hosted
// at `m2` and `m3` and store the result at `m3`. In case of
// materialization is forced, first transfer to `m2` the vehicles
// SiloRef and the closure (line 18). Next, transfer to `m3` the
// adults from `m2` and the closure (line 20).
// Now, at `m3`, we've the adults `ps` and vehicles `vs` and can
// combine correspondingly, resulting in a new SiloRef at `m3`
// referencing the new silo of List[(Person,Vehicle)] at `m3`.
// Eventually this new SiloRef at `m3` is tranferred back to
// `m1` and stored in `owner`.
val vehicles: SiloRef[List[Vehicle]] = ...
val owners: SiloRef[List[(Person,Vehicle)]] =
  adults.flatMap(spore {
    val localVehicles = vehicles
    ps => localVehicles.map(spore {
        val localPersons = ps
        vs => localPersons.flatMap(p => vs.flatMap(v =>
          if(v.owner.name == p.name)
            List((p,v))
          else Nil
        ) )
  }) })

# REshare - A Reverse Engineering Exchange Format

A human- and machine-readable schema to represent knowledge obtained during reverse engineering.Inspired by [Travis Goodspeed – A Keynote in Praise of Junk Hacking](https://www.youtube.com/watch?v=HyTkqcfSv4w).

With an exchange format we only have to implement a single importer/exporter pair for each tool we want to support to be able to transfer data between all tools. 

The repo contains a [JSON Type Definition](https://jsontypedef.com/) that can be automatically converted to serializers/deserializers in multiple languages using `jtd-convert`. 

With serializers we can build source-specific exporters to generate JSON representation of program information from arbitrary sources. We are currently aware of the following exporters:

* [reshare-pdb](https://github.com/v-p-b/reshare-pdb) - Export from PDB
* [reshare-pyghidra](https://github.com/v-p-b/reshare-pyghidra) - Export from Ghidra

With deserializers we can build target-specific importers to provide the information in the REshare JSON representation to arbitrary tools. We are currently aware of the following importers:

* [reshare-pyghidra](https://github.com/v-p-b/reshare-pyghidra) - Import to Ghidra
* [reshare-r2](https://github.com/v-p-b/reshare-r2) - Import to r2

**The type definition is currently highly unstable. Expect breaking changes and always pin exact library versions in your tools!**

## Principles of the data model

* **Embrace redundancy** - Redundant data can be used by importers for error recovery.
* **Flexibility** - Export what you can. Most properties are optional, while extra information can be embedded in the output. (Note: we will enable JTD's `additionalProperties` once the code is somewhat stabilized and we ahve enough tests)
* **Reasonable abstractions** - We aim to support common architectures and formats. If you need something special, feel free to create a variant!

## Building

Use the provided `Makefile` - we assume `./jtd-codegen` to be present in the current directory, but you can override that:

```
$ make java
$ JTD=/path/to/jtd-codegen make python
```

Currently Python and Java generation are implemented. `make format` formats the JTD definition with `jq`.

### Java

Gradle configuration is provided to build a library from the generated code:

```
java/ $ ./gradlew jar # builds simple Jar 
java/ $ ./gradlew shadowJar # builds fat Jar with dependencies included
```

## Contributing

Please use the `make format` command before sending patches!

JTD generated code should not appear in the repo. 


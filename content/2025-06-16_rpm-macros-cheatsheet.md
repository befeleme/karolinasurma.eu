Title: RPM macros cheatsheet
Date: 2025-06-16 16:24
Category: Fedora
Tags: EN, fedora, tools
Slug: rpm-macros-cheatsheet

## Architecture macros

Basic filtering
```
%ifarch
%ifnarch
```

Macros applicable to Fedora
```
%ix86   i386 i486 i586 i686 pentium3 pentium4 athlon geode
%x86_64	x86_64 x86_64_v2 x86_64_v3 x86_64_v4 amd64 em64t
%arm64	aarch64
%power64	ppc64 ppc64p7 ppc64le
%riscv		%{riscv32} %{riscv64} %{riscv128}
```

s390x doesn't have a macro, use the string.

[Full list of arch macros](https://github.com/rpm-software-management/rpm/blob/f8fb0690582b60307c7ec6f8babb48d49b2578ad/macros.in#L1121)

Note: `%{java_arches}` is there if needed.

Super important note: If a package is noarch, you can't filter the arches with `%ifarch`/`%ifnarch`, `%ifarch` in such case only matches `noarch`.
This only works correctly for arched packages.

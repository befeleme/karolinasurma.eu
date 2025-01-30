Title: fedrq - querying Fedora repositories
Date: 2024-02-29 16:18
Category: Fedora
Tags: EN, fedora, tools
Slug: fedrq-querying-fedora-repositories

## Querying repositories

Part of my $DAILYJOB is digging in multiple Fedora repositories.
Every time I prepare a package update, I check whether the update has a potential to break something.
Typically I set up lists of packages that require my package and build them in a isolated environment, before hitting the real Fedora.
I heavily use Copr as a test bed (described in detail in the talk from [DevConf 2023](./devconf-2023-packaging-talk.html)).
In that talk I show and comment a bunch of repoqueries.
Repoqueries do the job, but they're nearly-impossible to come up with (correctly) and if I lost my bash history, I'd be left crying on the floor.
(_Not really though_, in the end I've got the talk recording \<evil laughter\>).

## fedrq

This is where [fedrq](https://fedrq.gtmx.me/) comes to the scene. A new tool with a new approach by an incredibly active Fedora community member, gotmax23.
I spent a jolly day with it and decided to create this cheatsheet to help me translate my use cases to fedrq and ease the migration.

## Cheatsheet

### formatters

Powerful feature of the tool; list them all with:
```
$ fedrq formatters --attrs
```
And format the output of the tool with `-F <formatter>`.
Many more things are possible, refer to [the documentation](https://fedrq.gtmx.me/fedrq1/#formatters_1).

### What package does a file belong to?

```
# Fedora Rawhide
$ fedrq pkgs -P /usr/bin/python3
# Fedora 39 (-b, --branch)
$ fedrq pkgs -b f39 -P /usr/bin/python3
# Koji - format output with name-version-release-repository
$ fedrq pkgs -r @koji:rawhide -P /usr/bin/python3 -F nevrr
# Copr repository (-r, --repo)
$ fedrq pkgs -r @copr:@python/python3.13 -P /usr/bin/python3
```

### List all files from the package

```
$ fedrq pkgs python3-rich -F files
```

### What's the full package name?

```
$ fedrq pkgs python-rich
python-rich-13.7.0-5.fc40.src

$ fedrq pkgs python3-rich
python3-rich-13.7.0-5.fc40.noarch
```

### What packages will be built from my source component?

I can also format output to get only names: `-F name` or full nevr `-F nevr`; or skip formatter at all.

```
$ fedrq subpkgs python-sphinx -F nev
python-sphinx-doc-1:7.2.6
python3-sphinx-1:7.2.6
python3-sphinx-latex-1:7.2.6
```

### The opposite: What source rpm comes my built package from?

It can take also the base name: `python3-sphinx-latex`.

```
$ fedrq pkgs python3-sphinx-latex-1:7.2.6-6.fc40.noarch -F source
python-sphinx
```

### Provides and requirements of my components

```
$ fedrq pkgs python3-sphinx -F provides
python3-sphinx = 1:7.2.6-6.fc40
python-sphinx = 1:7.2.6-6.fc40
python3.12-sphinx = 1:7.2.6-6.fc40
python3.12dist(sphinx) = 7.2.6
python3dist(sphinx) = 7.2.6

# runtime requirements
$ fedrq pkgs python3-rich -F requires
python(abi) = 3.12
(python3.12dist(pygments) < 3~~ with python3.12dist(pygments) >= 2.13)
python3.12dist(markdown-it-py) >= 2.2

# buildtime requirements
$ fedrq pkgs python-rich -F requires
python3-devel
python3dist(packaging)
pyproject-rpm-macros
python3dist(pytest)
python3dist(setuptools)
python3dist(attrs)
python3dist(pip) >= 19
(python3dist(tomli) if python3-devel < 3.11)
python3dist(poetry-core) >= 1
(python3dist(pygments) < 3~~ with python3dist(pygments) >= 2.13)
python3dist(markdown-it-py) >= 2.2
```

### Dependencies

#### What other packages need my binary package?

`whatrequires` equals to `wr`.
`whatrequires-src` equals to `wrsrc`.
`-s, --src` means only source rpms.
`-S, --nosrc` means exclude source rpms.

> For Python `-s/-S` may not seem relevant, as source and built components are usually named differently,
> but for any other components it's crucial, compare e.g.
> `$ fedrq pkgs ocrmypdf -S -F requires` and
> `$ fedrq pkgs ocrmypdf -F requires`


equivalent to: `repoquery -q --repo=rawhide{,-source} --whatrequires python3-rich`

```
$ fedrq whatrequires python3-rich

# It can work with virtual provides too!
# don't use it though, it only matches the literal provides
$ fedrq whatrequires -s 'python3dist(rich)' -F name

# released Fedora: both fedora and updates repos
$ fedrq whatrequires --branch f38 python3-rich
```

Only interested in fedora repo?
equivalent to: `repoquery --repo=fedora{,-source} --releasever 38 --whatrequires python3-rich`

```
$ fedrq whatrequires --branch f38 --repo @release python3-rich
```

#### What packages require any subpackage of my srpm?

equivalent to: `repoquery -q --repo=rawhide{,-source} --whatrequires python3-sphinx --whatrequires python3-sphinx-latex --whatrequires python-sphinx-doc`

```
# wrsrc is used with the source package name
$ fedrq wrsrc python-sphinx | wc -l
821

# compared to this - it only takes care about this concrete built package name
$ fedrq wr python3-sphinx | wc -l
815
```

#### What packages require python-sphinx' components on build time?

equivalent to: `repoquery -q --repo=rawhide{,-source} --whatrequires python3-sphinx --whatrequires python3-sphinx-latex --whatrequires python-sphinx-doc | grep 'src$' | pkgname | sort | uniq | wc -l`

```
$ fedrq wrsrc -s python-sphinx -F source | wc -l
739
```

#### The Big Python Query

Get names of the source packages in Koji that require any of the given Python provides - needed for Python rebuilds.
```
$ repoquery --repo=koji --source --whatrequires 'libpython3.12.so.1.0()(64bit)' --whatrequires 'python(abi) = 3.12' --whatrequires 'python3.12dist(*)' | pkgname | env LANG=en_US.utf-8 sort | uniq
```

Fedrq equivalent:
```
fedrq wr --repo='@koji:rawhide' 'python3.12dist(*)' 'python(abi) = 3.12' 'libpython3.12.so.1.0()(64bit)' -F source | env LANG=en_US.utf-8 sort | uniq
```

### Nice little things repoquery doesn't provide easily

Breakdown of the buildtime, runtime deps and their srpm names:

```
$ fedrq whatrequires --branch f38 python3-rich -F breakdown
```

Resolve the packages required by rich on runtime.
Same with build time - just change the queried package name

```
$ fedrq pkgs python3-rich -F requires | fedrq pkgs -iSP
python3-3.12.2-2.fc41.x86_64
python3-markdown-it-py-3.0.0-4.fc40.noarch
python3-pygments-2.17.2-3.fc40.noarch
```

Print lines matching the required package in packages that require the given package (yeah, I can't explain it).
Useful for finding packages that use aggresive version constraints.
Semantically the same as our notoriously horrible oneliner: `for pkg in $(repoquery -q --repo=rawhide{,-source} --whatrequires python3-sphinx); do repoquery -q --repo=rawhide{,-source} --requires $pkg | grep -E '\bsphinx\b' | grep '<' && echo -e "${pkg}\n"; done`

```
$ fedrq wr -F narm:python3-sphinx python3-sphinx | grep "<"
# only interested in runtime? -S means --nosrc
$ fedrq wr -S -F narm:python3-sphinx python3-sphinx | grep "<"
```

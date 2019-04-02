# `repobee-gofmt`
Plugin for RepoBee that runs `gofmt` on .go files and reports whether `gofmt`
thought changes were necessary or not. It's useful for quickly checking if
students have formatted their code or not. The source files are not modified.
This is a very simple plugin made in some haste, and it's not unit tested.  It
should work pretty well though because it's so simple.

### Install
I'm not particularly committed to this plugin so it's not on PyPi, but you can
easily install it from this repo with:

```
python3 -m pip install git+https://github.com/slarse/repobee-gofmt.git
```

### Usage
Simply run `repobee clone` with the plugin activated, and it will run `gofmt`
on all .go files it can find in student repos. That is to say, invoke `repobee
clone` like this:

```
repobee -p gofmt clone [... REST OF ARG LIST ...]
```

# License
See [LICENSE](LICENSE) for details.

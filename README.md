# fpk - The Flatpak Development Tool

`fpk` is a command line interface for developing apps using [Flatpak](https://flatpak.org/).

## State of the Project

I've just started working on this, and it's not usable yet.

## Goals of the Project

- Make it easy to build and run a Flatpak app from source (like Gnome Builder).
- Enable developers to use the Flatpak SDK as an SDK.
  - i.e. `fpk run rust-analyzer` will run `rust-analyzer` from the Rust SDK extension
- Integrate language specific tools for `flatpak-builder`.
  - i.e. `fpk python add click` or `fpk cargo add clap`
- Validate flatpak-builder manifests using [`flatpak-builder-lint`](https://github.com/flathub-infra/flatpak-builder-lint).
- Easily publish to [Flathub](https://flathub.org/).

## Tools Used

- [`flatpak`](https://github.com/flatpak/flatpak)
- [`flatpak-builder`](https://github.com/flatpak/flatpak-builder)
- [`flatpak-builder-lint`](https://github.com/flathub-infra/flatpak-builder-lint)
- [`fenv`](https://gitlab.gnome.org/ZanderBrown/fenv) for inspiration

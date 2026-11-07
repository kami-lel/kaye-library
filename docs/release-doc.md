# Release Documentation

Pushing a version tag publishes the plugin `.zip` as a GitHub Release asset. The workflow is [.github/workflows/release.yml](../.github/workflows/release.yml); the `build-github-release` command it calls belongs to [kaye-engine](https://github.com/kami-lel/kaye-engine).

## Tag to Release

1. set `version` in `pyproject.toml`, eg `1.2.0` or `1.2.0-beta`
2. push the tag `v` plus that version, eg `v1.2.0-beta`
3. the workflow fails when the tag differs from `v` plus the `pyproject.toml` version
4. it runs `kaye-library build-github-release kaye-library -o dist` and creates the release with `dist/*.zip` and generated notes
5. a tag containing `-alpha` or `-beta` is marked a pre-release

## Installed Versions

- the engine installs from its GitHub tag `v<X>`, with `<X>` read from the `kaye-engine==X` pin in `pyproject.toml`; raising the pin changes the release build, and that engine tag must exist first
- `kamilog` installs from its default branch, as it carries no pin
- the package itself installs with `--no-deps`, so the pins above are the only source of dependency versions

## Permissions

The workflow needs no secret: engine and `kamilog` are public, and checkout plus the release upload use the built-in `GITHUB_TOKEN` with `contents: write`.

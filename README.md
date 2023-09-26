MVP showcasing an import issue with poetry importing a Rust package with namespace clashes

In order to generate the wheel, clone the repo and run
```shell
poetry install
poetry build
```

This will generate wheels under `my_rust/dist/`.
# Contributing

Thanks for contributing.

## Security guidelines for contributors
- Do not commit secrets, keys, tokens, or production credentials.
- Copy `.env.example` to `.env` locally and keep real values out of version control.
- Run local checks before creating a PR when tooling is available:

```bash
pre-commit run --all-files
```

- If you discover a vulnerability, use private vulnerability reporting via the repository Security tab instead of public issues.

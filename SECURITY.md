# Security Policy

## Supported security baseline
This repository uses automated security checks (CodeQL, dependency review, secret scanning) and local pre-commit checks to reduce risk for a Python Data Engineering project.

## Reporting a vulnerability
Please **do not** open a public issue for vulnerabilities or exposed secrets.

Use GitHub's private vulnerability reporting flow in the repository:
- Open the repository on GitHub
- Go to the **Security** tab
- Use **Report a vulnerability** (private report)

If private reporting is not available yet, repository owners should enable it in repository settings.

## Secret handling requirements
- Never commit real credentials, tokens, private keys, certificates, or production connection strings.
- Use `.env.example` for placeholders only.
- Keep real values in local `.env` or in GitHub/AWS secret managers.
- Rotate credentials immediately if exposure is suspected.

## Dependency management
- Keep dependencies updated through Dependabot pull requests.
- Review dependency diffs and security advisories before merging.
- Prefer pinned or constrained versions where appropriate for reproducibility and risk control.

## Local checks before opening a PR
Run these checks locally when available:

```bash
pre-commit run --all-files
```

Optional project checks (if dependencies/tests exist):

```bash
ruff check .
bandit -q -r .
pytest -q
```

## Incident response (minimum)
1. Contain: revoke/rotate exposed credentials and block compromised tokens.
2. Assess: identify affected systems, data, and blast radius.
3. Eradicate: remove secrets from code/history where applicable and patch root cause.
4. Recover: redeploy clean credentials and monitor for abuse.
5. Learn: document timeline, impact, and preventive actions.

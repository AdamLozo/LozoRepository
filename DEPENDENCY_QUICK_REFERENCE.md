# Dependency Management Quick Reference

A cheat sheet for common dependency management tasks across different platforms.

## Daily Commands

### Check for Security Vulnerabilities

| Platform | Command |
|----------|---------|
| Node.js | `npm audit` |
| Python | `pip-audit` or `safety check` |
| Ruby | `bundle audit` |
| Go | `govulncheck ./...` |
| Rust | `cargo audit` |

### Check for Outdated Packages

| Platform | Command |
|----------|---------|
| Node.js | `npm outdated` |
| Python | `pip list --outdated` |
| Ruby | `bundle outdated` |
| Go | `go list -m -u all` |
| Rust | `cargo outdated` |

### Update Dependencies

| Platform | Safe Update Command |
|----------|---------------------|
| Node.js | `npm update` (respects package.json ranges) |
| Python | `pip install --upgrade <package>` |
| Ruby | `bundle update --patch` (patch only) |
| Go | `go get -u=patch ./...` (patch only) |
| Rust | `cargo update --patch` |

## Installation

### Add New Dependency (Production)

| Platform | Command |
|----------|---------|
| Node.js | `npm install --save-exact <package>@<version>` |
| Python | Add to `requirements.txt`: `<package>==<version>` |
| Ruby | Add to `Gemfile`: `gem '<package>', '~> <version>'` |
| Go | `go get <package>@<version>` |
| Rust | `cargo add <package>@<version>` |

### Add New Dependency (Development)

| Platform | Command |
|----------|---------|
| Node.js | `npm install --save-dev --save-exact <package>` |
| Python | Add to `requirements-dev.txt` |
| Ruby | In `Gemfile`: `gem '<package>', group: :development` |
| Go | Same as production (use build tags if needed) |
| Rust | `cargo add --dev <package>` |

## Cleanup

### Remove Unused Dependencies

| Platform | Command |
|----------|---------|
| Node.js | `npm prune` or use `npx depcheck` to find unused |
| Python | Manually remove from requirements.txt |
| Ruby | `bundle clean` |
| Go | `go mod tidy` |
| Rust | Manually remove from Cargo.toml, then `cargo update` |

### Clean Cache

| Platform | Command |
|----------|---------|
| Node.js | `npm cache clean --force` |
| Python | `pip cache purge` |
| Ruby | `bundle clean --force` |
| Go | `go clean -modcache` |
| Rust | `cargo clean` |

## Analysis

### View Dependency Tree

| Platform | Command |
|----------|---------|
| Node.js | `npm ls` or `npm ls --all` |
| Python | `pipdeptree` (install first: `pip install pipdeptree`) |
| Ruby | `bundle viz` (requires graphviz) |
| Go | `go mod graph` |
| Rust | `cargo tree` |

### Check Package Size (Before Installing)

| Platform | Command/Tool |
|----------|--------------|
| Node.js | Visit `https://bundlephobia.com/package/<package>` |
| Python | `pip show <package>` after installing |
| Ruby | `gem info <package>` |
| Go | Check via `go list -m -json <package>` |
| Rust | `cargo metadata` after adding |

### Find Why a Package is Installed

| Platform | Command |
|----------|---------|
| Node.js | `npm why <package>` (npm 7+) or `npm ls <package>` |
| Python | `pipdeptree -r -p <package>` |
| Ruby | `bundle show <package>` |
| Go | `go mod why <package>` |
| Rust | `cargo tree -i <package>` |

## Security

### Fix Vulnerabilities Automatically

| Platform | Command | Note |
|----------|---------|------|
| Node.js | `npm audit fix` | Use `--force` for breaking changes |
| Python | Manually update in requirements.txt | No auto-fix |
| Ruby | `bundle update <gem>` | Update specific gem |
| Go | Update via `go get <package>@latest` | Manual |
| Rust | `cargo update <package>` | Manual |

### Check License Compliance

| Platform | Command |
|----------|---------|
| Node.js | `npx license-checker --summary` |
| Python | `pip-licenses` (install: `pip install pip-licenses`) |
| Ruby | `bundle exec license_finder` (install gem first) |
| Go | `go-licenses report ./...` (install first) |
| Rust | `cargo-license` (install: `cargo install cargo-license`) |

## Version Locking

### Generate Lock File

| Platform | File | Command |
|----------|------|---------|
| Node.js | `package-lock.json` | `npm install` |
| Python | None (use `pip-tools`) | `pip-compile requirements.in` |
| Ruby | `Gemfile.lock` | `bundle install` |
| Go | `go.sum` | `go mod download` |
| Rust | `Cargo.lock` | `cargo build` |

### Update Lock File

| Platform | Command |
|----------|---------|
| Node.js | `npm install` (after updating package.json) |
| Python | `pip-compile --upgrade requirements.in` |
| Ruby | `bundle update` |
| Go | `go get -u && go mod tidy` |
| Rust | `cargo update` |

## CI/CD Integration

### Run in CI Pipeline

```bash
# Node.js
npm ci                          # Clean install from lock file
npm audit --production          # Security audit
npm outdated || true            # Check outdated (non-failing)

# Python
pip install -r requirements.txt
pip-audit                       # Security audit
pip list --outdated             # Check outdated

# Ruby
bundle install --deployment     # Install from lock file
bundle audit                    # Security audit
bundle outdated                 # Check outdated

# Go
go mod download                 # Download dependencies
go mod verify                   # Verify checksums
govulncheck ./...              # Security scan

# Rust
cargo fetch                     # Download dependencies
cargo audit                     # Security audit
cargo outdated                  # Check outdated
```

## Common Issues

### Issue: Conflicting Dependencies

| Platform | Solution |
|----------|----------|
| Node.js | Use `npm ls <package>` to find conflicts, consider `npm dedupe` |
| Python | Use virtual environments, check with `pipdeptree` |
| Ruby | Run `bundle update` or specify version ranges in Gemfile |
| Go | Go modules handle this automatically |
| Rust | Cargo handles this, but check with `cargo tree -d` |

### Issue: Installation Fails

| Platform | First Steps |
|----------|-------------|
| Node.js | Delete `node_modules` and `package-lock.json`, run `npm install` |
| Python | Upgrade pip: `pip install --upgrade pip`, check Python version |
| Ruby | Run `bundle clean --force`, then `bundle install` |
| Go | Run `go clean -modcache`, then `go mod download` |
| Rust | Run `cargo clean`, then `cargo build` |

### Issue: Slow Installation

| Platform | Solution |
|----------|----------|
| Node.js | Use `npm ci` in CI, enable npm cache |
| Python | Use pip cache, consider `pip-tools` for faster installs |
| Ruby | Use `bundle install --jobs=4` for parallel installs |
| Go | Use `GOPROXY`, enable module cache |
| Rust | Enable incremental compilation, use `sccache` |

## Version Constraint Syntax

### Node.js (package.json)
- `1.2.3` - Exact version
- `^1.2.3` - Compatible with 1.2.3 (>=1.2.3 <2.0.0)
- `~1.2.3` - Approximately 1.2.3 (>=1.2.3 <1.3.0)
- `1.2.x` - Any patch version of 1.2
- `*` - Any version (avoid in production)

### Python (requirements.txt)
- `package==1.2.3` - Exact version
- `package>=1.2.3` - Minimum version
- `package>=1.2,<2.0` - Version range
- `package~=1.2.3` - Compatible release (>=1.2.3, ==1.2.*)

### Ruby (Gemfile)
- `gem 'package', '1.2.3'` - Exact version
- `gem 'package', '~> 1.2.3'` - Pessimistic (>=1.2.3, <1.3)
- `gem 'package', '>= 1.2'` - Minimum version
- `gem 'package', '>= 1.2', '< 2.0'` - Range

### Go (go.mod)
- `require package v1.2.3` - Minimum version (semantic import versioning)
- Go automatically manages versions via Minimal Version Selection

### Rust (Cargo.toml)
- `package = "1.2.3"` - Caret requirement (^1.2.3)
- `package = "=1.2.3"` - Exact version
- `package = "~1.2.3"` - Tilde requirement
- `package = ">=1.2, <2.0"` - Range

## Emergency Commands

### Rollback to Previous Versions

```bash
# Node.js - Rollback package-lock.json from git
git checkout HEAD -- package-lock.json
npm ci

# Python - Pin specific version
pip install package==1.2.3

# Ruby - Rollback Gemfile.lock
git checkout HEAD -- Gemfile.lock
bundle install

# Go - Use specific version
go get package@v1.2.3

# Rust - Edit Cargo.toml and specify exact version
# package = "=1.2.3"
cargo update
```

## Useful Aliases

Add to your shell profile (~/.bashrc, ~/.zshrc):

```bash
# Node.js
alias npmaudit='npm audit --production'
alias npmoutdated='npm outdated'
alias npmclean='rm -rf node_modules package-lock.json && npm install'

# Python
alias pipaudit='pip-audit'
alias pipoutdated='pip list --outdated'
alias pipfreeze='pip freeze > requirements.txt'

# Ruby
alias bundleaudit='bundle audit check --update'
alias bundleoutdated='bundle outdated'

# Go
alias govuln='govulncheck ./...'
alias gomodupdate='go get -u ./... && go mod tidy'

# Rust
alias cargoaudit='cargo audit'
alias cargooutdated='cargo outdated'
```

## Resources

- **Node.js**: https://docs.npmjs.com/
- **Python**: https://pip.pypa.io/en/stable/
- **Ruby**: https://bundler.io/
- **Go**: https://go.dev/ref/mod
- **Rust**: https://doc.rust-lang.org/cargo/

---
**Last Updated:** 2026-01-13

# Dependency Management Guidelines

## Purpose

This document provides practical guidelines for managing dependencies in this repository to ensure security, maintainability, and performance.

## Core Principles

1. **Minimize Dependencies**: Every dependency is a liability. Only add what's truly necessary.
2. **Security First**: Vulnerabilities in dependencies are vulnerabilities in our code.
3. **Stay Updated**: Outdated dependencies accumulate security debt.
4. **Know Your Dependencies**: Understand what each dependency does and why it's needed.

## Before Adding a New Dependency

Use this checklist before adding any new dependency:

### Security Assessment
- [ ] Check the package's security history on GitHub Security Advisories
- [ ] Verify the package has more than one active maintainer
- [ ] Confirm the package has a security policy (SECURITY.md)
- [ ] Review the last commit date (should be within the last year)
- [ ] Check for known vulnerabilities using:
  - npm: `npm audit`
  - Python: `pip-audit` or `safety check`
  - Ruby: `bundle audit`
  - Go: `govulncheck`
  - Rust: `cargo audit`

### Quality Assessment
- [ ] Minimum weekly downloads/usage threshold met
- [ ] Active issue resolution (check response time on issues)
- [ ] Good documentation available
- [ ] Test coverage > 70% (if available)
- [ ] Compatible license (MIT, Apache 2.0, BSD preferred)
- [ ] Established project (prefer > 1 year old with > 1.0 version)

### Necessity Assessment
- [ ] Feature cannot be reasonably implemented in-house
- [ ] Not a micro-dependency (avoid packages < 10 lines of code)
- [ ] Dependency tree is reasonable (check transitive dependencies)
- [ ] Size impact is acceptable:
  - JavaScript: Check on bundlephobia.com
  - Python: Check package size with `pip show <package>`
- [ ] Alternatives have been evaluated

### Documentation
- [ ] Add entry to DEPENDENCIES.md explaining why this package is needed
- [ ] Document any configuration or setup required
- [ ] Note any known issues or limitations

## Adding a Dependency

### Preferred Installation Methods

**Node.js/npm:**
```bash
# Install with exact version
npm install --save-exact <package>@<version>

# Or allow patch updates only
npm install --save <package>@~<version>

# For development dependencies
npm install --save-dev --save-exact <package>
```

**Python/pip:**
```bash
# Add to requirements.txt with pinned version
echo "<package>==<version>" >> requirements.txt
pip install -r requirements.txt

# Or using pip-tools
echo "<package>" >> requirements.in
pip-compile requirements.in
pip install -r requirements.txt
```

**Ruby/Bundler:**
```ruby
# In Gemfile, use pessimistic version constraint
gem '<package>', '~> <major>.<minor>'

# Then install
bundle install
```

**Go:**
```bash
# Go modules automatically manage versions
go get <package>@<version>
go mod tidy
```

**Rust:**
```bash
# Add to Cargo.toml, then
cargo update <package>
```

## Regular Maintenance Tasks

### Weekly Tasks
- [ ] Review security advisories for dependencies
- [ ] Check Dependabot PRs and merge approved updates
- [ ] Monitor CI/CD pipeline for dependency-related failures

### Monthly Tasks
- [ ] Run security audit:
  ```bash
  # Node.js
  npm audit

  # Python
  pip-audit

  # Ruby
  bundle audit

  # Go
  govulncheck ./...

  # Rust
  cargo audit
  ```
- [ ] Check for outdated packages:
  ```bash
  # Node.js
  npm outdated

  # Python
  pip list --outdated

  # Ruby
  bundle outdated

  # Go
  go list -m -u all

  # Rust
  cargo outdated
  ```
- [ ] Review and update patch versions

### Quarterly Tasks
- [ ] Evaluate major version updates
- [ ] Review dependency tree for bloat
- [ ] Audit unused dependencies:
  ```bash
  # Node.js
  npx depcheck

  # Python
  pip-audit

  # Ruby
  bundle clean
  ```
- [ ] Update DEPENDENCIES.md
- [ ] Review and optimize bundle size (frontend projects)

### Before Each Release
- [ ] Full dependency audit
- [ ] Ensure all dependencies are up to date on security patches
- [ ] Run full test suite with current dependencies
- [ ] Document any known vulnerable dependencies with risk assessment

## Handling Security Vulnerabilities

### Severity Levels

**Critical/High Severity:**
1. Stop using the affected functionality immediately if possible
2. Check for patches or updates
3. Apply fix within 24 hours
4. If no fix available, evaluate alternatives or implement workaround
5. Document the issue and resolution

**Medium Severity:**
1. Assess actual risk to this project
2. Plan update within 1 week
3. Test thoroughly before deploying
4. Document the vulnerability and fix

**Low Severity:**
1. Include in next regular update cycle
2. Monitor for severity changes
3. Document for tracking

### Response Workflow

```
Security Alert Received
         ↓
    Assess Severity
         ↓
    ├─ Critical/High → Immediate Action
    ├─ Medium → Plan Fix (1 week)
    └─ Low → Next Update Cycle
         ↓
    Check for Update/Patch
         ↓
    ├─ Available → Test & Apply
    └─ Not Available → Assess Alternatives
         ↓
    Update Dependencies
         ↓
    Run Tests
         ↓
    Deploy Fix
         ↓
    Document Resolution
```

## Dependency Update Strategy

### Semantic Versioning Quick Reference

- **MAJOR.MINOR.PATCH** (e.g., 2.3.1)
  - MAJOR: Breaking changes
  - MINOR: New features, backward compatible
  - PATCH: Bug fixes, backward compatible

### Update Policy

**Patch Updates (0.0.X):**
- Auto-merge if CI passes
- Low risk, typically bug fixes only
- Review Dependabot PRs within 48 hours

**Minor Updates (0.X.0):**
- Review changelog before merging
- Test thoroughly
- Merge within 1 week if no issues

**Major Updates (X.0.0):**
- Review breaking changes carefully
- Plan migration if needed
- Test extensively
- May require code changes
- Schedule during low-activity periods

## Reducing Dependency Bloat

### Strategies

1. **Use Standard Library First**
   - Many common tasks can be done with built-in functions
   - Reduces bundle size and dependency tree complexity

2. **Choose Lightweight Alternatives**
   - Example: date-fns (tree-shakeable) vs moment.js (large bundle)
   - Example: axios vs native fetch API
   - Example: lodash-es (modular) vs lodash

3. **Leverage Tree Shaking** (JavaScript)
   - Import only what you need: `import { specific } from 'package'`
   - Avoid: `import * as everything from 'package'`
   - Use ES modules, not CommonJS

4. **Analyze Bundle Size** (JavaScript/TypeScript)
   ```bash
   # Install analyzer
   npm install --save-dev webpack-bundle-analyzer

   # Or check before installing
   npx bundlephobia <package-name>
   ```

5. **Regular Cleanup**
   - Remove unused dependencies quarterly
   - Check for duplicate dependencies in tree
   - Consolidate versions where possible

### Size Budgets (Frontend Projects)

Set and enforce bundle size limits:

```json
// In package.json
{
  "bundlesize": [
    {
      "path": "./dist/bundle.js",
      "maxSize": "200 kB"
    }
  ]
}
```

## Documentation Requirements

### DEPENDENCIES.md

Maintain a `DEPENDENCIES.md` file with this structure:

```markdown
# Dependencies

## Production Dependencies

### package-name (version)
- **Purpose**: Why this package is used
- **Alternatives Considered**: Other options evaluated
- **Size Impact**: Bundle size contribution (if applicable)
- **Last Reviewed**: Date of last evaluation

## Development Dependencies

### package-name (version)
- **Purpose**: Why this package is used
- **Scope**: Which part of development process
```

## CI/CD Integration

### Recommended Checks

Add these to your CI pipeline:

```yaml
# Example GitHub Actions
security-audit:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: Security Audit
      run: npm audit --production --audit-level=moderate

dependency-check:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: Check Outdated
      run: npm outdated || true
    - name: Check Unused
      run: npx depcheck

license-check:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3
    - name: License Compliance
      run: npx license-checker --summary
```

## Tools and Resources

### Security Tools
- **npm**: npm audit, Snyk
- **Python**: pip-audit, safety, bandit
- **Ruby**: bundle audit, bundler-audit
- **Go**: govulncheck, nancy
- **Rust**: cargo audit

### Update Management
- **GitHub Dependabot**: Automated PRs for updates
- **Renovate Bot**: Advanced configuration options
- **npm-check-updates**: Interactive update tool for npm

### Analysis Tools
- **bundlephobia.com**: Check JavaScript package sizes
- **depcheck**: Find unused npm dependencies
- **pipdeptree**: Visualize Python dependency tree
- **bundle viz**: Visualize Ruby gem dependencies

### Monitoring
- **Libraries.io**: Track dependencies across platforms
- **Snyk**: Vulnerability monitoring and alerts
- **GitHub Security Alerts**: Built-in vulnerability scanning

## Common Pitfalls to Avoid

1. **Never commit dependency files with vulnerabilities** without documenting accepted risk
2. **Don't ignore security warnings** - investigate even if they seem unrelated
3. **Avoid version wildcards in production** (`*` or `latest`)
4. **Don't install from untrusted sources** - use official registries
5. **Never run install scripts without reviewing them** (postinstall hooks can be malicious)
6. **Don't use deprecated packages** - plan migration to maintained alternatives
7. **Avoid circular dependencies** - indicates poor architecture
8. **Don't mix dependency managers** - choose one per language

## Emergency Procedures

### If a Critical Vulnerability is Discovered

1. **Immediate**: Assess if the vulnerability affects our usage
2. **Within 1 hour**: Create incident ticket and notify team
3. **Within 4 hours**: Identify fix or workaround
4. **Within 24 hours**: Deploy fix to production
5. **Within 48 hours**: Post-mortem and process improvement

### If Dependency Becomes Unmaintained

1. Search for maintained fork or alternative
2. Assess effort to maintain fork internally
3. Plan migration timeline
4. Document decision and rationale
5. Create tracking issue for migration

## Approval Process

### For New Dependencies

1. Create PR with dependency addition
2. Fill out checklist in PR description
3. Update DEPENDENCIES.md
4. Require at least one review
5. Ensure CI passes including security checks
6. Document any accepted risks

### For Major Updates

1. Create PR with update
2. Include changelog summary in PR description
3. Note any breaking changes
4. Update code as needed
5. Run full test suite
6. Require review from code owner

## Metrics to Track

Monitor these over time:

- Total dependency count (direct + transitive)
- Outdated dependency count
- Known vulnerabilities count
- Average dependency age
- Bundle size (frontend)
- Dependency churn rate (additions/removals per month)
- Time to patch critical vulnerabilities

---

**Last Updated:** 2026-01-13
**Review Schedule:** Quarterly
**Owner:** Repository maintainers

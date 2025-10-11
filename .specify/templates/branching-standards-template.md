# Branching and Repository Standards

This file contains branching standards used by the specify prompt for branch creation and management.

---

## Branch Naming Convention

**Description**: All Git branches must follow a strict naming pattern for consistency and automation

**Pattern**: `type/short-description`

### Constraints

#### Must

- Follow pattern `type/short-description`
- Start with valid type prefix from allowed list
- Use only lowercase letters (a-z), numbers (0-9), hyphens (-), and forward slashes (/)
- Be between 10-50 characters in length
- Be created from up-to-date develop branch (except hotfix from main, maintenance from main or develop)

#### Must Not

- Begin with numbers or numeric prefixes
- Contain uppercase letters
- Contain spaces or special characters (\_, @, #, $, %, ?, !)
- Use invalid type prefixes

#### May

- Include numbers inside the name when semantically relevant (e.g., version or API level)

### Allowed Type Prefixes

- `feat` - New feature development
- `fix` - Bug fixes
- `chore` - Maintenance tasks
- `refactor` - Code refactoring
- `test` - Test additions or updates
- `docs` - Documentation changes
- `hotfix` - Critical production fixes
- `maintenance` - Dependency updates and operational maintenance

### Length Constraints

- **Minimum**: 10 characters
- **Maximum**: 50 characters

### Examples

#### Valid

- `feat/add-payment-endpoint`
- `fix/handle-auth-timeout`
- `docs/update-readme`
- `maintenance/update-dependencies`
- `feat/add-v2-endpoint`
- `chore/refactor-logging`

#### Invalid

- `user-authentication-system` - Missing type prefix
- `123-fix-bug` - Starts with number
- `Fix_DB_Bug` - Contains uppercase and underscore
- `feat/123-add-endpoint` - Number after type prefix
- `new-feature` - Too short

---

## Branch Lifecycle Management

**Description**: Defines the lifecycle and merge patterns for different branch types

### main

- **Description**: Production-ready code only
- **Protection Level**: Protected
- **Deployment Ready**: Yes
- **Merge Sources**:
  - `develop`
  - `hotfix/*`
- **Merge Method**: Pull request

### develop

- **Description**: Integration branch for features
- **Merge Sources**:
  - `feature/*`
  - `maintenance/*`
- **Merge Destination**: `main`
- **Merge Requirements**:
  - Successful audit
  - All tests passing
  - Code review approved

### feature/\*

- **Description**: New feature development
- **Created From**: `develop`
- **Merge Destination**: `develop`
- **Lifecycle**: Short-lived
- **Merge Requirements**:
  - All checks pass
  - PR review approved
  - No merge conflicts

### hotfix/\*

- **Description**: Critical production fixes
- **Created From**: `main`
- **Merge Destinations**:
  - `main`
  - `develop`
- **Priority**: Critical
- **Merge Method**: Emergency procedure

### maintenance/\*

- **Description**: Dependency updates, security patches, operational maintenance
- **Created From**:
  - `main`
  - `develop`
- **Merge Destinations**:
  - `main`
  - `develop`
- **Merge Requirements**:
  - Code review
  - Successful tests
  - Security scan passed

---

## Commit Message Standards

**Description**: Standardized commit message format for clarity and automation

**Format**: `[TYPE]: [BRIEF_DESCRIPTION]`

### Constraints

#### Must

- Follow format `[TYPE]: [BRIEF_DESCRIPTION]`
- Use imperative mood (add, fix, update - NOT added, fixed, updated)
- Be clear and descriptive of the change
- Match the branch type prefix
- Use lowercase for type prefix

#### Must Not

- Exceed 72 characters in subject line
- Use past tense or present continuous
- Include sensitive information
- Be vague or non-descriptive

### Components

#### Type

- **Description**: Commit category matching branch type
- **Values**:
  - `feat`
  - `fix`
  - `chore`
  - `refactor`
  - `test`
  - `docs`
  - `hotfix`
  - `maintenance`

#### Brief Description

- **Description**: Concise description of the change
- **Max Length**: 72 characters
- **Style**: Imperative mood

### Examples

#### Valid

- `feat: add user authentication endpoint`
- `fix: resolve timeout issue in payment processing`
- `docs: update API documentation for v2.1`
- `refactor: simplify error handling logic`
- `test: add unit tests for validation module`

#### Invalid

- `added new feature` - Past tense
- `bug fix` - Missing type prefix format
- `Updated the readme file with new instructions` - Too long, wrong tense
- `fix stuff` - Not descriptive
- `FEAT: Add Feature` - Uppercase type

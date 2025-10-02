# Specify

Create or update the feature specification from a natural language feature description.

## Usage

- `@specify <feature_description>` - Create a new feature specification
- `@specify <feature_description> -ref <reference_folder>` - Create specification with additional context from a reference folder

---

## Create Feature Specification

The user will provide a feature description and optionally a reference folder for additional context.

### Steps

0. **Create a branch name**: Before running the script, create a concise, descriptive name suitable for a git branch that captures the essence of the feature. This name should be clear and meaningful, preserving key technical terms while being suitable for branch naming conventions. The script will automatically process this into a valid git branch name limited to 65 characters.

1. Run the script `.specify/scripts/bash/create-new-feature.sh --json "<branch_description>"` from repo root and parse its JSON output for BRANCH_NAME and SPEC_FILE. All file paths must be absolute.
   **IMPORTANT** You must only ever run this script once. The JSON is provided in the terminal as output - always refer to it to get the actual content you're looking for.

   **Branch Name Generation**: The script automatically generates a git branch name from your description by:

   - Converting the description to lowercase
   - Replacing all non-alphanumeric characters with hyphens
   - Removing consecutive hyphens
   - Trimming leading and trailing hyphens
   - Truncating to a maximum of 65 characters
   - Example: "High-Value Field Redaction & Structured Context" → "high-value-field-redaction-structured-context" (62 chars)

1.5. **Load Reference Folder (if provided)**: If the user specified a reference folder with `-ref <folder_name>`, check for `.specify/reference/<folder_name>/` and load all files in the folder for additional context about:

- Primary User Story details (from README.md)
- Acceptance Scenarios examples
- Edge Cases to consider
- Functional Requirements templates
- Key Entities definitions
- Any additional supporting files in the folder

**Important**: If a reference folder is used, add a metadata section at the top of the spec file:

```yaml
---
reference: <folder_name>
---
```

This allows @plan and @tasks to automatically source the reference context without needing to pass `-ref` explicitly.

2. Load `.specify/templates/spec-template.md` to understand required sections.

3. Write the specification to SPEC_FILE using the template structure, replacing placeholders with concrete details derived from the feature description and reference folder (if provided) while preserving section order and headings. If a reference folder was used, ensure the YAML frontmatter is at the very top of the file.

4. Report completion with branch name, spec file path, reference folder used (if any), and readiness for the next phase.

Note: The script creates the feature directory and initializes the spec file.

---

## Creating Reference Folders

Reference folders provide reusable context that enhances @specify, @plan, and @tasks workflows.

### How to Create a Reference Folder

1. **Create folder name**: Create a concise, descriptive folder name in kebab-case format that represents the domain or feature area.

2. **Check if folder exists**: First check if `.specify/reference/<folder_name>/` already exists

3. **Create folder structure**: If it doesn't exist, create the folder `.specify/reference/<folder_name>/`

4. **Create README.md**: Create a `README.md` file in the new folder using the template below

5. **Confirm creation**: Let the user know the reference folder has been created and they can now edit it

### Template for README.md

```markdown
# [Feature Name] Requirements

## Primary User Story

As a [user type], I want [goal] so that [benefit].

## Acceptance Criteria

- [ ] Must have: [critical requirement]
- [ ] Should have: [important requirement]
- [ ] Could have: [nice-to-have requirement]

## User Scenarios

### Happy Path

1. User does X
2. System responds with Y
3. User sees Z

### Edge Cases

- What happens when [edge case 1]
- How to handle [edge case 2]
- Behavior for [edge case 3]

## Functional Requirements

### Core Features

- Feature 1: [description]
- Feature 2: [description]

### Business Rules

- Rule 1: [constraint/validation]
- Rule 2: [business logic]

## Key Entities

### Data Models

- **Entity1**: fields, relationships, constraints
- **Entity2**: fields, relationships, constraints

### APIs/Interfaces

- Endpoint patterns
- Expected inputs/outputs
- Error handling

## Technical Constraints

- Performance: [requirements]
- Security: [requirements]
- Compatibility: [requirements]

## Success Metrics

- How to measure success
- Key performance indicators
- User experience goals
```

### Using Reference Folders

After creating a reference folder:

1. Edit the README.md with specific requirements for that domain/feature area
2. Add additional files to the folder as needed
3. Use the folder when creating specifications:
   - `@specify <feature_description> -ref <folder_name>` - Creates spec with reference context
   - The reference folder name is stored in the spec's YAML frontmatter
   - `@plan` and `@tasks` automatically source the reference from the spec file
   - No need to pass `-ref` to @plan or @tasks - they read it from the spec

### Important Notes

- Only create the folder if it doesn't already exist
- The folder name should be descriptive and kebab-case (e.g., `user-authentication`, `payment-system`)
- The README.md serves as the primary reference document but additional files can be added
- Reference folders provide consistent context: define once in @specify, automatically used by @plan and @tasks

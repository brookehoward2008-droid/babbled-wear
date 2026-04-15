```markdown
# babbled-wear Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the core development patterns and conventions used in the `babbled-wear` TypeScript codebase. You'll learn about file naming, import/export styles, commit message patterns, and how to work with tests. This guide is designed to help you quickly onboard and contribute effectively to the project.

## Coding Conventions

### File Naming
- Use **camelCase** for file names.
  - Example: `userProfile.ts`, `orderManager.ts`

### Import Style
- Use **relative imports** for modules within the project.
  - Example:
    ```typescript
    import { getUser } from './userProfile';
    ```

### Export Style
- Use **named exports** for all modules.
  - Example:
    ```typescript
    // In userProfile.ts
    export function getUser(id: string) { ... }
    export const USER_STATUS = { ... };
    ```

### Commit Messages
- Commit messages are **freeform** (no strict prefixes).
- Average commit message length: ~48 characters.
- Example:
  ```
  Fix bug in user authentication flow
  ```

## Workflows

### Adding a New Feature
**Trigger:** When implementing a new feature or module  
**Command:** `/add-feature`

1. Create a new file using camelCase naming.
2. Implement your feature using named exports.
3. Import any dependencies using relative paths.
4. Write corresponding tests in a `.test.ts` file.
5. Commit your changes with a clear, descriptive message.

### Fixing a Bug
**Trigger:** When addressing a bug or issue  
**Command:** `/fix-bug`

1. Locate the relevant file(s) using camelCase naming.
2. Apply your fix, maintaining the import/export conventions.
3. Update or add tests in the corresponding `.test.ts` file.
4. Commit with a message describing the fix.

### Writing Tests
**Trigger:** When adding or updating tests  
**Command:** `/write-test`

1. Create or update a test file matching `*.test.*` (e.g., `userProfile.test.ts`).
2. Write tests for your functions or components.
3. Use the project's (unknown) test framework conventions.
4. Run tests to ensure correctness.

## Testing Patterns

- Test files follow the pattern: `*.test.*` (e.g., `orderManager.test.ts`).
- The specific test framework is not detected; follow existing patterns in the repository.
- Place tests alongside or near the modules they test.
- Example:
  ```typescript
  // userProfile.test.ts
  import { getUser } from './userProfile';

  describe('getUser', () => {
    it('returns user by ID', () => {
      // test implementation
    });
  });
  ```

## Commands
| Command      | Purpose                                      |
|--------------|----------------------------------------------|
| /add-feature | Start the workflow for adding a new feature  |
| /fix-bug     | Start the workflow for fixing a bug          |
| /write-test  | Start the workflow for writing or updating tests |
```

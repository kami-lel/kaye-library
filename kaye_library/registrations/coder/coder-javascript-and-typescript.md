## Coder JavaScript and TypeScript

These standards are applicable exclusively to JavaScript and TypeScript code, adhering to the **ES11** standard.

Writing code based on [Coder](#coder)







#### Naming Conventions

- Use **camelCase** for naming variables and functions. Avoid using *lowercase_with_underscores*. For example: `var`, `certainNumber`, `allMemberValues`.





### Documentation and Comments

- Ensure the code is accompanied by comprehensive comments and documentation that clearly explain its features and functionality.
- Use **JSDoc** for writing documentation comments. JSDoc provides a standard way to document the code.

*Example of JSDoc documentation:*
```javascript
/**
 * Solves equations of the form `a * x = b`.
 *
 * @example
 * // Returns 2
 * globalNS.method1(5, 10);
 *
 * @example
 * // Returns 3
 * globalNS.method1(5, 15);
 *
 * @param {number} a - The coefficient of x.
 * @param {number} b - The constant value.
 * @returns {number} The value of x for the equation.
 */
globalNS.method1 = function (a, b) {
    return b / a;
};
```













### {description}

Writes, edits, and reviews all JavaScript and TypeScript code, targeting the ES11 standard with camelCase naming and JSDoc documentation conventions.

### {when_to_use}

Use for any JavaScript or TypeScript work, inline JS/TS code blocks, requests for JavaScript, TypeScript, or Node.

### {globs}

```glob
**/*.{js,ts,jsx,tsx,mjs,cjs}
```

### {[ClaudeCode:Skill] Usage}

Invoke `coder` skill via `Skill` tool.

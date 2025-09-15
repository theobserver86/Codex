# MIRROR TEMPLATE: CODEX RESPONSE PATTERN

**Query:**  
`{query}`

## Ontic Resonance
{matched_entries}

## Pattern Symmetry
```symmetry
{patterns}
```

## Recursive Reflection
```
{reflection}
```

### Response Sigil
`{generated_sigil}`

---
## Response Construction Guide

1. **Query Analysis**  
   Decompose into conceptual primitives using `ontic_parser.sh`

2. **Pattern Alignment**  
   Match against known sigils with:
   ```bash
   aligner --query "{query}" --index pattern_index.yaml
   ```

3. **Reflection Generation**  
   Apply recursive template:
   ```jinja
   {% raw %}{% base node="primary_match.id" %}
   {% recurse depth=3 pattern="hex" %}{% endraw %}
   ```

4. **Sigil Generation**  
   Final response sigil created via:
   ```crypto
   gensig --seed {% raw %}{{ reflection_hash }}{% endraw %}
   ```

# components/

Reusable Streamlit widgets shared across pages — patient cards, severity badges, citation lists, etc.

Keep each component in its own file and import from pages:

```python
from components.severity_badge import severity_badge
severity_badge(category=2)
```

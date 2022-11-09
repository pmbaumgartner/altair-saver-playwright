# Altair Saver - Playwright

[Installing the requirements](https://github.com/altair-viz/altair_saver#additional-requirements) for `altair_saver` correctly is annoying. This library makes it much easier if you want `png` or `svg` output for `altair` plots.

## Install

```
pip install git+https://github.com/pmbaumgartner/altair-saver-playwright
playwright install chromium
```

Don't forget that second step to install chromium!

## Use

```python
from altair_saver_playwright import save

import altair as alt
import pandas as pd

source = pd.DataFrame(
    {
        "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
        "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
    }
)

chart = alt.Chart(source).mark_bar().encode(x="a", y="b")

save(chart, "mycoolchart.svg")
```

## What is this doing?

This package:
  - Saves the chart as HTML (which is built into `altair`) in a temporary file
  - Uses chromium installed via [playwright](https://playwright.dev/python/) (much easier install) to navigate to the saved HTML
  - Clicks the Menu in the HTML file to "Save to PNG/SVG"
  - Saves the download to the path you determine


from altair_saver_playwright import save
from tempfile import NamedTemporaryFile
import altair as alt
import pandas as pd

from pathlib import Path


def test_png():
    source = pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    chart = alt.Chart(source).mark_bar().encode(x="a", y="b")
    with NamedTemporaryFile(suffix=".png") as f:
        save(chart, f.name)
        assert Path(f.name).exists()


def test_svg():
    source = pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    chart = alt.Chart(source).mark_bar().encode(x="a", y="b")
    with NamedTemporaryFile(suffix=".svg") as f:
        save(chart, f.name)
        assert Path(f.name).exists()

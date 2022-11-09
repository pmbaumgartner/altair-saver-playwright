from pathlib import Path
from tempfile import NamedTemporaryFile

import altair as alt
import pandas as pd
import pytest

from altair_saver_playwright import save, save_async


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


@pytest.mark.asyncio
async def test_png_async():
    source = pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    chart = alt.Chart(source).mark_bar().encode(x="a", y="b")
    with NamedTemporaryFile(suffix=".png") as f:
        await save_async(chart, f.name)
        assert Path(f.name).exists()


@pytest.mark.asyncio
async def test_svg_async():
    source = pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    chart = alt.Chart(source).mark_bar().encode(x="a", y="b")
    with NamedTemporaryFile(suffix=".svg") as f:
        await save_async(chart, f.name)
        assert Path(f.name).exists()

from pathlib import Path
from typing import Union
from tempfile import NamedTemporaryFile
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright

CLICK = {"png": "Save as PNG", "svg": "Save as SVG"}


def _run(playwright, chart, input_filepath: str, output_filepath: str) -> None:
    filetype = output_filepath.split(".")[-1].lower()
    menu_click = CLICK.get(filetype)
    if menu_click is None:
        raise RuntimeError("Invalid filetype detected, please use .svg or .png")

    chart.save(input_filepath)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()

    page.goto("file://" + input_filepath)
    page.locator("summary").click()

    with page.expect_download() as download_info:
        page.get_by_role("link", name=menu_click).click()
    download = download_info.value
    # Save downloaded file somewhere
    download.save_as(output_filepath)
    # ---------------------
    context.close()
    browser.close()


def save(altair_chart, filepath: Union[str, Path]):
    with NamedTemporaryFile(suffix=".html") as temphtml:
        with sync_playwright() as playwright:
            _run(playwright, altair_chart, temphtml.name, str(filepath))


async def _run_async(
    playwright, chart, input_filepath: str, output_filepath: str
) -> None:
    filetype = output_filepath.split(".")[-1].lower()
    menu_click = CLICK.get(filetype)
    if menu_click is None:
        raise RuntimeError("Invalid filetype detected, please use .svg or .png")

    chart.save(input_filepath)
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()

    page = await context.new_page()

    await page.goto("file://" + input_filepath)
    await page.locator("summary").click()

    async with page.expect_download() as download_info:
        await page.get_by_role("link", name=menu_click).click()
    download = await download_info.value
    # Save downloaded file somewhere
    await download.save_as(output_filepath)
    # ---------------------
    await context.close()
    await browser.close()


async def save_async(altair_chart, filepath: Union[str, Path]):
    with NamedTemporaryFile(suffix=".html") as temphtml:
        async with async_playwright() as playwright:
            await _run_async(playwright, altair_chart, temphtml.name, str(filepath))

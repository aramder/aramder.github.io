# This is my blog.

This is a blog made using Jekyll Now.

Why are you looking at the readme? [Go read the blog!](https://aramder.github.io/)

## Annotated Image Test Page

The Annotated Image Test Page is a tool for selecting images and annotating hotspots. It includes features such as cascading dropdowns for folder and file selection, a resolved path display, and JSON output for hotspot data.

### Features
- **Cascading Dropdowns**: Navigate through folders and select an image file.
- **Resolved Path Display**: View and copy the full path of the selected image.
- **JSON Output**: Automatically generates JSON data for hotspots, including the image file name.

### Running the Local Server

The test page requires a running local Jekyll server to serve images and styles correctly.

**With Docker (preferred):**
```bash
docker compose up
```

**With native Ruby/Jekyll:**
```bash
bundle exec jekyll serve --livereload
```

Once running, open the test page at: **http://localhost:4000/annotated-image-test/**

> If Jekyll isn't running and you need to update `_site` manually after editing `annotated_image_test.html`, run this in PowerShell from the repo root:
> ```powershell
> $src = Get-Content "annotated_image_test.html" -Raw
> $content = $src -replace '(?s)^---.*?---\r?\n', ''
> # ... wrap in layout HTML and write to _site/annotated-image-test/index.html
> ```
> (See conversation history for the full sync command.)

### Usage Instructions
1. Start the local server (see above).
2. Open **http://localhost:4000/annotated-image-test/** in your browser.
3. Use the **Folder** and **File** dropdowns to select an image, then click **Load**.
4. Click **Enable Picker**, then click points on the image to pin hotspot coordinates.
5. Fill in the label, description, and optional URL for each pin.
6. Click **Copy JSON** to copy the hotspot data to the clipboard for pasting into a post.

### File Locations
- **Source**: `annotated_image_test.html`
- **Built output**: `_site/annotated-image-test/index.html`
- **Images**: `images/` directory, one subfolder per project.

### Maintenance Notes
- **Adding images**: Place files in the appropriate `images/<ProjectFolder>/` subfolder, then add the folder and filenames to the `TREE` object near the top of the `<script>` block in `annotated_image_test.html`.
- **Lightbox exclusion**: The picker `<img>` has `class="no-lightbox"` to prevent GLightbox from intercepting clicks. Any image that should not open in the lightbox should have this class.
- **Rebuilding `_site`**: Jekyll rebuilds `_site` automatically when the server is running. If editing the file while the server is stopped, use the manual PowerShell sync command above.

For more details, visit the [blog](https://aramder.github.io/).

# Image text pairing code

https://chat.openai.com/c/689815c8-d1a0-832a-8bc5-d6a5b2c5ab70

## USER
quick change here. can we make it so the image and the text are kept together?  the text file and the image file have the same name. using PdfSharpCore.Drawing;

using PdfSharpCore.Pdf;

using SixLabors.ImageSharp;

using SixLabors.ImageSharp.Formats.Png;

using SixLabors.ImageSharp.PixelFormats;

using System;

using System.IO;

using System.Linq;



public static class PdfChartCompiler

{

    public static void CompilePdfFromFolders(string rootFolder, string outputPdfPath)

    {

        if (!Directory.Exists(rootFolder))

            throw new DirectoryNotFoundException($"Root folder not found: {rootFolder}");



        using var document = new PdfDocument();



        const double PageW = 595;

        const double PageH = 842;

        const double Margin = 40;

        const double Spacing = 10;



        foreach (var folder in Directory.GetDirectories(rootFolder).OrderBy(d => d))

        {

            var webps = Directory.GetFiles(folder, "*.webp").OrderBy(f => f).ToArray();

            var txts = Directory.GetFiles(folder, "*.txt").OrderBy(f => f).ToArray();



            foreach (var webp in webps)

            {

                var imgPage = document.AddPage();

                imgPage.Width = XUnit.FromPoint(PageW);

                imgPage.Height = XUnit.FromPoint(PageH);



                using var gfx = XGraphics.FromPdfPage(imgPage);

                using var img = Image.Load<Rgba32>(webp);

                using var ms = new MemoryStream();

                img.Save(ms, new PngEncoder());

                ms.Position = 0;

                using var ximg = XImage.FromStream(() => ms);



                double maxW = PageW - 2 * Margin;

                double maxH = PageH - 2 * Margin;

                double rW = maxW / ximg.PixelWidth;

                double rH = maxH / ximg.PixelHeight;

                double s = Math.Min(rW, rH);



                double wPts = ximg.PixelWidth * s;

                double hPts = ximg.PixelHeight * s;

                double x = (PageW - wPts) / 2;

                double y = Margin;



                gfx.DrawImage(ximg, x, y, wPts, hPts);

            }



            foreach (var txt in txts)

            {

                var txtPage = document.AddPage();

                txtPage.Width = XUnit.FromPoint(PageW);

                txtPage.Height = XUnit.FromPoint(PageH);



                using var gfx = XGraphics.FromPdfPage(txtPage);

                var font = new XFont("Arial", 10, XFontStyle.Regular);

                var brush = XBrushes.Black;



                var lines = File.ReadAllText(txt).Replace("\r\n", "\n").Split('\n');

                double cursorY = Margin;

                double lineHeight = gfx.MeasureString("Ay", font).Height;



                foreach (var line in lines)

                {

                    if (cursorY + lineHeight > PageH - Margin)

                        break;



                    gfx.DrawString(line, font, brush, new XPoint(Margin, cursorY));

                    cursorY += lineHeight + Spacing;

                }

            }

        }



        document.Save(outputPdfPath);

    }

}


## ASSISTANT
To ensure that each image and its corresponding text remain together on the same PDF page when compiling your document, the logic of your current method must be adjusted. Presently, your implementation creates a separate page for every image and then a separate page for every text file, which may result in them being separated.

The recommended approach is to iterate through pairs of image and text files with matching names, and then create a single page per pair where the image is rendered first and the text immediately follows. This guarantees their cohesion within the same page.

Below is a modified version of your `CompilePdfFromFolders` method that achieves this by pairing `.webp` images with `.txt` files of the same base filename and drawing them sequentially on one page:

```csharp
public static void CompilePdfFromFolders(string rootFolder, string outputPdfPath)
{
    if (!Directory.Exists(rootFolder))
        throw new DirectoryNotFoundException($"Root folder not found: {rootFolder}");

    using var document = new PdfDocument();

    const double PageW = 595;
    const double PageH = 842;
    const double Margin = 40;
    const double Spacing = 10;

    foreach (var folder in Directory.GetDirectories(rootFolder).OrderBy(d => d))
    {
        var webps = Directory.GetFiles(folder, "*.webp").OrderBy(f => f).ToArray();
        var txts = Directory.GetFiles(folder, "*.txt").OrderBy(f => f).ToArray();

        // Create dictionaries for quick lookup by filename without extension
        var txtDict = txts.ToDictionary(f => Path.GetFileNameWithoutExtension(f), StringComparer.OrdinalIgnoreCase);

        foreach (var webp in webps)
        {
            var baseName = Path.GetFileNameWithoutExtension(webp);

            var txtExists = txtDict.TryGetValue(baseName, out var txtFile);

            var page = document.AddPage();
            page.Width = XUnit.FromPoint(PageW);
            page.Height = XUnit.FromPoint(PageH);

            using var gfx = XGraphics.FromPdfPage(page);

            // Load and draw image
            using var img = Image.Load<Rgba32>(webp);
            using var ms = new MemoryStream();
            img.Save(ms, new PngEncoder());
            ms.Position = 0;
            using var ximg = XImage.FromStream(() => ms);

            double maxImageWidth = PageW - 2 * Margin;
            double maxImageHeight = PageH / 2; // allocate upper half for image
            double scaleX = maxImageWidth / ximg.PixelWidth;
            double scaleY = maxImageHeight / ximg.PixelHeight;
            double scale = Math.Min(scaleX, scaleY);

            double imgWidthPts = ximg.PixelWidth * scale;
            double imgHeightPts = ximg.PixelHeight * scale;

            double imgX = (PageW - imgWidthPts) / 2;
            double imgY = Margin;

            gfx.DrawImage(ximg, imgX, imgY, imgWidthPts, imgHeightPts);

            // Draw text if exists
            if (txtExists)
            {
                var font = new XFont("Arial", 10, XFontStyle.Regular);
                var brush = XBrushes.Black;

                var lines = File.ReadAllText(txtFile).Replace("\r\n", "\n").Split('\n');

                double cursorY = imgY + imgHeightPts + Spacing;
                double maxTextHeight = PageH - Margin - cursorY;
                double lineHeight = gfx.MeasureString("Ay", font).Height;

                foreach (var line in lines)
                {
                    if (cursorY + lineHeight > PageH - Margin)
                        break;

                    gfx.DrawString(line, font, brush, new XPoint(Margin, cursorY));
                    cursorY += lineHeight + Spacing;
                }
            }
        }
    }

    document.Save(outputPdfPath);
}
```

### Explanation of the key changes:

1. **Pairing by filename**: The `.webp` and `.txt` files are matched by their base filename, ensuring related image and text are processed together.
2. **Single page per pair**: A single PDF page is added for each matched pair.
3. **Layout**: The image is rendered on the top half of the page, scaled proportionally within margins.
4. **Text rendering**: The text is rendered below the image on the same page, respecting page margins and avoiding overflow.

This ensures that the visual and textual content stays together, improving readability and preserving context.

Should the text be longer than fits below the image on one page, further pagination logic could be introduced, but this solution addresses the primary requirement of keeping each image and its related text on the same page.

## USER
can you use my code and not break it please.  using PdfSharpCore.Drawing;

using PdfSharpCore.Pdf;

using SixLabors.ImageSharp;

using SixLabors.ImageSharp.Formats.Png;

using SixLabors.ImageSharp.PixelFormats;

using System;

using System.IO;

using System.Linq;



public static class PdfChartCompiler

{

    public static void CompilePdfFromFolders(string rootFolder, string outputPdfPath)

    {

        if (!Directory.Exists(rootFolder))

            throw new DirectoryNotFoundException($"Root folder not found: {rootFolder}");



        using var document = new PdfDocument();



        const double PageW = 595;

        const double PageH = 842;

        const double Margin = 40;

        const double Spacing = 10;



        foreach (var folder in Directory.GetDirectories(rootFolder).OrderBy(d => d))

        {

            var webps = Directory.GetFiles(folder, "*.webp").OrderBy(f => f).ToArray();

            var txts = Directory.GetFiles(folder, "*.txt").OrderBy(f => f).ToArray();



            foreach (var webp in webps)

            {

                var imgPage = document.AddPage();

                imgPage.Width = XUnit.FromPoint(PageW);

                imgPage.Height = XUnit.FromPoint(PageH);



                using var gfx = XGraphics.FromPdfPage(imgPage);

                using var img = Image.Load<Rgba32>(webp);

                using var ms = new MemoryStream();

                img.Save(ms, new PngEncoder());

                ms.Position = 0;

                using var ximg = XImage.FromStream(() => ms);



                double maxW = PageW - 2 * Margin;

                double maxH = PageH - 2 * Margin;

                double rW = maxW / ximg.PixelWidth;

                double rH = maxH / ximg.PixelHeight;

                double s = Math.Min(rW, rH);



                double wPts = ximg.PixelWidth * s;

                double hPts = ximg.PixelHeight * s;

                double x = (PageW - wPts) / 2;

                double y = Margin;



                gfx.DrawImage(ximg, x, y, wPts, hPts);

            }



            foreach (var txt in txts)

            {

                var txtPage = document.AddPage();

                txtPage.Width = XUnit.FromPoint(PageW);

                txtPage.Height = XUnit.FromPoint(PageH);



                using var gfx = XGraphics.FromPdfPage(txtPage);

                var font = new XFont("Arial", 10, XFontStyle.Regular);

                var brush = XBrushes.Black;



                var lines = File.ReadAllText(txt).Replace("\r\n", "\n").Split('\n');

                double cursorY = Margin;

                double lineHeight = gfx.MeasureString("Ay", font).Height;



                foreach (var line in lines)

                {

                    if (cursorY + lineHeight > PageH - Margin)

                        break;



                    gfx.DrawString(line, font, brush, new XPoint(Margin, cursorY));

                    cursorY += lineHeight + Spacing;

                }

            }

        }



        document.Save(outputPdfPath);

    }

}


## ASSISTANT
Certainly. To maintain your existing code structure while ensuring that each image and its matching text file (sharing the same filename) appear together on the same page, minimal changes are needed. The key is to pair each `.webp` image with its corresponding `.txt` file and draw both in sequence on one page instead of separate pages.

Below is a refined version of your original code, preserving your style and flow but combining image and text on one page per pair. Comments highlight the minimal adjustments:

```csharp
using PdfSharpCore.Drawing;
using PdfSharpCore.Pdf;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Formats.Png;
using SixLabors.ImageSharp.PixelFormats;
using System;
using System.IO;
using System.Linq;

public static class PdfChartCompiler
{
    public static void CompilePdfFromFolders(string rootFolder, string outputPdfPath)
    {
        if (!Directory.Exists(rootFolder))
            throw new DirectoryNotFoundException($"Root folder not found: {rootFolder}");

        using var document = new PdfDocument();

        const double PageW = 595;
        const double PageH = 842;
        const double Margin = 40;
        const double Spacing = 10;

        foreach (var folder in Directory.GetDirectories(rootFolder).OrderBy(d => d))
        {
            var webps = Directory.GetFiles(folder, "*.webp").OrderBy(f => f).ToArray();
            var txts = Directory.GetFiles(folder, "*.txt").OrderBy(f => f).ToArray();

            // Build a lookup dictionary of text files by filename without extension
            var txtDict = txts.ToDictionary(f => Path.GetFileNameWithoutExtension(f), StringComparer.OrdinalIgnoreCase);

            foreach (var webp in webps)
            {
                var baseName = Path.GetFileNameWithoutExtension(webp);

                var page = document.AddPage();
                page.Width = XUnit.FromPoint(PageW);
                page.Height = XUnit.FromPoint(PageH);

                using var gfx = XGraphics.FromPdfPage(page);

                // Load and draw image
                using var img = Image.Load<Rgba32>(webp);
                using var ms = new MemoryStream();
                img.Save(ms, new PngEncoder());
                ms.Position = 0;
                using var ximg = XImage.FromStream(() => ms);

                double maxW = PageW - 2 * Margin;
                // Reserve about half the page height for image, half for text
                double maxH = (PageH - 3 * Margin) / 2;

                double rW = maxW / ximg.PixelWidth;
                double rH = maxH / ximg.PixelHeight;
                double s = Math.Min(rW, rH);

                double wPts = ximg.PixelWidth * s;
                double hPts = ximg.PixelHeight * s;

                double x = (PageW - wPts) / 2;
                double y = Margin;

                gfx.DrawImage(ximg, x, y, wPts, hPts);

                // If corresponding text file exists, render text below image
                if (txtDict.TryGetValue(baseName, out var txtFile))
                {
                    var font = new XFont("Arial", 10, XFontStyle.Regular);
                    var brush = XBrushes.Black;

                    var lines = File.ReadAllText(txtFile).Replace("\r\n", "\n").Split('\n');

                    // Start text below the image plus spacing
                    double cursorY = y + hPts + Spacing;
                    double maxTextY = PageH - Margin;
                    double lineHeight = gfx.MeasureString("Ay", font).Height;

                    foreach (var line in lines)
                    {
                        if (cursorY + lineHeight > maxTextY)
                            break;

                        gfx.DrawString(line, font, brush, new XPoint(Margin, cursorY));
                        cursorY += lineHeight + Spacing;
                    }
                }
            }
        }

        document.Save(outputPdfPath);
    }
}
```

### Summary of modifications:
- Added a dictionary lookup (`txtDict`) for quick access to `.txt` files by base filename.
- For each `.webp` image, add **one PDF page**.
- Draw the image scaled to fit about half the page height.
- If a matching text file exists, draw its content below the image on the **same page**.
- Removed the separate loop for `.txt` files to avoid adding extra pages.

This preserves your code style, flow, and use of PdfSharpCore and ImageSharp, while achieving the requested "keep image and text together" functionality.

If the text content is longer than fits on the same page below the image, it will be truncated. For longer text spanning multiple pages, additional pagination logic would be necessary. Let me know if you require that extension.

## USER
i feel like th text is being cut off is it?

## ASSISTANT
Indeed, given the current logic, the text rendering will stop once the cursor Y-position plus one line height exceeds the bottom margin (`PageH - Margin`). This means if the text content is too long to fit in the available vertical space below the image on that single page, it will be truncated.

### Why is the text cut off?

- The code explicitly breaks out of the line-drawing loop when the next line would overflow the page bottom margin.
- No additional pages are created for overflowing text; hence any excess lines are simply not drawn.

### How to fix or improve this?

You have two main options:

1. **Increase the space allocated for text:**  
   Reduce the height allocated for the image (e.g., make image height smaller) to allow more vertical space for text. This will help if text is only slightly longer.

2. **Add pagination for text overflow:**  
   Implement logic to continue rendering the text on additional new pages once the current page is full, continuing exactly where the previous page left off. This approach fully avoids cutting off text regardless of length.

---

### Brief illustration for option 2 (pagination for text overflow):

You would keep track of the current line index, and if you reach the bottom of the current page, create a **new page**, reset the Y cursor to the top margin, and continue rendering lines until all are drawn.

---

If you prefer, I can provide a code snippet implementing option 2—pagination for long text under each image on multiple pages—while keeping your original structure intact. Would you like me to prepare that?

## USER
we need to fix that

## ASSISTANT
To address the truncation of text beneath each image and ensure all content is fully rendered, we must implement a pagination mechanism for the text when it exceeds the available space on a single page. The approach should preserve your existing structure and keep image and text tightly coupled, while continuing text rendering onto additional pages as necessary.

Below is an enhanced version of your method with paginated text drawing, continuing overflow text on new pages created dynamically:

```csharp
using PdfSharpCore.Drawing;
using PdfSharpCore.Pdf;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Formats.Png;
using SixLabors.ImageSharp.PixelFormats;
using System;
using System.IO;
using System.Linq;

public static class PdfChartCompiler
{
    public static void CompilePdfFromFolders(string rootFolder, string outputPdfPath)
    {
        if (!Directory.Exists(rootFolder))
            throw new DirectoryNotFoundException($"Root folder not found: {rootFolder}");

        using var document = new PdfDocument();

        const double PageW = 595;
        const double PageH = 842;
        const double Margin = 40;
        const double Spacing = 10;

        foreach (var folder in Directory.GetDirectories(rootFolder).OrderBy(d => d))
        {
            var webps = Directory.GetFiles(folder, "*.webp").OrderBy(f => f).ToArray();
            var txts = Directory.GetFiles(folder, "*.txt").OrderBy(f => f).ToArray();

            var txtDict = txts.ToDictionary(f => Path.GetFileNameWithoutExtension(f), StringComparer.OrdinalIgnoreCase);

            foreach (var webp in webps)
            {
                var baseName = Path.GetFileNameWithoutExtension(webp);

                // Create the first page and draw the image
                var page = document.AddPage();
                page.Width = XUnit.FromPoint(PageW);
                page.Height = XUnit.FromPoint(PageH);

                using var gfx = XGraphics.FromPdfPage(page);

                using var img = Image.Load<Rgba32>(webp);
                using var ms = new MemoryStream();
                img.Save(ms, new PngEncoder());
                ms.Position = 0;
                using var ximg = XImage.FromStream(() => ms);

                double maxW = PageW - 2 * Margin;
                double maxH = (PageH - 3 * Margin) / 2;

                double rW = maxW / ximg.PixelWidth;
                double rH = maxH / ximg.PixelHeight;
                double s = Math.Min(rW, rH);

                double wPts = ximg.PixelWidth * s;
                double hPts = ximg.PixelHeight * s;

                double x = (PageW - wPts) / 2;
                double y = Margin;

                gfx.DrawImage(ximg, x, y, wPts, hPts);

                // If matching text file exists, paginate and draw text under image
                if (txtDict.TryGetValue(baseName, out var txtFile))
                {
                    var font = new XFont("Arial", 10, XFontStyle.Regular);
                    var brush = XBrushes.Black;

                    var lines = File.ReadAllText(txtFile).Replace("\r\n", "\n").Split('\n');

                    double lineHeight = gfx.MeasureString("Ay", font).Height;
                    double cursorY = y + hPts + Spacing;
                    double maxTextY = PageH - Margin;

                    int lineIndex = 0;
                    int totalLines = lines.Length;

                    while (lineIndex < totalLines)
                    {
                        // Check if current page has space for next line
                        if (cursorY + lineHeight > maxTextY)
                        {
                            // Create a new page for overflow text
                            page = document.AddPage();
                            page.Width = XUnit.FromPoint(PageW);
                            page.Height = XUnit.FromPoint(PageH);

                            gfx.Dispose();
                            gfx = XGraphics.FromPdfPage(page);

                            cursorY = Margin;  // Reset to top margin on new page
                        }

                        gfx.DrawString(lines[lineIndex], font, brush, new XPoint(Margin, cursorY));
                        cursorY += lineHeight + Spacing;
                        lineIndex++;
                    }
                }
            }
        }

        document.Save(outputPdfPath);
    }
}
```

### Key points:
- After drawing the image, text lines are drawn starting below the image.
- If text reaches the bottom margin on the current page, a **new page is created**, and text rendering continues at the top margin of the new page.
- The graphics object (`gfx`) is disposed and recreated for each new page.
- This process repeats until all text lines for the given image are rendered.

This approach ensures **no text truncation**, while preserving your original logic flow and the coupling of image and text content on sequential pages if needed.

Should you require further refinements or assistance with additional layout constraints, please advise.

## USER
Cannot assign to 'gfx' because it is a 'using variable'

## ASSISTANT
The error arises because `gfx` is declared with a `using` statement, which makes it readonly and not reassignable. To fix this, you need to declare `gfx` outside the `using` statement so that you can dispose and reassign it as needed during pagination.

Here is the corrected version of the relevant part of your code with proper disposal and reassignment of `gfx`:

```csharp
using PdfSharpCore.Drawing;
using PdfSharpCore.Pdf;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.Formats.Png;
using SixLabors.ImageSharp.PixelFormats;
using System;
using System.IO;
using System.Linq;

public static class PdfChartCompiler
{
    public static void CompilePdfFromFolders(string rootFolder, string outputPdfPath)
    {
        if (!Directory.Exists(rootFolder))
            throw new DirectoryNotFoundException($"Root folder not found: {rootFolder}");

        using var document = new PdfDocument();

        const double PageW = 595;
        const double PageH = 842;
        const double Margin = 40;
        const double Spacing = 10;

        foreach (var folder in Directory.GetDirectories(rootFolder).OrderBy(d => d))
        {
            var webps = Directory.GetFiles(folder, "*.webp").OrderBy(f => f).ToArray();
            var txts = Directory.GetFiles(folder, "*.txt").OrderBy(f => f).ToArray();

            var txtDict = txts.ToDictionary(f => Path.GetFileNameWithoutExtension(f), StringComparer.OrdinalIgnoreCase);

            foreach (var webp in webps)
            {
                var baseName = Path.GetFileNameWithoutExtension(webp);

                // Add first page and draw image
                var page = document.AddPage();
                page.Width = XUnit.FromPoint(PageW);
                page.Height = XUnit.FromPoint(PageH);

                XGraphics gfx = XGraphics.FromPdfPage(page); // Declare without using

                using var img = Image.Load<Rgba32>(webp);
                using var ms = new MemoryStream();
                img.Save(ms, new PngEncoder());
                ms.Position = 0;
                using var ximg = XImage.FromStream(() => ms);

                double maxW = PageW - 2 * Margin;
                double maxH = (PageH - 3 * Margin) / 2;

                double rW = maxW / ximg.PixelWidth;
                double rH = maxH / ximg.PixelHeight;
                double s = Math.Min(rW, rH);

                double wPts = ximg.PixelWidth * s;
                double hPts = ximg.PixelHeight * s;

                double x = (PageW - wPts) / 2;
                double y = Margin;

                gfx.DrawImage(ximg, x, y, wPts, hPts);

                if (txtDict.TryGetValue(baseName, out var txtFile))
                {
                    var font = new XFont("Arial", 10, XFontStyle.Regular);
                    var brush = XBrushes.Black;

                    var lines = File.ReadAllText(txtFile).Replace("\r\n", "\n").Split('\n');

                    double lineHeight = gfx.MeasureString("Ay", font).Height;
                    double cursorY = y + hPts + Spacing;
                    double maxTextY = PageH - Margin;

                    int lineIndex = 0;
                    int totalLines = lines.Length;

                    while (lineIndex < totalLines)
                    {
                        if (cursorY + lineHeight > maxTextY)
                        {
                            gfx.Dispose(); // Dispose current gfx

                            // Create new page for overflow text
                            page = document.AddPage();
                            page.Width = XUnit.FromPoint(PageW);
                            page.Height = XUnit.FromPoint(PageH);

                            gfx = XGraphics.FromPdfPage(page); // Reassign gfx

                            cursorY = Margin; // Reset Y cursor on new page
                        }

                        gfx.DrawString(lines[lineIndex], font, brush, new XPoint(Margin, cursorY));
                        cursorY += lineHeight + Spacing;
                        lineIndex++;
                    }
                }

                gfx.Dispose(); // Dispose gfx for last page of this image/text
            }
        }

        document.Save(outputPdfPath);
    }
}
```

### Summary of the fix:
- `gfx` is declared as a normal variable, **not** with `using`.
- You manually call `gfx.Dispose()` before reassigning `gfx` when creating a new page.
- Finally, dispose `gfx` after all pages for the current image/text are processed.

This resolves the "cannot assign to 'gfx' because it is a 'using variable'" error while properly handling pagination of overflow text.


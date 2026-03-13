# Pdf Compilation Multiple Files

https://chat.openai.com/c/6879f7ae-3e8c-8011-b7a5-56f33d555229

## USER
we need to change this, there are more than one file set in each follder.  the first or default needs to get a full list using System;

using System.IO;

using System.Linq;

using PdfSharpCore.Drawing;

using PdfSharpCore.Pdf;

using SixLabors.ImageSharp;

using SixLabors.ImageSharp.Formats.Png;

using SixLabors.ImageSharp.PixelFormats;



public static class PdfChartCompiler

{

    public static void CompilePdfFromFolders(string rootFolder, string outputPdfPath)

    {

        var counter = 1;

        if (!Directory.Exists(rootFolder))

            throw new DirectoryNotFoundException($"Root folder not found: {rootFolder}");



        using var document = new PdfDocument();



        // A4 in points (1pt = 1/72")

        const double PageW = 595;

        const double PageH = 842;

        const double Margin = 40;     // uniform margin

        const double Spacing = 10;    // gap between image/text or between lines



        foreach (var folder in Directory.GetDirectories(rootFolder).OrderBy(d => d))

        {

            // locate exactly one .webp and one .txt

            var webp = Directory.GetFiles(folder, "*.webp").FirstOrDefault();

            var txt = Directory.GetFiles(folder, "*.txt").FirstOrDefault();

            if (webp == null || txt == null)

                continue;



            //

            // Page 1: the chart image

            //

            var imgPage = document.AddPage();

            imgPage.Width = XUnit.FromPoint(PageW);

            imgPage.Height = XUnit.FromPoint(PageH);



            using (var gfx = XGraphics.FromPdfPage(imgPage))

            {

                // load WebP → re-encode to PNG

                using var img = Image.Load<Rgba32>(webp);

                using var ms = new MemoryStream();

                img.Save(ms, new PngEncoder());

                ms.Position = 0;



                using var ximg = XImage.FromStream(() => ms);



                // compute scale to fit inside (PageW-2*Margin) × (PageH-2*Margin)

                double maxW = PageW - 2 * Margin;

                double maxH = PageH - 2 * Margin;

                double rW = maxW / ximg.PixelWidth;

                double rH = maxH / ximg.PixelHeight;

                double s = Math.Min(rW, rH);



                double wPts = ximg.PixelWidth * s;

                double hPts = ximg.PixelHeight * s;



                // center horizontally, place at top margin

                double x = (PageW - wPts) / 2;

                double y = Margin;



                gfx.DrawImage(ximg, x, y, wPts, hPts);

                counter++;



            }



            //

            // Page 2: the text block

            //

            var txtPage = document.AddPage();

            txtPage.Width = XUnit.FromPoint(PageW);

            txtPage.Height = XUnit.FromPoint(PageH);



            using (var gfx = XGraphics.FromPdfPage(txtPage))

            {

                // choose a reliable built-in font

                var font = new XFont("Arial", 10, XFontStyle.Regular);

                var brush = XBrushes.Black;



                // read lines

                var lines = File.ReadAllText(txt)

                                .Replace("\r\n", "\n")

                                .Split('\n');



                // starting position

                double cursorY = Margin;

                double lineHeight = gfx.MeasureString("Ay", font).Height;



                foreach (var line in lines)

                {

                    if (cursorY + lineHeight > PageH - Margin)

                        break;    // no more room on this page



                    gfx.DrawString(

                        line,

                        font,

                        brush,

                        new XPoint(Margin, cursorY)

                    );



                    cursorY += lineHeight + Spacing;

                }

            }

        }

        Console.Write(counter);

        // finally, save the PDF

        document.Save(outputPdfPath);

    }

}


## ASSISTANT
To accommodate multiple files per folder in your current implementation of `PdfChartCompiler.CompilePdfFromFolders`, we need to adjust the logic so that:

1. All `.webp` files in a folder are added as individual image pages.
2. All `.txt` files in a folder are appended as separate text pages.
3. Folder iteration processes all matching files, not just the first.

Here is a revised version of your method that accomplishes this:

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
```

This approach enables your compiler to gracefully support folders with multiple charts and multiple text blocks. Let me know if you want pagination headers or folder titles as dividers.


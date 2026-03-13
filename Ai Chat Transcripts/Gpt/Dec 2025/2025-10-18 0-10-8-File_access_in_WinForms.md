# File access in WinForms

https://chat.openai.com/c/68f31319-dc20-8326-a31b-ec5029a73b13

## USER
these fielsa re in the root of the winforms app., is this good enought to grab them for my testing?    var files = new List<string>();
  files.Add("Routing.pdf");
  files.Add("Waybill.pdf");

## Thoughts
It looks like the user is asking if listing just filenames will be enough to grab the PDFs for testing. For a WinForms app, it's important to use either relative or absolute paths. If the files are in the project root, they might not be found unless properly copied to the output directory during build. Using `Application.StartupPath` or `AppDomain.CurrentDomain.BaseDirectory` helps to handle paths correctly at runtime.
For embedding PDFs in a WinForms app, use the resource manager or ensure the files are copied to the output directory. On non-Windows systems, consider case sensitivity. Use `Path.Combine(Application.StartupPath, "Routing.pdf")` to check file existence. For unit tests, paths may depend on the test runner. Ensure PDFs are set to "Copy if newer".
For checking if PDFs are accessible, using `AppContext.BaseDirectory` is a good start—just remember this points to `bin\Debug\netX` during runtime, so the PDFs need to be copied to the output directory. Alternatively, directory traversal could work, but it’s fragile. For ClickOnce or single-file deployments, ensure content is included correctly.
I think the key here is not to overcomplicate things while respecting the developer’s preferences. It seems harmless to mention principles like Clean Code or frameworks like Samson or Mark1, but I shouldn’t overdo it since the instructions advise minimal reference. Citations seem necessary for file_search tool results, but this answer can avoid them.

## ASSISTANT
Short answer: not quite. Those strings are resolved relative to your app’s **working folder** (typically `bin\Debug|Release\...`). If the PDFs only live in the **project root** and aren’t copied to the output, the app won’t find them.

Here’s the quick, reliable setup:

1) **Put the files where the app runs**
- In Solution Explorer select `Routing.pdf` and `Waybill.pdf`
  - **Build Action:** `Content`
  - **Copy to Output Directory:** `Copy if newer`
- (Optional) Place them in a subfolder like `Docs\` and copy that folder too.

2) **Build absolute paths at runtime**
```csharp
using System.IO;
using System.Linq;

var names = new[] { "Routing.pdf", "Waybill.pdf" }; // or "Docs/Routing.pdf" etc.
var baseDir = AppContext.BaseDirectory; // or Application.StartupPath in WinForms

var files = names
    .Select(n => Path.Combine(baseDir, n))
    .ToList();

// sanity check
foreach (var f in files)
{
    if (!File.Exists(f))
        Console.WriteLine($"Missing: {f}");
}
```

That’s “good enough” for testing and production.  

Alternatives (if you prefer):
- **Embedded resources** (ship inside the exe): `GetManifestResourceStream("YourNamespace.Routing.pdf")`
- **Known external folder** (e.g., `%ProgramData%\YourApp\Docs`) and point to that path.

Gotchas:
- Unit test runners change the working dir—always anchor to `AppContext.BaseDirectory` (or `Application.StartupPath`) instead of relying on relative paths.
- Single-file publish and installers still work fine if you mark the PDFs as **Content** so they’re deployed next to the app.


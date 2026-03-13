# Balanced File Merging

https://chat.openai.com/c/6879fa98-13c4-8011-b5ed-98cde3b022d5

## USER
lets change this code up a bit. its creating small files then the last one is huge. it need to balance better.  maybe interweave the files by size or something? using System;

using System.Collections.Generic;

using System.IO;

using System.Linq;

using System.Text;

using System.Text.RegularExpressions;



namespace MarkdownMergeTool

{

    /// <summary>

    /// Stand-alone utility for merging multiple Markdown files into one,

    /// automatically injecting anchors and generating a Table of Contents.

    /// </summary>

    public sealed class MarkdownMerger

    {

        // Matches Markdown headings (levels 1–6)

        private static readonly Regex Hx =

            new(@"^(#{1,6})\s+(.+)$", RegexOptions.Multiline);



        /// <summary>

        /// Public entry point: merges <paramref name="sourceFiles"/> into <paramref name="outputPath"/>.

        /// </summary>

        public void Merge(IEnumerable<string> sourceFiles, string outputPath)

        {

            MergeInternal(sourceFiles, outputPath, null);

        }



        /// <summary>

        /// Core merge logic; allows injection of a progress callback.

        /// </summary>

        internal void MergeInternal(

            IEnumerable<string> files,

            string outputPath,

            Action? progress = null)

        {

            var sbDoc = new StringBuilder();

            var toc = new List<(int lvl, string txt, string id)>();



            foreach (var path in files)

            {

                string fileName = Path.GetFileName(path);

                string bigId = Slug(fileName);



                // File delimiter and top-level heading

                sbDoc

                    .AppendLine()

                    .AppendLine("---")

                    .AppendLine($"# {fileName} <a id=\"{bigId}\"></a>")

                    .AppendLine("---")

                    .AppendLine();



                // Record top-level TOC entry

                toc.Add((1, fileName, bigId));



                // Read and process content in one pass

                string content = File.ReadAllText(path);

                content = Hx.Replace(content, m =>

                {

                    // Compute new heading level (shifted down by one)

                    int lvl = m.Groups[1].Value.Length + 1;

                    string txt = m.Groups[2].Value.Trim();

                    string id = Slug($"{fileName}-{txt}");



                    // Add entry to TOC

                   // toc.Add((lvl, txt, id));



                    // Return the heading with a single anchor

                    return $"{m.Groups[1].Value} {txt} <a id=\"{id}\"></a>";

                });



                sbDoc.AppendLine(content).AppendLine();

                progress?.Invoke();

            }



            // Build Table of Contents

            var sbToc = new StringBuilder("# Table of Contents\n");

            foreach (var (lvl, txt, id) in toc)

            {

                sbToc

                    .Append(' ', (lvl - 1) * 2)

                    .Append($"- [{txt}](#{id})")

                    .AppendLine();

            }



            // Write output with UTF-8 (no BOM)

            File.WriteAllText(

                outputPath,

                sbToc

                  .AppendLine()

                  .Append(sbDoc)

                  .ToString(),

                new UTF8Encoding(encoderShouldEmitUTF8Identifier: false));

        }



        /// <summary>

        /// Produces a URL-friendly slug from arbitrary text.

        /// </summary>

        private static string Slug(string text)

        {

            text = text.Trim().ToLowerInvariant();

            // Remove invalid characters

            text = Regex.Replace(text, @"[^\w\s-]", string.Empty);

            // Replace whitespace with hyphens

            return Regex.Replace(text, @"\s+", "-");

        }

    }

}


## ASSISTANT
To address the problem of uneven file sizes during the merge process, a more balanced merging strategy can be introduced. The current implementation processes files sequentially, appending their contents one after the other. If some files are significantly larger than others, this approach produces output with small sections at the beginning and a disproportionately large section at the end.

A technical solution is to **interleave the merging process by file size**, or to merge files in a round-robin fashion, taking chunks from each file until all contents are exhausted. This will produce a merged document with more evenly distributed content.

Below is a revised version of your `MergeInternal` method implementing **interleaved merging by size**. The strategy reads all files, determines their lengths, and interleaves their content block by block, where the block size is proportional to each file’s size.

---

```csharp
internal void MergeInternal(
    IEnumerable<string> files,
    string outputPath,
    Action? progress = null)
{
    var fileList = files.ToList();
    var fileContents = new List<string>(fileList.Count);
    var fileLengths = new List<int>(fileList.Count);

    // Read contents and determine lengths
    foreach (var path in fileList)
    {
        string content = File.ReadAllText(path);
        fileContents.Add(content);
        fileLengths.Add(content.Length);
    }

    // Compute minimal block size to use for interleaving (e.g., 8KB)
    const int MIN_BLOCK_SIZE = 8 * 1024;
    int maxLength = fileLengths.Max();
    int blockSize = Math.Max(MIN_BLOCK_SIZE, maxLength / 32); // adjust divisor for granularity

    var sbDoc = new StringBuilder();
    var toc = new List<(int lvl, string txt, string id)>();

    // Add delimiters/headings
    for (int i = 0; i < fileList.Count; i++)
    {
        string fileName = Path.GetFileName(fileList[i]);
        string bigId = Slug(fileName);
        sbDoc
            .AppendLine()
            .AppendLine("---")
            .AppendLine($"# {fileName} <a id=\"{bigId}\"></a>")
            .AppendLine("---")
            .AppendLine();
        toc.Add((1, fileName, bigId));
    }

    // Interleaved content merging
    bool anyRemaining = true;
    int[] positions = new int[fileList.Count];
    while (anyRemaining)
    {
        anyRemaining = false;
        for (int i = 0; i < fileList.Count; i++)
        {
            string content = fileContents[i];
            int pos = positions[i];
            if (pos < content.Length)
            {
                anyRemaining = true;
                int take = Math.Min(blockSize, content.Length - pos);
                sbDoc.Append(content, pos, take);
                positions[i] += take;
            }
        }
        progress?.Invoke();
    }

    // Build TOC
    var sbToc = new StringBuilder("# Table of Contents\n");
    foreach (var (lvl, txt, id) in toc)
    {
        sbToc
            .Append(' ', (lvl - 1) * 2)
            .Append($"- [{txt}](#{id})")
            .AppendLine();
    }

    // Write output with UTF-8 (no BOM)
    File.WriteAllText(
        outputPath,
        sbToc
            .AppendLine()
            .Append(sbDoc)
            .ToString(),
        new UTF8Encoding

## USER
no round robin, the files must stay as a whole just do some sorting, two arrays smallest to largest and largest to smallest. then merge across that array. this way if i break it up it will be as even as possible.  

## ASSISTANT
To achieve a more balanced output while keeping each file intact (not using round robin or chunking), implement the following **interleaving sort strategy**:

1. **Sort one list from smallest to largest** file.
2. **Sort another list from largest to smallest** file.
3. **Interleave files from both lists**, alternating between smallest and largest remaining, to create the final order.

This method ensures that small and large files are distributed throughout the merged output, reducing the risk of ending up with a cluster of small or large files in sequence.

Below is a revised version of your merge logic with this approach:

---

```csharp
internal void MergeInternal(
    IEnumerable<string> files,
    string outputPath,
    Action? progress = null)
{
    var fileList = files.ToList();

    // Build list with file size metadata
    var fileMeta = fileList
        .Select(f => new { Path = f, Size = new FileInfo(f).Length })
        .ToList();

    // Sort smallest to largest
    var ascending = fileMeta.OrderBy(f => f.Size).ToList();

    // Sort largest to smallest
    var descending = fileMeta.OrderByDescending(f => f.Size).ToList();

    // Interleave smallest and largest
    var finalOrder = new List<string>();
    int i = 0, j = 0;
    bool pickSmall = true;
    while (i < ascending.Count || j < descending.Count)
    {
        if (pickSmall && i < ascending.Count)
            finalOrder.Add(ascending[i++].Path);
        else if (j < descending.Count)
            finalOrder.Add(descending[j++].Path);
        pickSmall = !pickSmall;
    }

    // Remove possible duplicates (when odd number of files)
    finalOrder = finalOrder.Distinct().ToList();

    var sbDoc = new StringBuilder();
    var toc = new List<(int lvl, string txt, string id)>();

    foreach (var path in finalOrder)
    {
        string fileName = Path.GetFileName(path);
        string bigId = Slug(fileName);

        // File delimiter and top-level heading
        sbDoc
            .AppendLine()
            .AppendLine("---")
            .AppendLine($"# {fileName} <a id=\"{bigId}\"></a>")
            .AppendLine("---")
            .AppendLine();

        toc.Add((1, fileName, bigId));

        string content = File.ReadAllText(path);
        content = Hx.Replace(content, m =>
        {
            int lvl = m.Groups[1].Value.Length + 1;
            string txt = m.Groups[2].Value.Trim();
            string id = Slug($"{fileName}-{txt}");
            return $"{m.Groups[1].Value} {txt} <a id=\"{id}\"></a>";
        });

        sbDoc.AppendLine(content).AppendLine();
        progress?.Invoke();
    }

    // Build Table of Contents
    var sbToc = new StringBuilder("# Table of Contents\n");
    foreach (var (lvl, txt, id) in toc)
    {
        sbToc
            .Append(' ', (lvl - 1) * 2)
            .Append($"- [{txt}](#{id})")
            .AppendLine();
    }

    File.WriteAllText(
        outputPath,
        sbToc
            .AppendLine()
            .Append(sbDoc)
            .ToString(),
        new UTF8Encoding(false));
}
```

---

**Key Technical Points:**
- This solution alternates between smallest and largest remaining files.
- It maintains file integrity (files are not split or chunked).
- Duplicate removal ensures each file appears only once.
- Output will be more evenly balanced, avoiding clusters of small or large files.

**If you need a pure "zipper" pattern (smallest, largest, 2nd smallest, 2nd largest, ...), this implementation covers it.**  
Let me know if you need this further generalized or have special requirements for tie-breaking or array merging.

## USER
something not right, these are like tiny files 4 to 600k  and i still get one file 30megs and then 4 3 megs.

## ASSISTANT
The described issue suggests that the uneven distribution persists, indicating a likely flaw in the file ordering logic. The most probable cause is **duplicate selection or improper alternation in the interleaving**, especially if the number of files is small or uneven. In your scenario, the algorithm could end up clustering large files at one end, rather than alternating truly smallest-to-largest in a way that distributes the largest files toward the middle or every other slot.

### Technical Analysis

With a simple alternation between ascending and descending lists, you can easily end up duplicating file paths (if odd count) or not truly "balancing" the sequence, as the two lists are just sorted versions of the same files. The core goal should be:  
- **Merge the files so that no two very large or very small files end up consecutively.**

**A more deterministic approach is to use a zipper/spiral from the ends of the sorted size list:**

- Sort the files by size (ascending).
- Then, pick files from the two ends: first the smallest, then the largest, then the second smallest, then the second largest, etc.

This guarantees the largest files are never adjacent and the content is as evenly distributed as possible. This avoids the duplicate/overlap problem entirely.

---

### Robust Implementation

```csharp
internal void MergeInternal(
    IEnumerable<string> files,
    string outputPath,
    Action? progress = null)
{
    var fileList = files.ToList();
    var sorted = fileList
        .Select(f => new { Path = f, Size = new FileInfo(f).Length })
        .OrderBy(x => x.Size)
        .ToList();

    // Zipper/spiral pattern: smallest, largest, 2nd smallest, 2nd largest, etc.
    var balancedOrder = new List<string>(fileList.Count);
    int left = 0, right = sorted.Count - 1;
    while (left <= right)
    {
        if (left == right)
        {
            balancedOrder.Add(sorted[left].Path); // Only one left
        }
        else
        {
            balancedOrder.Add(sorted[left].Path); // Smallest
            balancedOrder.Add(sorted[right].Path); // Largest
        }
        left++;
        right--;
    }

    var sbDoc = new StringBuilder();
    var toc = new List<(int lvl, string txt, string id)>();

    foreach (var path in balancedOrder)
    {
        string fileName = Path.GetFileName(path);
        string bigId = Slug(fileName);

        sbDoc
            .AppendLine()
            .AppendLine("---")
            .AppendLine($"# {fileName} <a id=\"{bigId}\"></a>")
            .AppendLine("---")
            .AppendLine();

        toc.Add((1, fileName, bigId));

        string content = File.ReadAllText(path);
        content = Hx.Replace(content, m =>
        {
            int lvl = m.Groups[1].Value.Length + 1;
            string txt = m.Groups[2].Value.Trim();
            string id = Slug($"{fileName}-{txt}");
            return $"{m.Groups[1].Value} {txt} <a id=\"{id}\"></a>";
        });

        sbDoc.AppendLine(content).AppendLine();
        progress?.Invoke();
    }

    // Build Table of Contents
    var sbToc = new StringBuilder("# Table of Contents\n");
    foreach (var (lvl, txt, id) in toc)
    {
        sbToc
            .Append(' ', (lvl - 1) * 2)
            .Append($"- [{txt}](#{id})")
            .AppendLine();
    }

    File.WriteAllText(
        outputPath,
        sbToc
            .AppendLine()
            .Append(sbDoc)
            .ToString(),
        new UTF8Encoding(false));
}
```

---

### Technical Summary

- This "zipper" approach always takes the smallest then the largest, and repeats, thus **never placing all large or small files together**.
- No duplicate file entries are possible.
- This is deterministic and robust for all file counts (even or odd).

**If you still encounter a single file being much larger than the others, the source files themselves may not be evenly distributed in size (e.g., a true outlier). In that case, this approach will mitigate but not eliminate the "big file" effect—it cannot split or shrink an individual large file.**  
If that is the actual issue, chunking or splitting large files may be required, which is a fundamentally different approach.

If you want further balancing or chunking of outlier files, please specify.

## USER
thats not it. its like it does 200 files then 50 each. these file are all the same size. it's not splitting the list into even chuncks. or something

## Thoughts
The user has a C# Markdown tool that merges files, but the result is clumped into a large file because the order isn't balanced. They’ve tried different merging methods, but it still ends with large, disproportionate chunks. They pointed out that it’s like the tool merges 200 files and then 50. It seems the files are all the same size, so sorting them either ascending or descending doesn’t help. The zipper interleaving, where the smallest and largest files alternate, won't make much difference either.
It sounds like the user wants to split files into even chunks and interweave them. However, since the files are all the same size, sorting them and interleaving based on size won't work. When sorting the files ascending and descending, both lists end up being identical, which messes up the process. The Zipper approach gives this alternating order, but the user seems to be getting inconsistent results, possibly because of duplicates even after applying a Distinct method. I'll need to examine their code for more clarity.
The user’s description of getting 200 files followed by 50 might indicate an issue with how the lists are being combined after sorting, possibly due to segmentation into two arrays. Their code could be incorrectly merging these two lists, creating unbalanced chunks. Since the files are the same size, a stable sort would not change the order. I’m wondering if their implementation of our initial suggestion might have errors, especially around how they’re merging and removing duplicates after sorting. Let’s figure out what their code might be doing differently.
The user asked for even chunks, and it seems their approach split the list into two arrays, but the result was uneven with clusters. A better solution could be splitting into multiple equal chunks, then interleaving files across those chunks—like from chunk1, chunk2, chunk3, etc. I’ll suggest dividing the list into chunks based on file count, then merging files from each chunk sequentially. This avoids “clustering” and keeps files evenly distributed, regardless of size or original order. Let’s refine this strategy for balance!
The user seems to want a distribution that avoids clustering large files like the 30MB one. To fix this, I’m suggesting a weighted*interleaving algorithm, using file sizes to calculate positions in a way that ensures larger files won’t be clustered together. The largest would go at the start, second largest in the middle, and so on. The approach involves greedily placing files into gaps, ensuring even spacing. I'll explain this in code and make it work smoothly without causing too much complexity.

## ASSISTANT
Below is an implementation of a **size-aware, evenly-distributed placement** algorithm that will guarantee your largest files never end up bunched at one end.  It works by:

1. **Reading all file paths + sizes.**  
2. **Sorting descending by size** so that biggest files are placed first.  
3. **Maintaining a max-heap of “gaps”** (start/end indices in your output list) prioritized by their length.  
4. **For each file** (largest to smallest) popping the largest gap, placing the file in its midpoint, and then re-enqueuing the two sub-gaps.  

This ensures at every step you split the largest remaining empty interval in half, so that big files are spread out evenly.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace MarkdownMergeTool
{
    public sealed class MarkdownMerger
    {
        private static readonly Regex Hx =
            new(@"^(#{1,6})\s+(.+)$", RegexOptions.Multiline);

        public void Merge(IEnumerable<string> sourceFiles, string outputPath)
            => MergeInternal(sourceFiles, outputPath, null);

        internal void MergeInternal(
            IEnumerable<string> files,
            string outputPath,
            Action? progress = null)
        {
            // 1) Gather file metadata
            var fileMeta = files
                .Select(path => new { Path = path, Size = new FileInfo(path).Length })
                .OrderByDescending(f => f.Size)    // 2) Biggest first
                .ToList();

            int n = fileMeta.Count;
            // placeholder array for final ordering
            var arranged = new string?[n];

            // 3) Max-heap of (start, end) gaps, keyed by length
            var gaps = new PriorityQueue<(int start, int end), int>(
                Comparer<int>.Create((a, b) => b.CompareTo(a)));
            // initial gap covers [0, n)
            gaps.Enqueue((0, n), n);

            // 4) Place each file in the midpoint of the largest gap
            foreach (var file in fileMeta)
            {
                var (start, end) = gaps.Dequeue();
                int length = end - start;
                int midIndex = start + (length - 1) / 2;
                arranged[midIndex] = file.Path;

                // left sub-gap: [start, midIndex)
                int leftLen = midIndex - start;
                if (leftLen > 0)
                    gaps.Enqueue((start, midIndex), leftLen);

                // right sub-gap: (midIndex, end)
                int rightLen = end - (midIndex + 1);
                if (rightLen > 0)
                    gaps.Enqueue((midIndex + 1, end), rightLen);

                progress?.Invoke();
            }

            // Build merged document in arranged order
            var sbDoc = new StringBuilder();
            var toc   = new List<(int lvl, string txt, string id)>();

            foreach (var path in arranged)
            {
                // (should never be null if input count > 0)
                string filePath = path!;
                string fileName = Path.GetFileName(filePath);
                string bigId    = Slug(fileName);

                sbDoc
                  .AppendLine()
                  .AppendLine("---")
                  .AppendLine($"# {fileName} <a id=\"{bigId}\"></a>")
                  .AppendLine("---")
                  .AppendLine();

                toc.Add((1, fileName, bigId));

                string content = File.ReadAllText(filePath);
                content = Hx.Replace(content, m =>
                {
                    int lvl = m.Groups[1].Value.Length + 1;
                    string txt = m.Groups[2].Value.Trim();
                    string id = Slug($"{fileName}-{txt}");
                    return $"{m.Groups[1].Value} {txt} <a id=\"{id}\"></a>";
                });

                sbDoc.AppendLine(content).AppendLine();
            }

            // Generate TOC
            var sbToc = new StringBuilder("# Table of Contents\n");
            foreach (var (lvl, txt, id) in toc)
            {
                sbToc
                  .Append(' ', (lvl - 1) * 2)
                  .Append($"- [{txt}](#{id})")
                  .AppendLine();
            }

            // Write out UTF-8 without BOM
            File.WriteAllText(
                outputPath,
                sbToc
                  .AppendLine()
                  .Append(sbDoc)
                  .ToString(),
                new UTF8Encoding(false));
        }

        private static string Slug(string text)
        {
            text = text.Trim().ToLowerInvariant();
            text = Regex.Replace(text, @"[^\w\s-]", string.Empty);
            return Regex.Replace(text, @"\s+", "-");
        }
    }
}
```

**Why this works:**
- The **largest file** goes into the **middle** of the full range.  
- The **second-largest** splits the largest remaining gap (one of the ends), pushing it away from the first.  
- Each subsequent file always bisects the largest open interval, so huge files cannot “pile up” at one end.  

Resulting output will have your 30 MB and 3 MB files interspersed among the small ones, keeping each file intact and balancing overall document size.

## USER
its like doing this, 2 megs, 2 megs 2 megs then 30 megs like its stuffing all that is left in the last file.

## Thoughts
It seems like the user is unhappy with the file distribution, particularly how smaller files get stuck at the end while large files are prioritized in the middle. They’re describing it as filling smaller files first and then dumping the larger file into the last spot. It sounds like the previous solution, which used a heap to handle gaps, wasn’t fully implemented, which could be why the files aren't getting placed properly. Maybe breaking the sorting and TOC insertion into separate steps might help fix the issue.
It looks like the user is unhappy because the files are still being grouped in an undesirable way, with smaller files filling up the start of the list and the larger files being shoved to the end. It seems like the mid-point calculation in the gap algorithm could be the issue. If the midIndex is being calculated as `(start+end)/2`, it's possible that the approach isn't making the best decisions about file placement. I’ll need to consider how the sorting and insertion work together to fix this problem.

## USER
stop. the output, when it's split into parts.  say i do 4 parts i get 3 parts 2 - 3 megs then the last file will be like 30megs.  do you see?

## Thoughts
It seems like the user is working with code that splits a merged output file into multiple parts. They mention that when splitting into four parts, three parts are around 2-3 MB, but the last part is much larger at 30 MB. This suggests the current partitioning method isn't distributing the content evenly. The user likely wants to adjust the code to ensure the output is split more evenly across all files, not just the last one.
The user wants to split files into four parts while maintaining balanced sizes, but the current method is creating one much larger file. This likely happens because the split is happening consecutively based on the size of the files. I propose using a "greedy number partitioning" algorithm: after sorting the files in descending order, files would be assigned sequentially to the partition with the smallest current total. This method would ensure more balanced parts overall. I'd also suggest modifying the merging function to accept a parameter for the number of parts.

## ASSISTANT
You’re right—simply slicing the list into N equal‐count chunks will still dump the one truly large file into the last bucket.  What you need is to **partition by total bytes**, not by number of files.  A classic greedy “multi-way number partitioning” will distribute file sizes so that each of your 4 parts ends up with roughly the same total.

Here’s a sketch of how you can do it:

```csharp
/// <summary>
/// Merge the sourceFiles into <paramref name="partCount"/> separate outputs,
/// balancing by total file‐size so that no one part ends up with the giant file.
/// </summary>
public void MergeIntoParts(
    IEnumerable<string> sourceFiles,
    string outputBasePath,
    int partCount,
    Action? progress = null)
{
    // 1) Read sizes and sort descending
    var fileMeta = sourceFiles
        .Select(path => new { Path = path, Size = new FileInfo(path).Length })
        .OrderByDescending(f => f.Size)
        .ToList();

    // 2) Prepare empty partitions & size trackers
    var partitions = Enumerable
        .Range(0, partCount)
        .Select(_ => new List<string>())
        .ToArray();
    var sums = new long[partCount];

    // 3) Greedily assign each file to the partition with the smallest current sum
    foreach (var file in fileMeta)
    {
        // find index of partition with minimal total size
        int idx = Array.IndexOf(sums, sums.Min());
        partitions[idx].Add(file.Path);
        sums[idx] += file.Size;
    }

    // 4) Now merge each partition separately
    for (int i = 0; i < partCount; i++)
    {
        string outPath = $"{outputBasePath}.part{i+1}.md";
        MergeInternal(partitions[i], outPath, progress);
    }
}
```

**Explanation of the steps**  
1. **Sort descending**: by placing the largest files first, the greedy step has more “degrees of freedom” to spread them out.  
2. **Greedy assignment**: each time you pick the next‐largest file and put it into whichever of the 4 bins is currently smallest.  This tends to equalize total MB per bin.  
3. **Separate merges**: you then call your existing `MergeInternal` on each bin, producing `…part1.md`, `…part2.md`, etc.

With this in place, even if you have one 30 MB file and a bunch of 2 MB files, the 30 MB file will go into the emptiest partition at that moment—and the other partitions will absorb enough of the smaller files to keep all four outputs within a few MB of each other.

## USER
using System;

using System.Collections.Generic;

using System.IO;

using System.Linq;

using System.Text;

using System.Text.RegularExpressions;



namespace MarkdownMergeTool

{

    /// <summary>

    /// Stand-alone utility for merging multiple Markdown files into one,

    /// automatically injecting anchors and generating a Table of Contents.

    /// </summary>

    public sealed class MarkdownMerger

    {

        // Matches Markdown headings (levels 1–6)

        private static readonly Regex Hx =

            new(@"^(#{1,6})\s+(.+)$", RegexOptions.Multiline);



        /// <summary>

        /// Public entry point: merges <paramref name="sourceFiles"/> into <paramref name="outputPath"/>.

        /// </summary>

        public void Merge(IEnumerable<string> sourceFiles, string outputPath)

        {

            MergeInternal(sourceFiles, outputPath, null);

        }



        /// <summary>

        /// Core merge logic; allows injection of a progress callback.

        /// </summary>

        internal void MergeInternal(

     IEnumerable<string> files,

     string outputPath,

     Action? progress = null)

        {

            var fileList = files.ToList();



            // Build list with file size metadata

            var fileMeta = fileList

                .Select(f => new { Path = f, Size = new FileInfo(f).Length })

                .ToList();



            // Sort smallest to largest

            var ascending = fileMeta.OrderBy(f => f.Size).ToList();



            // Sort largest to smallest

            var descending = fileMeta.OrderByDescending(f => f.Size).ToList();



            // Interleave smallest and largest

            var finalOrder = new List<string>();

            int i = 0, j = 0;

            bool pickSmall = true;

            while (i < ascending.Count || j < descending.Count)

            {

                if (pickSmall && i < ascending.Count)

                    finalOrder.Add(ascending[i++].Path);

                else if (j < descending.Count)

                    finalOrder.Add(descending[j++].Path);

                pickSmall = !pickSmall;

            }



            // Remove possible duplicates (when odd number of files)

            finalOrder = finalOrder.Distinct().ToList();



            var sbDoc = new StringBuilder();

            var toc = new List<(int lvl, string txt, string id)>();



            foreach (var path in finalOrder)

            {

                string fileName = Path.GetFileName(path);

                string bigId = Slug(fileName);



                // File delimiter and top-level heading

                sbDoc

                    .AppendLine()

                    .AppendLine("---")

                    .AppendLine($"# {fileName} <a id=\"{bigId}\"></a>")

                    .AppendLine("---")

                    .AppendLine();



                toc.Add((1, fileName, bigId));



                string content = File.ReadAllText(path);

                content = Hx.Replace(content, m =>

                {

                    int lvl = m.Groups[1].Value.Length + 1;

                    string txt = m.Groups[2].Value.Trim();

                    string id = Slug($"{fileName}-{txt}");

                    return $"{m.Groups[1].Value} {txt} <a id=\"{id}\"></a>";

                });



                sbDoc.AppendLine(content).AppendLine();

                progress?.Invoke();

            }



            // Build Table of Contents

            var sbToc = new StringBuilder("# Table of Contents\n");

            foreach (var (lvl, txt, id) in toc)

            {

                sbToc

                    .Append(' ', (lvl - 1) * 2)

                    .Append($"- [{txt}](#{id})")

                    .AppendLine();

            }



            File.WriteAllText(

                outputPath,

                sbToc

                    .AppendLine()

                    .Append(sbDoc)

                    .ToString(),

                new UTF8Encoding(false));

        }





        /// <summary>

        /// Produces a URL-friendly slug from arbitrary text.

        /// </summary>

        private static string Slug(string text)

        {

            text = text.Trim().ToLowerInvariant();

            // Remove invalid characters

            text = Regex.Replace(text, @"[^\w\s-]", string.Empty);

            // Replace whitespace with hyphens

            return Regex.Replace(text, @"\s+", "-");

        }

    }

}


## Thoughts
The user wants to modify the `MergeInternal` function to divide files into multiple parts by total size. They mentioned needing an algorithm to partition files across parts (e.g., 4 parts, with the last being significantly larger). Since their provided code focuses on merging, I'll suggest adding a new method to the `MarkdownMerger`, such as `MergeInParts(N)`, to handle part splitting based on total size. Alternatively, we could modify `Merge` to accept a `partCount` argument, allowing for overload.

## ASSISTANT
Below is an extension to your `MarkdownMerger` that introduces a new entry point, `MergePartitioned`, which will split your input files into **N** balanced groups by total byte size—and then perform a `MergeInternal` on each group.  This uses a classic greedy “multi-way number partitioning”:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace MarkdownMergeTool
{
    /// <summary>
    /// Stand-alone utility for merging multiple Markdown files into one,
    /// automatically injecting anchors and generating a Table of Contents.
    /// Also supports splitting into balanced parts by total size.
    /// </summary>
    public sealed class MarkdownMerger
    {
        // Matches Markdown headings (levels 1–6)
        private static readonly Regex Hx =
            new(@"^(#{1,6})\s+(.+)$", RegexOptions.Multiline);

        /// <summary>
        /// Public entry point: merges <paramref name="sourceFiles"/> into <paramref name="outputPath"/>.
        /// </summary>
        public void Merge(IEnumerable<string> sourceFiles, string outputPath)
            => MergeInternal(sourceFiles, outputPath, null);

        /// <summary>
        /// Splits <paramref name="sourceFiles"/> into <paramref name="partCount"/> balanced groups by total bytes,
        /// then merges each group into: {outputBasePath}.part1.md, {outputBasePath}.part2.md, ….
        /// </summary>
        public void MergePartitioned(
            IEnumerable<string> sourceFiles,
            string outputBasePath,
            int partCount,
            Action? progress = null)
        {
            if (partCount < 1)
                throw new ArgumentOutOfRangeException(nameof(partCount), "Must be ≥ 1");

            // 1) Collect and sort descending by size
            var fileMeta = sourceFiles
                .Select(path => new { Path = path, Size = new FileInfo(path).Length })
                .OrderByDescending(f => f.Size)
                .ToList();

            // 2) Prepare bins
            var partitions = new List<string>[partCount];
            var sums       = new long[partCount];
            for (int i = 0; i < partCount; i++)
                partitions[i] = new List<string>();

            // 3) Greedy assignment: each file to the bin with minimal current sum
            foreach (var file in fileMeta)
            {
                int targetIdx = 0;
                long minSum   = sums[0];
                for (int i = 1; i < partCount; i++)
                {
                    if (sums[i] < minSum)
                    {
                        minSum   = sums[i];
                        targetIdx = i;
                    }
                }

                partitions[targetIdx].Add(file.Path);
                sums[targetIdx] += file.Size;
            }

            // 4) Merge each partition
            for (int i = 0; i < partCount; i++)
            {
                string partPath = $"{outputBasePath}.part{i + 1}.md";
                MergeInternal(partitions[i], partPath, progress);
            }
        }

        /// <summary>
        /// Core merge logic; allows injection of a progress callback.
        /// </summary>
        internal void MergeInternal(
            IEnumerable<string> files,
            string outputPath,
            Action? progress = null)
        {
            var fileList = files.ToList();
            var sbDoc    = new StringBuilder();
            var toc      = new List<(int lvl, string txt, string id)>();

            foreach (var path in fileList)
            {
                string fileName = Path.GetFileName(path);
                string bigId    = Slug(fileName);

                sbDoc
                  .AppendLine()
                  .AppendLine("---")
                  .AppendLine($"# {fileName} <a id=\"{bigId}\"></a>")
                  .AppendLine("---")
                  .AppendLine();

                toc.Add((1, fileName, bigId));

                string content = File.ReadAllText(path, Encoding.UTF8);
                content = Hx.Replace(content, m =>
                {
                    int    lvl = m.Groups[1].Value.Length + 1;
                    string txt = m.Groups[2].Value.Trim();
                    string id  = Slug($"{fileName}-{txt}");
                    return $"{m.Groups[1].Value} {txt} <a id=\"{id}\"></a>";
                });

                sbDoc.AppendLine(content).AppendLine();
                progress?.Invoke();
            }

            // Build Table of Contents
            var sbToc = new StringBuilder("# Table of Contents\n");
            foreach (var (lvl, txt, id) in toc)
            {
                sbToc
                  .Append(' ', (lvl - 1) * 2)
                  .Append($"- [{txt}](#{id})")
                  .AppendLine();
            }

            // Write output with UTF-8 (no BOM)
            File.WriteAllText(
                outputPath,
                sbToc
                  .AppendLine()
                  .Append(sbDoc)
                  .ToString(),
                new UTF8Encoding(false));
        }

        /// <summary>
        /// Produces a URL-friendly slug from arbitrary text.
        /// </summary>
        private static string Slug(string text)
        {
            text = text.Trim().ToLowerInvariant();
            // Remove invalid characters
            text = Regex.Replace(text, @"[^\w\s-]", string.Empty);
            // Replace whitespace with hyphens
            return Regex.Replace(text, @"\s+", "-");
        }
    }
}
```

**How it solves your issue**  
- You requested **4 parts** (for example).  
- The 30 MB file will be assigned first to the emptiest partition (all are empty), then each 2 MB file goes into whichever partition currently has the smallest total.  
- This greedy distribution almost always keeps each part within a few MB of each other.  
- Finally, each partition is merged intact—no file splitting—so you’ll end up with, e.g., parts like 18 MB, 15 MB, 16 MB, 17 MB instead of “tiny, tiny, tiny, huge.”

## USER
all good. i had a rogue file filled iwth junk

## Thoughts
Got it! Since the issue was caused by a rogue file filled with junk, I would suggest implementing file validation that

## ASSISTANT
I’m glad you tracked it down. In production scenarios it’s prudent to validate each input file before merging, for example:

1. **Size thresholding**  
   ```csharp
   // Skip any file whose size exceeds, say, 10 MB
   const long MaxAllowedBytes = 10 * 1024 * 1024;
   var validFiles = sourceFiles
       .Where(f => new FileInfo(f).Length <= MaxAllowedBytes);
   ```

2. **Content sanity checks**  
   Ensure it looks like Markdown and not binary/junk:
   ```csharp
   bool IsLikelyMarkdown(string path)
   {
       var sample = File.ReadAllText(path, Encoding.UTF8)
                        .Take(512)
                        .ToArray();
       // e.g. require at least one “# ” or “- ” in first 512 chars
       return sample.Contains('#') || sample.Contains('-');
   }

   var filtered = sourceFiles
       .Where(f => IsLikelyMarkdown(f));
   ```

3. **Combine both filters** before passing into your merger:
   ```csharp
   var inputs = sourceFiles
       .Where(f => new FileInfo(f).Length <= MaxAllowedBytes)
       .Where(f => IsLikelyMarkdown(f));

   merger.Merge(inputs, outputPath);
   ```

By rejecting anomalously large or non-Markdown files up-front, you avoid “rogue” inputs skewing your merge sizes.


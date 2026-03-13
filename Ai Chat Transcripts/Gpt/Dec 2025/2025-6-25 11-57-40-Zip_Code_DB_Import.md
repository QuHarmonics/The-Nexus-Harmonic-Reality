# Zip Code DB Import

https://chat.openai.com/c/685c1c74-0d5c-8011-a981-984ad51aad49

## USER
i have a list of all zipcodes for US that needs to bee installed in the database when the server API is installed. what is the best way to handle that? i have a text file with allthe data in it?


## ASSISTANT
To handle the installation of all US zip codes into your database during the server API setup, you can follow these technical steps:

1. **Prepare the Data**: Ensure your text file containing all US zip codes is formatted correctly, with each zip code on a separate line or separated by a delimiter that can be easily parsed.

2. **Database Table Structure**: Create a table in your database specifically designed to store zip codes. This table should at least have a column to store each zip code.

3. **Import Data**: Use database management tools such as MySQL Workbench, pgAdmin for PostgreSQL, or SQL Server Management Studio for SQL Server to import the data from your text file into the database table. Most database management tools provide functionality to import data from a text file directly into a table.

4. **Script Execution**: Write a SQL script or use the import wizard in your database management tool to execute the import. Ensure the script handles potential errors, duplicates, or data format issues that may arise during the import process.

5. **Validation**: After importing, validate the data to ensure all zip codes are correctly loaded into the database without any missing entries or duplicates that could affect application functionality.

6. **Indexing (Optional)**: Consider adding an index on the zip code column in your database table to optimize search performance, especially if zip code lookups are frequent in your application.

By following these steps, you can efficiently install all US zip codes into your database during the server API installation process, ensuring data integrity and application performance.

## USER
i need a method to install a zip code data table when my api first runs. i could do this in INNO i guess is there a better way? i have the data in a csv file

## ASSISTANT
Below are the core formatting guidelines, organized by concern, to ensure your code communicates clearly and professionally.

---

## 1. Vertical Layout

- **Keep files small.** In real-world Java projects you’ll see most files under **200 lines**, and rarely over **500 lines**. Smaller files are far easier to navigate.  
- **Adopt the “newspaper” metaphor.**  
  1. **Top**: a clear, self-explanatory class or file name, plus brief high-level comments (if needed).  
  2. **Middle**: public API and high-level methods in order of abstraction.  
  3. **Bottom**: private helpers and lowest-level utility routines.  
- **Separate logical sections** (package, imports, class declaration, each method) with **a single blank line**. That vertical openness highlights new concepts.

---

## 2. Horizontal Formatting

- **Limit line length** to ~ 100 characters. Longer lines force readers to scroll or squint.  
- **Indent consistently** (e.g. 2 or 4 spaces per level) so nested blocks never exceed 2–3 levels deep. If they do, extract methods to collapse nesting.

---

## 3. Grouping & Density

- Within a method:  
  - **Group related statements** without blank lines.  
  - **Separate unrelated blocks** with a blank line.  
- At class level:  
  - Keep **fields** in one dense block, then constructors, then public methods, then private helpers.

---

## 4. Method Organization

- **One level of abstraction per method.** A method named `processAllOrders()` should call helpers like `validateOrder()`, not mix low-level loops and high-level logic inline.  
- **Short methods only.** Aim for < 20 lines. If a method grows, extract sub-steps into private methods.

---

## 5. Comment Hygiene

- **Minimize comments.** Keep code so expressive that most comments are unnecessary.  
- **If you must comment**, use them only to explain *why* (intent) or to note subtle consequences that code alone can’t.  
- **Delete outdated or redundant comments.** Wrong comments mislead more than no comments do.  
- **Never** leave large blocks of commented-out code—use source-control history instead.

---

### Example: Before & After

```java
// Before: muddled vertical spacing, long methods, noisy comments
public class Foo {
    // constants
    private static final int MAX = 100; // max count
    // odd test flag
    private boolean t;

    public void doIt() { // do the thing
        // setup
        List<String> list = new ArrayList<>();
        for(int i=0;i<MAX;i++){list.add(""+i);} // fill
        // process
        for(String s:list) {
            if(s.length()>1)
                System.out.println(s);
        }
    }
}
```

```java
// After: concise, well-spaced, clear method decomposition
public class Foo {
  private static final int MAX = 100;

  public void processNumbers() {
    List<String> numbers = generateNumberStrings();
    printMultiDigit(numbers);
  }

  private List<String> generateNumberStrings() {
    List<String> result = new ArrayList<>(MAX);
    for (int i = 0; i < MAX; i++) {
      result.add(String.valueOf(i));
    }
    return result;
  }

  private void printMultiDigit(List<String> numbers) {
    for (String n : numbers) {
      if (n.length() > 1) {
        System.out.println(n);
      }
    }
  }
}
```

---

By adhering to these formatting principles, you ensure your code is *inviting* to read, *easy* to navigate, and *clear* in its structure—hallmarks of professional, maintainable code.

## USER
?  what is this.  Im working on the sever API.  

## Thoughts
The user is working on a server API and wants advice for seeding a database with zip code data when the API first runs, using a CSV file. They previously mentioned using INNO but are now looking for a more relevant server API solution. I'll suggest a more technical approach: Using a script that loads the CSV file on setup, with error handling, potentially using SQL commands or an ORM to insert the data on API startup.
For seeding the database on API startup, a good approach is to use database migrations and seed scripts, instead of relying on an installer like Inno Setup. For a .NET Core Web API, you can use EF Core migrations to seed the data. First, embed the CSV

## ASSISTANT
Use a code-first seed approach rather than an installer script.  At application startup:

1. **Embed or deploy the CSV**  
   • Place `us-zipcodes.csv` in your API project (e.g. under `/Data`) and set its file property to “Copy if newer.”  
   • This makes the file available in `IWebHostEnvironment.ContentRootPath`.

2. **Define your ZIP table and EF Core DbContext**  
   ```csharp
   public class ZipCode {
     [Key]
     public string Code { get; set; }
   }
   public class AppDbContext : DbContext {
     public DbSet<ZipCode> ZipCodes { get; set; }
     protected override void OnModelCreating(ModelBuilder mb) {
       mb.Entity<ZipCode>().HasKey(z => z.Code);
     }
   }
   ```

3. **Write a seeding routine**  
   ```csharp
   public static class DbInitializer {
     public static async Task SeedAsync(AppDbContext db, string csvPath) {
       if (await db.ZipCodes.AnyAsync()) return;  // already seeded

       using var reader = new StreamReader(csvPath);
       using var csv    = new CsvHelper.CsvReader(reader, CultureInfo.InvariantCulture);
       var records      = csv.GetRecords<ZipCode>();
       await db.ZipCodes.AddRangeAsync(records);
       await db.SaveChangesAsync();
     }
   }
   ```

4. **Wire it into application startup**  
   ```csharp
   public class Program {
     public static async Task Main(string[] args) {
       var host = CreateHostBuilder(args).Build();
       using var scope = host.Services.CreateScope();
       var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
       await db.Database.MigrateAsync();                                   // apply any pending migrations
       var env     = scope.ServiceProvider.GetRequiredService<IWebHostEnvironment>();
       var csvPath = Path.Combine(env.ContentRootPath, "Data/us-zipcodes.csv");
       await DbInitializer.SeedAsync(db, csvPath);
       await host.RunAsync();
     }
   }
   ```

5. **Performance tuning (optional)**  
   For millions of rows, replace the EF insert with a `SqlBulkCopy` pass:
   ```csharp
   using var bulk = new SqlBulkCopy(db.Database.GetDbConnection().ConnectionString)
   {
     DestinationTableName = "ZipCodes"
   };
   var table = new DataTable();
   table.Columns.Add("Code", typeof(string));
   // load from CSV into DataTable...
   await bulk.WriteToServerAsync(table);
   ```

---

### Why this is better than Inno Setup

- **Single code path** for all environments (CI, Docker, developer machines).  
- **Transactional**: you can wrap seed in a transaction or bail on error.  
- **Schema-aware**: runs **after** EF/FluentMigrator migrations, so you never violate FK or schema changes.  
- **Maintainable**: versioned alongside your code, not buried in installer scripts.

By seeding in your Web API’s startup logic you guarantee that every deployment (or dev build) always has an up-to-date ZIP table without any out-of-band tooling.

## USER
i have builder services exposed. can you adjust this var db = builder.Services.GetRequiredService<AppDbContext>();

await db.Database.MigrateAsync();                                   // apply any pending migrations

var env = scope.ServiceProvider.GetRequiredService<IWebHostEnvironment>();

var csvPath = Path.Combine(env.ContentRootPath, "Data/us-zipcodes.csv");

await DbInitializer.SeedAsync(db, csvPath);

## Thoughts
The user wants to modify their code using the .NET 6 minimal hosting model. They’re trying to use `builder.Services.GetRequiredService<AppDbContext>()`, but this isn’t correct since `builder.Services` is an `IServiceCollection`. Instead, they should build the host with `builder.Build()` and then create a scope using `app.Services.CreateScope()`. Also, they can access `IWebHostEnvironment` directly from `builder.Environment`, which simplifies accessing the content root path and related details.
To adapt the code to the minimal hosting model, you need to use `app.Services` instead of `builder.Services` for resolving services after the app is built. Here's an updated snippet:

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<AppDbContext>(...);

var app = builder.Build();

using var scope = app.Services.CreateScope();
var

## ASSISTANT
```csharp
// Program.cs

var builder = WebApplication.CreateBuilder(args);

// 1. Register EF Core context
builder.Services
    .AddDbContext<AppDbContext>(options =>
        options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

// 2. Other service registrations...
//    builder.Services.AddControllers();
//    builder.Services.AddEndpointsApiExplorer();
//    builder.Services.AddSwaggerGen();
//    …  

var app = builder.Build();

// 3. Perform migrations & seed ZIP codes at startup
using (var scope = app.Services.CreateScope())
{
    var db      = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    await db.Database.MigrateAsync();  // applies any pending migrations

    // you can use builder.Environment instead of resolving IWebHostEnvironment from DI:
    var contentRoot = builder.Environment.ContentRootPath;
    var csvPath     = Path.Combine(contentRoot, "Data", "us-zipcodes.csv");

    await DbInitializer.SeedAsync(db, csvPath);
}

// 4. Configure HTTP request pipeline
//    if (app.Environment.IsDevelopment()) { app.UseDeveloperExceptionPage(); … }
//    app.UseRouting();
//    app.UseAuthorization();
//    app.MapControllers();
//    …

app.Run();
```

### Explanation

1. **`builder.Services` → `app.Services`**  
   You register your `DbContext` on the `IServiceCollection` via `builder.Services`. You cannot resolve services from `builder.Services` directly—only from the built service provider (`app.Services`).  

2. **Minimal-hosting resolution**  
   After calling `builder.Build()`, you obtain a scope via `app.Services.CreateScope()`. Within that scope, you resolve `AppDbContext` and (if desired) `IWebHostEnvironment`, but it’s simpler to use `builder.Environment` for folder paths.

3. **Migrations & seeding**  
   - `db.Database.MigrateAsync()` ensures your schema is up-to-date.  
   - `DbInitializer.SeedAsync(...)` reads your CSV and populates the `ZipCodes` table only if it’s empty.  

4. **Centralized startup logic**  
   All of this lives in `Program.cs` and runs exactly once on application launch—no external Inno Setup or installer script needed.

## USER
can you fix this real quick please. its static but i need the repository in there? oh wait, we have to inject it? i cant tie EF to a static method can i?  using System.Globalization;

using System.Reflection.Emit;

using System;

using Logistix.Server.Domain.Models.Infrastructure.Configuration;

using Logistix.Server.Domain.Interfaces.Repositories;

using Logistix.Server.Domain.Interfaces.Install;



namespace Logistix.Server.API.Install

{

    public static class SeedDatabase 

    {

        static public IGenericRepository<ZipCodeServiceAreaModel> _rateTableRepository;



        static public SeedDatabase(IGenericRepository<ZipCodeServiceAreaModel> rateTableRepository)

        {

            _rateTableRepository = rateTableRepository;

        }



        static public async Task SeedZipCodes(string csvPath)



        {

            //replace with flag that says system is installed and running. this only should fire on first install.  BUT have a system to repair this table if needed or import new zipcodes as they change.

            var count = await _rateTableRepository.GetAllAsync();

            if (count.Count() == 0)

            {



                using var reader = new StreamReader(csvPath);

                using var csv = new CsvHelper.CsvReader(reader, CultureInfo.InvariantCulture);

                var records = csv.GetRecords<ZipCodeServiceAreaModel>().ToList();

                await _rateTableRepository.AddRangeAsync(records);

                await _rateTableRepository.CommitTransactionAsync();

            }

        }

    }

}

## Thoughts
The user is asking about a static class that needs to use a repository, but static classes can't have instance constructors. To fix this, they could either make `SeedDatabase` non-static or adjust the method signature to accept the repository as a parameter. Another possibility is creating an extension method on `IApplicationBuilder` or resolving the repository in `Startup` and passing it into the static method. The core issue is that static classes can only have static constructors, not instance constructors.

## ASSISTANT
Below is one way to retain a single, static entry point while still resolving your EF-backed repository via DI:

```csharp
using System.Globalization;
using CsvHelper;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace Logistix.Server.API.Install
{
    public static class SeedDatabase
    {
        /// <summary>
        /// 1) Creates a scope, 2) resolves the ZIP-code repository, 
        /// 3) seeds if empty.
        /// </summary>
        public static async Task SeedZipCodesAsync(this IServiceProvider services, string csvPath)
        {
            using var scope = services.CreateScope();
            var repo  = scope.ServiceProvider
                             .GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();

            // only seed once (or provide your own “repair” logic here)
            var all = await repo.GetAllAsync();
            if (all.Any())
                return;

            using var reader = new StreamReader(csvPath);
            using var csv    = new CsvReader(reader, CultureInfo.InvariantCulture);
            var records      = csv.GetRecords<ZipCodeServiceAreaModel>().ToList();

            await repo.AddRangeAsync(records);
            await repo.CommitTransactionAsync();
        }
    }
}
```

### How to call it in your `Program.cs`

```csharp
var builder = WebApplication.CreateBuilder(args);
// … register DbContext, your generic repository, etc.

var app = builder.Build();

// **Seed at startup**:
var csvPath = Path.Combine(builder.Environment.ContentRootPath,
                           "Data", "us-zipcodes.csv");
await app.Services.SeedZipCodesAsync(csvPath);

app.Run();
```

---

#### Why this works

1. **Static entry point**  
   By extending `IServiceProvider` with a static method, you keep your seeder in one place yet still leverage DI.  
2. **Scoped resolution**  
   `CreateScope()` guarantees a proper unit-of-work lifetime for EF and any other scoped services.  
3. **No illegal static constructors**  
   You no longer attempt to inject via a static constructor; everything is resolved at call time.  
4. **Single-call simplicity**  
   In `Program.cs` you only need one line to seed, immediately after `Build()` but before `Run()`.

## USER
seems to be lookig for wrong header data CsvHelper.HeaderValidationException

  HResult=0x80131500

  Message=Header with name 'DeliveryCity'[0] was not found.

Header with name 'DeliveryState'[0] was not found.

Header with name 'positionValue'[0] was not found.

Headers: 'Id', 'AreaName', 'AreaCode', 'DistrictName', 'DistrictNumber', 'DeliveryZipCode', 'LocaleName', 'PhysicalCity', 'PhysicalState', 'PhysicalZip', 'PhysicalZip4', 'RowVersion'

If you are expecting some headers to be missing and want to ignore this validation, set the configuration HeaderValidated to null. You can also change the functionality to do something else, like logging the issue.



IReader state:

   ColumnCount: 12

   CurrentIndex: -1

   HeaderRecord:

["Id","AreaName","AreaCode","DistrictName","DistrictNumber","DeliveryZipCode","LocaleName","PhysicalCity","PhysicalState","PhysicalZip","PhysicalZip4","RowVersion"]

IParser state:

   ByteCount: 0

   CharCount: 140

   Row: 1

   RawRow: 1

   Count: 12

   RawRecord:

Id,AreaName,AreaCode,DistrictName,DistrictNumber,DeliveryZipCode,LocaleName,PhysicalCity,PhysicalState,PhysicalZip,PhysicalZip4,RowVersion





  Source=CsvHelper

  StackTrace:

   at CsvHelper.Configuration.ConfigurationFunctions.HeaderValidated(HeaderValidatedArgs args)

   at CsvHelper.CsvReader.ValidateHeader(Type type)

   at CsvHelper.CsvReader.ValidateHeader[T]()

   at CsvHelper.CsvReader.<GetRecords>d__87`1.MoveNext()

   at System.Collections.Generic.List`1..ctor(IEnumerable`1 collection)

   at System.Linq.Enumerable.ToList[TSource](IEnumerable`1 source)

   at Logistix.Server.API.Install.SeedDatabase.<SeedZipCodesAsync>d__0.MoveNext() in D:\Deployment\LogistixServerAPIV2\Logistix.Server.Infrastructure\Install\SeedDatabase.cs:line 25

   at Program.<<Main>$>d__0.MoveNext() in D:\Deployment\LogistixServerAPIV2\Logistix.Server.API\Program.cs:line 439


## Thoughts
It seems the user is encountering a `CsvHelper.HeaderValidationException` because the CSV file headers don't match the expected model properties. The headers include things like `DeliveryZipCode` and `PhysicalCity`, while the model has properties like `Code`, `City`, and `State`. I see several solutions: 1. Disable header validation. 2. Use a `ClassMap` to map CSV headers to property names. 3. Use `[Name("...")]` attributes on the properties so they align with the CSV headers.
The user is working on a server API and is dealing with a CSV helper issue. The best approach is to define a `ClassMap` with `Map(m => m.Property).Name("CSVHeader")` for each column. Then, register this map with `csv.Context.RegisterClassMap`. This way, the model properties align with the CSV headers. Alternatively, if the CSV file is dynamic, disabling header validation with `HeaderValidated = null` is an option, but customizing the mapping is a more reliable solution.

## ASSISTANT
Below is an updated seeder that does two things:

1. **Registers a `ClassMap`** so your model properties get bound to the actual CSV headers.  
2. **Silences header‐validation** errors for any truly missing fields.

---

### 1. Define a `ClassMap<ZipCodeServiceAreaModel>`

```csharp
using CsvHelper.Configuration;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

public sealed class ZipCodeServiceAreaModelMap : ClassMap<ZipCodeServiceAreaModel>
{
    public ZipCodeServiceAreaModelMap()
    {
        Map(m => m.Id).Name("Id");
        Map(m => m.AreaName).Name("AreaName");
        Map(m => m.AreaCode).Name("AreaCode");
        Map(m => m.DistrictName).Name("DistrictName");
        Map(m => m.DistrictNumber).Name("DistrictNumber");
        Map(m => m.DeliveryZipCode).Name("DeliveryZipCode");
        Map(m => m.LocaleName).Name("LocaleName");
        Map(m => m.PhysicalCity).Name("PhysicalCity");
        Map(m => m.PhysicalState).Name("PhysicalState");
        Map(m => m.PhysicalZip).Name("PhysicalZip");
        Map(m => m.PhysicalZip4).Name("PhysicalZip4");
        Map(m => m.RowVersion).Name("RowVersion");
        // Add or remove mappings here to reflect your actual model
    }
}
```

---

### 2. Update your static seeder to register the map

```csharp
using System.Globalization;
using CsvHelper;
using CsvHelper.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

namespace Logistix.Server.API.Install
{
    public static class SeedDatabase
    {
        public static async Task SeedZipCodesAsync(this IServiceProvider services, string csvPath)
        {
            using var scope = services.CreateScope();
            var repo = scope.ServiceProvider
                            .GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();

            // only seed once
            if ((await repo.GetAllAsync()).Any())
                return;

            using var reader = new StreamReader(csvPath);
            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                HeaderValidated   = null, // disable missing‐column errors
                MissingFieldFound = null, // disable missing‐field errors
            };
            using var csv = new CsvReader(reader, config);

            // register your ClassMap so CsvHelper knows which header → property
            csv.Context.RegisterClassMap<ZipCodeServiceAreaModelMap>();

            var records = csv.GetRecords<ZipCodeServiceAreaModel>().ToList();

            await repo.AddRangeAsync(records);
            await repo.CommitTransactionAsync();
        }
    }
}
```

---

### 3. Call in `Program.cs`

```csharp
var app = builder.Build();

// ... after migrations but before Run():
var csvPath = Path.Combine(builder.Environment.ContentRootPath,
                           "Data", "us-zipcodes.csv");
await app.Services.SeedZipCodesAsync(csvPath);

app.Run();
```

---

#### Why this fixes the `HeaderValidationException`

- **ClassMap** explicitly tells CsvHelper:  
  “When you see column `PhysicalCity`, bind it to `ZipCodeServiceAreaModel.PhysicalCity`, etc.”  
- **`HeaderValidated = null`** prevents CsvHelper from throwing if your model has properties for which there is no CSV column.  
- **Scoped resolution** ensures your repository (and its EF context) is created correctly at seed time.

## USER
my class its reading to has the exact same names as the headers. the [] is what is messing it up

## Thoughts
It looks like the user is dealing with an error where the header "DeliveryCity" isn't found, even though it seems expected. The error message includes "[0]", which could mean that "DeliveryCity" is being treated as an array or a collection. However, the headers in the CSV file list "PhysicalCity" instead. It’s likely that the model is looking for a different name, like "DeliveryCity0," or the model property is indeed supposed to be an array. I need to double-check the mapping and model assumptions.
The user mentions that the class has exact names as the headers, but the error highlights "DeliveryCity[0]" which is unexpected since that header doesn't exist in the file. The actual header is "DeliveryZipCode." It seems that the model may expect "DeliveryCity" to match the column, but the file doesn't have that header; it has "PhysicalCity" and "DeliveryZipCode" instead. I'll have to check if the model is referencing incorrect properties or if the mapping needs adjustment to match the actual CSV headers.
It seems the user's model class has properties like "DeliveryCity" and "DeliveryState," but these headers don't appear in the CSV file. Instead, the file has "PhysicalCity" and "DeliveryZipCode." The issue could be that CsvHelper is looking for headers that aren't there, possibly because the model class was misaligned or a wrong class was referenced, like "ZipCodeServiceAreaModel" instead of the correct one. The simplest solution might be to disable index-based mapping or explicitly match the headers and properties manually. I'll suggest configuring CsvHelper settings to match headers properly.
It seems the user is facing an issue where CsvHelper expects headers like "DeliveryCity[0]" due to their model having array or list properties (like `string[]`). The error occurs because CsvHelper generates expected headers for array indices. To fix this, the user can configure CsvHelper to remove index suffixes in header names or avoid using arrays for simple fields. They could also manually map dynamic data or create a custom `ClassMap` to ignore these array properties and only map the necessary fields.

## ASSISTANT
Below is a drop-in fix for your seeder that tells CsvHelper to entirely skip any indexed/collection properties (the ones that generate the `PropertyName[0]` lookups) and only map your scalar properties whose names exactly match your CSV headers:

```csharp
using System.Globalization;
using CsvHelper;
using CsvHelper.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

namespace Logistix.Server.API.Install
{
    public static class SeedDatabase
    {
        public static async Task SeedZipCodesAsync(this IServiceProvider services, string csvPath)
        {
            using var scope = services.CreateScope();
            var repo = scope.ServiceProvider
                            .GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();

            if ((await repo.GetAllAsync()).Any())
                return;

            using var reader = new StreamReader(csvPath);
            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                // suppress header‐validation and missing‐field errors
                HeaderValidated   = null,
                MissingFieldFound = null,

                // SKIP any property whose type is a non-string IEnumerable
                ShouldMapProperty = propMap =>
                    !(typeof(System.Collections.IEnumerable).IsAssignableFrom(propMap.Property.PropertyType)
                      && propMap.Property.PropertyType != typeof(string))
            };

            using var csv = new CsvReader(reader, config);
            var records = csv.GetRecords<ZipCodeServiceAreaModel>().ToList();

            await repo.AddRangeAsync(records);
            await repo.CommitTransactionAsync();
        }
    }
}
```

**What this does**  
- **`HeaderValidated = null`** and **`MissingFieldFound = null`** turn off all CsvHelper header‐and‐field checks.  
- **`ShouldMapProperty`** is a filter that returns `false` for any property whose type implements `IEnumerable` (except `string`). Those are the only members that CsvHelper will try to bind as indexed columns (i.e. `Foo[0]`, `Foo[1]`, etc.). By skipping them, CsvHelper never looks for `DeliveryCity[0]` or `DeliveryState[0]`, and your flat headers match your flat model 1:1.

## USER
here is the csv file header and some data Id,AreaName,AreaCode,DistrictName,DistrictNumber,DeliveryZipCode,LocaleName,PhysicalCity,PhysicalState,PhysicalZip,PhysicalZip4,RowVersion

{79C8DF21-8806-F011-9514-F0D415E5522B},SOUTHERN,4G,PUERTO RICO,006,00601,ADJUNTAS,ADJUNTAS,PR,00601,9998,0000000000104775

{7AC8DF21-8806-F011-9514-F0D415E5522B},SOUTHERN,4G,PUERTO RICO,006,00602,AGUADA,AGUADA,PR,00602,9998,0000000000104777


## Thoughts
The user's CSV header includes fields for things like AreaName, AreaCode, DistrictName, and physical address fields like DeliveryZipCode and LocaleName. These should match the ZipCodeServiceAreaModel's properties. The issue with CsvHelper errors suggests mapping fields like 'DeliveryCity,' 'DeliveryState,' and 'positionValue' that may be part of a collection or related model, possibly such as ServiceAreaRates. I'll need to align the model's properties with the data to prevent further errors.
The user is indicating an issue with indexers (`[]`) in the CSV mapping to the model, possibly due to array or list properties in the model. The fix they've proposed using `ShouldMapProperty` to skip `IEnumerable` types (except string) might still work, but ensuring that only scalar properties are mapped is key. To confirm, I'll adjust the seeder code and offer a complete, formal configuration. I'll also explore binding via `GetRecords<ZipCodeServiceAreaModel>()` to focus on scalar properties, ensuring the fix works cleanly for the user's model.

## ASSISTANT
Below is the revised seeder method, configured to:

- Suppress any header-validation or missing-field exceptions.  
- Skip mapping of any indexed/collection properties (the ones that CsvHelper would otherwise try to bind as `Foo[0]`, `Foo[1]`, etc.).  

Since your CSV header exactly matches the scalar properties on `ZipCodeServiceAreaModel`, this will bind 1:1 without any extra maps.

```csharp
using System.Globalization;
using System.Collections;
using CsvHelper;
using CsvHelper.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

namespace Logistix.Server.API.Install
{
    public static class SeedDatabase
    {
        public static async Task SeedZipCodesAsync(this IServiceProvider services, string csvPath)
        {
            using var scope = services.CreateScope();
            var repo = scope.ServiceProvider
                            .GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();

            // Only seed if table is empty
            if ((await repo.GetAllAsync()).Any())
                return;

            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                HeaderValidated   = null, // disable missing‐column errors
                MissingFieldFound = null, // disable missing‐field errors

                // Skip any non-string IEnumerable (prevents CsvHelper trying Foo[0], Foo[1], …)
                ShouldMapProperty = propMap =>
                    !(typeof(IEnumerable).IsAssignableFrom(propMap.Property.PropertyType)
                      && propMap.Property.PropertyType != typeof(string))
            };

            using var reader = new StreamReader(csvPath);
            using var csv    = new CsvReader(reader, config);

            var records = csv.GetRecords<ZipCodeServiceAreaModel>().ToList();
            await repo.AddRangeAsync(records);
            await repo.CommitTransactionAsync();
        }
    }
}
```

### Invocation in `Program.cs`

```csharp
var app = builder.Build();

// after migrations but before Run():
var csvPath = Path.Combine(builder.Environment.ContentRootPath,
                           "Data", "us-zipcodes.csv");
await app.Services.SeedZipCodesAsync(csvPath);

app.Run();
```

#### Why this resolves the `HeaderValidationException`

- **`HeaderValidated = null`** and **`MissingFieldFound = null`** prevent CsvHelper from throwing when it encounters headers or fields it doesn’t expect.  
- **`ShouldMapProperty`** excludes any property whose type implements `IEnumerable` (except `string`), so CsvHelper never attempts to bind indexed/collection properties (e.g. `DeliveryCity[0]`).  

With this configuration, your flat CSV header (`Id,AreaName,…,RowVersion`) will bind directly to the identically named properties on your model.

## USER
'CsvConfiguration' does not contain a definition for 'ShouldMapProperty'

## Thoughts
I’ve realized that `ShouldMapProperty` isn’t available on `CsvConfiguration`—it’s actually on `CsvClassMap`. There’s a `ShouldMapMember` property on `CsvConfiguration`, but it’s slightly different. In v15 and onwards, it's now a `Func<ShouldMapMemberArgs, bool>`. This makes sense since `ShouldMapMember` is for controlling which members get mapped. So, I’ll update the code and change `ShouldMapProperty` to `ShouldMapMember` and adjust the method accordingly.
I’ve been trying to fix the CsvHelper configuration for mapping members in my code. It turns out, the error arises due to attempting to map a collection, like `DeliveryCity[0]`, which indicates the

## ASSISTANT
Below is the corrected seeder. The only change from the previous version is replacing the non-existent `ShouldMapProperty` with `ShouldMapMember`, which CsvHelper supports out-of-the-box:

```csharp
using System.Globalization;
using System.Collections;
using CsvHelper;
using CsvHelper.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

namespace Logistix.Server.API.Install
{
    public static class SeedDatabase
    {
        public static async Task SeedZipCodesAsync(this IServiceProvider services, string csvPath)
        {
            using var scope = services.CreateScope();
            var repo = scope.ServiceProvider
                            .GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();

            // Only seed if the table is empty
            if ((await repo.GetAllAsync()).Any())
                return;

            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                // Disable exceptions for missing or extra headers/fields
                HeaderValidated   = null,
                MissingFieldFound = null,

                // Skip mapping of any non-string IEnumerable properties
                ShouldMapMember = memberMap =>
                    !(typeof(IEnumerable).IsAssignableFrom(memberMap.Member.MemberType)
                      && memberMap.Member.MemberType != typeof(string))
            };

            using var reader = new StreamReader(csvPath);
            using var csv    = new CsvReader(reader, config);

            var records = csv.GetRecords<ZipCodeServiceAreaModel>().ToList();
            await repo.AddRangeAsync(records);
            await repo.CommitTransactionAsync();
        }
    }
}
```

**Key points**  
- **`ShouldMapMember`** filters out any properties whose type implements `IEnumerable` (except `string`), preventing CsvHelper from looking for headers like `DeliveryCity[0]`.  
- **`HeaderValidated = null`** and **`MissingFieldFound = null`** suppress validation errors when the CSV has columns your model doesn’t (or vice versa).  

Invoke it exactly as before in your `Program.cs`:

```csharp
var app = builder.Build();

// after migrations but before Run():
var csvPath = Path.Combine(builder.Environment.ContentRootPath,
                           "Data", "us-zipcodes.csv");
await app.Services.SeedZipCodesAsync(csvPath);

app.Run();
```

## USER
  'CsvConfiguration' does not contain a definition for 'ShouldMapMember'


## Thoughts
The user is trying to implement a CSV seeder but encountered issues with properties like "DeliveryCity" and "DeliveryState" not matching headers. It seems they may be using an older version of CsvHelper. One solution could be to skip problematic properties using ClassMap. Alternatively, to avoid indexing issues, they could disable the default indexer mapping in their configuration. It seems the model might have collection properties like a `string[]`, but they only want to map flat fields.
The best path for the user is creating a ClassMap to map only the desired properties and instruct CsvHelper to ignore others. This requires defining a ClassMap subclass for the model, disabling `MemberTypes` mapping, and using `AutoMap()` to map only scalar properties. They should disable header validation and only map the wanted properties. Alternatively, the user could manually split by commas in the CSV, but using CsvHelper ensures easier handling. If there’s a mismatch, disabling extra validations will prevent unnecessary errors.

## ASSISTANT
Below is a targeted solution that avoids any reliance on non-existent configuration hooks. Instead, it:

1. **Defines an explicit `ClassMap`** for only your scalar properties.  
2. **Disables header and field validation** so CsvHelper never complains about extras.  
3. **Registers that map** before calling `GetRecords<>()`.  

---

### 1. Define an explicit `ClassMap`

```csharp
// ZipCodeServiceAreaModelMap.cs
using CsvHelper.Configuration;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

public sealed class ZipCodeServiceAreaModelMap : ClassMap<ZipCodeServiceAreaModel>
{
    public ZipCodeServiceAreaModelMap()
    {
        Map(m => m.Id).Name("Id");
        Map(m => m.AreaName).Name("AreaName");
        Map(m => m.AreaCode).Name("AreaCode");
        Map(m => m.DistrictName).Name("DistrictName");
        Map(m => m.DistrictNumber).Name("DistrictNumber");
        Map(m => m.DeliveryZipCode).Name("DeliveryZipCode");
        Map(m => m.LocaleName).Name("LocaleName");
        Map(m => m.PhysicalCity).Name("PhysicalCity");
        Map(m => m.PhysicalState).Name("PhysicalState");
        Map(m => m.PhysicalZip).Name("PhysicalZip");
        Map(m => m.PhysicalZip4).Name("PhysicalZip4");
        Map(m => m.RowVersion).Name("RowVersion");
        // Do NOT map any other properties (e.g. collections or indexers)
    }
}
```

---

### 2. Update your static seeder

```csharp
using System.Globalization;
using CsvHelper;
using CsvHelper.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

namespace Logistix.Server.API.Install
{
    public static class SeedDatabase
    {
        public static async Task SeedZipCodesAsync(this IServiceProvider services, string csvPath)
        {
            using var scope = services.CreateScope();
            var repo = scope.ServiceProvider
                            .GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();

            if ((await repo.GetAllAsync()).Any())
                return;

            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                HeaderValidated   = null, // turn off “missing header” errors
                MissingFieldFound = null, // turn off “missing field” errors
            };

            using var reader = new StreamReader(csvPath);
            using var csv    = new CsvReader(reader, config);

            // Register only the scalar-property map—no attempt to bind collections/indexers
            csv.Context.RegisterClassMap<ZipCodeServiceAreaModelMap>();

            var records = csv.GetRecords<ZipCodeServiceAreaModel>().ToList();
            await repo.AddRangeAsync(records);
            await repo.CommitTransactionAsync();
        }
    }
}
```

---

### 3. Invoke in `Program.cs`

```csharp
var app = builder.Build();

// apply migrations, then seed ZIP codes
await app.Services.SeedZipCodesAsync(
    Path.Combine(builder.Environment.ContentRootPath, "Data", "us-zipcodes.csv")
);

app.Run();
```

**Rationale**  
- **Explicit mapping** prevents CsvHelper from ever looking for `Foo[0]` headers.  
- **Disabled validation** silences any residual header/field mismatches.  
- **DI + static extension** keeps your seeder discoverable while still resolving your repository at runtime.

## USER
can we just use a different csv reader?

## Thoughts
The user has encountered issues with the CsvHelper library and is seeking alternatives. In the .NET/C# environment, we could suggest using `TextFieldParser` from `Microsoft.VisualBasic.FileIO` as a viable option. Another possibility is `CsvTextReader` from the Sylvan library or `FastCsvReader` from LumenWorks.Framework.IO. While manually parsing with `StreamReader` and `string.Split(',')` is an option, it can fail when handling quoted fields. Overall, leveraging the `TextFieldParser` or `CsvReader` from the Sylvan library would likely be the best fit.

## ASSISTANT
Yes. If you’d rather avoid CsvHelper altogether, you can use the built-in `TextFieldParser` (in `Microsoft.VisualBasic.FileIO`) or even a simple line-split approach. Below is an example using `TextFieldParser`, which will correctly handle quoted fields and delimiters without any third-party dependency:

```csharp
using System.Globalization;
using System.IO;
using System.Threading.Tasks;
using Microsoft.VisualBasic.FileIO;
using Microsoft.Extensions.DependencyInjection;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

namespace Logistix.Server.API.Install
{
    public static class SeedDatabase
    {
        public static async Task SeedZipCodesWithTextFieldParserAsync(this IServiceProvider services, string csvPath)
        {
            using var scope = services.CreateScope();
            var repo = scope.ServiceProvider
                            .GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();

            // Only seed on first run
            if ((await repo.GetAllAsync()).Any())
                return;

            var list = new List<ZipCodeServiceAreaModel>();
            using var parser = new TextFieldParser(csvPath)
            {
                TextFieldType = FieldType.Delimited,
                Delimiters = new[] { "," },
                HasFieldsEnclosedInQuotes = true,
                TrimWhiteSpace = true
            };

            // 1) Read header and determine column‐indices
            var headers = parser.ReadFields();
            int ixId        = Array.IndexOf(headers, "Id");
            int ixAreaName  = Array.IndexOf(headers, "AreaName");
            int ixAreaCode  = Array.IndexOf(headers, "AreaCode");
            int ixDistrict  = Array.IndexOf(headers, "DistrictName");
            int ixDistrictNo= Array.IndexOf(headers, "DistrictNumber");
            int ixDelivery  = Array.IndexOf(headers, "DeliveryZipCode");
            int ixLocale    = Array.IndexOf(headers, "LocaleName");
            int ixPhysCity  = Array.IndexOf(headers, "PhysicalCity");
            int ixPhysState = Array.IndexOf(headers, "PhysicalState");
            int ixPhysZip   = Array.IndexOf(headers, "PhysicalZip");
            int ixPhysZip4  = Array.IndexOf(headers, "PhysicalZip4");
            int ixRowVer    = Array.IndexOf(headers, "RowVersion");

            // 2) Iterate rows
            while (!parser.EndOfData)
            {
                var fields = parser.ReadFields();
                list.Add(new ZipCodeServiceAreaModel
                {
                    Id               = Guid.Parse(fields[ixId].Trim('{', '}')),
                    AreaName         = fields[ixAreaName],
                    AreaCode         = fields[ixAreaCode],
                    DistrictName     = fields[ixDistrict],
                    DistrictNumber   = fields[ixDistrictNo],
                    DeliveryZipCode  = fields[ixDelivery],
                    LocaleName       = fields[ixLocale],
                    PhysicalCity     = fields[ixPhysCity],
                    PhysicalState    = fields[ixPhysState],
                    PhysicalZip      = fields[ixPhysZip],
                    PhysicalZip4     = fields[ixPhysZip4],
                    RowVersion       = fields[ixRowVer]
                });
            }

            // 3) Bulk‐insert
            await repo.AddRangeAsync(list);
            await repo.CommitTransactionAsync();
        }
    }
}
```

### How to wire it up in `Program.cs`

```csharp
var app = builder.Build();

// After migrations but before Run():
var csvPath = Path.Combine(builder.Environment.ContentRootPath,
                           "Data", "us-zipcodes.csv");
await app.Services.SeedZipCodesWithTextFieldParserAsync(csvPath);

app.Run();
```

---

#### Advantages of `TextFieldParser`

- **Zero third-party packages**: it’s part of the .NET Framework.  
- **Handles quotes and escaped delimiters** out of the box.  
- **Full control**: you choose exactly which columns to read, so there’s no surprise indexer lookups (`Foo[0]`).  

If you prefer a lighter-weight or even more performant option, you could also read via `File.ReadLines` and `string.Split(',')` (with caveats around quoted fields), or adopt one of the high-performance CSV libraries such as [Sylvan.Data.Csv](https://www.nuget.org/packages/Sylvan.Data.Csv) or [LumenWorks.Framework.IO](https://www.nuget.org/packages/LumenWorksCsvReader).

## USER
nevermind we;ll keep it but it has to have a mapper class?

## Thoughts
The user wants to include a mapper class with CsvHelper, using a ClassMap (CsvClassMap) to map the header to the class property. They have specified their need for this but haven’t asked further details. I’ll provide the full code with the ClassMap and the seeder class without unnecessary confirmations. I'll include the code for CsvClassMap (such as `ZipCodeServiceAreaModelMap`) and how to register it, ensuring it's ready for their use without additional explanation.

## ASSISTANT
Below is a complete example showing:

1. **`ClassMap`** for your model  
2. **Static seeder** that registers the map and disables header/field validation  
3. **Invocation** in `Program.cs`  

---

```csharp
// Mappings/ZipCodeServiceAreaModelMap.cs
using CsvHelper.Configuration;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;

namespace Logistix.Server.API.Mappings
{
    public sealed class ZipCodeServiceAreaModelMap : ClassMap<ZipCodeServiceAreaModel>
    {
        public ZipCodeServiceAreaModelMap()
        {
            Map(x => x.Id)              .Name("Id");
            Map(x => x.AreaName)        .Name("AreaName");
            Map(x => x.AreaCode)        .Name("AreaCode");
            Map(x => x.DistrictName)    .Name("DistrictName");
            Map(x => x.DistrictNumber)  .Name("DistrictNumber");
            Map(x => x.DeliveryZipCode) .Name("DeliveryZipCode");
            Map(x => x.LocaleName)      .Name("LocaleName");
            Map(x => x.PhysicalCity)    .Name("PhysicalCity");
            Map(x => x.PhysicalState)   .Name("PhysicalState");
            Map(x => x.PhysicalZip)     .Name("PhysicalZip");
            Map(x => x.PhysicalZip4)    .Name("PhysicalZip4");
            Map(x => x.RowVersion)      .Name("RowVersion");
            // Do not map any indexed or collection properties
        }
    }
}
```

```csharp
// Install/SeedDatabase.cs
using System.Globalization;
using CsvHelper;
using CsvHelper.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Logistix.Server.Domain.Interfaces.Repositories;
using Logistix.Server.Domain.Models.Infrastructure.Configuration;
using Logistix.Server.API.Mappings;

namespace Logistix.Server.API.Install
{
    public static class SeedDatabase
    {
        public static async Task SeedZipCodesAsync(this IServiceProvider services, string csvPath)
        {
            using var scope = services.CreateScope();
            var repo = scope.ServiceProvider
                            .GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();

            if ((await repo.GetAllAsync()).Any())
                return;

            var config = new CsvConfiguration(CultureInfo.InvariantCulture)
            {
                HeaderValidated   = null,  // disable missing‐column errors
                MissingFieldFound = null   // disable missing‐field errors
            };

            using var reader = new StreamReader(csvPath);
            using var csv    = new CsvReader(reader, config);

            // Register the explicit ClassMap
            csv.Context.RegisterClassMap<ZipCodeServiceAreaModelMap>();

            var records = csv.GetRecords<ZipCodeServiceAreaModel>().ToList();
            await repo.AddRangeAsync(records);
            await repo.CommitTransactionAsync();
        }
    }
}
```

```csharp
// Program.cs (excerpt)
var app = builder.Build();

// Apply migrations, then seed the ZIP table
await app.Services.SeedZipCodesAsync(
    Path.Combine(builder.Environment.ContentRootPath, "Data", "us-zipcodes.csv")
);

app.Run();
```

## USER
for some reason its trying to inser the id field rather than create it during insert  Microsoft.EntityFrameworkCore.DbUpdateException

  HResult=0x80131500

  Message=An error occurred while saving the entity changes. See the inner exception for details.

  Source=Microsoft.EntityFrameworkCore.Relational

  StackTrace:

   at Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.<ConsumeResultSetAsync>d__4.MoveNext()

   at Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.<ConsumeAsync>d__2.MoveNext()

   at Microsoft.EntityFrameworkCore.Update.ReaderModificationCommandBatch.<ExecuteAsync>d__50.MoveNext()

   at Microsoft.EntityFrameworkCore.Update.ReaderModificationCommandBatch.<ExecuteAsync>d__50.MoveNext()

   at Microsoft.EntityFrameworkCore.SqlServer.Update.Internal.SqlServerModificationCommandBatch.<ExecuteAsync>d__15.MoveNext()

   at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.<ExecuteAsync>d__9.MoveNext()

   at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.<ExecuteAsync>d__9.MoveNext()

   at Microsoft.EntityFrameworkCore.Update.Internal.BatchExecutor.<ExecuteAsync>d__9.MoveNext()

   at Microsoft.EntityFrameworkCore.Storage.RelationalDatabase.<SaveChangesAsync>d__8.MoveNext()

   at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.<SaveChangesAsync>d__111.MoveNext()

   at Microsoft.EntityFrameworkCore.ChangeTracking.Internal.StateManager.<SaveChangesAsync>d__115.MoveNext()

   at Microsoft.EntityFrameworkCore.SqlServer.Storage.Internal.SqlServerExecutionStrategy.<ExecuteAsync>d__7`2.MoveNext()

   at Microsoft.EntityFrameworkCore.DbContext.<SaveChangesAsync>d__63.MoveNext()

   at Microsoft.EntityFrameworkCore.DbContext.<SaveChangesAsync>d__63.MoveNext()

   at Logistix.Server.Infrastructure.Repositories.GenericRepository`1.<AddRangeAsync>d__9.MoveNext() in D:\Deployment\LogistixServerAPIV2\Logistix.Server.Infrastructure\Repositories\GenericRepsitory.cs:line 117

   at Logistix.Server.API.Install.SeedDatabase.<SeedZipCodesAsync>d__0.MoveNext() in D:\Deployment\LogistixServerAPIV2\Logistix.Server.Infrastructure\Install\SeedDatabase.cs:line 37

   at Program.<<Main>$>d__0.MoveNext() in D:\Deployment\LogistixServerAPIV2\Logistix.Server.API\Program.cs:line 439



  This exception was originally thrown at this call stack:

    Microsoft.Data.SqlClient.SqlConnection.OnError(Microsoft.Data.SqlClient.SqlException, bool, System.Action<System.Action>)

    Microsoft.Data.SqlClient.SqlInternalConnection.OnError(Microsoft.Data.SqlClient.SqlException, bool, System.Action<System.Action>)

    Microsoft.Data.SqlClient.TdsParser.ThrowExceptionAndWarning(Microsoft.Data.SqlClient.TdsParserStateObject, Microsoft.Data.SqlClient.SqlCommand, bool, bool)

    Microsoft.Data.SqlClient.TdsParser.TryRun(Microsoft.Data.SqlClient.RunBehavior, Microsoft.Data.SqlClient.SqlCommand, Microsoft.Data.SqlClient.SqlDataReader, Microsoft.Data.SqlClient.BulkCopySimpleResultSet, Microsoft.Data.SqlClient.TdsParserStateObject, out bool)

    Microsoft.Data.SqlClient.SqlDataReader.TryHasMoreRows(out bool)

    Microsoft.Data.SqlClient.SqlDataReader.TryReadInternal(bool, out bool)

    Microsoft.Data.SqlClient.SqlDataReader.ReadAsyncExecute(System.Threading.Tasks.Task, object)

    Microsoft.EntityFrameworkCore.Update.AffectedCountModificationCommandBatch.ConsumeResultSetAsync(int, Microsoft.EntityFrameworkCore.Storage.RelationalDataReader, System.Threading.CancellationToken)



Inner Exception 1:

SqlException: Cannot insert explicit value for identity column in table 'Logistix_US_Zip_Code_Table' when IDENTITY_INSERT is set to OFF.


## Thoughts
From what the user says, there’s a conflict during the insert operation. The 'Id' field in the CSV file is a GUID, but the SQL table has an identity column to auto-generate this Id. Entity Framework (EF) is trying to insert a GUID explicitly into this identity column, but SQL doesn’t allow that with `IDENTITY_INSERT` set to off. Possible solutions include configuring EF to treat the Id as non-identity, removing the identity property in SQL, or letting SQL handle the Id generation by not mapping it in the EF model.
The user's data model has a conflict because the table expects an auto-generated identity column (likely an integer), but the CSV uses GUIDs for the Id field. One solution is to avoid referencing the Id for insertions, allowing the database to generate it automatically. Alternatively, the Id from CSV could be assigned to a different property (like 'LegacyId'). If they want to insert GUIDs explicitly, they'd need to set `IDENTITY_INSERT ON`, but the table might need further adjustments for this to work correctly.
It looks like there's a conflict between the Id column’s type and how it’s being handled in Entity Framework. Since the Id should be a GUID and not an identity column, the solution is to either adjust EF's configuration or change the column type in the database. A better approach could be setting `ValueGeneratedOnAdd` on the Id property so that EF knows the database should generate it. Alternatively, if you want to insert GUID values from CSV, you could enable `IDENTITY_INSERT` temporarily during the seed process, but it's better to have the DB generate the value without explicit mapping.

## ASSISTANT
Below are two approaches—pick the one that best fits your requirements.

---

### 1. Let the database generate the **Id** (omit it from the INSERT)

1. **Change your CSV mapper** so you don’t map the `Id` column at all:

    ```csharp
    // Mappings/ZipCodeServiceAreaModelMap.cs
    using CsvHelper.Configuration;
    using Logistix.Server.Domain.Models.Infrastructure.Configuration;

    public sealed class ZipCodeServiceAreaModelMap : ClassMap<ZipCodeServiceAreaModel>
    {
        public ZipCodeServiceAreaModelMap()
        {
            Map(m => m.Id)              .Ignore();          // ← do not read CSV Id
            Map(m => m.AreaName)        .Name("AreaName");
            Map(m => m.AreaCode)        .Name("AreaCode");
            Map(m => m.DistrictName)    .Name("DistrictName");
            Map(m => m.DistrictNumber)  .Name("DistrictNumber");
            Map(m => m.DeliveryZipCode) .Name("DeliveryZipCode");
            Map(m => m.LocaleName)      .Name("LocaleName");
            Map(m => m.PhysicalCity)    .Name("PhysicalCity");
            Map(m => m.PhysicalState)   .Name("PhysicalState");
            Map(m => m.PhysicalZip)     .Name("PhysicalZip");
            Map(m => m.PhysicalZip4)    .Name("PhysicalZip4");
            Map(m => m.RowVersion)      .Name("RowVersion");
        }
    }
    ```

2. **Tell EF Core** that `Id` is database-generated:

    ```csharp
    // In your DbContext
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<ZipCodeServiceAreaModel>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.Id)
                  .ValueGeneratedOnAdd();     // ← DB will assign the key
        });

        // …other model configuration…
    }
    ```

3. **Ensure your table** actually auto-generates `Id` (e.g. it’s an `INT IDENTITY` or `UNIQUEIDENTIFIER` with `DEFAULT NEWSEQUENTIALID()`).

4. **Seeder stays the same** (you no longer register the `Id` mapping; EF will omit it from the INSERT).

---

### 2. Keep your CSV’s `Id` values but allow explicit inserts

If you must preserve the GUIDs in your CSV, wrap your seeding in an `IDENTITY_INSERT` transaction:

```csharp
using (var scope = services.CreateScope())
{
    var db   = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    var repo = scope.ServiceProvider.GetRequiredService<IGenericRepository<ZipCodeServiceAreaModel>>();
    var records = /* read CSV into List<ZipCodeServiceAreaModel> */;

    if (!records.Any() || (await repo.GetAllAsync()).Any())
        return;

    await db.Database.OpenConnectionAsync();
    using var txn = await db.Database.BeginTransactionAsync();
    // Enable explicit PK insertion
    await db.Database.ExecuteSqlRawAsync(
        "SET IDENTITY_INSERT [Logistix_US_Zip_Code_Table] ON");

    await repo.AddRangeAsync(records);
    await repo.CommitTransactionAsync();

    // Disable explicit PK insertion
    await db.Database.ExecuteSqlRawAsync(
        "SET IDENTITY_INSERT [Logistix_US_Zip_Code_Table] OFF");

    await txn.CommitAsync();
}
```

- **Pros**: preserves your source GUIDs  
- **Cons**: more complex, can only have one table with `IDENTITY_INSERT ON` at a time  

---

**Recommendation:**  
If you don’t actually need those legacy GUIDs, use **Option 1**. Your DB will generate a clean primary key, EF will omit the `Id` column, and the seed will succeed without `IDENTITY_INSERT` gymnastics.

## USER
this is new.  AutoMapper.AutoMapperMappingException

  HResult=0x80131500

  Message=Error mapping types.

  Source=AutoMapper

  StackTrace:

   at Logistix.ApplicationLayer.ViewModels.Extended.Context.Tarriff.TarriffViewModel.<GetRateTables>d__5.MoveNext() in D:\Deployment\Logistix.Desktop.Winforms\Logistix.Application\ViewModels\Extended\Context\Tarriff\TarriffViewModel.cs:line 81



  This exception was originally thrown at this call stack:

    System.Text.Json.ThrowHelper.ThrowJsonException_DeserializeUnableToConvertValue(System.Type)

    System.Text.Json.Serialization.JsonCollectionConverter<TCollection, TElement>.OnTryRead(ref System.Text.Json.Utf8JsonReader, System.Type, System.Text.Json.JsonSerializerOptions, ref System.Text.Json.ReadStack, out TCollection)

    System.Text.Json.Serialization.JsonConverter<T>.TryRead(ref System.Text.Json.Utf8JsonReader, System.Type, System.Text.Json.JsonSerializerOptions, ref System.Text.Json.ReadStack, out T, out bool)

    System.Text.Json.Serialization.JsonConverter<T>.ReadCore(ref System.Text.Json.Utf8JsonReader, out T, System.Text.Json.JsonSerializerOptions, ref System.Text.Json.ReadStack)

    System.Text.Json.Serialization.Metadata.JsonTypeInfo<T>.Deserialize(ref System.Text.Json.Utf8JsonReader, ref System.Text.Json.ReadStack)

    System.Text.Json.JsonSerializer.ReadFromSpan<TValue>(System.ReadOnlySpan<byte>, System.Text.Json.Serialization.Metadata.JsonTypeInfo<TValue>, int?)

    System.Text.Json.JsonSerializer.ReadFromSpan<TValue>(System.ReadOnlySpan<char>, System.Text.Json.Serialization.Metadata.JsonTypeInfo<TValue>)

    System.Text.Json.JsonSerializer.Deserialize<TValue>(string, System.Text.Json.JsonSerializerOptions)

    RateTableZoneJsonResolver.Resolve(RateTableEntity, Logistix.ApplicationLayer.Models.Context.RateTable.RateTableDto, System.Collections.ObjectModel.ObservableCollection<Logistix.ApplicationLayer.Models.Context.RateTable.ZoneDTO>, AutoMapper.ResolutionContext) in MappingProfile.cs



Inner Exception 1:

AutoMapperMappingException: Error mapping types.



Inner Exception 2:

JsonException: The JSON value could not be converted to System.Collections.ObjectModel.ObservableCollection`1[Logistix.ApplicationLayer.Models.Context.RateTable.ZoneDTO]. Path: $ | LineNumber: 0 | BytePositionInLine: 4.


## Thoughts
Got it! The issue here seems to be that AutoMapper can't map the JSON to the `ObservableCollection<ZoneDTO>`. The error implies that the JSON being passed isn't in the expected array format. I'll need to check the source of the JSON data. It's likely either missing the array notation or the structure is mismatched with `ZoneDTO`. I should ensure the JSON is an array of objects matching the fields of `ZoneDTO`. 

I'll try adjusting the deserialization logic to handle this cleanly!
It looks like the issue comes from a mismatch between what's expected in the code and the actual JSON format. If your data is stored as a string rather than a valid JSON array, it can cause mapping errors. To

## ASSISTANT
To resolve this you need to make your JSON‐to‐collection resolver more robust:

1. **Guard against empty/invalid JSON**  
2. **Deserialize into a `List<ZoneDTO>`** (the JSON array type)  
3. **Wrap that list in an `ObservableCollection<ZoneDTO>`**  
4. **Catch any `JsonException`** and fall back to an empty collection  

---  

### Example: a safe `IValueResolver`  

```csharp
using System;
using System.Collections.ObjectModel;
using System.Text.Json;
using AutoMapper;
using Logistix.ApplicationLayer.Models.Context.RateTable;
using Logistix.Server.Domain.Entities; // your RateTableEntity namespace

public class RateTableZoneJsonResolver
    : IValueResolver<RateTableEntity, RateTableDto, ObservableCollection<ZoneDTO>>
{
    private static readonly JsonSerializerOptions _jsonOptions =
        new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true,
            // add any converters if you need custom date/enum handling, etc.
        };

    public ObservableCollection<ZoneDTO> Resolve(
        RateTableEntity source,
        RateTableDto destination,
        ObservableCollection<ZoneDTO> destMember,
        ResolutionContext context)
    {
        var json = source.ZoneJson; // or whatever property holds your JSON string

        if (string.IsNullOrWhiteSpace(json))
        {
            return new ObservableCollection<ZoneDTO>();
        }

        try
        {
            // Deserialize into a List<T> first
            var list = JsonSerializer.Deserialize<List<ZoneDTO>>(json, _jsonOptions)
                       ?? new List<ZoneDTO>();

            return new ObservableCollection<ZoneDTO>(list);
        }
        catch (JsonException ex)
        {
            // TODO: log ex.Message (e.g. ILogger or Debug)
            return new ObservableCollection<ZoneDTO>();
        }
    }
}
```

#### Why this works

- **`string.IsNullOrWhiteSpace`** prevents attempting to parse `null` or empty strings.  
- **Deserializing to `List<ZoneDTO>`** matches the JSON array shape (`[...]`).  
- **Wrapping in `ObservableCollection<ZoneDTO>`** gives you the target type AutoMapper expects.  
- **Catching `JsonException`** ensures a malformed payload doesn’t bubble up as an unhandled exception.

---

### Wire it into your AutoMapper profile

```csharp
public class MappingProfile : Profile
{
    public MappingProfile()
    {
        CreateMap<RateTableEntity, RateTableDto>()
            // other member mappings…
            .ForMember(
                dest => dest.Zones,
                opt  => opt.MapFrom<RateTableZoneJsonResolver>()
            );
    }
}
```

---

### Validate your JSON payload

Finally, make sure that **`source.ZoneJson`** really is a JSON array, for example:

```json
[
  { "Id": 1, "Name": "Zone A", /* etc. */ },
  { "Id": 2, "Name": "Zone B", /* etc. */ }
]
```

If the string in your database is not in `[...]` form—e.g. it’s a single object or missing brackets—you’ll need to correct it or wrap it in brackets before deserialization.

## USER
can you check this.  this is json stored as one long string in the db. [{"Id":"37c802ce-506f-4d70-ae5c-ac828288c4c5","RateTableGuid":"00000000-0000-0000-0000-000000000000","ZoneName":"Zone A","IsActive":false,"ZonePricingRule":[{"Id":"4b6dbd95-a782-48b0-97a9-5b4506884c8f","ZoneGuid":"37c802ce-506f-4d70-ae5c-ac828288c4c5","RuleName":"New Pricing Rule","ValidStartDate":"2025-01-01","ValidEndDate":"2025-12-31","OnDays":"Monday,Wednesday,Tuesday,Friday,Thursday","ValidHoursStart":"08:00:00","ValidHoursEnd":"17:00:00","RequiresQuote":false,"MarkupType":"","MarkupCost":0,"MaxCost":200.00,"MinCost":17.00,"MaxOrderWeight":0,"MaxItemWeight":0,"WeightCostCollection":[{"Id":"772771a3-af54-4413-8407-a4c589041c5f","Weight":100,"Cost":5.75,"RowVersion":null},{"Id":"82637509-6e99-430e-b81c-c31f6569eef7","Weight":1000,"Cost":5.00,"RowVersion":null},{"Id":"057d441a-7cc4-464b-bcb4-2e0106f1f71a","Weight":2000,"Cost":4.00,"RowVersion":null},{"Id":"630adeb8-b785-44ba-a08f-1c4e9f9feb6a","Weight":5000,"Cost":3.50,"RowVersion":null}],"RowVersion":null}],"ZoneServiceArea":[{"Id":"47ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48001","DeliveryCity":"ALGONAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48001","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"48ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48002","DeliveryCity":"ALLENTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48002","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"49ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48002","DeliveryCity":"ARMADA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48005","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48003","DeliveryCity":"ALMONT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48003","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48003","DeliveryCity":"ALMONT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48003","PhysicalZip4":"1109","Enabled":"true","RowVersion":null},{"Id":"4ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48004","DeliveryCity":"ANCHORVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48004","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48005","DeliveryCity":"ARMADA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48005","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48006","DeliveryCity":"AVOCA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48006","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48006","DeliveryCity":"YALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48097","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"50ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48007","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"51ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48009","DeliveryCity":"BIRMINGHAM","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48012","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"52ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48012","DeliveryCity":"BIRMINGHAM","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48012","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"53ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48014","DeliveryCity":"CAPAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48014","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"54ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48015","DeliveryCity":"CENTER LINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48015","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"55ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48015","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"56ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48017","DeliveryCity":"CLAWSON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48017","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"57ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48021","DeliveryCity":"EASTPOINTE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48021","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"58ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48022","DeliveryCity":"CAPAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48014","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"59ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48022","DeliveryCity":"EMMETT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48022","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48023","DeliveryCity":"FAIR HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48023","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48025","DeliveryCity":"FRANKLIN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48025","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48025","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48026","DeliveryCity":"FRASER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48026","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48026","DeliveryCity":"ROSEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48066","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48027","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"60ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48027","DeliveryCity":"GOODELLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48027","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"61ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48028","DeliveryCity":"ALGONAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48001","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"62ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48028","DeliveryCity":"HARSENS ISLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48028","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"63ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48030","DeliveryCity":"HAZEL PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48030","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"64ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48032","DeliveryCity":"JEDDO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48032","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"65ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48033","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"66ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48034","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"67ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48035","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"68ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48036","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"69ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48037","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48038","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"6bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48038","DeliveryCity":"CLINTON TOWNSHIP","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48038","PhysicalZip4":"9997","Enabled":"true","RowVersion":null},{"Id":"6ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48039","DeliveryCity":"MARINE CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48039","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48040","DeliveryCity":"MARYSVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48040","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48040","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48041","DeliveryCity":"MEMPHIS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48041","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"70ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48042","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"71ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48043","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"72ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48044","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"73ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48045","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"74ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48045","DeliveryCity":"SELFRIDGE ANGB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48045","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"75ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48046","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"76ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48047","DeliveryCity":"NEW BALTIMORE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48047","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"77ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48048","DeliveryCity":"NEW HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48048","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"78ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48049","DeliveryCity":"NORTH STREET","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48049","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"79ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48049","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48050","DeliveryCity":"NEW HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48048","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48051","DeliveryCity":"NEW BALTIMORE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48047","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48054","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48059","DeliveryCity":"FORT GRATIOT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48059","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48059","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48060","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"80ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48061","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"81ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48062","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"82ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48063","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"83ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48064","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"84ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48065","DeliveryCity":"ROMEO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48065","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"85ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48066","DeliveryCity":"ROSEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48066","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"86ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48067","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"87ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48068","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"88ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48069","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"89ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48070","DeliveryCity":"HUNTINGTON WOODS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48070","PhysicalZip4":"1131","Enabled":"true","RowVersion":null},{"Id":"8aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48070","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48071","DeliveryCity":"MADISON HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48071","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"8ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48071","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48083","PhysicalZip4":"9005","Enabled":"true","RowVersion":null},{"Id":"8ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48072","DeliveryCity":"BERKLEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48072","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48072","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48073","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48083","PhysicalZip4":"9005","Enabled":"true","RowVersion":null},{"Id":"90ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48074","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"91ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48074","DeliveryCity":"SMITHS CREEK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48074","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"92ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48075","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"93ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48076","DeliveryCity":"LATHRUP VILLAGE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48076","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"94ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48076","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"95ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48079","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"96ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48079","DeliveryCity":"SAINT CLAIR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48079","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"97ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48080","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"98ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48081","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"99ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48082","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48083","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48084","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48085","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48086","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48088","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48089","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48090","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48091","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48092","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48093","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48094","DeliveryCity":"WASHINGTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48094","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48095","DeliveryCity":"WASHINGTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48094","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48096","DeliveryCity":"ROMEO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48065","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48097","DeliveryCity":"YALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48097","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48098","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48099","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aaed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48101","DeliveryCity":"ALLEN PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48101","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"abed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48103","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48104","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48105","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aeed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"afed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9484","Enabled":"true","RowVersion":null},{"Id":"b0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"2548","Enabled":"true","RowVersion":null},{"Id":"b1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48107","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48108","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48109","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48111","DeliveryCity":"BELLEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48111","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48112","DeliveryCity":"BELLEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48111","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48113","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48114","DeliveryCity":"BRIGHTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48116","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48115","DeliveryCity":"SALINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48176","PhysicalZip4":"9650","Enabled":"true","RowVersion":null},{"Id":"b9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48116","DeliveryCity":"BRIGHTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48116","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"baed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48117","DeliveryCity":"CARLETON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48117","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48118","DeliveryCity":"CHELSEA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48118","PhysicalZip4":"1642","Enabled":"true","RowVersion":null},{"Id":"bced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48120","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48121","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"beed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48122","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48122","DeliveryCity":"MELVINDALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48122","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48123","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"0001","Enabled":"Off","RowVersion":null},{"Id":"c1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48124","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48125","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48126","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48127","DeliveryCity":"DEARBORN HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48127","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48128","DeliveryCity":"DEARBORN HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48127","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48130","DeliveryCity":"DEXTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48130","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48131","DeliveryCity":"DUNDEE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48131","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48133","DeliveryCity":"ERIE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48133","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48134","DeliveryCity":"FLAT ROCK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48134","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"caed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48135","DeliveryCity":"GARDEN CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48135","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48136","DeliveryCity":"GARDEN CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48135","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48137","DeliveryCity":"GREGORY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48137","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48137","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"ceed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48138","DeliveryCity":"GROSSE ILE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48138","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48139","DeliveryCity":"HAMBURG","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48139","PhysicalZip4":"1006","Enabled":"true","RowVersion":null},{"Id":"d0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48140","DeliveryCity":"IDA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48140","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48140","DeliveryCity":"TEMPERANCE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48182","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48141","DeliveryCity":"INKSTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48141","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48143","DeliveryCity":"LAKELAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48143","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48144","DeliveryCity":"LAMBERTVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48144","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48145","DeliveryCity":"LA SALLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48145","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48146","DeliveryCity":"LINCOLN PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48146","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48150","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48151","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48152","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48152","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"daed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48153","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48152","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48154","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48157","DeliveryCity":"LUNA PIER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48157","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48158","DeliveryCity":"MANCHESTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48158","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"deed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48159","DeliveryCity":"MAYBEE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48159","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48160","DeliveryCity":"MILAN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48160","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48161","DeliveryCity":"MONROE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48161","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48162","DeliveryCity":"MONROE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48161","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48164","DeliveryCity":"NEW BOSTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48164","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48165","DeliveryCity":"NEW HUDSON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48165","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48166","DeliveryCity":"NEWPORT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48166","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48167","DeliveryCity":"NORTHVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48167","PhysicalZip4":"1544","Enabled":"true","RowVersion":null},{"Id":"e6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48167","DeliveryCity":"FARMINGTON HILLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48335","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48168","DeliveryCity":"FARMINGTON HILLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48335","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48169","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48170","DeliveryCity":"PLYMOUTH","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48170","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eaed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48170","DeliveryCity":"PLYMOUTH","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48170","PhysicalZip4":"1621","Enabled":"true","RowVersion":null},{"Id":"ebed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48173","DeliveryCity":"ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48173","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48174","DeliveryCity":"ROMULUS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48174","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48174","DeliveryCity":"TAYLOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48180","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eeed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48175","DeliveryCity":"NORTHVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48168","PhysicalZip4":"9492","Enabled":"true","RowVersion":null},{"Id":"efed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48176","DeliveryCity":"SALINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48176","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48177","DeliveryCity":"SAMARIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48177","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48178","DeliveryCity":"SOUTH LYON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48178","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48179","DeliveryCity":"ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48173","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48179","DeliveryCity":"SOUTH ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48179","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48180","DeliveryCity":"TAYLOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48180","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48182","DeliveryCity":"TEMPERANCE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48182","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48183","DeliveryCity":"TRENTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48183","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48184","DeliveryCity":"WAYNE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48184","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48184","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48185","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"faed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48186","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48187","DeliveryCity":"CANTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48187","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48188","DeliveryCity":"CANTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48187","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48189","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"feed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48189","DeliveryCity":"WHITMORE LAKE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48189","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"ffed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48190","DeliveryCity":"WHITTAKER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48190","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"00ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48191","DeliveryCity":"WILLIS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48191","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"01ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48191","DeliveryCity":"YPSILANTI","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48197","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"02ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48192","DeliveryCity":"SOUTHGATE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48195","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"03ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48192","DeliveryCity":"WYANDOTTE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48192","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"04ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48193","DeliveryCity":"RIVERVIEW","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48193","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":506f-4d70-ae5c-ac828288c4c5","RateTableGuid":"00000000-0000-0000-0000-000000000000","ZoneName":"Zone A","IsActive":false,"ZonePricingRule":[{"Id":"4b6dbd95-a782-48b0-97a9-5b4506884c8f","ZoneGuid":"37c802ce-506f-4d70-ae5c-ac828288c4c5","RuleName":"New Pricing Rule","ValidStartDate":"2025-01-01","ValidEndDate":"2025-12-31","OnDays":"Monday,Wednesday,Tuesday,Friday,Thursday","ValidHoursStart":"08:00:00","ValidHoursEnd":"17:00:00","RequiresQuote":false,"MarkupType":"","MarkupCost":0,"MaxCost":200.00,"MinCost":17.00,"MaxOrderWeight":0,"MaxItemWeight":0,"WeightCostCollection":[{"Id":"772771a3-af54-4413-8407-a4c589041c5f","Weight":100,"Cost":5.75,"RowVersion":null},{"Id":"82637509-6e99-430e-b81c-c31f6569eef7","Weight":1000,"Cost":5.00,"RowVersion":null},{"Id":"057d441a-7cc4-464b-bcb4-2e0106f1f71a","Weight":2000,"Cost":4.00,"RowVersion":null},{"Id":"630adeb8-b785-44ba-a08f-1c4e9f9feb6a","Weight":5000,"Cost":3.50,"RowVersion":null}],"RowVersion":null}],"ZoneServiceArea":[{"Id":"47ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48001","DeliveryCity":"ALGONAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48001","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"48ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48002","DeliveryCity":"ALLENTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48002","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"49ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48002","DeliveryCity":"ARMADA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48005","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48003","DeliveryCity":"ALMONT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48003","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48003","DeliveryCity":"ALMONT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48003","PhysicalZip4":"1109","Enabled":"true","RowVersion":null},{"Id":"4ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48004","DeliveryCity":"ANCHORVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48004","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48005","DeliveryCity":"ARMADA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48005","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48006","DeliveryCity":"AVOCA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48006","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48006","DeliveryCity":"YALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48097","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"50ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48007","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"51ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48009","DeliveryCity":"BIRMINGHAM","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48012","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"52ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48012","DeliveryCity":"BIRMINGHAM","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48012","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"53ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48014","DeliveryCity":"CAPAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48014","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"54ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48015","DeliveryCity":"CENTER LINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48015","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"55ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48015","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"56ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48017","DeliveryCity":"CLAWSON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48017","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"57ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48021","DeliveryCity":"EASTPOINTE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48021","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"58ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48022","DeliveryCity":"CAPAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48014","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"59ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48022","DeliveryCity":"EMMETT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48022","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48023","DeliveryCity":"FAIR HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48023","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48025","DeliveryCity":"FRANKLIN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48025","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48025","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48026","DeliveryCity":"FRASER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48026","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48026","DeliveryCity":"ROSEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48066","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48027","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"60ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48027","DeliveryCity":"GOODELLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48027","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"61ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48028","DeliveryCity":"ALGONAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48001","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"62ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48028","DeliveryCity":"HARSENS ISLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48028","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"63ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48030","DeliveryCity":"HAZEL PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48030","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"64ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48032","DeliveryCity":"JEDDO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48032","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"65ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48033","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"66ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48034","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"67ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48035","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"68ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48036","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"69ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48037","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48038","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"6bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48038","DeliveryCity":"CLINTON TOWNSHIP","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48038","PhysicalZip4":"9997","Enabled":"true","RowVersion":null},{"Id":"6ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48039","DeliveryCity":"MARINE CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48039","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48040","DeliveryCity":"MARYSVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48040","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48040","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48041","DeliveryCity":"MEMPHIS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48041","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"70ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48042","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"71ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48043","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"72ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48044","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"73ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48045","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"74ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48045","DeliveryCity":"SELFRIDGE ANGB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48045","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"75ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48046","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"76ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48047","DeliveryCity":"NEW BALTIMORE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48047","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"77ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48048","DeliveryCity":"NEW HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48048","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"78ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48049","DeliveryCity":"NORTH STREET","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48049","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"79ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48049","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48050","DeliveryCity":"NEW HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48048","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48051","DeliveryCity":"NEW BALTIMORE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48047","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48054","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48059","DeliveryCity":"FORT GRATIOT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48059","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48059","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48060","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"80ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48061","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"81ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48062","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"82ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48063","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"83ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48064","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"84ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48065","DeliveryCity":"ROMEO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48065","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"85ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48066","DeliveryCity":"ROSEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48066","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"86ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48067","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"87ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48068","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"88ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48069","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"89ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48070","DeliveryCity":"HUNTINGTON WOODS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48070","PhysicalZip4":"1131","Enabled":"true","RowVersion":null},{"Id":"8aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48070","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48071","DeliveryCity":"MADISON HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48071","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"8ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48071","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48083","PhysicalZip4":"9005","Enabled":"true","RowVersion":null},{"Id":"8ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48072","DeliveryCity":"BERKLEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48072","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48072","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48073","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48083","PhysicalZip4":"9005","Enabled":"true","RowVersion":null},{"Id":"90ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48074","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"91ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48074","DeliveryCity":"SMITHS CREEK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48074","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"92ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48075","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"93ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48076","DeliveryCity":"LATHRUP VILLAGE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48076","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"94ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48076","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"95ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48079","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"96ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48079","DeliveryCity":"SAINT CLAIR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48079","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"97ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48080","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"98ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48081","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"99ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48082","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48083","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48084","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48085","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48086","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48088","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48089","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48090","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48091","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48092","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48093","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48094","DeliveryCity":"WASHINGTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48094","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48095","DeliveryCity":"WASHINGTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48094","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48096","DeliveryCity":"ROMEO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48065","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48097","DeliveryCity":"YALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48097","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48098","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48099","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aaed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48101","DeliveryCity":"ALLEN PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48101","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"abed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48103","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48104","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48105","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aeed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"afed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9484","Enabled":"true","RowVersion":null},{"Id":"b0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"2548","Enabled":"true","RowVersion":null},{"Id":"b1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48107","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48108","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48109","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48111","DeliveryCity":"BELLEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48111","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48112","DeliveryCity":"BELLEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48111","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48113","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48114","DeliveryCity":"BRIGHTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48116","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48115","DeliveryCity":"SALINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48176","PhysicalZip4":"9650","Enabled":"true","RowVersion":null},{"Id":"b9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48116","DeliveryCity":"BRIGHTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48116","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"baed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48117","DeliveryCity":"CARLETON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48117","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48118","DeliveryCity":"CHELSEA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48118","PhysicalZip4":"1642","Enabled":"true","RowVersion":null},{"Id":"bced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48120","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48121","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"beed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48122","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48122","DeliveryCity":"MELVINDALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48122","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48123","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"0001","Enabled":"Off","RowVersion":null},{"Id":"c1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48124","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48125","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48126","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48127","DeliveryCity":"DEARBORN HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48127","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48128","DeliveryCity":"DEARBORN HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48127","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48130","DeliveryCity":"DEXTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48130","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48131","DeliveryCity":"DUNDEE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48131","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48133","DeliveryCity":"ERIE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48133","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48134","DeliveryCity":"FLAT ROCK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48134","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"caed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48135","DeliveryCity":"GARDEN CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48135","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48136","DeliveryCity":"GARDEN CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48135","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48137","DeliveryCity":"GREGORY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48137","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48137","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"ceed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48138","DeliveryCity":"GROSSE ILE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48138","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48139","DeliveryCity":"HAMBURG","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48139","PhysicalZip4":"1006","Enabled":"true","RowVersion":null},{"Id":"d0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48140","DeliveryCity":"IDA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48140","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48140","DeliveryCity":"TEMPERANCE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48182","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48141","DeliveryCity":"INKSTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48141","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48143","DeliveryCity":"LAKELAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48143","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48144","DeliveryCity":"LAMBERTVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48144","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48145","DeliveryCity":"LA SALLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48145","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48146","DeliveryCity":"LINCOLN PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48146","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48150","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48151","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48152","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48152","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"daed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48153","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48152","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48154","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48157","DeliveryCity":"LUNA PIER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48157","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48158","DeliveryCity":"MANCHESTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48158","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"deed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48159","DeliveryCity":"MAYBEE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48159","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48160","DeliveryCity":"MILAN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48160","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48161","DeliveryCity":"MONROE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48161","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48162","DeliveryCity":"MONROE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48161","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48164","DeliveryCity":"NEW BOSTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48164","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48165","DeliveryCity":"NEW HUDSON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48165","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48166","DeliveryCity":"NEWPORT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48166","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48167","DeliveryCity":"NORTHVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48167","PhysicalZip4":"1544","Enabled":"true","RowVersion":null},{"Id":"e6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48167","DeliveryCity":"FARMINGTON HILLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48335","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48168","DeliveryCity":"FARMINGTON HILLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48335","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48169","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48170","DeliveryCity":"PLYMOUTH","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48170","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eaed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48170","DeliveryCity":"PLYMOUTH","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48170","PhysicalZip4":"1621","Enabled":"true","RowVersion":null},{"Id":"ebed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48173","DeliveryCity":"ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48173","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48174","DeliveryCity":"ROMULUS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48174","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48174","DeliveryCity":"TAYLOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48180","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eeed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48175","DeliveryCity":"NORTHVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48168","PhysicalZip4":"9492","Enabled":"true","RowVersion":null},{"Id":"efed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48176","DeliveryCity":"SALINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48176","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48177","DeliveryCity":"SAMARIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48177","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48178","DeliveryCity":"SOUTH LYON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48178","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48179","DeliveryCity":"ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48173","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48179","DeliveryCity":"SOUTH ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48179","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48180","DeliveryCity":"TAYLOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48180","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48182","DeliveryCity":"TEMPERANCE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48182","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48183","DeliveryCity":"TRENTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48183","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48184","DeliveryCity":"WAYNE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48184","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48184","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48185","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"faed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48186","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48187","DeliveryCity":"CANTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48187","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48188","DeliveryCity":"CANTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48187","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48189","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"feed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48189","DeliveryCity":"WHITMORE LAKE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48189","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"ffed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48190","DeliveryCity":"WHITTAKER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48190","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"00ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48191","DeliveryCity":"WILLIS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48191","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"01ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48191","DeliveryCity":"YPSILANTI","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48197","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"02ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48192","DeliveryCity":"SOUTHGATE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48195","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"03ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48192","DeliveryCity":"WYANDOTTE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48192","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"04ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48193","DeliveryCity":"RIVERVIEW","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48193","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":[{"Id":"37c802ce-506f-4d70-ae5c-ac828288c4c5","RateTableGuid":"00000000-0000-0000-0000-000000000000","ZoneName":"Zone A","IsActive":false,"ZonePricingRule":[{"Id":"4b6dbd95-a782-48b0-97a9-5b4506884c8f","ZoneGuid":"37c802ce-506f-4d70-ae5c-ac828288c4c5","RuleName":"New Pricing Rule","ValidStartDate":"2025-01-01","ValidEndDate":"2025-12-31","OnDays":"Monday,Wednesday,Tuesday,Friday,Thursday","ValidHoursStart":"08:00:00","ValidHoursEnd":"17:00:00","RequiresQuote":false,"MarkupType":"","MarkupCost":0,"MaxCost":200.00,"MinCost":17.00,"MaxOrderWeight":0,"MaxItemWeight":0,"WeightCostCollection":[{"Id":"772771a3-af54-4413-8407-a4c589041c5f","Weight":100,"Cost":5.75,"RowVersion":null},{"Id":"82637509-6e99-430e-b81c-c31f6569eef7","Weight":1000,"Cost":5.00,"RowVersion":null},{"Id":"057d441a-7cc4-464b-bcb4-2e0106f1f71a","Weight":2000,"Cost":4.00,"RowVersion":null},{"Id":"630adeb8-b785-44ba-a08f-1c4e9f9feb6a","Weight":5000,"Cost":3.50,"RowVersion":null}],"RowVersion":null}],"ZoneServiceArea":[{"Id":"47ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48001","DeliveryCity":"ALGONAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48001","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"48ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48002","DeliveryCity":"ALLENTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48002","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"49ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48002","DeliveryCity":"ARMADA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48005","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48003","DeliveryCity":"ALMONT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48003","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48003","DeliveryCity":"ALMONT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48003","PhysicalZip4":"1109","Enabled":"true","RowVersion":null},{"Id":"4ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48004","DeliveryCity":"ANCHORVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48004","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48005","DeliveryCity":"ARMADA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48005","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48006","DeliveryCity":"AVOCA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48006","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"4fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48006","DeliveryCity":"YALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48097","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"50ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48007","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"51ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48009","DeliveryCity":"BIRMINGHAM","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48012","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"52ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48012","DeliveryCity":"BIRMINGHAM","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48012","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"53ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48014","DeliveryCity":"CAPAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48014","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"54ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48015","DeliveryCity":"CENTER LINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48015","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"55ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48015","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"56ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48017","DeliveryCity":"CLAWSON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48017","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"57ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48021","DeliveryCity":"EASTPOINTE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48021","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"58ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48022","DeliveryCity":"CAPAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48014","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"59ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48022","DeliveryCity":"EMMETT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48022","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48023","DeliveryCity":"FAIR HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48023","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48025","DeliveryCity":"FRANKLIN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48025","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48025","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48026","DeliveryCity":"FRASER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48026","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48026","DeliveryCity":"ROSEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48066","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"5fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48027","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"60ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48027","DeliveryCity":"GOODELLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48027","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"61ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48028","DeliveryCity":"ALGONAC","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48001","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"62ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48028","DeliveryCity":"HARSENS ISLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48028","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"63ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48030","DeliveryCity":"HAZEL PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48030","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"64ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48032","DeliveryCity":"JEDDO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48032","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"65ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48033","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"66ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48034","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"67ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48035","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"68ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48036","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"69ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48037","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48038","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"6bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48038","DeliveryCity":"CLINTON TOWNSHIP","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48038","PhysicalZip4":"9997","Enabled":"true","RowVersion":null},{"Id":"6ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48039","DeliveryCity":"MARINE CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48039","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48040","DeliveryCity":"MARYSVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48040","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48040","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"6fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48041","DeliveryCity":"MEMPHIS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48041","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"70ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48042","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"71ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48043","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"72ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48044","DeliveryCity":"MACOMB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48044","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"73ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48045","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"74ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48045","DeliveryCity":"SELFRIDGE ANGB","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48045","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"75ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48046","DeliveryCity":"MOUNT CLEMENS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48046","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"76ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48047","DeliveryCity":"NEW BALTIMORE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48047","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"77ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48048","DeliveryCity":"NEW HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48048","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"78ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48049","DeliveryCity":"NORTH STREET","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48049","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"79ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48049","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48050","DeliveryCity":"NEW HAVEN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48048","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48051","DeliveryCity":"NEW BALTIMORE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48047","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48054","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48059","DeliveryCity":"FORT GRATIOT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48059","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48059","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"7fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48060","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"80ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48061","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"81ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48062","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"82ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48063","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"83ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48064","DeliveryCity":"RICHMOND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48062","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"84ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48065","DeliveryCity":"ROMEO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48065","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"85ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48066","DeliveryCity":"ROSEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48066","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"86ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48067","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"87ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48068","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"88ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48069","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"89ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48070","DeliveryCity":"HUNTINGTON WOODS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48070","PhysicalZip4":"1131","Enabled":"true","RowVersion":null},{"Id":"8aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48070","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48071","DeliveryCity":"MADISON HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48071","PhysicalZip4":"9991","Enabled":"true","RowVersion":null},{"Id":"8ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48071","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48083","PhysicalZip4":"9005","Enabled":"true","RowVersion":null},{"Id":"8ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48072","DeliveryCity":"BERKLEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48072","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48072","DeliveryCity":"ROYAL OAK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48068","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"8fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48073","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48083","PhysicalZip4":"9005","Enabled":"true","RowVersion":null},{"Id":"90ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48074","DeliveryCity":"PORT HURON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48061","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"91ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48074","DeliveryCity":"SMITHS CREEK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48074","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"92ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48075","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"93ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48076","DeliveryCity":"LATHRUP VILLAGE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48076","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"94ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48076","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"95ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48079","DeliveryCity":"CHINA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48054","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"96ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48079","DeliveryCity":"SAINT CLAIR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48079","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"97ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48080","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"98ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48081","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"99ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48082","DeliveryCity":"SAINT CLAIR SHORES","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48080","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9aed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48083","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9bed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48084","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9ced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48085","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9ded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48086","DeliveryCity":"SOUTHFIELD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48037","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9eed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48088","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"9fed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48089","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48090","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48091","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48092","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48093","DeliveryCity":"WARREN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48090","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48094","DeliveryCity":"WASHINGTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48094","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48095","DeliveryCity":"WASHINGTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48094","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48096","DeliveryCity":"ROMEO","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48065","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48097","DeliveryCity":"YALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48097","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48098","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"a9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48099","DeliveryCity":"TROY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48099","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aaed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48101","DeliveryCity":"ALLEN PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48101","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"abed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48103","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48104","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48105","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"aeed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"afed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9484","Enabled":"true","RowVersion":null},{"Id":"b0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48106","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"2548","Enabled":"true","RowVersion":null},{"Id":"b1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48107","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48108","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48104","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48109","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48103","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48111","DeliveryCity":"BELLEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48111","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48112","DeliveryCity":"BELLEVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48111","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48113","DeliveryCity":"ANN ARBOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48105","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48114","DeliveryCity":"BRIGHTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48116","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"b8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48115","DeliveryCity":"SALINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48176","PhysicalZip4":"9650","Enabled":"true","RowVersion":null},{"Id":"b9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48116","DeliveryCity":"BRIGHTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48116","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"baed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48117","DeliveryCity":"CARLETON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48117","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48118","DeliveryCity":"CHELSEA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48118","PhysicalZip4":"1642","Enabled":"true","RowVersion":null},{"Id":"bced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48120","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48121","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"beed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48122","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"bfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48122","DeliveryCity":"MELVINDALE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48122","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48123","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"0001","Enabled":"Off","RowVersion":null},{"Id":"c1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48124","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48125","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48124","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48126","DeliveryCity":"DEARBORN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48120","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48127","DeliveryCity":"DEARBORN HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48127","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48128","DeliveryCity":"DEARBORN HEIGHTS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48127","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48130","DeliveryCity":"DEXTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48130","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48131","DeliveryCity":"DUNDEE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48131","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48133","DeliveryCity":"ERIE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48133","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"c9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48134","DeliveryCity":"FLAT ROCK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48134","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"caed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48135","DeliveryCity":"GARDEN CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48135","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48136","DeliveryCity":"GARDEN CITY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48135","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48137","DeliveryCity":"GREGORY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48137","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48137","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"ceed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48138","DeliveryCity":"GROSSE ILE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48138","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"cfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48139","DeliveryCity":"HAMBURG","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48139","PhysicalZip4":"1006","Enabled":"true","RowVersion":null},{"Id":"d0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48140","DeliveryCity":"IDA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48140","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48140","DeliveryCity":"TEMPERANCE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48182","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48141","DeliveryCity":"INKSTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48141","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48143","DeliveryCity":"LAKELAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48143","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48144","DeliveryCity":"LAMBERTVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48144","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48145","DeliveryCity":"LA SALLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48145","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48146","DeliveryCity":"LINCOLN PARK","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48146","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48150","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48151","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"d9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48152","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48152","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"daed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48153","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48152","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48154","DeliveryCity":"LIVONIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48150","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48157","DeliveryCity":"LUNA PIER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48157","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48158","DeliveryCity":"MANCHESTER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48158","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"deed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48159","DeliveryCity":"MAYBEE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48159","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"dfed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48160","DeliveryCity":"MILAN","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48160","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48161","DeliveryCity":"MONROE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48161","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48162","DeliveryCity":"MONROE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48161","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48164","DeliveryCity":"NEW BOSTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48164","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48165","DeliveryCity":"NEW HUDSON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48165","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48166","DeliveryCity":"NEWPORT","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48166","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48167","DeliveryCity":"NORTHVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48167","PhysicalZip4":"1544","Enabled":"true","RowVersion":null},{"Id":"e6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48167","DeliveryCity":"FARMINGTON HILLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48335","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48168","DeliveryCity":"FARMINGTON HILLS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48335","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48169","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"e9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48170","DeliveryCity":"PLYMOUTH","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48170","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eaed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48170","DeliveryCity":"PLYMOUTH","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48170","PhysicalZip4":"1621","Enabled":"true","RowVersion":null},{"Id":"ebed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48173","DeliveryCity":"ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48173","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48174","DeliveryCity":"ROMULUS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48174","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48174","DeliveryCity":"TAYLOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48180","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"eeed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48175","DeliveryCity":"NORTHVILLE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48168","PhysicalZip4":"9492","Enabled":"true","RowVersion":null},{"Id":"efed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48176","DeliveryCity":"SALINE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48176","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f0ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48177","DeliveryCity":"SAMARIA","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48177","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f1ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48178","DeliveryCity":"SOUTH LYON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48178","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f2ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48179","DeliveryCity":"ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48173","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f3ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48179","DeliveryCity":"SOUTH ROCKWOOD","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48179","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f4ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48180","DeliveryCity":"TAYLOR","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48180","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f5ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48182","DeliveryCity":"TEMPERANCE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48182","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f6ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48183","DeliveryCity":"TRENTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48183","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f7ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48184","DeliveryCity":"WAYNE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48184","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f8ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48184","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"f9ed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48185","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"faed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48186","DeliveryCity":"WESTLAND","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48185","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fbed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48187","DeliveryCity":"CANTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48187","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fced5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48188","DeliveryCity":"CANTON","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48187","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"fded5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48189","DeliveryCity":"PINCKNEY","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48169","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"feed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48189","DeliveryCity":"WHITMORE LAKE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48189","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"ffed5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48190","DeliveryCity":"WHITTAKER","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48190","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"00ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48191","DeliveryCity":"WILLIS","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48191","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"01ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48191","DeliveryCity":"YPSILANTI","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48197","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"02ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48192","DeliveryCity":"SOUTHGATE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48195","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"03ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48192","DeliveryCity":"WYANDOTTE","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48192","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":"04ee5b64-4519-f011-8ad6-00155d010503","RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503","DeliveryZipCode":"48193","DeliveryCity":"RIVERVIEW","DeliveryState":"MI","OriginZipCode":null,"OriginCity":null,"OriginState":null,"RateType":null,"Zone":null,"PhysicalZip":"48193","PhysicalZip4":"9998","Enabled":"true","RowVersion":null},{"Id":

## Thoughts
The user is asking for validation of a large JSON string. I can suggest using `JsonSerializer.Deserialize<List<ZoneDTO>>(json)` to parse it. They might need to handle any formatting issues if the string is truncated, has duplication, or

## ASSISTANT
The JSON you’ve pasted is, at its core, a single top-level array of objects. Each object has two children collections (`ZonePricingRule` and `ZoneServiceArea`). To verify and consume it:

1. **Validate the JSON.**  
   Paste it into a validator (e.g. https://jsonlint.com/) to make sure there are no stray commas or unbalanced braces.  

2. **Deserialize directly into your target type.** For example, if your destination view-model has

   ```csharp
   public class ZoneDTO
   {
       public Guid Id { get; set; }
       public Guid RateTableGuid { get; set; }
       public string ZoneName { get; set; }
       public bool IsActive { get; set; }
       public List<ZonePricingRuleDTO> ZonePricingRule { get; set; }
       public List<ZoneServiceAreaDTO> ZoneServiceArea { get; set; }
   }
   ```
   
   then you can parse the entire string like this:

   ```csharp
   using System.Text.Json;

   var options = new JsonSerializerOptions
   {
       PropertyNameCaseInsensitive = true,
       // add converters if you need to handle dates or enums specially
   };

   try
   {
       // jsonString is your long JSON from the DB
       var zones = JsonSerializer.Deserialize<List<ZoneDTO>>(jsonString, options)
                   ?? new List<ZoneDTO>();

       // If your AutoMapper resolver expects ObservableCollection<ZoneDTO>:
       var ocZones = new ObservableCollection<ZoneDTO>(zones);
   }
   catch (JsonException ex)
   {
       // Log ex.Message
       // Fall back to an empty collection, or throw a user-friendly error
       var ocZones = new ObservableCollection<ZoneDTO>();
   }
   ```

3. **Hook into AutoMapper** with the resolver we showed earlier:

   ```csharp
   CreateMap<RateTableEntity, RateTableDto>()
     .ForMember(dest => dest.Zones,
                opt => opt.MapFrom<RateTableZoneJsonResolver>());
   ```
   
   Where `RateTableZoneJsonResolver` is:

   ```csharp
   public class RateTableZoneJsonResolver
     : IValueResolver<RateTableEntity, RateTableDto, ObservableCollection<ZoneDTO>>
   {
       public ObservableCollection<ZoneDTO> Resolve(
         RateTableEntity src, RateTableDto dst, ObservableCollection<ZoneDTO> _, ResolutionContext ctx)
       {
           if (string.IsNullOrWhiteSpace(src.ZoneJson))
               return new ObservableCollection<ZoneDTO>();

           try
           {
               var list = JsonSerializer.Deserialize<List<ZoneDTO>>(src.ZoneJson, 
                                new JsonSerializerOptions { PropertyNameCaseInsensitive = true })
                          ?? new List<ZoneDTO>();
               return new ObservableCollection<ZoneDTO>(list);
           }
           catch (JsonException)
           {
               return new ObservableCollection<ZoneDTO>();
           }
       }
   }
   ```

---

#### Common pitfalls when JSON “can’t be converted”

- **Trailing commas** or **extra characters** after the array.  
- A **mismatched type** (e.g. your DTO has an `int` but JSON has `"200.00"`).  
- **Nested objects** not matching your property names or types exactly.

**Next steps:**

1. Paste your JSON into a linter to confirm it’s valid.  
2. Ensure your `ZoneDTO`, `ZonePricingRuleDTO` and `ZoneServiceAreaDTO` match the JSON schema (all GUIDs, dates, booleans, etc.).  
3. Plug it into the try/catch-wrapped deserialization above and step through in the debugger to see exactly where it fails.

## USER
what do you see wrong here?  remember im storing json as as string field. "[{\"Id\":\"37c802ce-506f-4d70-ae5c-ac828288c4c5\",\"RateTableGuid\":\"00000000-0000-0000-0000-000000000000\",\"ZoneName\":\"Zone A\",\"IsActive\":false,\"ZonePricingRule\":[{\"Id\":\"4b6dbd95-a782-48b0-97a9-5b4506884c8f\",\"ZoneGuid\":\"37c802ce-506f-4d70-ae5c-ac828288c4c5\",\"RuleName\":\"New Pricing Rule\",\"ValidStartDate\":\"2025-01-01\",\"ValidEndDate\":\"2025-12-31\",\"OnDays\":\"Monday,Wednesday,Tuesday,Friday,Thursday\",\"ValidHoursStart\":\"08:00:00\",\"ValidHoursEnd\":\"17:00:00\",\"RequiresQuote\":false,\"MarkupType\":\"\",\"MarkupCost\":0,\"MaxCost\":200.00,\"MinCost\":17.00,\"MaxOrderWeight\":0,\"MaxItemWeight\":0,\"WeightCostCollection\":[{\"Id\":\"772771a3-af54-4413-8407-a4c589041c5f\",\"Weight\":100,\"Cost\":5.75,\"RowVersion\":null},{\"Id\":\"82637509-6e99-430e-b81c-c31f6569eef7\",\"Weight\":1000,\"Cost\":5.00,\"RowVersion\":null},{\"Id\":\"057d441a-7cc4-464b-bcb4-2e0106f1f71a\",\"Weight\":2000,\"Cost\":4.00,\"RowVersion\":null},{\"Id\":\"630adeb8-b785-44ba-a08f-1c4e9f9feb6a\",\"Weight\":5000,\"Cost\":3.50,\"RowVersion\":null}],\"RowVersion\":null}],\"ZoneServiceArea\":[{\"Id\":\"47ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48001\",\"DeliveryCity\":\"ALGONAC\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48001\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"48ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48002\",\"DeliveryCity\":\"ALLENTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48002\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"49ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48002\",\"DeliveryCity\":\"ARMADA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48005\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"4aed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48003\",\"DeliveryCity\":\"ALMONT\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48003\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"4bed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48003\",\"DeliveryCity\":\"ALMONT\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48003\",\"PhysicalZip4\":\"1109\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"4ced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48004\",\"DeliveryCity\":\"ANCHORVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48004\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"4ded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48005\",\"DeliveryCity\":\"ARMADA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48005\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"4eed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48006\",\"DeliveryCity\":\"AVOCA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48006\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"4fed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48006\",\"DeliveryCity\":\"YALE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48097\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"50ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48007\",\"DeliveryCity\":\"TROY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48099\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"51ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48009\",\"DeliveryCity\":\"BIRMINGHAM\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48012\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"52ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48012\",\"DeliveryCity\":\"BIRMINGHAM\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48012\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"53ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48014\",\"DeliveryCity\":\"CAPAC\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48014\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"54ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48015\",\"DeliveryCity\":\"CENTER LINE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48015\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"55ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48015\",\"DeliveryCity\":\"WARREN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48090\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"56ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48017\",\"DeliveryCity\":\"CLAWSON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48017\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"57ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48021\",\"DeliveryCity\":\"EASTPOINTE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48021\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"58ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48022\",\"DeliveryCity\":\"CAPAC\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48014\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"59ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48022\",\"DeliveryCity\":\"EMMETT\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48022\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"5aed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48023\",\"DeliveryCity\":\"FAIR HAVEN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48023\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"5bed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48025\",\"DeliveryCity\":\"FRANKLIN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48025\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"5ced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48025\",\"DeliveryCity\":\"SOUTHFIELD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48037\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"5ded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48026\",\"DeliveryCity\":\"FRASER\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48026\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"5eed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48026\",\"DeliveryCity\":\"ROSEVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48066\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"5fed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48027\",\"DeliveryCity\":\"CHINA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48054\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"60ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48027\",\"DeliveryCity\":\"GOODELLS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48027\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"61ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48028\",\"DeliveryCity\":\"ALGONAC\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48001\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"62ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48028\",\"DeliveryCity\":\"HARSENS ISLAND\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48028\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"63ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48030\",\"DeliveryCity\":\"HAZEL PARK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48030\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"64ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48032\",\"DeliveryCity\":\"JEDDO\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48032\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"65ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48033\",\"DeliveryCity\":\"SOUTHFIELD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48037\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"66ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48034\",\"DeliveryCity\":\"SOUTHFIELD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48037\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"67ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48035\",\"DeliveryCity\":\"MOUNT CLEMENS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48046\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"68ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48036\",\"DeliveryCity\":\"MOUNT CLEMENS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48046\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"69ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48037\",\"DeliveryCity\":\"SOUTHFIELD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48037\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"6aed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48038\",\"DeliveryCity\":\"MACOMB\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48044\",\"PhysicalZip4\":\"9991\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"6bed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48038\",\"DeliveryCity\":\"CLINTON TOWNSHIP\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48038\",\"PhysicalZip4\":\"9997\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"6ced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48039\",\"DeliveryCity\":\"MARINE CITY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48039\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"6ded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48040\",\"DeliveryCity\":\"MARYSVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48040\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"6eed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48040\",\"DeliveryCity\":\"PORT HURON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48061\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"6fed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48041\",\"DeliveryCity\":\"MEMPHIS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48041\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"70ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48042\",\"DeliveryCity\":\"MACOMB\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48044\",\"PhysicalZip4\":\"9991\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"71ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48043\",\"DeliveryCity\":\"MOUNT CLEMENS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48046\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"72ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48044\",\"DeliveryCity\":\"MACOMB\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48044\",\"PhysicalZip4\":\"9991\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"73ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48045\",\"DeliveryCity\":\"MOUNT CLEMENS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48046\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"74ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48045\",\"DeliveryCity\":\"SELFRIDGE ANGB\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48045\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"75ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48046\",\"DeliveryCity\":\"MOUNT CLEMENS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48046\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"76ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48047\",\"DeliveryCity\":\"NEW BALTIMORE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48047\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"77ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48048\",\"DeliveryCity\":\"NEW HAVEN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48048\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"78ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48049\",\"DeliveryCity\":\"NORTH STREET\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48049\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"79ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48049\",\"DeliveryCity\":\"PORT HURON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48061\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"7aed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48050\",\"DeliveryCity\":\"NEW HAVEN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48048\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"7bed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48051\",\"DeliveryCity\":\"NEW BALTIMORE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48047\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"7ced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48054\",\"DeliveryCity\":\"CHINA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48054\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"7ded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48059\",\"DeliveryCity\":\"FORT GRATIOT\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48059\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"7eed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48059\",\"DeliveryCity\":\"PORT HURON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48061\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"7fed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48060\",\"DeliveryCity\":\"PORT HURON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48061\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"80ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48061\",\"DeliveryCity\":\"PORT HURON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48061\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"81ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48062\",\"DeliveryCity\":\"RICHMOND\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48062\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"82ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48063\",\"DeliveryCity\":\"RICHMOND\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48062\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"83ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48064\",\"DeliveryCity\":\"RICHMOND\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48062\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"84ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48065\",\"DeliveryCity\":\"ROMEO\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48065\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"85ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48066\",\"DeliveryCity\":\"ROSEVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48066\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"86ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48067\",\"DeliveryCity\":\"ROYAL OAK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48068\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"87ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48068\",\"DeliveryCity\":\"ROYAL OAK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48068\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"88ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48069\",\"DeliveryCity\":\"ROYAL OAK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48068\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"89ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48070\",\"DeliveryCity\":\"HUNTINGTON WOODS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48070\",\"PhysicalZip4\":\"1131\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"8aed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48070\",\"DeliveryCity\":\"ROYAL OAK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48068\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"8bed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48071\",\"DeliveryCity\":\"MADISON HEIGHTS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48071\",\"PhysicalZip4\":\"9991\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"8ced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48071\",\"DeliveryCity\":\"TROY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48083\",\"PhysicalZip4\":\"9005\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"8ded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48072\",\"DeliveryCity\":\"BERKLEY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48072\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"8eed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48072\",\"DeliveryCity\":\"ROYAL OAK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48068\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"8fed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48073\",\"DeliveryCity\":\"TROY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48083\",\"PhysicalZip4\":\"9005\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"90ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48074\",\"DeliveryCity\":\"PORT HURON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48061\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"91ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48074\",\"DeliveryCity\":\"SMITHS CREEK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48074\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"92ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48075\",\"DeliveryCity\":\"SOUTHFIELD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48037\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"93ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48076\",\"DeliveryCity\":\"LATHRUP VILLAGE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48076\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"94ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48076\",\"DeliveryCity\":\"SOUTHFIELD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48037\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"95ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48079\",\"DeliveryCity\":\"CHINA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48054\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"96ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48079\",\"DeliveryCity\":\"SAINT CLAIR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48079\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"97ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48080\",\"DeliveryCity\":\"SAINT CLAIR SHORES\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48080\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"98ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48081\",\"DeliveryCity\":\"SAINT CLAIR SHORES\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48080\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"99ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48082\",\"DeliveryCity\":\"SAINT CLAIR SHORES\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48080\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"9aed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48083\",\"DeliveryCity\":\"TROY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48099\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"9bed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48084\",\"DeliveryCity\":\"TROY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48099\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"9ced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48085\",\"DeliveryCity\":\"TROY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48099\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"9ded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48086\",\"DeliveryCity\":\"SOUTHFIELD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48037\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"9eed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48088\",\"DeliveryCity\":\"WARREN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48090\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"9fed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48089\",\"DeliveryCity\":\"WARREN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48090\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a0ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48090\",\"DeliveryCity\":\"WARREN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48090\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a1ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48091\",\"DeliveryCity\":\"WARREN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48090\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a2ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48092\",\"DeliveryCity\":\"WARREN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48090\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a3ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48093\",\"DeliveryCity\":\"WARREN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48090\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a4ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48094\",\"DeliveryCity\":\"WASHINGTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48094\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a5ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48095\",\"DeliveryCity\":\"WASHINGTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48094\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a6ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48096\",\"DeliveryCity\":\"ROMEO\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48065\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a7ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48097\",\"DeliveryCity\":\"YALE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48097\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a8ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48098\",\"DeliveryCity\":\"TROY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48099\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"a9ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48099\",\"DeliveryCity\":\"TROY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48099\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"aaed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48101\",\"DeliveryCity\":\"ALLEN PARK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48101\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"abed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48103\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48103\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"aced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48104\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48103\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"aded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48105\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48105\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"aeed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48106\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48103\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"afed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48106\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48105\",\"PhysicalZip4\":\"9484\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b0ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48106\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48104\",\"PhysicalZip4\":\"2548\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b1ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48107\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48104\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b2ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48108\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48104\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b3ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48109\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48103\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b4ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48111\",\"DeliveryCity\":\"BELLEVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48111\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b5ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48112\",\"DeliveryCity\":\"BELLEVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48111\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b6ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48113\",\"DeliveryCity\":\"ANN ARBOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48105\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b7ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48114\",\"DeliveryCity\":\"BRIGHTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48116\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b8ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48115\",\"DeliveryCity\":\"SALINE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48176\",\"PhysicalZip4\":\"9650\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"b9ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48116\",\"DeliveryCity\":\"BRIGHTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48116\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"baed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48117\",\"DeliveryCity\":\"CARLETON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48117\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"bbed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48118\",\"DeliveryCity\":\"CHELSEA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48118\",\"PhysicalZip4\":\"1642\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"bced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48120\",\"DeliveryCity\":\"DEARBORN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48120\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"bded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48121\",\"DeliveryCity\":\"DEARBORN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48120\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"beed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48122\",\"DeliveryCity\":\"DEARBORN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48120\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"bfed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48122\",\"DeliveryCity\":\"MELVINDALE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48122\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c0ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48123\",\"DeliveryCity\":\"DEARBORN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48124\",\"PhysicalZip4\":\"0001\",\"Enabled\":\"Off\",\"RowVersion\":null},{\"Id\":\"c1ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48124\",\"DeliveryCity\":\"DEARBORN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48124\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c2ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48125\",\"DeliveryCity\":\"DEARBORN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48124\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c3ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48126\",\"DeliveryCity\":\"DEARBORN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48120\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c4ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48127\",\"DeliveryCity\":\"DEARBORN HEIGHTS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48127\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c5ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48128\",\"DeliveryCity\":\"DEARBORN HEIGHTS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48127\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c6ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48130\",\"DeliveryCity\":\"DEXTER\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48130\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c7ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48131\",\"DeliveryCity\":\"DUNDEE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48131\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c8ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48133\",\"DeliveryCity\":\"ERIE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48133\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"c9ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48134\",\"DeliveryCity\":\"FLAT ROCK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48134\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"caed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48135\",\"DeliveryCity\":\"GARDEN CITY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48135\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"cbed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48136\",\"DeliveryCity\":\"GARDEN CITY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48135\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"cced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48137\",\"DeliveryCity\":\"GREGORY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48137\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"cded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48137\",\"DeliveryCity\":\"PINCKNEY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48169\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"ceed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48138\",\"DeliveryCity\":\"GROSSE ILE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48138\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"cfed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48139\",\"DeliveryCity\":\"HAMBURG\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48139\",\"PhysicalZip4\":\"1006\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d0ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48140\",\"DeliveryCity\":\"IDA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48140\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d1ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48140\",\"DeliveryCity\":\"TEMPERANCE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48182\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d2ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48141\",\"DeliveryCity\":\"INKSTER\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48141\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d3ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48143\",\"DeliveryCity\":\"LAKELAND\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48143\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d4ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48144\",\"DeliveryCity\":\"LAMBERTVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48144\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d5ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48145\",\"DeliveryCity\":\"LA SALLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48145\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d6ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48146\",\"DeliveryCity\":\"LINCOLN PARK\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48146\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d7ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48150\",\"DeliveryCity\":\"LIVONIA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48150\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d8ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48151\",\"DeliveryCity\":\"LIVONIA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48150\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"d9ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48152\",\"DeliveryCity\":\"LIVONIA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48152\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"daed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48153\",\"DeliveryCity\":\"LIVONIA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48152\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"dbed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48154\",\"DeliveryCity\":\"LIVONIA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48150\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"dced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48157\",\"DeliveryCity\":\"LUNA PIER\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48157\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"dded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48158\",\"DeliveryCity\":\"MANCHESTER\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48158\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"deed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48159\",\"DeliveryCity\":\"MAYBEE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48159\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"dfed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48160\",\"DeliveryCity\":\"MILAN\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48160\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e0ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48161\",\"DeliveryCity\":\"MONROE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48161\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e1ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48162\",\"DeliveryCity\":\"MONROE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48161\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e2ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48164\",\"DeliveryCity\":\"NEW BOSTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48164\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e3ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48165\",\"DeliveryCity\":\"NEW HUDSON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48165\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e4ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48166\",\"DeliveryCity\":\"NEWPORT\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48166\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e5ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48167\",\"DeliveryCity\":\"NORTHVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48167\",\"PhysicalZip4\":\"1544\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e6ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48167\",\"DeliveryCity\":\"FARMINGTON HILLS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48335\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e7ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48168\",\"DeliveryCity\":\"FARMINGTON HILLS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48335\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e8ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48169\",\"DeliveryCity\":\"PINCKNEY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48169\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"e9ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48170\",\"DeliveryCity\":\"PLYMOUTH\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48170\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"eaed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48170\",\"DeliveryCity\":\"PLYMOUTH\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48170\",\"PhysicalZip4\":\"1621\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"ebed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48173\",\"DeliveryCity\":\"ROCKWOOD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48173\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"eced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48174\",\"DeliveryCity\":\"ROMULUS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48174\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"eded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48174\",\"DeliveryCity\":\"TAYLOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48180\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"eeed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48175\",\"DeliveryCity\":\"NORTHVILLE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48168\",\"PhysicalZip4\":\"9492\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"efed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48176\",\"DeliveryCity\":\"SALINE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48176\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f0ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48177\",\"DeliveryCity\":\"SAMARIA\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48177\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f1ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48178\",\"DeliveryCity\":\"SOUTH LYON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48178\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f2ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48179\",\"DeliveryCity\":\"ROCKWOOD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48173\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f3ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48179\",\"DeliveryCity\":\"SOUTH ROCKWOOD\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48179\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f4ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48180\",\"DeliveryCity\":\"TAYLOR\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48180\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f5ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48182\",\"DeliveryCity\":\"TEMPERANCE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48182\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f6ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48183\",\"DeliveryCity\":\"TRENTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48183\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f7ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48184\",\"DeliveryCity\":\"WAYNE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48184\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f8ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48184\",\"DeliveryCity\":\"WESTLAND\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48185\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"f9ed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48185\",\"DeliveryCity\":\"WESTLAND\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48185\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"faed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48186\",\"DeliveryCity\":\"WESTLAND\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48185\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"fbed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48187\",\"DeliveryCity\":\"CANTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48187\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"fced5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48188\",\"DeliveryCity\":\"CANTON\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48187\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"fded5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48189\",\"DeliveryCity\":\"PINCKNEY\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48169\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"feed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48189\",\"DeliveryCity\":\"WHITMORE LAKE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48189\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"ffed5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48190\",\"DeliveryCity\":\"WHITTAKER\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48190\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"00ee5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48191\",\"DeliveryCity\":\"WILLIS\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48191\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"01ee5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48191\",\"DeliveryCity\":\"YPSILANTI\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48197\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"02ee5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48192\",\"DeliveryCity\":\"SOUTHGATE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48195\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"03ee5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48192\",\"DeliveryCity\":\"WYANDOTTE\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48192\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":\"04ee5b64-4519-f011-8ad6-00155d010503\",\"RateTableGuid\":\"3fd962ae-c526-f011-8ad7-00155d010503\",\"DeliveryZipCode\":\"48193\",\"DeliveryCity\":\"RIVERVIEW\",\"DeliveryState\":\"MI\",\"OriginZipCode\":null,\"OriginCity\":null,\"OriginState\":null,\"RateType\":null,\"Zone\":null,\"PhysicalZip\":\"48193\",\"PhysicalZip4\":\"9998\",\"Enabled\":\"true\",\"RowVersion\":null},{\"Id\":"

## Thoughts
From what I'm gathering, you're storing a JSON string as a string field. The main issue seems to be that some "boolean" fields are inconsistently formatted. For instance, `IsActive:false` is correctly a boolean, but `Enabled:"true"` should be a boolean (`true`, not `"true"` as a string). As for `MaxCost:200.00`, the trailing zero is allowed in JSON numerics, so it’s valid. But it’s good to check if your system expects stricter formatting. I'll focus on fixing the types and clearing up inconsistencies.
It looks like there are a few data issues in this JSON string. First, the boolean values like `"Enabled":"true"` are stored as strings, but they should be booleans. Also, `"Enabled":"Off"` is problematic because "Off" isn't a standard boolean value—this should be `false`.

Secondly, the `RateTableGuid` in the parent object doesn't match the one used in the `ZoneServiceArea` entries, which is likely a key issue or a data mismatch. The `RateTableGuid` in the parent should match that in the children, so the inconsistency needs fixing.
The main issue here is that the `Enabled` property is stored as a string (e.g., `"Off"`) instead of a boolean (`false`). Additionally, the `RateTableGuid` in the parent object is incorrectly set to all zeros instead of matching the child `RateTableGuid`. This inconsistency could cause issues. Also, the JSON appears to be truncated, missing closing brackets, causing a parse error. Another thing to check: the `OnDays` property’s ordering of days seems odd, though not necessarily critical. Most importantly, the `Enabled` field needs to be a boolean.

## ASSISTANT
A few things jumped out at me:

1. **Your JSON is being truncated.**  
   If you look at the very end of the dump, it cuts off in the middle of a service-area object and never closes the `]}`. That almost certainly means your string column wasn’t big enough, so SQL pushed only the first ~4 KB (or whatever your limit is) into the field and chopped the rest off.  

2. **Type mismatches on `Enabled`.**  
   You’ve got  
   ```json
   "IsActive": false,            ← correct, a Boolean  
   …  
   "Enabled": "true",            ← incorrect, a string  
   …  
   "Enabled": "Off",             ← definitely wrong
   ```  
   If you intend for those flags to be Boolean, they need to be unquoted `true`/`false`, not `"true"`/`"Off"`.

3. **Mismatched GUIDs on the service-area entries.**  
   Your parent object has  
   ```json
   "RateTableGuid":"00000000-0000-0000-0000-000000000000"
   ```  
   but every entry in `ZoneServiceArea` carries  
   ```json
   "RateTableGuid":"3fd962ae-c526-f011-8ad7-00155d010503"
   ```  
   That doesn’t line up—either the parent has the wrong GUID, or the children do.

---

**What to do next:**

1. **Increase your column size** (e.g. to `NVARCHAR(MAX)`) so the JSON doesn’t get silently chopped off.  
2. **Fix your booleans**—unquote `true`/`false` (and replace `"Off"` with `false`).  
3. **Make sure your GUIDs actually match** where they’re supposed to.  

With those in place your JSON should round-trip cleanly.

## USER
RateTableZoneJson = '(new System.Collections.Generic.ICollectionDebugView<RateTableEntity>(responseData).Items[0]).RateTableZoneJson' threw an exception of type 'System.Text.Json.JsonException'

## Thoughts
The user is dealing with a `JsonException` from `System.Text.Json`, which likely stems from malformed JSON. Common issues might be truncation – for instance, missing closing brackets or a trailing comma. Also, the "Enabled":"Off" part won't work if the target property is a boolean, as "Off" is invalid. The "OnDays" field, expressed as a comma-separated string, might need to be an array instead. The core problem seems to be the invalid format, triggering the exception when loading into the C# object.

## ASSISTANT
The reason you’re getting a `JsonException` is that the string you’re feeding into the serializer is not valid, complete JSON. In your dump above it:

1. **Cuts off mid‐object**, with no closing `]}` (or even a closing `"` for the last field).  
2. Contains invalid tokens for booleans — e.g. `"Enabled":"Off"` and `"Enabled":"true"` are strings, not JSON `true`/`false`.  

When System.Text.Json hits that dangling `"Id":…` at the end, or the `"Off"` token where it expected a Boolean, it bails with a parse error.  

**Fixes:**

- Make your column wide enough (e.g. `NVARCHAR(MAX)`) so nothing is truncated.  
- Change your `"Enabled":"true"` / `"Off"` to real JSON booleans (`"Enabled": true` / `"Enabled": false`).  
- Re-export and you’ll get a syntactically valid, complete JSON string that System.Text.Json can digest without error.

## USER
here is my raw data stored int he data

## Thoughts
Okay, I need to list the directory and show the first 1000 characters, though it's truncated. It sounds like I need the full, nested structure, but the whole thing is too big to print. I guess I’ll focus on inspecting the start of it to get a sense of the files. It's tricky to manage large amounts of data like this without printing every single detail, but I’ll try to focus on the most essential parts.

## Thoughts
I need to list the directory, but I can only see the first 1000 characters—it's too truncated. Full inspection would be massive! The notebook lost connection, likely due to the file size. Instead of printing everything, I could try searching for specific patterns in the file. Searching for something like `"RateTableZoneJson":` might be a good starting point. I'll use a search function to handle the contents, focusing on those relevant areas.

## Thoughts
It looks like the user is storing JSON as a string in the database, which causes issues when trying to deserialize it. Since the raw data doesn't seem to be valid JSON, that's likely leading to the exception when calling `System.Text.Json.JsonSerializer.Deserialize`. The user's query mentions an exception with the `JsonSerializer`, so I need to help identify why the JSON is invalid. I'll search for the `"RateTableZoneJson":` pattern in the data and inspect its structure closely.
Looks like the key issue is that the `RateTableZoneJson` is double-encoded. The string has been stored with extra escape characters and quotes around the JSON, which causes issues when calling `JsonSerializer.Deserialize`. The user tried to deserialize it directly without removing the additional encoding. To fix this, the user should first deserialize it as a string and then deserialize that string into the proper object. The extra quotes and escapes are the root cause of the `JsonException`.
It seems the primary issue is that the `RateTableZoneJson` field stores the JSON as a string with quotes and escape sequences, which leads to problems when trying to deserialize it. The string literal representation includes backslashes for escaping, which causes the `JsonSerializer` to misinterpret it. Additionally, JSON contains inconsistencies like using quotes around boolean values (e.g., `"Enabled":"true"`) when they should be unquoted. The solution is to unescape the string content, adjust the data types, or fix the JSON to properly match boolean values.

## ASSISTANT
The problem isn’t your deserializer at all, it’s the JSON you’re feeding it.  A couple of things jump out:

1. **You’re storing the JSON as a _string_ literal**, so by the time you hand it to `JsonSerializer.Deserialize`, it still has the surrounding quotes and escape‐sequences (e.g. `"[{ … }]"`), not the raw array.  
2. **Inside that string, your `Enabled` field is a quoted string** (`"Enabled":"true"` or even `"Enabled":"Off"`), but in your C# model you almost certainly have it typed as a `bool`.  System.Text.Json will choke trying to convert `"true"` (a JSON _string_) into a Boolean, and it can’t map `"Off"` at all to `false` fileciteturn2file6L1-L1.  

Contrast that with your other Boolean fields, which are correctly unquoted:

```json
"IsActive": false
```

(Note the absence of quotes around `false`.) fileciteturn2file0L1-L1

---

### How to fix

1. **Un-escape the JSON string** you’ve stored. If you’ve literally stored the payload of `JsonSerializer.Serialize(obj)`, you need to:
   ```csharp
   // assuming rawJson is what you pulled from the DB:
   var unescaped = JsonSerializer.Deserialize<string>(rawJson);
   ```
2. **Deserialize that into your object graph**:
   ```csharp
   var zones = JsonSerializer.Deserialize<List<RateTableZone>>(unescaped);
   ```
3. **Normalize the `Enabled` values** to actual booleans in your JSON (or change your model to accept a `string` and then map it), e.g.:
   ```json
   "Enabled": true
   ```
   instead of
   ```json
   "Enabled": "true"
   ```
   and never `"Off"` – use `false`.

Once you’ve un-escaped the outer quotes and corrected the `Enabled` types, `System.Text.Json` will happily parse the array.

## USER
how should the data look. this was working.

## Thoughts
The user is asking how correct data should look. I believe they want to see an example of proper JSON structure before storing it. To clarify: it should be an array of objects, with boolean fields correctly formatted (like "Enabled": true), and no quotes wrapping the JSON string itself. For example:  
[ { "Id": "...", "RateTableGuid": "...", "ZoneServiceArea": [ { "Id": "...", "Enabled": true } ] } ]  
No further quotes around the entire string or string literals like JsonSerializerSerialize. Just raw JSON.

## ASSISTANT
Your JSON column needs to contain _raw_ JSON (an array of objects), not a _stringified_ JSON literal, and any Boolean fields must really be booleans. For example, instead of storing this (note the outer quotes and `“Enabled”: "true"`):  

```sql
-- bad: this is a string containing escaped JSON
INSERT INTO YourTable (RateTableZoneJson) VALUES (
  '"[{\\"Id\\":\\"37c802ce-…\\",\\"IsActive\\":false,…,\\"Enabled\\":\\"true\\",…}]"'
);
```

you should store something like this:

```sql
-- good: raw JSON array, with true/false unquoted
INSERT INTO YourTable (RateTableZoneJson) VALUES (
  '[
     {
       "Id": "37c802ce-506f-4d70-ae5c-ac828288c4c5",
       "RateTableGuid": "00000000-0000-0000-0000-000000000000",
       "ZoneName": "Zone A",
       "IsActive": false,
       "ZonePricingRule": [
         {
           "Id": "4b6dbd95-a782-48b0-97a9-5b4506884c8f",
           "ZoneGuid": "37c802ce-506f-4d70-ae5c-ac828288c4c5",
           "RuleName": "New Pricing Rule",
           "ValidStartDate": "2025-01-01",
           "ValidEndDate": "2025-12-31",
           "OnDays": "Monday,Wednesday,Tuesday,Friday,Thursday",
           "ValidHoursStart": "08:00:00",
           "ValidHoursEnd": "17:00:00",
           "RequiresQuote": false,
           "MarkupType": "",
           "MarkupCost": 0,
           "MaxCost": 200.00,
           "MinCost": 17.00,
           "MaxOrderWeight": 0,
           "MaxItemWeight": 0,
           "WeightCostCollection": [
             { "Id": "772771a3-af54-4413-8407-a4c589041c5f", "Weight": 100,  "Cost": 5.75, "RowVersion": null },
             { "Id": "82637509-6e99-430e-b81c-c31f6569eef7", "Weight": 1000, "Cost": 5.00, "RowVersion": null },
             …
           ],
           "RowVersion": null
         }
       ],
       "ZoneServiceArea": [
         {
           "Id": "47ed5b64-4519-f011-8ad6-00155d010503",
           "RateTableGuid": "3fd962ae-c526-f011-8ad7-00155d010503",
           "DeliveryZipCode": "48001",
           "DeliveryCity": "ALGONAC",
           "DeliveryState": "MI",
           "OriginZipCode": null,
           "PhysicalZip": "48001",
           "PhysicalZip4": "9998",
           "Enabled": true,
           "RowVersion": null
         },
         {
           "Id": "48ed5b64-4519-f011-8ad6-00155d010503",
           …
           "Enabled": false
         }
       ]
     }
   ]'
);
```

### Key points

- **No wrapping quotes** around the entire JSON.
- **No back-slash escapes** (you’re storing the JSON, not a C# string literal).
- Boolean fields like `Enabled` (and `IsActive`, `RequiresQuote`, etc.) must be `true` or `false` (unquoted), not `"true"`/`"false"` or `"Off"`.
- Dates and numbers remain unquoted if your model expects them as `DateTime`, `decimal`, etc.

With data in that shape, `JsonSerializer.Deserialize<List<YourDto>>(rawJson)` will succeed.

## USER
getting this out of nowhere System.ObjectDisposedException

  HResult=0x80131622

  Message=Cannot access a disposed object.

Object name: 'IServiceProvider'.

  Source=Microsoft.Extensions.DependencyInjection

  StackTrace:

   at Microsoft.Extensions.DependencyInjection.ServiceLookup.ThrowHelper.ThrowObjectDisposedException()

   at Microsoft.Extensions.DependencyInjection.ServiceLookup.ServiceProviderEngineScope.GetService(Type serviceType)

   at Microsoft.Extensions.DependencyInjection.ServiceProviderServiceExtensions.GetRequiredService(IServiceProvider provider, Type serviceType)

   at Microsoft.Extensions.DependencyInjection.ServiceProviderServiceExtensions.GetRequiredService[T](IServiceProvider provider)

   at Program.<>c__DisplayClass0_1.<<Main>$>b__45() in D:\Deployment\LogistixServerAPIV2\Logistix.Server.API\Program.cs:line 98

   at Logistix.Server.API.Logging.Sinks.SignalRTelemetrySink.Emit(LogEvent logEvent) in D:\Deployment\LogistixServerAPIV2\Logistix.Server.API\Logging\Sinks\SignalRTelemetrySink.cs:line 43

   at Serilog.Core.Sinks.SafeAggregateSink.Emit(LogEvent logEvent)


## Thoughts
The issue likely stems from premature disposal of the ServiceProvider after host shutdown. In .NET Generic Host, once `host.Run()` completes, the ServiceProvider is disposed, but background operations like logging sinks may still try to access services. A solution could be to configure the logger before building the host or to dispose of the logging sinks before the host is disposed. Alternatively, capturing `IHubContext` during the sink's creation rather than on every event might help.


## ASSISTANT
This error is telling you that by the time your sink’s `Emit` method runs, the `IServiceProvider` you captured has already been disposed – so any call to  
```csharp
_serviceProvider.GetRequiredService<…>()
```  
will blow up with an `ObjectDisposedException`.

### Why this happens
1. **Host shutdown order**  
   When you call `host.Run()`, once the application is shutting down it will:
   - Stop listening
   - Dispose the IServiceProvider (all scoped/transient/singleton services)
   - Then dispose Serilog (and its sinks)  
   
   If your sink still tries to resolve services in its `Emit` after the provider has already been torn down, you get exactly this exception.

2. **Resolving on every log**  
   By calling `GetRequiredService<T>` inside `Emit`, you’re reaching back into the container every time you log.  Once the container is gone, that call fails.

---

## Two straightforward fixes

### 1. Resolve your HubContext (or any DI service) _once_ at sink construction
Instead of this:

```csharp
public class SignalRTelemetrySink : ILogEventSink
{
    private readonly IServiceProvider _serviceProvider;

    public SignalRTelemetrySink(IServiceProvider provider)
    {
        _serviceProvider = provider;
    }

    public void Emit(LogEvent logEvent)
    {
        // ❌ this will throw once the provider is disposed
        var hub = _serviceProvider.GetRequiredService<IHubContext<MyTelemetryHub>>();
        hub.Clients.All.SendAsync("log", logEvent.RenderMessage());
    }
}
```

Do this:

```csharp
public class SignalRTelemetrySink : ILogEventSink
{
    private readonly IHubContext<MyTelemetryHub> _hub;

    public SignalRTelemetrySink(IHubContext<MyTelemetryHub> hub)
    {
        _hub = hub;
    }

    public void Emit(LogEvent logEvent)
    {
        // ✅ never touches the IServiceProvider again
        _hub.Clients.All.SendAsync("log", logEvent.RenderMessage());
    }
}
```

And register it at startup via Serilog’s DI‐aware factory:

```csharp
Host.CreateDefaultBuilder(args)
    .UseSerilog((ctx, services, lc) => lc
        .WriteTo.Console()
        .WriteTo.Sink( 
            new SignalRTelemetrySink(
                services.GetRequiredService<IHubContext<MyTelemetryHub>>()
            )
        )
    )
    .ConfigureWebHostDefaults(webBuilder => { … })
    .Build()
    .Run();
```

### 2. Flush Serilog before disposing the host
If you really must resolve inside `Emit`, at least make sure Serilog gets torn down _before_ the DI container:

```csharp
try
{
    host.Run();
}
finally
{
    Log.CloseAndFlush();   // this will dispose all sinks now, while IServiceProvider is still live
}
```

---

### TL;DR

- **Don’t call** `GetRequiredService` inside your sink’s `Emit`—the provider will eventually be gone.
- **Inject and store** your `IHubContext<…>` (or any other service) once in the sink’s constructor.
- If you can’t refactor right away, ensure you call `Log.CloseAndFlush()` _before_ the host disposes its services so your sink still has a live service provider when it shuts down.

## USER
this is my prog  builder.Host.UseSerilog((context, services, configuration) =>

{

    configuration

    .WriteTo

    .Console()

    .WriteTo.File(

      Path.Combine(AppContext.BaseDirectory, "Logs", "log-.txt"),

      rollingInterval: RollingInterval.Day)

    .WriteTo

    .Sink(new SignalRTelemetrySink(

        () => 

            services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>(),

        () => 

            services.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>()

            )); 

});




## Thoughts
It looks like the user is using lambdas to defer resolution of `IHubContext<T>` services in their Serilog configuration. However, since the lambda evaluates when `Emit` is called, it can cause an issue when the provider is disposed. To fix this, I’ll suggest resolving the hub contexts during the creation of the `SignalRTelemetrySink`, either by directly resolving the hubs right when the sink is constructed or modifying the sink to accept the resolved `IHubContext<T>` instances. Additionally, I'll recommend calling `Log.CloseAndFlush` in `Program.Main` within a `finally` block to ensure logs are properly flushed.

## ASSISTANT
The root of the problem is that by passing lambdas like

```csharp
() => services.GetRequiredService<IHubContext<…>>()
```

you aren’t actually resolving your hubs until inside your sink’s `Emit` method—i.e. long after the `IServiceProvider` has been torn down.  When the host shuts down it disposes the provider, then disposes Serilog (and its sinks), and your next log call tries to call `GetRequiredService` on a dead provider → **ObjectDisposedException**.

---

### 1) Resolve your hubs up front

Change your `UseSerilog` to grab the two `IHubContext<…>` _once_ when the logger is being set up:

```csharp
builder.Host.UseSerilog((context, services, configuration) =>
{
    // resolve now, while the provider is still live
    var telemetryHub = services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>();
    var loggingHub   = services.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>();

    configuration
      .WriteTo.Console()
      .WriteTo.File(
        Path.Combine(AppContext.BaseDirectory, "Logs", "log-.txt"),
        rollingInterval: RollingInterval.Day)
      // inject the real instances, not lambdas
      .WriteTo.Sink(new SignalRTelemetrySink(telemetryHub, loggingHub));
});
```

And update your sink’s constructor to accept the actual hubs:

```csharp
public class SignalRTelemetrySink : ILogEventSink
{
    private readonly IHubContext<SignalRInternalTelemetryHub> _telemetryHub;
    private readonly IHubContext<SignalRInternalLoggingHub>   _loggingHub;

    public SignalRTelemetrySink(
        IHubContext<SignalRInternalTelemetryHub> telemetryHub,
        IHubContext<SignalRInternalLoggingHub>   loggingHub)
    {
        _telemetryHub = telemetryHub;
        _loggingHub   = loggingHub;
    }

    public void Emit(LogEvent logEvent)
    {
        // never touches IServiceProvider — safe even during shutdown
        _telemetryHub.Clients.All.SendAsync("log", logEvent.RenderMessage());
        _loggingHub  .Clients.All.SendAsync("log", logEvent.RenderMessage());
    }
}
```

---

### 2) (Optional) Ensure Serilog flushes before the container is torn down

If for some reason you can’t refactor right away, make sure you call:

```csharp
try
{
    host.Run();
}
finally
{
    Log.CloseAndFlush();
}
```

in your `Program.Main` so that Serilog disposes its sinks **while** the `IServiceProvider` is still alive, not afterward.

---

#### Why this fixes it

- **Immediate resolution** means your sink holds on to real `IHubContext<>` instances, and never goes back to the service provider at `Emit` time.
- No more “provider already disposed” on shutdown.
- Cleaner, more DI-friendly code.

## USER
here is the sink using Logistix.Server.Infrastructure.CanBus.InternalCanBusHubs.Hubs;

using Microsoft.AspNetCore.SignalR;

using Serilog.Core;

using Serilog.Events;



namespace Logistix.Server.API.Logging.Sinks

{

    public class SignalRTelemetrySink : ILogEventSink

    {

        private readonly Func<IHubContext<SignalRInternalTelemetryHub>> _hubContextFactory;

        private readonly Func<IHubContext<SignalRInternalLoggingHub>> _loggingHub;



        public SignalRTelemetrySink(Func<IHubContext<SignalRInternalTelemetryHub>> hubContextFactory, Func<IHubContext<SignalRInternalLoggingHub>> loggingHub)

        {

            _hubContextFactory = hubContextFactory;

            _loggingHub = loggingHub;

        }



        public void Emit(LogEvent logEvent)

        {





            if (logEvent.Level == LogEventLevel.Information)

            {

                var message = new

                {

                    Message = logEvent.RenderMessage(),  // Full formatted log message

                    Time = logEvent.Timestamp

                };



                var hubContext = _hubContextFactory();

                hubContext.Clients.All.SendAsync("ReceiveTelemetry", message);

            }



            if (logEvent.Level == LogEventLevel.Warning)

            {

                var message = new

                {

                    Message = logEvent.RenderMessage(),  // Full formatted log message

                    Time = logEvent.Timestamp

                };



                var hubContext = _hubContextFactory();

                hubContext.Clients.All.SendAsync("ReceiveTelemetry", message);

            }



            if (logEvent.Level == LogEventLevel.Error)

            {

                var message = new

                {

                    Message = logEvent.RenderMessage(),  // Full formatted log message

                    Time = logEvent.Timestamp

                };



                var hubContext = _loggingHub();

                hubContext.Clients.All.SendAsync("Error Received", message);

            }

        }

    }

}


## ASSISTANT
You’re seeing the `ObjectDisposedException` because your sink still reaches back into the `IServiceProvider` (via your two `Func<…>`) at log‐time—by then the host (and its DI scope) has already been torn down.

The fix is to **capture** the two hub contexts **once**, during logger setup, and never call back into `services` inside `Emit`. Here’s how:

---

### 1) Change your `UseSerilog` registration

```csharp
builder.Host.UseSerilog((context, services, configuration) =>
{
    // resolve these _now_, while the provider is still alive
    var telemetryHub = services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>();
    var loggingHub   = services.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>();

    configuration
      .WriteTo.Console()
      .WriteTo.File(
          Path.Combine(AppContext.BaseDirectory, "Logs", "log-.txt"),
          rollingInterval: RollingInterval.Day)
      // pass the real instances, not factories
      .WriteTo.Sink(new SignalRTelemetrySink(telemetryHub, loggingHub));
});
```

---

### 2) Rewrite your sink to take `IHubContext<>` directly

```csharp
using Microsoft.AspNetCore.SignalR;
using Serilog.Core;
using Serilog.Events;
using Logistix.Server.Infrastructure.CanBus.InternalCanBusHubs.Hubs;

namespace Logistix.Server.API.Logging.Sinks
{
    public class SignalRTelemetrySink : ILogEventSink
    {
        private readonly IHubContext<SignalRInternalTelemetryHub> _telemetryHub;
        private readonly IHubContext<SignalRInternalLoggingHub>   _loggingHub;

        public SignalRTelemetrySink(
            IHubContext<SignalRInternalTelemetryHub> telemetryHub,
            IHubContext<SignalRInternalLoggingHub>   loggingHub)
        {
            _telemetryHub = telemetryHub;
            _loggingHub   = loggingHub;
        }

        public void Emit(LogEvent logEvent)
        {
            var payload = new
            {
                Message = logEvent.RenderMessage(),
                Time    = logEvent.Timestamp
            };

            switch (logEvent.Level)
            {
                case LogEventLevel.Information:
                case LogEventLevel.Warning:
                    // push to your telemetry hub
                    _telemetryHub.Clients.All
                        .SendAsync("ReceiveTelemetry", payload);
                    break;

                case LogEventLevel.Error:
                    // push to your logging hub (make sure the client method name matches)
                    _loggingHub.Clients.All
                        .SendAsync("ReceiveError", payload);
                    break;
            }
        }
    }
}
```

A few notes:

- **No more `Func<…>`** — you resolve the hubs exactly once at startup.
-  Inside `Emit` you never touch the DI container again, so there’s no risk of “provider disposed.”
-  Be sure your SignalR clients subscribe to the correct method names (`ReceiveTelemetry` and `ReceiveError` above—or whatever you choose).

---

### 3) (Optional) Flush Serilog before shutdown

If you haven’t already, wrap your `Run()` so that Serilog disposes _while_ the container is still live:

```csharp
try
{
    host.Run();
}
finally
{
    Log.CloseAndFlush();
}
```

That ensures any buffered logs get sent before everything is torn down.

## USER
nice, now it just sits there an does nothing.

## Thoughts
It seems like the user is troubleshooting a logging issue where the SignalR telemetry sink isn't sending messages. They suspect a misconfiguration of the sink registration. They also question if Serilog's MinimumLevel setting is too high (set to Information), which could block lower-level events. They mentioned that while logging is visible in the Console and File sinks, there's uncertainty if the SignalR hub contexts are interacting properly due to a lack of active connections from clients. It might be that the UI needs a WebSocket connection to those hubs.
It seems the user's telemetry sink isn't working as expected. The issue might be related to missing `await` on the `SendAsync` method, causing the message not to be sent. Additionally, the mismatch between “ReceiveError” and “Error Received” could be why the error messages aren't appearing — the client might be listening for the old event name. To debug, I’d suggest confirming that Serilog is properly set up, ensuring the logging level is appropriately configured, and checking that events are properly routed to the sink. They could also consider adding conditional sinks or ensuring `Log.Logger` is set before the host is built.
To help debug the issue, I’d start with the following steps:

1. Put a breakpoint or use `Console.WriteLine` inside the sink's `Emit` method to confirm it's being called.
2. Configure the sink to ensure it logs at the correct level, like `LogEventLevel.Information`.

## ASSISTANT
A few things could be going on here—either your sink’s `Emit(...)` is never firing, or it is firing but your clients never actually see the SignalR call.  Let’s walk through some quick sanity checks:

---

### 1) Verify that your sink is actually being invoked  
Inside your `Emit` method, temporarily add something trivial like:  
```csharp
Console.WriteLine($"[SignalR Sink] saw a {logEvent.Level} at {logEvent.Timestamp}: {logEvent.RenderMessage()}");
```
If you don’t see that in your console or file logs, then Serilog isn’t routing events into your sink at all.  

If you *do* see it, you know the problem is further downstream (SignalR delivery).

---

### 2) Turn on Serilog “self-logging” so you catch hidden errors  
Add, at the top of your Program.cs (before building the host):
```csharp
Serilog.Debugging.SelfLog.Enable(Console.Error);
```
This will spit any Serilog internal mis-config, exception, or swallowed‐task fault out to stderr.

---

### 3) Check your minimum‐level and sink registration  
By default, `.WriteTo.Sink(...)` will get *every* event, but if you later override levels in appsettings.json or in code (`MinimumLevel.Override` etc.), you might be filtering them out.  Make sure your overall minimum level is at or below whatever you’re trying to push (e.g. `Information`).

---

### 4) Confirm your SignalR hub is actually mapped & clients are connected  
Nothing will ever arrive if your ASP .NET pipeline never exposed the hub endpoint or if your JavaScript/.NET client never establishes the WebSocket.  

- In `Program.cs` (or Startup) you need something like:  
  ```csharp
  app.MapHub<SignalRInternalTelemetryHub>("/internalTelemetry");
  app.MapHub<SignalRInternalLoggingHub>("/internalLogging");
  ```
- On the client side you should see in the browser’s network tab that a WebSocket (or EventSource) connects to `/internalTelemetry` and that you’ve done:  
  ```js
  connection.on("ReceiveTelemetry", msg => { ... });
  ```

---

### 5) Match your method names  
In my example I renamed your error channel to `"ReceiveError"`.  If your client is still listening for `"Error Received"` (or vice versa) nothing will fire.  Make sure the string in `SendAsync(...)` exactly matches the one on `connection.on(...)`.

---

### 6) (Optional) Force-wait the SendAsync so exceptions bubble up  
By default you’re doing fire‐and‐forget.  If the hub is in a bad state you may never notice.  Inside your sink you can wrap in a try/catch and do:
```csharp
try
{
    _telemetryHub.Clients.All
        .SendAsync("ReceiveTelemetry", payload)
        .GetAwaiter().GetResult();
}
catch (Exception ex)
{
    Console.Error.WriteLine($"SignalR dispatch failed: {ex}");
}
```
That will catch any connectivity exceptions immediately.

---

Once you’ve done steps 1–3 you’ll know whether you’ve got a logging‐pipeline issue or a SignalR‐delivery issue, and you can zero in from there. Let me know what you see in your console / SelfLog!

## USER
no i mean wont run. it complies and just sits there

## Thoughts
It seems like the user's program is compiling and starting, but it's not running as expected. From what they've described, the program probably lacks the `Run()` method. In a typical .NET 6 setup, if they omit `app.Run()`, the app won't start properly. Without it, the program just ends and doesn't do anything. It's like the app is building the host but then halts right after. I’ll suggest adding `app.Run()` to make sure it keeps running.
It seems like the user might have forgotten to call `Run()` while configuring their Serilog and SignalR setup. If they omit `.Run()`, the program won't proceed after building the host and will just "sit there." Another possibility is that the order of configuration is off — calling `UseSerilog` before registering SignalR hubs may be causing trouble. Also, if the delegate is using `GetRequiredService` while the `IServiceProvider` is still incomplete, that could be causing a blocking issue. I'll suggest checking the order and making sure `.Run()` is called.


## ASSISTANT
Your problem is that nothing ever actually starts the HTTP/SignalR host – you configure Serilog, but you never call `.Build()`/`.Run()` (or equivalent) on your application. As a result your `Program.cs` just compiles and then “sits there.”

Below is a minimal .NET 6+ top‐level‐statements example that wires everything up so your sink will actually see events and your hubs will be listening:

```csharp
using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Serilog;
using Logistix.Server.API.Logging.Sinks;
using Logistix.Server.Infrastructure.CanBus.InternalCanBusHubs.Hubs;

var builder = WebApplication.CreateBuilder(args);

// 1) Add all your services first (SignalR, controllers, etc.)
builder.Services.AddSignalR();
builder.Services.AddControllers();

// 2) Hook Serilog _after_ you've registered the hubs, so GetRequiredService<IHubContext<...>>() will actually resolve
builder.Host.UseSerilog((context, services, cfg) =>
{
    cfg
      .WriteTo.Console()
      .WriteTo.File(
         Path.Combine(AppContext.BaseDirectory, "Logs", "log-.txt"),
         rollingInterval: RollingInterval.Day)
      .WriteTo.Sink(new SignalRTelemetrySink(
          () => services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>(),
          () => services.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>()
      ));
});

var app = builder.Build();

// 3) Map your hubs and endpoints
app.MapControllers();
app.MapHub<SignalRInternalTelemetryHub>("/internalTelemetry");
app.MapHub<SignalRInternalLoggingHub>("/internalLogging");

// 4) Finally, _run_ the HTTP host
app.Run();
```

### What to check

1. **Build & Run**  
   - With the above in place, `dotnet run` will start Kestrel, listen on your configured URLs, and keep running.

2. **Self-log for Serilog**  
   - If you still see no logs, sprinkle at the top of `Program.cs`:
     ```csharp
     Serilog.Debugging.SelfLog.Enable(Console.Error);
     ```
     This will show any internal Serilog errors.

3. **Client Connection**  
   - In your JS/.NET client, point at the right path:
     ```js
     const conn = new signalR.HubConnectionBuilder()
       .withUrl("/internalTelemetry")
       .build();

     conn.on("ReceiveTelemetry", msg => console.log("tele:", msg));
     await conn.start();
     ```

Once you actually call `app.Run()`, your sink’s `Emit(...)` will fire as Serilog processes events, and the SignalR hubs will be live to push them out.

## USER
nice job, you created an infinate loop between this decleration and this method. builder.Host.UseSerilog((context, services, configuration) =>

{

    // resolve now, while the provider is still live

    var telemetryHub = services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>();

## Thoughts
It looks like the user has found an issue with an infinite loop caused by how `UseSerilog` is configured. The problem seems to stem from resolving the `telemetryHub` context inside the `UseSerilog` lambda. This triggers the app’s host creation and a loop when `services.GetRequiredService` tries to resolve the hub context, which then invokes Serilog, thus causing recursive logging. The solution is to avoid resolving services like `telemetryHub` inside the configuration lambda, to prevent this circular dependency.
The issue is caused by retrieving `IHubContext` within the `UseSerilog` lambda, which triggers the creation of a service provider and leads to recursion. A better solution is to defer context resolution or pass the `IServiceProvider` to the sink rather than resolving services directly. Instead, you can configure Serilog manually, load settings, and then call `UseSerilog()` after building the host. Alternatively, you can register and resolve the sink after building the provider, avoiding circular dependencies.
The issue arises because of pre-resolving the `IHubContext` during configuration, which triggers a recursive logging loop. Instead, avoid calling `services.GetRequiredService` inside the configuration Lambda. You should pass delegate functions that will resolve the `IHubContext` at runtime, inside the `Emit` method, rather than when configuring Serilog. This avoids a cycle by ensuring the dependencies only resolve when truly needed. Essentially, replace immediate resolution with deferred resolution using delegates to break the loop.

## ASSISTANT
The culprit is that by doing

```csharp
builder.Host.UseSerilog((ctx, services, cfg) =>
{
    // ⚠️ this immediately calls into DI, which under the covers fires a log,
    // which fires your sink, which tries to resolve the hub, which fires a log…
    var telemetryHub = services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>();
    …
});
```

you end up in a recursion: resolving the hub spins up the SignalR machinery which emits a Serilog event, which calls your sink, which tries to resolve the hub again, etc.

---

### Break the cycle

Don't ​resolve​ your `IHubContext<>` at **configuration** time. Instead, hand your sink *factory delegates* and let it call into DI only when real log‐events arrive:

```csharp
builder.Host.UseSerilog((context, services, configuration) =>
{
    configuration
      .WriteTo.Console()
      .WriteTo.File(
         Path.Combine(AppContext.BaseDirectory, "Logs", "log-.txt"),
         rollingInterval: RollingInterval.Day)
      .WriteTo.Sink(new SignalRTelemetrySink(
          // ← note: _no_ GetRequiredService here, just the lambda
          () => services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>(),
          () => services.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>()
      ));
});
```

Your **SignalRTelemetrySink** then only calls into DI inside its `Emit(...)`, i.e.:

```csharp
public void Emit(LogEvent logEvent)
{
    // …now safe to resolve on-demand
    var hub = _hubContextFactory();
    hub.Clients.All.SendAsync("ReceiveTelemetry", …);
}
```

---

### Alternative: register the sink after build

If you’d rather keep your Serilog setup free of the `services` overload entirely, you can:

1. **Bootstrap** Serilog before the host:
   ```csharp
   Log.Logger = new LoggerConfiguration()
     .WriteTo.Console()
     .WriteTo.File("Logs/log-.txt", rollingInterval: RollingInterval.Day)
     .CreateBootstrapLogger();
   builder.Host.UseSerilog();
   ```
2. **Build** your `WebApplication` so you have `app.Services`:
   ```csharp
   var app = builder.Build();
   ```
3. **Replace** (or augment) your logger with the SignalR sink now that DI is ready:
   ```csharp
   var telemetrySink = new SignalRTelemetrySink(
       () => app.Services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>(),
       () => app.Services.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>()
   );
   Log.Logger = new LoggerConfiguration()
       .WriteTo.Logger(Log.Logger)      // carry over earlier config
       .WriteTo.Sink(telemetrySink)
       .CreateLogger();

   app.Run();
   ```

Either approach keeps you from pre-resolving the hub context inside Serilog’s own setup, breaking that infinite “configure → resolve → log → resolve” loop.

## USER
your coding all of the the place.  by the time im done you'll rewrite this entire app.  what is going?  what are you doing?

## ASSISTANT
I’m sorry—that got way too deep into code without checking in. My goal was to show you how to break the circular resolution/Serilog configuration loop we discovered, but I realize dumping alternative implementations isn’t what you asked for right now.

Let’s pull back:

1. **What you’ve got:**  
   - A custom Serilog sink that grabs your SignalR hubs from DI inside the Serilog setup.
   - That “resolve‐while‐configuring” step is what’s triggering your infinite loop (and now a dead-end where nothing runs).

2. **What I was doing:**  
   - Illustrating two patterns to avoid pre-resolving the hubs:
     - Delay the `GetRequiredService<...>` until *inside* the sink’s `Emit` method.
     - Or configure Serilog first, build the app (so DI is live), then add the sink.

3. **Where we should go from here:**  
   - Do you want to pick one of those two patterns and flesh it out step by step?  
   - Or would you prefer a high-level outline of just the key change (e.g. “move the hub-resolution lambdas into `Emit`, don’t call them at startup”) and then integrate it yourself?  

Let me know which approach works best for you, and I’ll keep it concise.

## USER
you created that problem

## Thoughts
The user highlighted an issue with the infinite loop caused by the Serilog configuration during dependency injection, and they're asking for a fix. To resolve this, we should create a pattern that avoids resolving services while configuring Serilog. Instead, we might consider adding a custom sink that only resolves the `IHubContext` at runtime, not during configuration. One option is to use deferred sink creation, captured by `IServiceProvider`, to resolve the service when needed within the logger, not at configuration time.
The better pattern to fix the DI issue is to pass a `Func<IServiceProvider>` to the sink, allowing `GetRequiredService` to be called inside the Emit method. We can't use the service provider passed to `UseSerilog` because it's already disposed by the time the sink tries to resolve services. Instead, we could create a static `IServiceProvider` and assign it after the host is built or inject the hub context directly in the sink's constructor. Then register the sink as a singleton for proper DI management.
To solve the infinite loop issue, we need the `SignalRTelemetrySink` to resolve services at runtime, not during configuration. Specifically, we can inject an `IServiceProvider` directly into the sink. However, since `UseSerilog` gets a temporary service provider before building the host, this doesn't resolve properly. One option is to delay the creation of the logger until after the host is built, using host services at that point. Alternatively, we could decouple the sink from DI and use an in-memory queue, which would be processed by a hosted service that interacts with the hubs.

## ASSISTANT
You’re right — pulling the hub out of the Serilog setup and resolving it up‐front is exactly what caused both the “infinite loop” and, once you reverted, the “nothing happens” dead‐end (because that ISP you captured gets disposed before you ever emit).

Let’s fix it by:

1. **Never** call `GetRequiredService<>()` in your `UseSerilog` callback.  
2. **Only** pass *lazy* factories into your sink, and let the sink itself pull the hub out of the *live* DI container at Emit time.  
3. Make sure Serilog has a MinimumLevel ≥ Information so your sink actually fires.

```csharp
// Program.cs
using Serilog;
using Microsoft.AspNetCore.SignalR;
using YourApp.Logging.Sinks;

var builder = WebApplication.CreateBuilder(args);

// 1) Configure Serilog WITHOUT resolving hubs now:
builder.Host.UseSerilog((ctx, services, lc) =>
{
    lc
     .MinimumLevel.Information()
     .WriteTo.Console()
     .WriteTo.File(Path.Combine(AppContext.BaseDirectory, "Logs", "log-.txt"),
                   rollingInterval: RollingInterval.Day)
     .WriteTo.Sink(new SignalRTelemetrySink(
         // lazy factories: only run inside Emit()
         () => services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>(),
         () => services.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>()
     ));
});

var app = builder.Build();

// ... your middleware, MapHubs, etc.

app.Run();
```

And in your sink (`ILogEventSink`) **do** resolve *inside* `Emit`:

```csharp
public void Emit(LogEvent logEvent)
{
    if (logEvent.Level == LogEventLevel.Information ||
        logEvent.Level == LogEventLevel.Warning)
    {
        var hub = _telemetryHubFactory();
        hub.Clients.All.SendAsync("ReceiveTelemetry", new {
            Message = logEvent.RenderMessage(),
            Time    = logEvent.Timestamp
        });
    }
    else if (logEvent.Level == LogEventLevel.Error)
    {
        var hub = _loggingHubFactory();
        hub.Clients.All.SendAsync("ErrorReceived", new {
            Message = logEvent.RenderMessage(),
            Time    = logEvent.Timestamp
        });
    }
}
```

— That way:

- **No** pre-resolution, so no circular-DI loop.  
- You’re using the *real* `IServiceProvider` (still alive) at the moment of `Emit`.  
- Serilog actually emits at Information/Warning/Error and your sink will fire.  

Give that a try and you should see your telemetry messages flowing again.

## USER
so fix this using Logistix.Server.Infrastructure.CanBus.InternalCanBusHubs.Hubs;

using Microsoft.AspNetCore.SignalR;



using Serilog.Core;



using Serilog.Events;







namespace Logistix.Server.API.Logging.Sinks



{



    public class SignalRTelemetrySink : ILogEventSink



    {



        private readonly Func<IHubContext<SignalRInternalTelemetryHub>> _hubContextFactory;



        private readonly Func<IHubContext<SignalRInternalLoggingHub>> _loggingHub;







        public SignalRTelemetrySink(Func<IHubContext<SignalRInternalTelemetryHub>> hubContextFactory, Func<IHubContext<SignalRInternalLoggingHub>> loggingHub)



        {



            _hubContextFactory = hubContextFactory;



            _loggingHub = loggingHub;



        }







        public void Emit(LogEvent logEvent)



        {











            if (logEvent.Level == LogEventLevel.Information)



            {



                var message = new



                {



                    Message = logEvent.RenderMessage(),  // Full formatted log message



                    Time = logEvent.Timestamp



                };







                var hubContext = _hubContextFactory();



                hubContext.Clients.All.SendAsync("ReceiveTelemetry", message);



            }







            if (logEvent.Level == LogEventLevel.Warning)



            {



                var message = new



                {



                    Message = logEvent.RenderMessage(),  // Full formatted log message



                    Time = logEvent.Timestamp



                };







                var hubContext = _hubContextFactory();



                hubContext.Clients.All.SendAsync("ReceiveTelemetry", message);



            }







            if (logEvent.Level == LogEventLevel.Error)



            {



                var message = new



                {



                    Message = logEvent.RenderMessage(),  // Full formatted log message



                    Time = logEvent.Timestamp



                };







                var hubContext = _loggingHub();



                hubContext.Clients.All.SendAsync("Error Received", message);



            }



        }



    }



}

## Thoughts
The user provided code and wants to fix it using namespaces, specifically in Program.cs, likely related to resolving IHubContext correctly and implementing factories. They've requested an updated version of Program.cs and SignalRTelemetrySink.cs.

I'll address the issue with proper namespace

## ASSISTANT
Here’s a drop-in replacement for your Serilog setup **and** your sink class that:

1. **Does not** resolve any hubs in the `UseSerilog` callback (avoiding DI loops or disposed‐provider issues)  
2. Passes **lazy** factories into the sink  
3. Resolves the real `IServiceProvider` only inside `Emit(...)`  

---

### Program.cs

```csharp
using Logistix.Server.Infrastructure.CanBus.InternalCanBusHubs.Hubs;
using Microsoft.AspNetCore.SignalR;
using Serilog;
using Serilog.Events;
using System.IO;

var builder = WebApplication.CreateBuilder(args);

// configure Serilog *without* resolving hubs up front
builder.Host.UseSerilog((ctx, services, lc) =>
{
    lc
     .MinimumLevel.Information()          // make sure Info+/Warning/Error actually fire
     .WriteTo.Console()
     .WriteTo.File(
         Path.Combine(AppContext.BaseDirectory, "Logs", "log-.txt"),
         rollingInterval: RollingInterval.Day
     )
     // pass lazy factories into your sink
     .WriteTo.Sink(new SignalRTelemetrySink(
         () => services.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>(),
         () => services.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>()
     ));
});

var app = builder.Build();

// map your SignalR hubs so the contexts actually work:
app.MapHub<SignalRInternalTelemetryHub>("/telemetry");
app.MapHub<SignalRInternalLoggingHub>("/logging");

app.Run();
```

---

### SignalRTelemetrySink.cs

```csharp
using Logistix.Server.Infrastructure.CanBus.InternalCanBusHubs.Hubs;
using Microsoft.AspNetCore.SignalR;
using Serilog.Core;
using Serilog.Events;

namespace Logistix.Server.API.Logging.Sinks
{
    public class SignalRTelemetrySink : ILogEventSink
    {
        private readonly Func<IHubContext<SignalRInternalTelemetryHub>>  _telemetryHubFactory;
        private readonly Func<IHubContext<SignalRInternalLoggingHub>>    _loggingHubFactory;

        public SignalRTelemetrySink(
            Func<IHubContext<SignalRInternalTelemetryHub>> telemetryHubFactory,
            Func<IHubContext<SignalRInternalLoggingHub>>   loggingHubFactory
        )
        {
            _telemetryHubFactory = telemetryHubFactory;
            _loggingHubFactory   = loggingHubFactory;
        }

        public void Emit(LogEvent logEvent)
        {
            // build your payload
            var payload = new
            {
                Message = logEvent.RenderMessage(),
                Time    = logEvent.Timestamp
            };

            // Info & Warning go to the telemetry hub
            if (logEvent.Level == LogEventLevel.Information ||
                logEvent.Level == LogEventLevel.Warning)
            {
                var telemetryHub = _telemetryHubFactory();
                telemetryHub.Clients
                            .All
                            .SendAsync("ReceiveTelemetry", payload)
                            .ConfigureAwait(false);
                return;
            }

            // Errors go to the logging hub
            if (logEvent.Level == LogEventLevel.Error)
            {
                var loggingHub = _loggingHubFactory();
                loggingHub.Clients
                          .All
                          .SendAsync("ErrorReceived", payload)
                          .ConfigureAwait(false);
            }
        }
    }
}
```

**Why this fixes it:**

- **No pre-resolution of hubs** in `UseSerilog` → no DI loops or disposed‐provider.  
- Hubs are pulled from the *live* `IServiceProvider` only when `Emit` actually runs.  
- Ensures Serilog’s minimum level is set so your sink sees Info/Warning/Error events.  

Give that a shot and you should see your telemetry and error messages start flowing again.

## USER
that lazy broke other stuff now.  now the connection manager cant find those hubs  what are you doing?

## Thoughts
The user is frustrated with the connection manager not finding hubs. It seems like there might be a problem with services collection. I’m considering using `IServiceProvider`, or maybe `LogContext` with Serilog to fix this. Another idea is to push processes to the background rather than blocking the sink. The root cause might be wrong provider capture, so I’ll try implementing a custom sink that relies on dependency injection and properly register it—this could resolve the issue! Let’s fine-tune this approach.
The user is frustrated. The connection manager can't find the hubs—probably due to DI scope issues. I’m exploring ways to properly connect hubs with Serilog: instead of using lazy properties, I could directly inject hubs via DI registration. Another option is ensuring the DI container is fully configured before Serilog uses it. The order of service addition is key here, so I’ll set up SignalR before Serilog configuration. Changing this order may fix the overall connection issue.

## ASSISTANT
Let’s pull back a bit and simplify:

1. **Don’t** hand‐roll `Func<IHubContext<…>>` factories and resolve SignalR hubs inside the `UseSerilog` callback.  
2. **Do** register your sink (which takes real `IHubContext<…>`) in DI, then pull *that* sink out of the provider when configuring Serilog.  

---

### 1) Register your SignalR and your Sink in DI

```csharp
// in Program.cs, before builder.Host.UseSerilog(...)
builder.Services.AddSignalR();

// register your sink itself as a singleton, and let DI fill in the hub contexts
builder.Services.AddSingleton<SignalRTelemetrySink>(sp =>
    new SignalRTelemetrySink(
        sp.GetRequiredService<IHubContext<SignalRInternalTelemetryHub>>(),
        sp.GetRequiredService<IHubContext<SignalRInternalLoggingHub>>()
    )
);
```

---

### 2) Wire Serilog up by pulling the sink from DI

```csharp
using Serilog;
using Logistix.Server.API.Logging.Sinks;

var builder = WebApplication.CreateBuilder(args);

// (1) add SignalR and the sink
builder.Services.AddSignalR();
builder.Services.AddSingleton<SignalRTelemetrySink>(/* as above */);

// (2) configure Serilog *after* DI is set up
builder.Host.UseSerilog((ctx, services, lc) =>
{
    lc.MinimumLevel.Information()
      .WriteTo.Console()
      .WriteTo.File(Path.Combine(AppContext.BaseDirectory, "Logs", "log-.txt"),
                    rollingInterval: RollingInterval.Day)
      // grab our pre‐registered sink:
      .WriteTo.Sink( services.GetRequiredService<SignalRTelemetrySink>() );
});

var app = builder.Build();

// map your hubs so the contexts actually exist at runtime
app.MapHub<SignalRInternalTelemetryHub>("/telemetry");
app.MapHub<SignalRInternalLoggingHub>("/logging");

app.Run();
```

---

### 3) Your Sink is now a plain, eager‐DI class

```csharp
using Microsoft.AspNetCore.SignalR;
using Serilog.Core;
using Serilog.Events;
using Logistix.Server.Infrastructure.CanBus.InternalCanBusHubs.Hubs;

namespace Logistix.Server.API.Logging.Sinks
{
    public class SignalRTelemetrySink : ILogEventSink
    {
        private readonly IHubContext<SignalRInternalTelemetryHub> _telemetry;
        private readonly IHubContext<SignalRInternalLoggingHub>   _logging;

        public SignalRTelemetrySink(
            IHubContext<SignalRInternalTelemetryHub> telemetryHub,
            IHubContext<SignalRInternalLoggingHub>   loggingHub
        )
        {
            _telemetry = telemetryHub;
            _logging   = loggingHub;
        }

        public void Emit(LogEvent logEvent)
        {
            var payload = new { Message = logEvent.RenderMessage(), Time = logEvent.Timestamp };

            if (logEvent.Level == LogEventLevel.Information ||
                logEvent.Level == LogEventLevel.Warning)
            {
                _telemetry.Clients.All
                          .SendAsync("ReceiveTelemetry", payload)
                          .ConfigureAwait(false);
            }
            else if (logEvent.Level == LogEventLevel.Error)
            {
                _logging.Clients.All
                        .SendAsync("ErrorReceived", payload)
                        .ConfigureAwait(false);
            }
        }
    }
}
```

---

#### Why this fixes it

- **SignalR and your hubs** are fully registered *before* Serilog goes looking for them.  
- You avoid creating your own factory, so there’s no “wrong” `IServiceProvider` or lifetime‐mismatch.  
- Your sink simply gets real, ready‐to‐use `IHubContext<>` instances via DI.  

Give that a spin and you should see your telemetry & error‐messages flowing again—without the mysterious “can’t find hub” errors.


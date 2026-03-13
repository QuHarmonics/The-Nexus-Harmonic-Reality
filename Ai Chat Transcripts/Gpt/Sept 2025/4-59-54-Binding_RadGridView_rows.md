# Binding RadGridView rows

https://chat.openai.com/c/68a19a07-dfa0-8326-a447-41460dffc3d7

## USER
so how do i take a List<> and make it a bindable for rad grid rows vs using like the Tag to hide the object model

## Thoughts
To bind a `List<T>` in WinForms Telerik RadGridView, use `BindingList<T>` or `BindingSource`. Set `AutoGenerateColumns` to true, and map columns with `DataPropertyName`. For updates, `BindingList<T>` with `INotifyPropertyChanged` is best. For editing, use `SelectedRows[0].DataBoundItem`. I'll provide full code, including sorting, filtering, and grouping.

## ASSISTANT
Great question. In WinForms (Telerik RadGridView), you don’t need to stash the object in `Tag`. Bind the grid to a proper binding source, and use each row’s `DataBoundItem` to access the underlying object. This yields cleaner code, supports edits, and enables sorting/filtering/grouping.

### Recommended pattern
1. Use `BindingList<T>` (or `BindingSource` over it) for two-way binding and change notifications.  
2. Implement `INotifyPropertyChanged` on your model type so in-place edits reflect in the UI.  
3. Bind `RadGridView.DataSource` to the `BindingSource`.  
4. Define columns and map them via each column’s `FieldName` to model properties (no `Tag` needed).  
5. When you need the selected object, read `row.DataBoundItem`.

### Complete, minimal example (WinForms, Telerik RadGridView)

```csharp
using System;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows.Forms;
using Telerik.WinControls.UI;

public partial class MainForm : Form
{
    private readonly BindingList<Person> _people;
    private readonly BindingSource _source;

    public MainForm()
    {
        InitializeComponent();

        // 1) Your in-memory data
        _people = new BindingList<Person>
        {
            new Person { Id = 1, FirstName = "Ada", LastName = "Lovelace", Age = 36, Active = true },
            new Person { Id = 2, FirstName = "Alan", LastName = "Turing", Age = 41, Active = false }
        };

        // 2) Wrap in a BindingSource (helps with currency, sorting, etc.)
        _source = new BindingSource { DataSource = _people };

        // 3) Configure the grid
        radGridView1.AutoGenerateColumns = false;  // explicit columns = safer & faster
        radGridView1.AllowAddNewRow = true;        // optional
        radGridView1.AllowDeleteRow = true;        // optional
        radGridView1.ReadOnly = false;             // allow inline editing

        // 4) Define columns and map to properties via FieldName
        var colId = new GridViewDecimalColumn("Id")
        {
            FieldName = nameof(Person.Id),
            IsVisible = true,
            ReadOnly = true, // often IDs are read-only
            Width = 60
        };

        var colFirst = new GridViewTextBoxColumn("First Name")
        {
            FieldName = nameof(Person.FirstName),
            Width = 120
        };

        var colLast = new GridViewTextBoxColumn("Last Name")
        {
            FieldName = nameof(Person.LastName),
            Width = 120
        };

        var colAge = new GridViewDecimalColumn("Age")
        {
            FieldName = nameof(Person.Age),
            Width = 60
        };

        var colActive = new GridViewCheckBoxColumn("Active")
        {
            FieldName = nameof(Person.Active),
            Width = 70
        };

        radGridView1.Columns.AddRange(colId, colFirst, colLast, colAge, colActive);

        // 5) Bind the grid
        radGridView1.DataSource = _source;

        // 6) Optional: enable built-in features
        radGridView1.EnableFiltering = true;
        radGridView1.MasterTemplate.EnableGrouping = true;
        radGridView1.MasterTemplate.EnableSorting = true;

        // 7) Example: handle row selection to get the underlying object (no Tag)
        radGridView1.SelectionChanged += (s, e) =>
        {
            if (radGridView1.CurrentRow is GridViewDataRowInfo row && row.DataBoundItem is Person p)
            {
                // Use 'p' directly; no hidden Tag required.
                this.Text = $"Selected: {p.FirstName} {p.LastName}";
            }
        };

        // 8) Example: mutate the list and see the grid update
        btnAdd.Click += (s, e) =>
        {
            _people.Add(new Person { Id = _people.Count + 1, FirstName = "Grace", LastName = "Hopper", Age = 85, Active = true });
        };
    }
}

// Model with INotifyPropertyChanged for live updates during editing
public class Person : INotifyPropertyChanged
{
    private int _id;
    private string _firstName;
    private string _lastName;
    private int _age;
    private bool _active;

    public int Id { get => _id; set => Set(ref _id, value); }
    public string FirstName { get => _firstName; set => Set(ref _firstName, value); }
    public string LastName { get => _lastName; set => Set(ref _lastName, value); }
    public int Age { get => _age; set => Set(ref _age, value); }
    public bool Active { get => _active; set => Set(ref _active, value); }

    public event PropertyChangedEventHandler PropertyChanged;
    protected bool Set<T>(ref T field, T value, [CallerMemberName] string name = null)
    {
        if (Equals(field, value)) return false;
        field = value;
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
        return true;
    }
}
```

#### Notes and practical tips
- **Why `BindingList<T>`?** It implements `IBindingList`, so the grid is notified about add/remove operations. For property edits, implementing `INotifyPropertyChanged` on `T` keeps the row in sync.
- **`BindingSource` vs. raw list:** `BindingSource` simplifies currency management, supports filtering/sorting (with compatible lists), and plays nicely with WinForms’ data-binding infrastructure.
- **Accessing the object:** Use `((Person)gridRow.DataBoundItem)` anywhere you’d have used `row.Tag`. This is the idiomatic approach.
- **Nested properties:** If you need `Customer.Address.City`, project to a flat view-model or use unbound/expression columns and update them on change.
- **Batch refresh:** If you must mutate many items without `INotifyPropertyChanged`, call `_source.ResetBindings(false)` as a last resort.

If you share your current grid setup or model, I can adapt this snippet precisely to your codebase (columns, formats, editors, validation, etc.).


# ComboBox Item Addition Error

https://chat.openai.com/c/67ebcc0b-d700-8011-9ae3-fa303f43a846

## USER
why wont this work  foreach ((string Code, string Name) state in StateList.GetState())

 {

     var combo = new System.Windows.Forms.ComboBox();

     combo.DisplayMember = state.Name;

     combo.ValueMember = state.Code;

     comboStateDropdown.Items.Add(combo);

 }

## ASSISTANT
The issue with your `foreach` loop lies in how you're using `ComboBox` controls instead of adding items to a single `ComboBox`.

You're **creating a new `ComboBox` in every iteration** and trying to add it as an item to `comboStateDropdown`, which is presumably another `ComboBox`. A `ComboBox` can only contain items like strings or objects, **not other `ComboBox` controls**.

### Here's the corrected version:
Assuming `comboStateDropdown` is your intended dropdown and `StateList.GetState()` returns a list of `(string Code, string Name)` tuples:

```csharp
foreach ((string Code, string Name) state in StateList.GetState())
{
    // Create a custom object to represent each item
    comboStateDropdown.Items.Add(new { Code = state.Code, Name = state.Name });
}

// Set display and value members (must be property names, not actual values)
comboStateDropdown.DisplayMember = "Name";
comboStateDropdown.ValueMember = "Code";
```

But **anonymous types** (`new { ... }`) won't work with `ValueMember` and `DisplayMember` in WinForms because those properties need real **named properties**, not anonymous ones.

### Best practice: use a custom class
```csharp
public class StateItem
{
    public string Code { get; set; }
    public string Name { get; set; }
}

comboStateDropdown.DisplayMember = "Name";
comboStateDropdown.ValueMember = "Code";

foreach ((string Code, string Name) state in StateList.GetState())
{
    comboStateDropdown.Items.Add(new StateItem { Code = state.Code, Name = state.Name });
}
```

Now the combo box will properly display the state name and use the code as the selected value.

Let me know if you're using a Telerik `RadDropDownList` instead—those have slightly different behavior and property names.

## USER
i uses anon, how do i get the value then?

## ASSISTANT
Great question. If you **used anonymous types** in the `ComboBox.Items.Add()` like this:

```csharp
comboBox.Items.Add(new { Code = state.Code, Name = state.Name });
```

You **cannot access `SelectedItem.Code` or `SelectedValue` directly** because the anonymous type isn't strongly typed or accessible by name. But you *can* still extract the data by casting.

### ✅ Here’s how you get the selected values:

```csharp
var selectedItem = comboBox.SelectedItem;
if (selectedItem != null)
{
    var code = selectedItem.GetType().GetProperty("Code")?.GetValue(selectedItem, null)?.ToString();
    var name = selectedItem.GetType().GetProperty("Name")?.GetValue(selectedItem, null)?.ToString();

    // Now you can use `code` and `name` as needed
}
```

This uses **reflection** to read the property from the anonymous type.

---

### 🟨 Alternative Tip (cleaner): use a tuple

You can also use a `Tuple<string, string>`:

```csharp
comboBox.Items.Add((state.Code, state.Name));
```

Then later:

```csharp
if (comboBox.SelectedItem is ValueTuple<string, string> tuple)
{
    var code = tuple.Item1;
    var name = tuple.Item2;
}
```

But the most robust and readable approach (especially for big apps) is to create a tiny class or struct—anonymous types are fine for quick views, but they limit you later.

Want me to whip up a reusable helper class that handles this cleaner?

